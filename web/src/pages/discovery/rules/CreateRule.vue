<template lang="pug">
.flex.justify-center.flex-col(class="w-3/4")
  t-card
    template(v-slot:default)
      form(autocomplete="off" @submit="onSubmit")
        .form-item
          t-input-group(label='Name', required)
            t-input(v-model="payload.name" required autofocus)
        .form-item
          t-input-group(label='Type')
            t-select(
              v-model="payload.type"
              :options="types",
              value-attribute='value',
              text-attribute="text"
            )
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
  props: ['connectionId'],
  components: {
    SimpleSpinner
  },
  data () {
    return {
      isSpinner: false,
      isValid: false,
      types: [
        { value: 'metadata', text: 'Naming' },
        { value: 'data', text: 'Data' }
      ],
      severities: [
        { value: 'low', text: 'Low' },
        { value: 'medium', text: 'Medium' },
        { value: 'high', text: 'High' }],
      payload: {
        name: '',
        type: 'metadata',
        severity: 'low',
        expression: '',
        description: ''
      }
    }
  },
  methods: {
    ...mapActions('discovery', ['createRule']),
    onSubmit (e) {
      e.preventDefault()
      this.isSpinner = true
      this.createRule(this.payload).then(() => {
        this.$toast.success('Success. Rule created')
      }).finally(() => {
        this.isSpinner = false
      }).catch(error => {
        console.log(error)
        this.$toast.error('Error. Failed to create rule')
      })
    },
    onCancel () { window.history.back() }
  }
}
</script>

<style lang="postcss">
</style>
