<template lang="pug">
.flex.justify-center.flex-col
  t-card
    template(v-slot:default)
      form(autocomplete="off" @submit="onSubmit")
        .form-item
          t-input-group(label='Alerts:', required)
            t-checkbox-group(
              v-model="payload.alerts" :options="alerts" autofocus
            )
        .form-item.mt-5
          .flex.justify-between.items-center
            .spinner.lds-dual-ring(v-if="isSpinner")
            .flex.gap-x-3(v-else class="w-1/2")
              t-button(type="submit" value="submit")
                span Save
            .end
              t-button(@click="onCancel" type="button" variant="error")
                | Close
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  components: {
  },
  data () {
    return {
      isSpinner: false,
      isValid: false,
      alerts: [
        { text: 'User logged in', value: 'user-login' },
        { text: 'Plan run complete', value: 'instance-run-done' }
      ],
      payload: {
        alerts: []
      }
    }
  },
  computed: {
    ...mapGetters('user', ['current_user'])
  },
  methods: {
    ...mapActions('user', ['setPreferences', 'getMe']),
    onCancel () {
      window.history.back()
    },
    initPreferences () {
      const { preferences } = this.current_user
      if (!preferences) { return }
      this.payload = { ...JSON.parse(preferences) }
    },
    onSubmit (e) {
      e.preventDefault()
      this.isSpinner = true
      const payload = { preferences: { ...this.payload } }
      this.setPreferences(payload).then(() => {
        this.$toasted.success('Success. Updated your preferences')
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Error. Failed to update preferences')
      }).finally(() => {
        this.isSpinner = false
      })
    }
  },
  created () {
    this.isSpinner = true
    this.getMe().then(this.initPreferences).finally(() => { this.isSpinner = false })
  }
}
</script>

<style lang="postcss">
</style>
