<template lang="pug">
.flex.justify-center.w-full()
  .body.w-full.flex.items-center.flex-col
    .toolbar.flex.flex-col.gap-y-2.p-5.w-full.bg-gray-50.rounded-md
      .flex.flex-row.justify-between
        .title
          | {{title}}
        .filter.flex.justify-end.text-xl.gap-x-3(v-if="!isSpinner")
          t-tag.p-1(
            :class="{ 'bg-red-200': status==='error',\
                'bg-blue-200': status==='running',\
                'bg-green-200': status==='success'}"
            tag-name="span" variant="badge"
          ) {{status}}
          .icon-btn.las.la-sync-alt.cursor-pointer(@click="onReload")
        .spinner.lds-dual-ring(v-else)
    .gap-y-5.flex.flex-col.w-full.mt-4
      discoveries-by-rule-chart(
        ref="byRuleChart"
        :planInstanceId="planInstanceId", :planId="planId")
      discoveries-by-schema-chart(
        ref="bySchemaChart"
        :planInstanceId="planInstanceId", :planId="planId")
</template>

<script>
import _ from 'lodash'
import { mapActions } from 'vuex'
import DiscoveriesByRuleChart from '@/components/DiscoveriesByRuleChart'
import DiscoveriesBySchemaChart from '@/components/DiscoveriesBySchemaChart'

export default {
  props: ['connectionId', 'planInstanceId', 'planId'],
  components: {
    DiscoveriesByRuleChart, DiscoveriesBySchemaChart
  },
  data () {
    return {
      isSpinner: false,
      plan: {},
      planInstance: {}
    }
  },
  computed: {
    title () {
      return `${this.plan.name} discoveries`
    },
    status () {
      return `${this.planInstance.status}`
    }
  },
  methods: {
    ...mapActions('plan', ['getPlan']),
    ...mapActions('planInstance', ['getPlanInstance']),
    onReload () {
      this.isSpinner = true
      Promise.all(_.map(['byRuleChart', 'bySchemaChart'], r => {
        return this.$refs[r].fetchData()
      })).finally(() => { this.isSpinner = false })
    }
  },
  created () {
    this.isSpinner = true
    Promise.all([
      this.getPlan(+this.planId),
      this.getPlanInstance({ id: +this.planInstanceId, planId: +this.planId })
    ]).then(([plan, planInstance]) => {
      this.planInstance = planInstance
      this.plan = plan
    }).finally(() => {
      this.isSpinner = false
    })
  }
}
</script>
