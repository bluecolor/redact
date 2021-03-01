<template lang="pug">
.main-layout.w-full.main-layout
  navbar.z-40.navbar
  .page-container.h-full.w-full.overflow-hidden.flex.flex-col
    router-view

</template>

<script>
import Navbar from '@/components/Navbar'

export default {
  name: 'App',
  components: {
    Navbar
  },
  data () {
    return {
    }
  },
  mounted () {
  }
}
</script>

<style>
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
