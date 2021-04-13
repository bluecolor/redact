<template lang="pug">
.flex.justify-center
  .notifications-layout(class="w-10/12")
    .content
      .empty.w-full(v-if="isNotificationsEmpty")
        .text-xl.text-gray-400.text-center There is nothing here!
        .flex.justify-center.mt-10.w-full()
          svg-icon(name="box", addClass="fill-current text-gray-300 w-24 h-24")
      notification-card(v-for="n in notifications", :n="n")
      t-button.mt-10.w-full.text-center(@click="onClear" variant="secondary") Clear All
</template>

<script>
import SvgIcon from '@/components/SvgIcon'
import { loaderMixin } from '@/mixins'
import { mapGetters, mapActions } from 'vuex'
import NotificationCard from '@/components/NotificationCard'

export default {
  mixins: [loaderMixin],
  components: {
    SvgIcon, NotificationCard
  },
  computed: {
    ...mapGetters('notification', ['notifications']),
    isNotificationsEmpty () {
      return this.notifications.length === 0
    }
  },
  methods: {
    ...mapActions('notification', ['clearNotifications']),
    onClear () {
      this.clearNotifications()
    }
  },
  watch: {
  }
}
</script>

<style lang="postcss">
.notifications-layout {
  @apply flex justify-center content-center space-x-10 pt-10;
}
.notifications-layout .content {
  @apply w-6/12;
}
</style>
