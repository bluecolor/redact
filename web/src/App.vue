<template lang="pug">
#app
  router-view
</template>

<script>

export default {
  name: 'App',
  components: {
  },
  data () {
    return {
    }
  }
}
</script>

<style lang="postcss">
#app {
  @apply flex-grow
  /* height: 100%; */
  /* height:calc(100vh + 100px); */
}
</style>
