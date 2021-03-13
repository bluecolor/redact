<template lang="pug">
.flex.justify-center.flex-col
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
            .end.flex.gap-x-2
              t-button(@click="onClear" type="button" text="Clear" variant="secondary")
              t-button(@click="onCancel" type="button" text="Close" variant="error")
</template>

<script>

import { mapActions } from 'vuex'
import SimpleSpinner from '@/components/loaders'
import ruleMixin from './ruleMixin'

export default {
  mixins: [ruleMixin],
  props: ['connectionId'],
  components: {
    SimpleSpinner
  },
  data () {
    return {
      isSpinner: false,
      isValid: false,
      payload_: {
        name: '',
        type: 'metadata',
        severity: 'low',
        expression: '',
        description: ''
      },
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
    ...mapActions('rule', ['createRule']),
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
    onCancel () { window.history.back() },
    onClear () {
      this.payload = { ...this.payload_ }
    }
  }
}
</script>

<style lang="postcss">
</style>
