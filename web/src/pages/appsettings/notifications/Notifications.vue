<template lang="pug">
.flex.justify-center.flex-col
  t-card
    template(v-slot:default)
      form(autocomplete="off" @submit="onSubmit")
        .form-item
          t-input-group(label='Send mail on:', required)
            t-checkbox-group(
              v-model="payload.redaction.events" :options="redaction.events" autofocus
            )
          t-input-group(label='To:', required)
            t-rich-select(v-model="payload.redaction.users" required
              :options="users"
              valueAttribute="id"
              textAttribute="name"
              multiple
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
import _ from 'lodash'
import { mapActions, mapGetters } from 'vuex'

export default {
  components: {
  },
  data () {
    return {
      isSpinner: false,
      isValid: false,
      redaction: {
        events: [
          { text: 'Create Policy', value: 'create-policy' },
          { text: 'Create Expression', value: 'create-expression' },
          { text: 'Drop Policy', value: 'drop-polciy' },
          { text: 'Drop Column', value: 'drop-column' },
          { text: 'Apply Expression', value: 'apply-expression' },
          { text: 'Disable Policy', value: 'disable-policy' },
          { text: 'Enable Policy', value: 'enable-policy' }
        ]
      },
      payload: {
        redaction: {
          events: [],
          users: []
        }

      }
    }
  },
  computed: {
    ...mapGetters('user', ['users'])
  },
  methods: {
    ...mapActions('user', ['getUsers']),
    ...mapActions('appsetting', ['setAppSettings', 'getAppSettings']),
    onCancel () {
      window.history.back()
    },
    getRedactionEvents () {
      const name = 'events.redaction'
      const value = JSON.stringify(this.payload.redaction)
      return { name, value }
    },
    initSettings (settings) {
      _.each(settings, ({ name, value }) => {
        switch (name) {
          case 'events.redaction':
            this.payload.redaction = { ...JSON.parse(value) }
        }
      })
    },
    onSubmit (e) {
      e.preventDefault()
      this.isSpinner = true
      const payload = []
      payload.push(this.getRedactionEvents())
      this.setAppSettings(payload).then(() => {
        this.$toasted.success('Success. Settings updated')
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Error. Failed to update settings')
      }).finally(() => { this.isSpinner = false })
    }
  },
  created () {
    this.isSpinner = true
    const u = this.getUsers()
    const s = this.getAppSettings()
    Promise.all([u, s]).then(([users, settings]) => {
      this.initSettings(settings)
    }).finally(() => { this.isSpinner = false })
  }
}
</script>

<style lang="postcss">
</style>
