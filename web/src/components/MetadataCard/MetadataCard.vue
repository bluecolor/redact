<template lang="pug">
t-card.card
  template(v-slot:header)
    .flex.justify-between
      .title.flex.gap-x-2.items-center
        .text-2xl(:class="icon")
        .text
          | {{name}}
      .actions.flex.justify-end
        .btns.gap-x-3.flex(v-if="!isSpinner")
          .icon-btn-.cursor-pointer.text-2xl.las.la-expand(:class="color" @click="onSample")
        .spinner.lds-dual-ring(v-else)
  template(v-slot:default)
    .flex
      .start.flex.flex-col.gap-y-2
        .text-gray-400 {{m.type}}
        .full-name {{fullName}}
        .sample.flex.gap-1.flex-wrap(v-if="!isSampleEmpty")
          t-tag.p-1.overflow-ellipsis(v-for="s in sample" tag-name="span" variant="badge") {{s}}
</template>

<script>
import _ from 'lodash'
import { mapActions } from 'vuex'

/* eslint-disable camelcase */
export default {
  props: { m: { type: Object, default: () => {} } },
  data () {
    return {
      isSpinner: false,
      sample: [],
      info: {}
    }
  },
  computed: {
    isSampleEmpty () {
      return this.sample?.length === 0
    },
    color () {
      const { type } = this.m
      switch (type) {
        case 'column': return 'text-blue-400 hover:text-blue-600'
        case 'table': return 'text-red-400 hover:text-red-600'
      }
      return 'text-gray-200'
    },
    icon () {
      const { type } = this.m
      switch (type) {
        case 'column': return 'las la-columns text-blue-200'
        case 'table': return 'las la-border-all text-red-200'
      }
      return 'text-gray-200'
    },
    name () {
      const { table_name, column_name } = this.m
      return column_name ?? table_name
    },
    fullName () {
      const { type, owner, table_name, column_name } = this.m
      if (type === 'column') {
        return `${owner}.${table_name}.${column_name}`
      }
      return `${owner}.${table_name}`
    }
  },
  methods: {
    ...mapActions('md', ['getColumnSample', 'getColumns']),
    ...mapActions('redaction', ['askRedactionInfo']),
    fetchColumnSample () {
      const { owner: schema_name, table_name, column_name } = this.m
      this.isSpinner = true
      this.getColumnSample({ schema_name, table_name, column_name }).then(result => {
        this.sample = _.map(result, r => r[column_name.toLowerCase()])
      }).finally(() => {
        this.isSpinner = false
      })
    },
    fetchColumns () {
      const { owner: object_schema, table_name: object_name } = this.m
      this.isSpinner = true
      this.getColumns({ object_schema, object_name }).then(result => {
        this.sample = _.map(result, r => r.column_name)
      }).finally(() => { this.isSpinner = false })
    },
    onSample () {
      if (!this.isSampleEmpty) {
        this.sample = []
        return
      }
      if (this.m.type === 'column') {
        this.fetchColumnSample()
      } else if (this.m.type === 'table') {
        this.fetchColumns()
      }
    }
  },
  created () {
    const { owner: schema_name, table_name, column_name } = this.m
    this.isSpinner = true
    this.askRedactionInfo({ schema_name, table_name, column_name }).then(result => {
      console.log(result)
    }).finally(() => { this.isSpinner = false })
  }
}
</script>>
