<template lang="pug">
.flex.justify-center
  .connection-layout(class="w-10/12")
    connection-side-nav.left-nav(:connectionId="connectionId")
    .content.pb-10
      router-view
</template>

<script>
import { mapActions } from 'vuex'
import ConnectionSideNav from '@/components/ConnectionSideNav'

export default {
  props: ['connectionId'],
  components: {
    ConnectionSideNav
  },
  methods: {
    ...mapActions('app', ['setConnection'])
  },
  watch: {
    connectionId (id) {
      this.setConnection(id)
    }
  },
  created () {
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
