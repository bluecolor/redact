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
        )
        .row-action-btn.icon-btn.las.la-certificate.tex-gray-400(
          content="Has policy" v-tippy='{ placement : "top" }'
          v-if="hasPolicy(props.row)"
        )
        t-icon-dropdown(
          :classes="{icon: 'las la-ellipsis-v'}"
          :emitValue="true" :items="menu", valueProp="value")

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
      headers: ['Schema', 'Table', 'Column'],
      menu: [
        { name: 'Apply expression', value: 'appy-exp', icon: 'las la-stamp' },
        { name: 'Add to policy', value: 'add-col', icon: 'las la-plus' },
        { name: 'Remove from policy', value: 'drop-col', icon: 'las la-minus' }
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
    hasPolicy ({ schema_name, table_name }) {
      const result = _.find(this.redaction.policies, p => {
        return p.table.owner === schema_name && p.table.table_name === table_name
      })
      return result?.policy
    }
  },
  created () {
    this.askPolicyTables(this.tables).then(result => {
      this.redaction.policies.push(...result)
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
