<template lang="pug">
.flex.justify-center.flex-col(class="w-3/4")
  form(autocomplete="off" @submit="onCreate")
    .form-item
      label Name
      input(v-model="payload.policy_expression_name" name='policy_expression_name' required autofocus)
    .form-item
      label Expression
      textarea(v-model="payload.expression" name='expression' required)
    .form-item
      label Description
      textarea(v-model="payload.policy_expression_description" name='policy_expression_description' required)
    .form-item.mt-5
      .flex.justify-between.items-center
        simple-spinner(v-if="isSpinner")
        .flex.gap-x-3(v-else class="w-1/2")
          button.btn(tag="button" type="submit" value="submit")
            span Save
        .end
          button.btn(tag="button" @click="onCancel")
            | Close
</template>

<script>

import { mapActions } from 'vuex'
import { SimpleSpinner } from '@/components/loaders'

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
    ...mapActions('redact', ['createExpression']),
    onCreate (e) {
      e.preventDefault()
      this.isSpinner = true
      const { connectionId } = this
      this.createExpression({ connectionId, ...this.payload }).then(() => {
        this.$toast.success('Success Expression created')
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
