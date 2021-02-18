<template lang="pug">
.flex.justify-center
  .settings-layout(class="w-10/12")
    left-nav.left-nav(:connectionId="connectionId")
    .content
      router-view
</template>

<script>
import { mapActions } from 'vuex'
import LeftNav from '@/components/LeftNav'

export default {
  props: ['connectionId'],
  components: {
    LeftNav
  },
  methods: {
    ...mapActions('app', ['setConnection'])
  },
  watch: {
    connectionId (id) {
      this.setConnection(id)
    }
  },
  created () {
    this.setConnection(this.connectionId)
  }

}
</script>

<style lang="postcss">
.settings-layout {
  @apply flex justify-center pt-10 content-center space-x-10;
}
.settings-layout .left-nav {
  @apply w-2/12;
}
.settings-layout .content {
  @apply w-6/12;
}
</style>
