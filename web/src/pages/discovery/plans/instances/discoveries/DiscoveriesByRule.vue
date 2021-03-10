<template lang="pug">
.policies-container
  .bg-white.empty.w-full(v-if="isDiscoveriesEmpty")
    .text-xl.text-gray-400.text-center There is nothing here!
    .project-logo.flex.justify-center.mt-10.w-full()
      svg-icon(name="cloud-computing", addClass="fill-current text-gray-300 w-24 h-24")
  .flex.justify-center.w-full(v-else)
    .body.w-full.flex.items-center.flex-col
      .connections.gap-y-3.flex.flex-col.w-full
        t-card.card(v-for="d in discoveries")
          template(v-slot:header)
            .flex.justify-between
              .title
                | {{d.rule.name}}
              .actions.flex.justify-end
                .btns.gap-x-3.flex(v-if="!isSpinner")
                  router-link.icon-btn.las.la-info-circle(
                    content="Details" v-tippy='{ placement : "top" }'
                    :to="`/`"
                  )
                .spinner.lds-dual-ring(v-else)
          template(v-slot:default)
            .flex.gap-x-3
              t-tag(tag-name="span" variant="badge") {{d.rule.type}}
              .result
                | {{d.count}} findings

</template>

<script>
/* eslint-disable camelcase */
import _ from 'lodash'
import { mapActions } from 'vuex'
import SvgIcon from '@/components/SvgIcon'
import { dateMixin } from '@/mixins'

export default {
  mixins: [dateMixin],
  props: ['connectionId', 'planInstanceId'],
  components: {
    SvgIcon
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
    ...mapActions('discovery', ['getDiscoveries', 'getPlanInstance']),
    load () {
      this.isSpinner = true
      const planInstanceId = +this.planInstanceId
      const query = { by_rule: true }
      return Promise.all([
        this.getDiscoveries({ planInstanceId, query }),
        this.getPlanInstance(planInstanceId)
      ]).then(([discoveries, planInstance]) => {
        this.discoveries = _.map(discoveries, ({ rule_id, count }) => {
          const rule = _.find(planInstance?.plan?.rules, { id: rule_id })
          return { rule, count }
        })
        this.planInstance = planInstance
      }).finally(() => { this.isSpinner = false })
    }
  },
  mounted () {
    this.load()
    const ws = new WebSocket('ws://localhost:8000/api/v1/ws/plans/instances')
    ws.onmessage = (message) => {
      console.log(message)
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
