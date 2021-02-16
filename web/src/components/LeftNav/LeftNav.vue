<template lang="pug">
.left-nav.flex.w-full
  nav.nav-menu
    router-link.nav-item(
      v-for="i in items"
      :to="i.path"
      :class="{'selected': i.group && routeGroup && routeGroup === i.group}") {{i.title}}
</template>

<script>
export default {
  props: ['connectionId'],
  data () {
    return {
      items: [{
        path: `/connections/${this.connectionId}/expressions`,
        title: 'Expressions',
        group: 'expressions'
      }, {
        path: `/connections/${this.connectionId}/categories`,
        title: 'Categories',
        group: 'categories'
      }, {
        path: '/',
        title: 'Policies',
        group: 'policies'
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
  @apply flex flex-col w-full;
  /* align-self: baseline; */
}
.left-nav .nav-item {
  @apply w-full border-b p-3 border-l border-r text-gray-500 hover:text-gray-800 hover:bg-gray-50 text-sm border-l-0;
}
.left-nav .nav-item:first-child {
  @apply border-t rounded-t-md;
}
.left-nav .nav-item:last-child {
  @apply rounded-b-md;
}
.left-nav .nav-item.selected {
  @apply border-l-4 text-gray-800;
  border-left-color: #DC2626;
}

</style>
