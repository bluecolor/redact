<template lang="pug">
.flex.justify-center.flex-col
  t-card
    template(v-slot:default)
      form(autocomplete="off" @submit="onSubmit")
        .form-item
          t-input-group(label='Name', required)
            t-input(v-model="payload.name")
        .form-item
          t-input-group(label='Username', required)
            t-input(v-model="payload.username"  required)
        .form-item
          t-input-group(label='Email', required)
            t-input(v-model="payload.email" required)
        .form-item
          t-input-group(label='Password', required)
            t-input(v-model="payload.password" required type="password")
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
import { mapActions } from 'vuex'

export default {
  components: {
  },
  data () {
    return {
      isSpinner: false,
      isValid: false,
      payload: {
        name: '',
        username: '',
        email: '',
        password: ''
      }
    }
  },
  methods: {
    ...mapActions('user', ['createUser']),
    onCancel () {
      window.history.back()
    },
    onSubmit (e) {
      e.preventDefault()
      this.isSpinner = true
      console.log(this.payload)
      this.createUser(this.payload).then(() => {
        this.$toast.success('Success. User created')
      }).finally(() => {
        this.isSpinner = false
      })
    }
  }
}
</script>

<style lang="postcss">
</style>
