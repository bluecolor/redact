<template lang="pug">
t-table.d-table(:headers="headers" :data="d" style="overflow:unset;")
  template(slot='row' slot-scope='props')
    tr(:class="[props.trClass, 'hover:bg-gray-50']")
      td.overflow-ellipsis(:class='props.tdClass')
        | {{ props.row.schema_name }}
      td.overflow-ellipsis(:class='props.tdClass')
        | {{ props.row.table_name }}
      td.overflow-ellipsis(:class='props.tdClass')
        | {{ props.row.column_name }}
      td.overflow-ellipsis(:class='props.tdClass')
      td.flex.gap-x-3.justify-end(:class='props.tdClass')
        .row-action-btn.icon-btn.las.la-code.tex-gray-400(
          content="Has expression" v-tippy='{ placement : "top" }'
          v-if="hasExpression(props.row)"
        )
        .row-action-btn.icon-btn.las.la-certificate.tex-gray-400(
          content="Has policy" v-tippy='{ placement : "top" }'
          v-if="hasPolicy(props.row)"
        )
        t-icon-dropdown(
          :classes="{icon: 'las la-ellipsis-v'}"
          :emitValue="true" :items="getMenu(props.row)", valueProp="value"
          @select="(v) => onMenuItemClick(v, props.row)"
        )

</template>

<script>
/* eslint-disable camelcase */
import { mapActions } from 'vuex'
import _ from 'lodash'
import TIconDropdown from '@/components/TIconDropdown'

export default {
  props: { d: { type: Array, default: () => [] } },
  components: {
    TIconDropdown
  },
  data () {
    return {
      isSpinner: false,
      headers: ['Schema', 'Table', 'Column'],
      menu: [
        { name: 'Apply expression', value: 'apply-expression', icon: 'las la-stamp' },
        { name: 'Add to policy', value: 'add-column', icon: 'las la-plus' },
        { name: 'Remove from policy', value: 'drop-column', icon: 'las la-minus' },
        { name: 'Create policy', value: 'create-policy', icon: 'las la-certificate' }
      ],
      redaction: {
        policies: [],
        columns: []
      }
    }
  },
  computed: {
    columns () {
      return _.map(this.d, d => {
        return { owner: d.schema_name, table_name: d.table_name, column_name: d.column_name }
      })
    },
    tables () {
      return _.map(this.d, d => {
        return { owner: d.schema_name, table_name: d.table_name }
      })
    }
  },
  methods: {
    ...mapActions('policy', ['askPolicyTables']),
    ...mapActions('redaction', ['askRedactionColumns']),
    getMenu (d) {
      return _.map(this.menu, m => {
        switch (m.value) {
          case 'apply-expression':
            m.disabled = !this.hasPolicy(d)
            break
          case 'add-column':
            m.disabled = !this.hasPolicy(d)
            break
          case 'drop-column':
            m.disabled = !this.hasExpression(d)
            break
          case 'create-policy':
            m.disabled = this.hasPolicy(d)
            break
        }
        return m
      })
    },
    hasPolicy ({ schema_name, table_name }) {
      const result = _.find(this.redaction.policies, p => {
        return p.table.owner === schema_name && p.table.table_name === table_name
      })
      return result?.policy
    },
    hasExpression ({ schema_name, table_name, column_name }) {
      const result = _.find(this.redaction.columns, c => {
        return c.owner === schema_name && c.table_name === table_name && c.column_name === column_name
      })
      return result?.expression
    },
    onMenuItemClick (i, { schema_name, table_name, column_name }) {
      switch (i) {
        case 'create-policy':
          this.$router.push({
            name: 'createPolicy',
            params: { object_schema: schema_name, object_name: table_name, column_name }
          })
          break
      }
    }
  },
  created () {
    this.isSpinner = true
    const p = this.askPolicyTables(this.tables)
    const c = this.askRedactionColumns(this.columns)
    Promise.all([p, c]).then(([policies, columns]) => {
      this.redaction.policies.push(...policies)
      this.redaction.columns.push(...columns)
    }).finally(() => {
      this.isSpinner = false
    })
  }
}
</script>

<style lang="postcss" scoped>
.row-action-btn {
  @apply text-gray-400;
}
.d-table, .d-table th, .d-table tr, .d-table td {
  border: 0 !important
}
</style>
