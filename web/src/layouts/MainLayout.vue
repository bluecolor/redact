<template lang="pug">
.main-layout.w-full.main-layout
  navbar.z-40.navbar
  .page-container.h-full.w-full.overflow-hidden.flex.flex-col
    router-view

</template>

<script>
import Navbar from '@/components/Navbar'
import { mapActions } from 'vuex'

export default {
  props: ['connectionId'],
  name: 'App',
  components: {
    Navbar
  },
  data () {
    return {
      ws: undefined
    }
  },
  watch: {
    connectionId () {
      if (!this.connectionId) {
        this.setConnection(undefined)
      }
    }
  },
  methods: {
    ...mapActions('app', ['setConnection']),
    ...mapActions('notification', ['addNotification'])
  },
  created () {
    const { connectionId } = this.$route.params
    if (connectionId) {
      this.setConnection(+connectionId)
    } else {
      this.setConnection(undefined)
    }
    const channel = 'ws/notifications'
    this.ws = new WebSocket(`ws://localhost:8000/api/v1/${channel}`)
    this.ws.onmessage = ({ data }) => {
      try {
        this.addNotification(JSON.parse(data))
      } catch (e) {
        console.log(e)
        console.warn('Unable to parse notification', data)
      }
    }
  },
  beforeDestroy () {
    this.ws.close()
  }
}
</script>

<style>
.main-layout {
  height: 100%;
}
.navbar {
    position: fixed;
    right:0;
    left:0;
    top: 0;
    z-index:300;
}
.main-layout {
  padding-bottom: 50px;
}
.page-container {
    padding-top:50px;
    position:relative;
    z-index:200;
    height: 100%;
}
</style>
