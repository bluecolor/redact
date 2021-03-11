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
                  .icon-btn.las.la-info-circle(
                    content="Delete" v-tippy='{ placement : "top" }'
                    @click="onDelete()"
                  )
                .spinner.lds-dual-ring(v-else)
          template(v-slot:default)
            | {{d.schema_name}}.{{d.table_name}}.{{d.column_name}}
      .loading.p-10.w-full.flex.bg-white(v-if="isLoading && this.items.length > 0")
        | Loading....

</template>

<script>
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
      discoveries: []
    }
  },
  computed: {
    isDiscoveriesEmpty () {
      return this.discoveries.length === 0
    }
  },
  methods: {
    ...mapActions('discovery', ['getDiscoveries']),
    load () {
      this.isSpinner = true
      const planInstanceId = +this.planInstanceId
      this.getDiscoveries({ planInstanceId })
        .then(result => {
          this.discoveries = result
        })
        .finally(() => { this.isSpinner = false })
    }
  },
  mounted () {
    this.load()
    const ws = new WebSocket('ws://localhost:8000/api/v1/ws/plans/instances')
    ws.onmessage = (message) => {
      console.log(message)
    }
  },
  created () {
    this.load = _.debounce(this.load, 300)
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
