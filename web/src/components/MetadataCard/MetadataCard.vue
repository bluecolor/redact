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
          router-link.icon-btn.las.la-pen(:to="`connections/`" v-slot="{ navigate }")
          .icon-btn.las.la-vial(
            content="Test connection" v-tippy='{ placement : "top" }'
          )
          .icon-btn.las.la-trash-alt.danger.text-center.items-center
        .spinner.lds-dual-ring(v-else)
  template(v-slot:default)
    .text-gray-400 {{m.type}}
    | {{fullName}}
</template>

<script>
/* eslint-disable camelcase */
export default {
  props: { m: { type: Object, default: () => {} } },
  data () {
    return {
      isSpinner: false
    }
  },
  computed: {
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
  }
}
</script>>
