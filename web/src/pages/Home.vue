<template lang="pug">
.flex.justify-center
  .pt-20(class="w-5/12")
    .flex.flex-col.w-full.justify-center.gap-y-12(v-if="!isConnectionsEmpty")
      .title.text-center.text-2xl
        | Connections
      .grid.grid-cols-3.gap-8.w-full()
        quick-connect-card.w-full(v-for="c in connections" :c="c")
        add-connection-card
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
