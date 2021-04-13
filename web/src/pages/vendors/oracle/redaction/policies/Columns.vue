<template lang="pug">
.policies-container
  .empty.bg-white.w-full(v-if="isColumnsEmpty")
    .text-xl.text-gray-400.text-center There is nothing here!
    .project-logo.flex.justify-center.mt-10.w-full()
      svg-icon(name="box", addClass="fill-current text-gray-300 w-24 h-24")
    .flex.justify-center.mt-10
      t-button.mt-10.w-full.text-center(tagName="a" :href="addColumnUrl")
        | Add New Column
  .flex.justify-center.w-full(v-else)
    .body.w-full.flex.items-center.flex-col
      .gap-y-3.flex.flex-col.w-full
        .flex.gap-x-5
          t-input(v-model="search" placeholder="Search")
          t-button(
            variant="secondary" tagName="a"
            :href="addColumnUrl"
          ) Add
        t-table(:headers="headers" :data="redColumns")
          template(slot='row' slot-scope='props')
            tr(:class="[props.trClass, 'hover:bg-gray-50']")
              td.overflow-ellipsis(:class='props.tdClass')
                | {{ props.row.object_owner }}
              td.overflow-ellipsis(:class='props.tdClass')
                | {{ props.row.object_name }}
              td.overflow-ellipsis(:class='props.tdClass')
                | {{ props.row.column_name }}
              td.overflow-ellipsis(:class='props.tdClass')
                | {{ props.row.function_type }}
              td.flex.gap-x-5(:class='props.tdClass')
                .row-action-btn.icon-btn.las.la-pen(@click="onEditColumn(props.row)")
                .row-action-btn.icon-btn.danger.las.la-trash-alt(@click="onDropColumn(props.row)")

</template>

<script>
/* eslint-disable camelcase */
import _ from 'lodash'
import { mapActions, mapGetters } from 'vuex'
import SvgIcon from '@/components/SvgIcon'
import qs from 'qs'
import { loaderMixin } from '@/mixins'

export default {
  mixins: [loaderMixin],
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
      headers: ['Owner', 'Table', 'Column', 'Function', ''],
      redColumns: []
    }
  },
  watch: {
    search (s) {
      if (_.isEmpty(this.redColumns_)) {
        this.redColumns_ = [...this.redColumns]
      }
      if (_.isEmpty(s)) {
        this.redColumns = this.redColumns_
        return
      }
      this.redColumns = _.filter(this.redColumns_, c => {
        return (
          c.column_name.toLowerCase().includes(s.toLowerCase())
        )
      })
    }
  },
  computed: {
    ...mapGetters('policy', ['policies']),
    isColumnsEmpty () {
      return _.isEmpty(this.search) && this.redColumns.length === 0
    },
    addColumnUrl () {
      const query = { action: 1, ...this.$route.query }
      return `/connections/${this.connectionId}/oracle/policies/edit?${qs.stringify(query)}`
    }
  },
  methods: {
    ...mapActions('policy', ['updatePolicy']),
    ...mapActions('column', { getRedColumns: 'getColumns' }),
    load () {
      const {
        policy_name, object_name, object_owner
      } = this.$route.query
      this.isSpinner = true
      this.getRedColumns({ policy_name, object_name, object_owner })
        .then(result => {
          this.redColumns = result
        })
        .finally(() => { this.isSpinner = false })
    },
    onEditColumn ({ column_name }) {
      const query = { action: 4, column_name, ...this.$route.query }
      const path = `/connections/${this.connectionId}/oracle/policies/edit?${qs.stringify(query)}`
      this.$router.push({ path })
    },
    onDropColumn ({ column_name }) {
      const {
        policy_name, object_name, object_owner
      } = this.$route.query
      const payload = { action: 2, policy_name, object_name, object_schema: object_owner, column_name }
      this.startLoader()
      this.updatePolicy(payload).then(() => {
        this.$toasted.success('Success. Column removed from policy')
        const i = _.findIndex(this.redColumns, { column_name })
        if (i > -1) {
          this.redColumns.splice(i, 1)
        }
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Error. Failed to remove column')
      }).finally(this.stopLoader)
    },
    onModifyExpression ({ column_name }) {
      const params = { ...this.$route.query, column_name }
      this.$router.push({ path: `columns/modify-expression?${qs.stringify(params)}` })
    }
  },
  created () {
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
tr .row-action-btn {
  @apply text-gray-100;
}
tr .row-action-btn.danger {
  @apply text-red-100;
}

tr:hover .row-action-btn.danger {
  @apply text-red-600;
}
tr:hover .row-action-btn {
  @apply text-gray-600;
}
</style>
