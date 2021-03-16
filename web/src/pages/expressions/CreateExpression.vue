<template lang="pug">
.flex.justify-center.flex-col
  t-card
    template(v-slot:default)
      form(autocomplete="off" @submit="onSumbit")
        .form-item
          t-input-group(label='Name', required)
            t-input(v-model="payload.policy_expression_name" required autofocus)
        .form-item
          t-input-group(label='Expression', required)
            t-textarea(v-model="payload.expression" required)
        .form-item
          t-input-group(label='Description', required)
            t-textarea(v-model="payload.policy_expression_description")
        .form-item.mt-5
          .flex.justify-between.items-center
            simple-spinner(v-if="isSpinner")
            .flex.gap-x-3(v-else class="w-1/2")
              t-button(type="submit" value="submit" text="Save")
            .end
              t-button(@click="onCancel" text="Close" variant="error")
</template>

<script>

import { mapActions } from 'vuex'
import SimpleSpinner from '@/components/loaders'

export default {
  props: ['connectionId'],
  components: {
    SimpleSpinner
  },
  data () {
    return {
      isSpinner: false,
      isValid: false,
      payload: {
        policy_expression_name: '',
        expression: '',
        policy_expression_description: ''
      }
    }
  },
  methods: {
    ...mapActions('expression', ['createExpression']),
    onSumbit (e) {
      e.preventDefault()
      this.isSpinner = true
      const { connectionId } = this
      this.createExpression({ connectionId, ...this.payload }).then(() => {
        this.$toasted.success('Success. Expression created')
      }).catch(error => {
        console.log(error)
        this.$toasted.success('Error. Failed to create expression')
      }).finally(() => {
        this.isSpinner = false
      })
    },
    onCancel () { window.history.back() }
  }
}
</script>

<style lang="postcss">
</style>
