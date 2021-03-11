<template lang="pug">
.policies-container
  .bg-white.empty.w-full(v-if="isPlanInstancesEmpty")
    .text-xl.text-gray-400.text-center There is nothing here!
    .project-logo.flex.justify-center.mt-10.w-full()
      svg-icon(name="cloud-computing", addClass="fill-current text-gray-300 w-24 h-24")
  .flex.justify-center.w-full(v-else)
    .body.w-full.flex.items-center.flex-col
      .plan-runs.gap-y-3.flex.flex-col.w-full
        .toolbar.p-5.w-full.bg-gray-50.rounded-md
          t-datepicker(v-model="date" placeholder="Pick a date")

        t-card.card(v-for="p in planInstances")
          template(v-slot:header)
            .flex.justify-between
              .title
                | {{p.plan.name}} {{fromNow(p.created_on)}}
              .actions.flex.justify-end
                .btns.gap-x-3.flex(v-if="!isSpinner")
                  router-link.icon-btn.las.la-info-circle(
                    content="Discoveries" v-tippy='{ placement : "top" }'
                    :to="`instances/${p.id}/discoveries-by-rule`")
                  router-link.icon-btn.las.la-stop-circle(
                    content="Stop" v-tippy='{ placement : "top" }'
                    :to="`policies/edit?policy_name=${encodeURI(p.policy_name)}&object_owner=${encodeURI(p.object_owner)}&object_name=${encodeURI(p.object_name)}`")
                  .icon-btn.las.la-trash-alt.danger(
                    content="Delete" v-tippy='{ placement : "top" }'
                    @click="onDelete()"
                  )
                .spinner.lds-dual-ring(v-else)
          template(v-slot:default)
            | Content of the card.
</template>

<script>
import { mapActions } from 'vuex'
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
      title: 'Plan Runs',
      planInstances: [],
      data: undefined
    }
  },
  computed: {
    isPlanInstancesEmpty () {
      return this.planInstances.length === 0
    }
  },
  methods: {
    ...mapActions('discovery', ['getAllPlanInstances']),
    load () {
      this.isSpinner = true
      return this.getAllPlanInstances().then(result => {
        this.planInstances = result
      }).finally(() => { this.isSpinner = false })
    }
  },
  mounted () {
    this.load()
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
