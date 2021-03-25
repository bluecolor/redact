<template lang="pug">
.flex.justify-center
  .pt-20(class="w-6/12")
    .empty.bg-white(v-if="isConnectionsEmpty")
      .text-xl.text-gray-400.text-center There is nothing here!
        .flex.justify-center.mt-10.w-full()
          svg-icon(name="box", addClass="fill-current text-gray-300 w-24 h-24")
        .flex.justify-center.mt-10
          t-button.mt-10.w-full.text-center(tagName="a" href="/")
            | Create New Conneciton
    .flex.w-full.justify-center(v-if="!isConnectionsEmpty")
      .grid.grid-cols-3.gap-4.w-full()
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
