<template lang="pug">
.policies-container
  .bg-white.empty.w-full(v-if="isPlanInstancesEmpty")
    .text-xl.text-gray-400.text-center There is nothing here!
    .project-logo.flex.justify-center.mt-10.w-full()
      svg-icon(name="box", addClass="fill-current text-gray-300 w-24 h-24")
  .flex.justify-center.w-full(v-else)
    .body.w-full.flex.items-center.flex-col
      .connections.gap-y-3.flex.flex-col.w-full
        plan-instance-card(v-for="p in planInstances" :p="p" @delete="onDelete" @reload="onReloadOne", @stop="onStop")
</template>

<script>
import _ from 'lodash'
import { mapActions } from 'vuex'
import SvgIcon from '@/components/SvgIcon'
import PlanInstanceCard from '@/components/PlanInstanceCard'

export default {
  props: ['connectionId', 'planId'],
  components: {
    SvgIcon, PlanInstanceCard
  },
  data () {
    return {
      isSpinner: false,
      title: 'Plan Runs',
      planInstances: []
    }
  },
  computed: {
    isPlanInstancesEmpty () {
      return this.planInstances.length === 0
    }
  },
  methods: {
    ...mapActions('planInstance', ['getPlanInstancesByPlan']),
    load () {
      this.isSpinner = true
      return this.getPlanInstancesByPlan(+this.planId).then(result => {
        this.planInstances = result
      }).finally(() => { this.isSpinner = false })
    },
    onDelete ({ id }) {
      const i = _.findIndex(this.planInstances, { id })
      if (i > -1) {
        this.planInstances.splice(i, 1)
      }
    },
    replace (p) {
      const { id } = p
      const i = _.findIndex(this.planInstances, { id })
      if (i > -1) {
        this.planInstances.splice(i, 1, p)
      }
    },
    onStop (p) {
      this.replace(p)
    },
    onReloadOne (p) {
      this.replace(p)
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
