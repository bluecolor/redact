<template lang="pug">
.policies-container
  .bg-white.empty.w-full(v-if="isPlanInstancesEmpty")
    .text-xl.text-gray-400.text-center There is nothing here!
    .project-logo.flex.justify-center.mt-10.w-full()
      svg-icon(name="cloud-computing", addClass="fill-current text-gray-300 w-24 h-24")
  .flex.justify-center.w-full(v-else)
    .body.w-full.flex.items-center.flex-col
      .plan-runs.gap-y-3.flex.flex-col.w-full
        .toolbar.flex.flex-col.gap-y-2.p-5.w-full.bg-gray-50.rounded-md
          .flex.flex-row.justify-between
            .title
              | All Plan Runs
            .filter.flex.justify-end.text-xl.gap-x-3
              .icon-btn.las.la-sync-alt.cursor-pointer(@click="onReload")
              .las.la-filter.cursor-pointer(@click="isFilter=!isFilter" :class="{'text-blue-500': isFilter}")
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
        t-card.card(v-for="p in planInstances")
          template(v-slot:header)
            .flex.justify-between
              .title
                | {{p.plan.name}}
              .actions.flex.justify-end
                .btns.gap-x-3.flex(v-if="!isSpinner")
                  .icon-btn.las.la-sync-alt
                  router-link.icon-btn.las.la-info-circle(
                    content="Discoveries" v-tippy='{ placement : "top" }'
                    :to="`instances/${p.id}/discoveries-by-rule`")
                  .icon-btn.las.la-stop-circle(
                    v-if="p.status==='running'"
                    content="Stop" v-tippy='{ placement : "top" }'
                    @click="onStop(p)")
                  .icon-btn.las.la-trash-alt.danger(
                    v-if="p.status!=='running'"
                    content="Delete" v-tippy='{ placement : "top" }'
                    @click="onDelete(p)"
                  )
                .spinner.lds-dual-ring(v-else)
          template(v-slot:default)
            .body.flex.justify-between
              .flex.flex-col
                .start-date.text-gray-400
                  | started {{fromNow(p.created_on)}}
                .description
                  | {{p.description}}
              .status
                t-tag.p-1(
                  :class="{ 'bg-red-200': p.status==='error',\
                      'bg-blue-200': p.status==='running',\
                      'bg-green-200': p.status==='success'}"
                  tag-name="span" variant="badge"
                ) {{p.status}}
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import SvgIcon from '@/components/SvgIcon'
import { dateMixin } from '@/mixins'

export default {
  mixins: [dateMixin],
  props: ['connectionId'],
  components: {
    SvgIcon
  },
  data () {
    return {
      isSpinner: false,
      isFilter: false,
      title: 'Plan Runs',
      planInstances: [],
      statuses: [
        { id: 'running', name: 'Running' },
        { id: 'success', name: 'Success' },
        { id: 'error', name: 'Error' }
      ],
      planId: undefined,
      data: undefined
    }
  },
  computed: {
    ...mapGetters('discovery', ['plans']),
    isPlanInstancesEmpty () {
      return this.planInstances.length === 0
    }
  },
  methods: {
    ...mapActions('planInstance', ['getAllPlanInstances', 'deletePlanInstance', 'stopPlanInstance']),
    ...mapActions('discovery', ['getPlans']),
    onReload () {
      this.isSpinner = true
      return this.getAllPlanInstances().then(result => {
        this.planInstances = result
      }).finally(() => { this.isSpinner = false })
    },
    onPlanSelect (id) {},
    onStatusSelect (id) {},
    onDelete (p) {
      this.deletePlanInstance({ id: p.id, planId: p.plan.id }).then(result => {
        this.$toasted.success('Success. Deleted plan run.')
      })
    },
    onStop (p) {
      this.isSpinner = true
      this.stopPlanInstance({ id: p.id, planId: p.plan.id }).then(() => {
        this.$toasted.success('Success. Stopped plan')
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Failed to stop plan')
      }).finally(() => {
        this.isSpinner = false
      })
    }
  },
  mounted () {
    this.onReload()
    if (this.plans.length === 0) {
      this.getPlans()
    }
    // const ws = new WebSocket('ws://localhost:8000/api/v1/ws/plans/instances')
    // ws.onmessage = (message) => {
    //   console.log(message)
    // }
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
