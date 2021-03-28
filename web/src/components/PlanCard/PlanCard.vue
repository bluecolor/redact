<template lang="pug">
t-card.card
  template(v-slot:header)
    .flex.justify-between
      .title.flex.gap-x-2.items-center
        .las.la-box.text-2xl.text-gray-400
        .text
          | {{p.name}}
      .actions.flex.justify-end
        .btns.gap-x-3.flex(v-if="!isSpinner")
          .icon-btn.las.la-sync-alt(@click="onReload(p)")
          .icon-btn.las.la-play(
            v-if="p.rules.length > 0"
            content="Run plan" v-tippy='{ placement : "top" }'
            @click="onRun(p)"
          )
          router-link.icon-btn.las.la-shipping-fast(:to="`plans/${p.id}/instances`")
          router-link.icon-btn.las.la-pen(:to="`plans/${p.id}`")
          .icon-btn.las.la-trash-alt.danger(
            content="Delete plan" v-tippy='{ placement : "top" }'
            @click="onDelete(p)"
          )
        .spinner.lds-dual-ring(v-else)
  template(v-slot:default)
    .flex.justify-between
      .start.flex.flex-col.gap-y-2
        .description.text-gray-400.overflow-ellipsis {{p.description}}
        .text-gray-600(v-if="p.rules.length!==0") {{p.rules.length}} rule{{p.rules.length>1?'s':''}}
        .text-red-300(v-if="p.rules.length==0") Does not have rules
      .end.flex.flex-col.justify-end.gap-y-3
        .flex.justify-end
          .status(@click="onNavLastRun(p)")
            t-tag.p-1.cursor-pointer(
              content="Last run" v-tippy='{ placement : "left" }'
              :class="{\
                'bg-blue-100': p.status=='running',\
                'bg-red-100': p.status=='error',\
                'bg-green-100': p.status=='success',\
              }"
              tag-name="span" variant="badge"
            ) {{p.status}}
        .text-gray-400.text-sm.flex.justify-end {{formatDate(p.created_on)}}
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import { dateMixin } from '@/mixins'

export default {
  mixins: [dateMixin],
  props: { p: { type: Object, default: () => {} } },
  data () {
    return {
      isSpinner: false,
      interval: undefined
    }
  },
  computed: {
    ...mapGetters('app', ['connectionId'])
  },
  methods: {
    ...mapActions('plan', ['deletePlan', 'runPlan', 'getLastInstance', 'reloadPlan']),
    onReload (p) {
      this.$emit('reload', p)
      const { id } = p
      this.isSpinner = true
      this.reloadPlan(id).finally(() => { this.isSpinner = false })
    },
    onDelete (p) {
      this.isSpinner = true
      this.deletePlan(p.id).then(() => {
        this.$toast.success('Success. Plan deleted')
        this.$emit('delete', p)
      }).catch(error => {
        console.log(error)
        this.$toast.error('Error. Failed to delete plan')
      }).finally(() => {
        this.isSpinner = false
      })
    },
    onRun (plan) {
      const { id } = plan
      this.isSpinner = true
      this.runPlan(id).then(({ id }) => {
        this.$emit('run', plan)
        this.$toasted.success('Plan started')
        this.triggerPlanChecker(id)
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Error. Failed to start plan')
      }).finally(() => {
        this.isSpinner = false
      })
    },
    onNavLastRun (plan) {
      this.isSpinner = true
      const planId = plan.id
      this.getLastInstance(plan.id).then((planInstance) => {
        const name = 'discoveriesGroupByRule'
        const { connectionId } = this
        const planInstanceId = planInstance.id
        this.$router.push({ name, params: { name, planId, planInstanceId, connectionId } })
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Errro. Failed to get last run.')
      }).finally(() => { this.isSpinner = false })
    },
    triggerPlanChecker () {
      const { id } = this.p
      this.interval = setInterval(() => {
        this.reloadPlan(id).then((status) => {
          if (status !== 'running') { clearInterval(this.interval) }
        })
      })
    }
  }
}
</script>
