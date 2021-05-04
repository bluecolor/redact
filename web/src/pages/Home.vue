<template lang="pug">
.flex.justify-center
  .pt-20(class="w-5/12")
    .flex.flex-col.w-full.justify-center.gap-y-12(v-if="!isConnectionsEmpty")
      .title.text-center.text-2xl
        | Connections
      .grid.grid-cols-3.gap-8.w-full(style="grid-auto-rows: 1fr;")
        quick-connect-card.w-full(v-for="c in connections" :c="c")
        add-connection-card
    .bg-white.empty.w-full(v-if="isConnectionsEmpty")
      .text-xl.text-gray-400.text-center There is nothing here!
      .flex.justify-center.mt-10.w-full()
        svg-icon(name="box", addClass="fill-current text-gray-300 w-24 h-24")
      .flex.justify-center.mt-10
        t-button.mt-10.w-full.text-center(tagName="a" :href="`/settings/connections/vendors`")
          | Create New Connection

</template>

<script>

import { mapGetters } from 'vuex'
import SvgIcon from '@/components/SvgIcon'
import QuickConnectCard from '@/components/QuickConnectCard'
import AddConnectionCard from '@/components/AddConnectionCard'

export default {
  name: 'Home',
  components: {
    SvgIcon, QuickConnectCard, AddConnectionCard
  },
  data () {
    return {
    }
  },
  computed: {
    ...mapGetters('connection', ['connections']),
    isConnectionsEmpty () {
      return this.connections.length === 0
    }
  },
  methods: {
  }
}
</script>
