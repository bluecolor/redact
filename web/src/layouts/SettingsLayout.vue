<template lang="pug">
.flex.justify-center
  .settings-layout(class="w-10/12")
    settings-side-nav.left-nav
    .content
      router-view
</template>

<script>
import SettingsSideNav from '@/components/SettingsSideNav'

export default {
  components: {
    SettingsSideNav
  },
  methods: {
  },
  watch: {
  }
}
</script>

<style lang="postcss">
.settings-layout {
  @apply flex justify-center content-center space-x-10 pt-10;
}
.settings-layout .left-nav {
  @apply w-2/12;
}
.settings-layout .content {
  @apply w-6/12;
}
</style>
