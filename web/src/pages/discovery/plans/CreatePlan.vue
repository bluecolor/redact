<template lang="pug">
.flex.justify-center.flex-col
  t-card
    template(v-slot:default)
      form(autocomplete="off" @submit="onSubmit")
        .form-item
          t-input-group(label='Name', required)
            t-input(v-model="payload.name" required autofocus)
        .form-item
          t-input-group(label='Rules', required)
            t-rich-select(v-model="payload.rules" required
              :options="rules"
              valueAttribute="id"
              textAttribute="name"
              multiple
            )
        .form-item
          t-input-group(label='Schemas', required)
            t-rich-select(v-model="payload.schemas" required
              :options="schemas"
              valueAttribute="schema_name"
              textAttribute="schema_name"
              multiple
            )
        .form-item
          t-input-group(label='Sample Size')
            t-input(v-model.number="payload.sample_size")
        .form-item
          t-input-group(label='Number of Workers')
            t-input(v-model.number="payload.worker_count")
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

import { loaderMixin } from '@/mixins'
import { mapActions, mapGetters } from 'vuex'
import SimpleSpinner from '@/components/loaders'

export default {
  mixins: [loaderMixin],
  props: ['connectionId'],
  components: {
    SimpleSpinner
  },
  data () {
    return {
      isValid: false,
      schemas: [],
      payload: {
        name: '',
        rules: [],
        schemas: [],
        sample_size: 5000,
        worker_count: 4,
        description: ''
      }
    }
  },
  computed: {
    ...mapGetters('rule', ['rules'])
  },
  methods: {
    ...mapActions('rule', ['getRules']),
    ...mapActions('plan', ['createPlan']),
    ...mapActions('md', ['getSchemas']),
    onSubmit (e) {
      e.preventDefault()
      this.isSpinner = true
      const schemas = JSON.stringify(this.payload.schemas)
      this.createPlan({ ...this.payload, schemas }).then(() => {
        this.$toasted.success('Success. Created plan')
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Error. Failed to create plan')
      }).finally(() => { this.isSpinner = false })
    },
    onCancel () { window.history.back() }
  },
  created () {
    this.startSpinner()
    Promise.all([this.getRules(), this.getSchemas()]).then(([rules, schemas]) => {
      this.schemas = schemas
    }).finally(this.stopSpinner)
  }
}
</script>

<style lang="postcss">
</style>
