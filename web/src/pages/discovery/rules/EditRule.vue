<template lang="pug">
.flex.justify-center.flex-col(class="w-3/4")
  t-card
    template(v-slot:default)
      form(autocomplete="off" @submit="onCreate")
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
        name: '',
        expression: '',
        description: ''
      }
    }
  },
  methods: {
    onCreate (e) {
      e.preventDefault()
    },
    onCancel () { window.history.back() }
  }
}
</script>

<style lang="postcss">
</style>
