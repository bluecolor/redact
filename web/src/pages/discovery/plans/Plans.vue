<template lang="pug">
.container
  .empty.w-full.bg-white(v-if="isPlansEmpty")
    .text-xl.text-gray-400.text-center There is nothing here!
    .project-logo.flex.justify-center.mt-10.w-full()
      svg-icon(name="box", addClass="fill-current text-gray-300 w-24 h-24")
    .flex.justify-center.mt-10
      t-button.mt-10.w-full.text-center(tagName="a" :href="`/connections/${connectionId}/discovery/plans/create`")
        | Create New Plan
  .flex.justify-center.w-full(v-else)
    .body.w-full.flex.items-center.flex-col
      .gap-y-3.flex.flex-col.w-full
        plan-card(v-for="p in plans" :p="p")
      t-button.mt-10.w-full.text-center(tagName="a" :href="`/connections/${connectionId}/discovery/plans/create`")
        | Create New Plan

</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import SvgIcon from '@/components/SvgIcon'
import PlanCard from '@/components/PlanCard'

export default {
  props: ['connectionId'],
  components: {
    SvgIcon, PlanCard
  },
  data () {
    return {
      isSpinner: false
    }
  },
  computed: {
    ...mapGetters('plan', ['plans']),
    isPlansEmpty () {
      return this.plans.length === 0
    }
  },
  methods: {
    ...mapActions('plan', ['getPlans'])
  },
  created () {
    this.getPlans()
  }
}
</script>

<style lang="postcss" scoped>
.empty {
  @apply border-dashed p-3 border-2 rounded-md w-full
}
</style>
