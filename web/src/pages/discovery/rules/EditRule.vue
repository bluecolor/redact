<template lang="pug">
.flex.justify-center.flex-col(class="w-3/4")
  t-card
    template(v-slot:default)
      form(autocomplete="off" @submit="onSubmit")
        .form-item
          t-input-group(label='Name', required)
            t-input(v-model="payload.name" required autofocus)
        .form-item
          t-input-group(label='Severity')
            t-select(
              v-model="payload.severity"
              :options="severities",
              value-attribute='value',
              text-attribute="text"
            )
        .form-item
          t-input-group(label='Expression', required)
            t-textarea(v-model="payload.expression" required)
        .form-item
          t-input-group(label='Description', required)
            t-textarea(v-model="payload.description")
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
  props: ['id'],
  components: {
    SimpleSpinner
  },
  data () {
    return {
      isSpinner: false,
      isValid: false,
      severities: [
        { value: 'low', text: 'Low' },
        { value: 'medium', text: 'Medium' },
        { value: 'high', text: 'High' }],
      payload: {
        id: +this.id,
        name: '',
        expression: '',
        description: ''
      }
    }
  },
  methods: {
    ...mapActions('rule', ['getRule', 'updateRule']),
    onSubmit (e) {
      e.preventDefault()
      this.isSpinner = true
      this.updateRule(this.payload).then(() => {
        this.$toast.success('Success. Rule updated')
      }).finally(() => {
        this.isSpinner = false
      }).catch(error => {
        console.log(error)
        this.$toast.error('Error. Failed to update rule')
      })
    },
    onCancel () { window.history.back() },
    load () {
      this.isSpinner = true
      this.getRule(+this.id).then(result => {
        const { id, name, expression, description } = result
        this.payload = { id, name, expression, description }
        return this.payload
      }).finally(() => {
        this.isSpinner = false
      })
    }
  },
  created () {
    this.load()
  }
}
</script>

<style lang="postcss">
</style>
