<template lang="pug">
.connections-container.flex.justify-center(class=" sm:px-6 lg:px-8")
  .body.w-full.flex.items-center.flex-col.py-10
    .empty(v-if="isConnectionsEmpty")
      .text-xl.text-gray-400.text-center There is nothing here!
      .project-logo.flex.justify-center.mt-10(class="h-1/4 ")
        svg-icon(name="cloud-computing", addClass="fill-current text-gray-300 w-24 h-24")
      .flex.justify-center.mt-10
        t-button.mt-10.w-full.text-center(tagName="a" :href="`/connections/create`")
          | Create New Connection
    .connections.gap-y-3.flex.flex-col.w-full(v-if="!isConnectionsEmpty")
      t-card.card(v-for="c in connections" :connection="c")
        template(v-slot:header)
          .flex.justify-between
            .title
              | {{c.name}}
            .actions.flex.justify-end
              .btns.gap-x-3.flex(v-if="!isSpinner")
                router-link.icon-btn.las.la-pen(:to="`connections/${c.id}/edit`" v-slot="{ navigate }")
                .icon-btn.las.la-vial(@click="onTest(c.id)")
                .icon-btn.las.la-trash-alt.danger(@click="onDelete(c.id)")
              .spinner.lds-dual-ring(v-else)
        template(v-slot:default)
          |{{c.host}}:{{c.port}}/{{c.service}}
    t-button.mt-10.w-full.text-center(tagName="a" href="connections/create" text="Create New Connection")
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import SvgIcon from '@/components/SvgIcon'
// import PageLoader from '@/components/loaders'

export default {
  components: {
    SvgIcon
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
  @apply border-dashed p-3 border-2 w-2/4 rounded-md
}

</style>
