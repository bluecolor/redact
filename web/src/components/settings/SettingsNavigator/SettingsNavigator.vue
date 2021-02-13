<template lang="pug">
.settings-navigator.flex.w-full
  nav.menu
    router-link.setting(to="/settings/projects" :class="{'selected': routeGroup === 'projects'}") Projects
    router-link.setting(to="/settings/profiles" :class="{'selected': routeGroup === 'profiles'}") Profiles
    router-link.setting(to="/settings/connections" :class="{'selected': routeGroup === 'connections'}") Connections
    router-link.setting(to="/settings/appearance" :class="{'selected': routeGroup === 'appearance'}") Appearance
    router-link.setting(to="#") Users
</template>

<script>
export default {
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
.settings-navigator nav.menu {
  @apply inline-flex flex-col border rounded-sm w-full border-l-0;
  align-self: baseline;
}
.settings-navigator .setting {
  @apply w-full p-2 text-gray-500 hover:text-gray-800 hover:bg-gray-50 text-sm border-l;
}
.settings-navigator .setting:not(:last-child) {
  @apply p-2 border-b;
}
.settings-navigator .setting.selected {
  @apply border-l-4 text-gray-800;
  border-left-color: #9CA3AF;
}

</style>
