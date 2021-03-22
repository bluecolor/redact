<template lang="pug">
.w-full.flex.items-center.flex-col
  .w-full.bg-white.empty.border-dashed(v-if="isConnectionsEmpty")
    .text-xl.text-gray-400.text-center There is nothing here!
    .project-logo.flex.justify-center.mt-10(class="h-1/4 ")
      svg-icon(name="box", addClass="fill-current text-gray-300 w-24 h-24")
    .flex.justify-center.mt-10
      t-button.mt-10.w-full.text-center(tagName="a" :href="`/settings/connections/create`")
        | Create New Connection
  .connections.gap-y-3.flex.flex-col.w-full(v-if="!isConnectionsEmpty")
    connection-card.card(v-for="c in connections" :c="c")

    t-button.mt-10.w-full.text-center(tagName="a" href="connections/create" text="Create New Connection")
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import SvgIcon from '@/components/SvgIcon'
import ConnectionCard from '@/components/ConnectionCard'

export default {
  components: {
    SvgIcon, ConnectionCard
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
    ...mapActions('connection', ['deleteConnection', 'testConnection', 'getConnections']),
    onDelete (id) {
      this.isSpinner = true
      this.deleteConnection(id).finally(() => { this.isSpinner = false })
    },
    onTest (id) {
      this.isSpinner = true
      this.testConnection(id).then(result => {
        if (result) {
          this.$toast.success('Success')
        } else {
          this.$toast.success('Error')
        }
      }).catch(e => {
        console.log(e)
        this.$toast.error('Error!')
      }).finally(() => {
        this.isSpinner = false
      })
    },
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
  @apply  p-3 border-2 w-2/4 rounded-md
}
.empty {
  @apply border-dashed p-3 border-2 rounded-md w-full
}

</style>
