<template lang="pug">
.flex.justify-center
  .settings-layout(class="w-10/12")
    settings-navigator.nav
    .content
      router-view
</template>

<script>
import { SettingsNavigator } from '@/components/settings'

export default {
  components: {
    SettingsNavigator
  }
}
</script>

<style lang="postcss">
.settings-layout {
  @apply flex justify-center pt-10 content-center space-x-10;
}
.settings-layout .nav {
  @apply w-2/12;
}
.settings-layout .content {
  @apply w-6/12;
}
</style>
