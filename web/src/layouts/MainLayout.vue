<template lang="pug">
.main-layout.h-full.w-full.overflow-y-hidden
  navbar.z-40(@toggle-left-menu="isSidebarOpen=!isSidebarOpen")
  .page-container.h-full.w-full.overflow-hidden
    router-view
</template>

<script>
import Sidebar from '@/components/Sidebar'
import HelloWorld from '@/components/HelloWorld.vue'
import Navbar from '@/components/Navbar'

export default {
  name: 'App',
  components: {
    HelloWorld,
    Navbar,
    Sidebar
  },
  data () {
    return {
      isSidebarOpen: false
    }
  },
  mounted () {
  }
}
</script>
