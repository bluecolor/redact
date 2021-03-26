<template lang="pug">
.left-nav.flex.w-full.fit
  nav.nav-menu.flex
    template(v-for="i in items")
      .nav-category.bg-white.flex.items-center.gap-x-2(
        v-if="i.category"
      ) {{i.title}}
      router-link.nav-item.bg-white.flex.items-center.gap-x-2.cursor-pointer(
        v-else
        :to="i.path"
        :class="{'selected': i.group && routeGroup && routeGroup === i.group}"
      )
        .icon-btn(:class="i.icon")
        .title {{i.title}}
</template>

<script>
export default {
  props: ['connectionId'],
  data () {
    return {
      items: [
        { category: true, title: 'Profile' },
        {
          path: '/settings/profile',
          title: 'Profile',
          group: 'profile',
          icon: 'las la-id-card'
        },
        {
          path: '/settings/preferences',
          title: 'Preferences',
          group: 'preferences',
          icon: 'las la-cog'
        },
        { category: true, title: 'System' }, {
          path: '/settings/connections',
          title: 'Connections',
          group: 'connections',
          icon: 'las la-plug'
        }, {
          path: '/settings/users',
          title: 'Users',
          group: 'users',
          icon: 'las la-user'
        }, {
          path: '/settings/notifications',
          title: 'Notifications',
          group: 'notifications',
          icon: 'las la-bell'
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
.left-nav .nav-category:first-child {
  @apply border-t rounded-t-md;
}
.left-nav .nav-category{
  @apply font-medium bg-gray-50 w-full border-b p-3 border-r text-gray-400 text-sm border-l;
}
.left-nav nav.nav-menu {
  @apply flex flex-col w-full;
  /* align-self: baseline; */
}
.left-nav .nav-item {
  @apply w-full border-b p-3 border-r text-gray-500 hover:text-gray-800 hover:bg-gray-50 text-sm border-l;
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
