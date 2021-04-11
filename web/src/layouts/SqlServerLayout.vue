<template lang="pug">
.w-full
  t-alert.alert(v-if="!connectionSuccess" variant="danger" show)
      | Not connected! Some of the features will not work.
      | Please check connection to database.
  .flex.justify-center
    .connection-layout(class="w-10/12")
      side-nav.left-nav(:connectionId="connectionId")
      .content.pb-10
        router-view
</template>

<script>
import _ from 'lodash'
import { mapActions, mapGetters } from 'vuex'
import SideNav from '@/components/vendors/mssql/SideNav'

export default {
  props: ['connectionId'],
  components: {
    SideNav
  },
  data () {
    return { connectionSuccess: true }
  },
  methods: {
    ...mapActions('app', ['setConnection']),
    checkConnection (id) {
      const conn = _.find(this.connections, { id })
      if (conn && conn.status === false) {
        this.connectionSuccess = false
      } else {
        this.connectionSuccess = true
      }
    }
  },
  computed: {
    ...mapGetters('connection', ['connections'])
  },
  watch: {
    connectionId (id) {
      this.setConnection(+id)
      this.checkConnection(+id)
    }
  },
  mounted () {
    this.checkConnection(+this.connectionId)
    this.setConnection(+this.connectionId)
  }

}
</script>

<style lang="postcss">
.connection-layout {
  @apply flex justify-center content-center space-x-10 pt-10;
}
.connection-layout .left-nav {
  @apply w-2/12;
}
.connection-layout .content {
  @apply w-6/12;
}
</style>

<style scoped>
.alert {
  border-radius: 0px;
}
</style>
