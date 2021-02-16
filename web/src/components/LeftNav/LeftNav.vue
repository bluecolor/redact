<template lang="pug">
.left-nav.flex.w-full.h-full
  nav.nav-menu
    router-link.nav-item(v-for="i in items" :to="i.path") {{i.title}}
</template>

<script>
export default {
  props: ['connectionId'],
  data () {
    return {
      items: [{
        path: `/connections/${this.connectionId}/expressions`,
        title: 'Expressions'
      }, {
        path: `/connections/${this.connectionId}/categories`,
        title: 'Categories'
      }, {
        path: '/',
        title: 'Policies'
      }]
    }
  },
  computed: {
    routeName () {
      return this.$route.name
    },
    routeGroup () {
      return this.$route.meta.group
    }
  }
}
</script>

<style lang="postcss">
.left-nav nav.nav-menu {
  @apply border rounded-sm flex flex-col w-full;
  /* align-self: baseline; */
}
.left-nav .nav-item {
  @apply w-full p-3 text-gray-500 hover:text-gray-800 hover:bg-gray-50 text-sm border-l-0;
}
.left-nav .nav-item:not(:last-child) {
  @apply border-b;
}
.left-nav .nav-item.selected {
  @apply border-l-4 text-gray-800;
  border-left-color: #9CA3AF;
}

</style>
