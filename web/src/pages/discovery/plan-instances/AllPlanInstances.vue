<template lang="pug">
.policies-container
  .bg-white.empty.w-full(v-if="isPlanInstancesEmpty")
    .text-xl.text-gray-400.text-center There is nothing here!
    .project-logo.flex.justify-center.mt-10.w-full()
      svg-icon(name="box", addClass="fill-current text-gray-300 w-24 h-24")
  .flex.justify-center.w-full(v-else)
    .body.w-full.flex.items-center.flex-col
      .plan-runs.gap-y-3.flex.flex-col.w-full
        .toolbar.flex.flex-col.gap-y-2.p-5.w-full.bg-gray-50.rounded-md
          .flex.flex-row.justify-between
            .title
              | All Plan Runs
            .filter.flex.justify-end.text-xl.gap-x-3(v-if="!isSpinner")
              .icon-btn.las.la-sync-alt.cursor-pointer(@click="onReload")
              .las.la-filter.cursor-pointer(@click="isFilter=!isFilter" :class="{'text-blue-500': isFilter}")
            .spinner.lds-dual-ring(v-else)
          .is-filter.flex.flex-col.gap-y-2(v-if="isFilter")
            t-datepicker(v-model="date" placeholder="Pick a date")
            t-select(
              v-model="planId"
              placeholder="Select plan"
              :options="plans",
              value-attribute='id',
              text-attribute="name"
              @input="onPlanSelect"
            )
            t-select(
              v-model="status"
              placeholder="Select status"
              :options="statuses",
              value-attribute='id',
              text-attribute="name"
              @input="onStatusSelect"
            )
        plan-instance-card(v-for="p in planInstances" :p="p")
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import SvgIcon from '@/components/SvgIcon'
import PlanInstanceCard from '@/components/PlanInstanceCard'

export default {
  props: ['connectionId'],
  components: {
    SvgIcon, PlanInstanceCard
  },
  data () {
    return {
      isDestroy: false,
      isSpinner: false,
      isFilter: false,
      title: 'Plan Runs',
      planInstances: [],
      date: undefined,
      status: undefined,
      statuses: [
        { id: 'running', name: 'Running' },
        { id: 'success', name: 'Success' },
        { id: 'error', name: 'Error' }
      ],
      planId: undefined
    }
  },
  computed: {
    ...mapGetters('plan', ['plans']),
    isPlanInstancesEmpty () {
      return this.planInstances.length === 0
    }
  },
  methods: {
    ...mapActions('planInstance', ['getAllPlanInstances']),
    ...mapActions('plan', ['getPlans']),
    onReload () {
      this.isSpinner = true
      return this.getAllPlanInstances().then(result => {
        this.planInstances = result
      }).finally(() => { this.isSpinner = false })
    },
    onPlanSelect (id) {},
    onStatusSelect (id) {}
  },
  mounted () {
    this.onReload()
    if (this.plans.length === 0) {
      this.getPlans()
    }
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
