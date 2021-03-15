<template lang="pug">
.flex.justify-center.flex-col
  t-card
    template(v-slot:default)
      form(autocomplete="off" @submit="onCreate")
        .form-item
          t-input-group(label='Name', required)
            t-input(disabled v-model="policy_expression_name" required autofocus)
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
/* eslint-disable camelcase */

import { mapActions } from 'vuex'
import SimpleSpinner from '@/components/loaders'

export default {
  props: ['connectionId', 'policy_expression_name'],
  components: {
    SimpleSpinner
  },
  data () {
    return {
      isSpinner: false,
      isValid: false,
      policy_expression_description: '',
      expression: '',
      polices: [],
      payload: {
        object_schema: '',
        object_name: '',
        column_name: ''
      }
    }
  },
  computed: {
  },
  methods: {
    ...mapActions('expression', ['getExpression']),
    ...mapActions('policy', ['getPolicies']),
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
    onCancel () { window.history.back() },
    load () {
      const { policy_expression_name } = this
      this.isSpinner = true
      this.getExpression(policy_expression_name).then(result => {
        this.expression = result.expression
        this.policy_expression_description = result.policy_expression_description
      }).finally(() => { this.isSpinner = false })
    }
  },
  created () {
    this.load()
  }
}
</script>

<style lang="postcss">
</style>
