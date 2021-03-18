<template lang="pug">
.policies-container
  .bg-white.empty.w-full(v-if="isDiscoveriesEmpty")
    .text-xl.text-gray-400.text-center There is nothing here!
    .project-logo.flex.justify-center.mt-10.w-full()
      svg-icon(name="box", addClass="fill-current text-gray-300 w-24 h-24")
  .flex.justify-center.w-full(v-else)
    .body.w-full.flex.items-center.flex-col
      .connections.gap-y-3.flex.flex-col.w-full
        discovery-rule-card(v-for="d in discoveries" :d="d")
</template>

<script>
/* eslint-disable camelcase */
import { mapActions } from 'vuex'
import SvgIcon from '@/components/SvgIcon'
import { dateMixin } from '@/mixins'
import DiscoveryRuleCard from '@/components/DiscoveryRuleCard'

export default {
  mixins: [dateMixin],
  props: ['connectionId', 'planInstanceId', 'planId'],
  components: {
    SvgIcon, DiscoveryRuleCard
  },
  data () {
    return {
      isSpinner: false,
      title: 'Discoveries',
      discoveries: [],
      planInstance: {}
    }
  },
  computed: {
    isDiscoveriesEmpty () {
      return this.discoveries.length === 0
    }
  },
  methods: {
    ...mapActions('discovery', ['getDiscoveriesGroupByRule']),
    load () {
      this.isSpinner = true
      const planId = +this.planId
      const planInstanceId = +this.planInstanceId
      this.getDiscoveriesGroupByRule({ planId, planInstanceId }).then(result => {
        this.discoveries = result
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
