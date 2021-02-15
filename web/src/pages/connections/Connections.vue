<template lang="pug">
.page
  page-loader(v-if="isSpinner")
  .connections-container.flex.justify-center.max-w-2xl(class="w-2/4 sm:px-6 lg:px-8")
    .body.w-full.flex.items-center.flex-col.py-10
      .empty(v-if="isConnectionsEmpty")
        .text-xl.text-gray-400.text-center There is nothing here!
        .project-logo.flex.justify-center.mt-10(class="h-1/4 ")
          svg-icon(name="cloud-computing", addClass="fill-current text-gray-300 w-24 h-24")
        .flex.justify-center.mt-10
          router-link.btn.create-btn.mt-10(tag="button" class="w-2/3" to="/connections/create")
            | Create New Connection
      .connections.gap-y-3.flex.flex-col.w-full(v-if="!isConnectionsEmpty")
        connection-card(v-for="c in connections" :connection="c")
      router-link.btn.create-btn.mt-10.w-full(tag="button" to="/connections/create")
        | Create New Connection
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import SvgIcon from '@/components/SvgIcon'
import PageLoader from '@/components/loaders'
import ConnectionCard from '@/components/ConnectionCard'

export default {
  components: {
    SvgIcon, PageLoader, ConnectionCard
  },
  data () {
    return {
      isSpinner: false,
      title: 'Connections'
    }
  },
  computed: {
    ...mapGetters('connection', ['connections', 'isConnectionsEmpty'])
  },
  methods: {
    ...mapActions('connection', ['getConnections']),
    load () {
      this.isSpinner = true
      this.getConnections().finally(() => { this.isSpinner = false })
    }
  },
  mounted () {
    this.load()
  }
}
</script>

<style lang="postcss">
.connections-container .empty {
  @apply border-dashed p-3 border-2 w-2/4 rounded-md
}

</style>
