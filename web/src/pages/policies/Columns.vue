<template lang="pug">
.policies-container
  .empty.w-full(v-if="isColumnsEmpty")
    .text-xl.text-gray-400.text-center There is nothing here!
    .project-logo.flex.justify-center.mt-10.w-full()
      svg-icon(name="cloud-computing", addClass="fill-current text-gray-300 w-24 h-24")
    .flex.justify-center.mt-10
      t-button.mt-10.w-full.text-center(tagName="a" :href="`/connections/${connectionId}/policies/columns/add`")
        | Add New Column
  .flex.justify-center.w-full(v-else)
    .body.w-full.flex.items-center.flex-col
      .connections.gap-y-3.flex.flex-col.w-full
        .flex.gap-x-5
          t-input(v-model="search" placeholder="Search")
          t-button(
            variant="secondary" tagName="a"
            :href="`/connections/${connectionId}/policies/columns/add?${qs.stringify(this.$route.query)}`"
          ) Add
        t-table(:headers="headers" :data="redactionColumns" variant="thin")
          template(slot='row' slot-scope='props')
            tr(:class="[props.trClass, 'hover:bg-gray-50']")
              td(:class='props.tdClass')
                | {{ props.row.object_owner }}
              td(:class='props.tdClass')
                | {{ props.row.object_name }}
              td(:class='props.tdClass')
                | {{ props.row.column_name }}
              td(:class='props.tdClass')
                | {{ props.row.function_type }}
              td.flex.gap-x-5(:class='props.tdClass')
                .icon-btn.las.la-code(@click="onModifyExpression(props.row)")
                .icon-btn.las.la-pen
                .icon-btn.danger.las.la-trash-alt(@click="onDropColumn(props.row)")

</template>

<script>
/* eslint-disable camelcase */
import { mapActions, mapGetters } from 'vuex'
import SvgIcon from '@/components/SvgIcon'
import { PolicyActions } from '@/utils'
import qs from 'qs'

export default {
  props: ['connectionId'],
  components: {
    SvgIcon
  },
  data () {
    return {
      qs: qs,
      isSpinner: false,
      title: 'Redaction Columns',
      search: '',
      headers: ['Owner', 'Table', 'Column', 'Function', '']
    }
  },
  computed: {
    ...mapGetters('redact', ['policies', 'redactionColumns']),
    isColumnsEmpty () {
      return this.redactionColumns.length === 0
    }
  },
  methods: {
    ...mapActions('redact', ['getPolicies', 'getRedactionColumns', 'alterPolicy']),
    load () {
      this.isSpinner = true
      this.getRedactionColumns().finally(() => { this.isSpinner = false })
    },
    onDropColumn (record) {
      const action = PolicyActions.DROP_COLUMN
      const {
        object_owner, object_name, column_name
      } = record
      const { policy_name } = this.$route.query
      const payload = {
        object_schema: object_owner, object_name, column_name, policy_name, action
      }
      this.alterPolicy(payload).then(() => {
        this.$toast.success('Success. Column removed from redactions')
      }).catch(error => {
        console.log(error)
        this.$toast.error('Error. Failed to remove column')
      })
    },
    onModifyExpression ({ column_name }) {
      const params = { ...this.$route.query, column_name }
      this.$router.push({ path: `columns/modify-expression?${qs.stringify(params)}` })
    }
  },
  mounted () {
    this.load()
  }
}
</script>

<style lang="postcss" scoped>
.empty {
  @apply border-dashed p-3 border-2 rounded-md w-full
}
.page {
}

</style>
