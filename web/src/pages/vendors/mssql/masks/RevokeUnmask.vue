<template lang="pug">
.flex.flex-col
  .loader.text-gray-600(v-if="isLoading")
  t-card(v-else)
    template(v-slot:default)
      form.flex.flex-col(autocomplete="off" @submit="onSubmit")
        .form-item
          t-input-group(label='Schema')
            t-input(v-model="schema_name" required disabled)
        .form-item
          t-input-group(label='Table')
            t-input(v-model="table_name" required disabled)
        .form-item
          t-input-group(label='Column')
            t-input(v-model="column_name" required)
        .form-item
          t-input-group(label='Function')
            t-select(
              v-model="payload.username"
              placeholder="Select user"
              :options="users",
              value-attribute='username',
              text-attribute="username"
              required
            )
        .form-item.mt-5
          .flex.justify-between.items-center
            .spinner.lds-dual-ring(v-if="isSpinner")
            .flex.gap-x-3(v-else class="w-1/2")
              t-button(type="submit" value="submit" text="Save")
            .end
              t-button(@click="onCancel" type="button" text="Close" variant="error")
</template>

<script>
/* eslint-disable camelcase */
import { loaderMixin } from '@/mixins'
import { mapActions } from 'vuex'

export default {
  props: ['connectionId'],
  components: {
  },
  mixins: [loaderMixin],
  data () {
    return {
      isValid: false,
      users: [],
      ...this.$route.query,
      payload: {
        username: undefined
      }
    }
  },
  methods: {
    ...mapActions('connection', ['getUsers']),
    ...mapActions('mask', ['revokeUnmask']),
    onCancel () { window.history.back() },
    onSubmit (e) {
      e.preventDefault()
      this.startSpinner()
      this.revokeUnmask(this.payload).then(() => {
        this.$toasted.success('Success. Unmask revoked')
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Error. Failed revoke revoked')
      }).finally(this.stopSpinner)
    }
  },
  created () {
    this.startLoader()
    this.getUsers().then(result => {
      this.users = result
    }).finally(this.stopLoader)
  }
}
</script>

<style lang="postcss">
</style>
