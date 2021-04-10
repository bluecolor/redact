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
import { mapGetters } from 'vuex'

export default {
  data () {
    return {
    }
  },
  computed: {
    ...mapGetters('app', ['connectionId']),
    items () {
      return [{ category: true, title: 'Redaction' }, {
        path: `/connections/oracle/${this.connectionId}/policies`,
        title: 'Policies',
        group: 'policies',
        icon: 'las la-certificate'
      }, {
        path: `/connections/oracle/${this.connectionId}/expressions`,
        title: 'Expressions',
        group: 'expressions',
        icon: 'las la-code'
      }, {
        path: `/connections/oracle/${this.connectionId}/categories`,
        title: 'Categories',
        group: 'categories',
        icon: 'las la-tag'
      }, { category: true, title: 'Discovery' }, {
        path: `/connections/oracle/${this.connectionId}/discovery/explore`,
        title: 'Explore',
        group: 'explore',
        icon: 'las la-compass'
      }, {
        path: `/connections/oracle/${this.connectionId}/discovery/rules`,
        title: 'Rules',
        group: 'rules',
        icon: 'las la-ruler'
      }, {
        path: `/connections/oracle/${this.connectionId}/discovery/plans`,
        title: 'Plans',
        group: 'plans',
        icon: 'las la-box'
      }, {
        path: `/connections/oracle/${this.connectionId}/discovery/plans/instances`,
        title: 'Plan Runs',
        group: 'planInstances',
        icon: 'las la-shipping-fast'
      }, { category: true, title: 'Settings' },
      {
        path: `/connections/oracle/${this.connectionId}/settings/export-import`,
        title: 'Export/Import',
        group: 'export-import',
        icon: 'las la-share'
      }]
    },
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
