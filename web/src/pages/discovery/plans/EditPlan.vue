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
              t-button(@click="onCancel" type="button" text="Close" variant="error")
</template>

<script>
/* eslint-disable camelcase */
import _ from 'lodash'
import { mapActions, mapGetters } from 'vuex'
import SimpleSpinner from '@/components/loaders'

export default {
  props: ['connectionId', 'id'],
  components: {
    SimpleSpinner
  },
  data () {
    return {
      isSpinner: false,
      isValid: false,
      payload: {
        id: +this.id,
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
    ...mapGetters('rule', ['rules']),
    ...mapGetters('md', ['schemas'])
  },
  methods: {
    ...mapActions('rule', ['getRules']),
    ...mapActions('plan', ['updatePlan', 'getPlan']),
    ...mapActions('md', ['getSchemas']),
    onSubmit (e) {
      e.preventDefault()
      this.isSpinner = true
      const schemas = JSON.stringify(this.payload.schemas)
      this.updatePlan({ ...this.payload, schemas }).then(() => {
        this.$toasted.success('Success. Plan updated')
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Error. Failed to update plan')
      }).finally(() => { this.isSpinner = false })
    },
    onCancel () { window.history.back() },
    setPayload (plan) {
      const { name, description, worker_count, sample_size } = plan
      const rules = _.map(plan.rules, r => r.id)
      const schemas = JSON.parse(plan.schemas)
      this.payload = { ...this.payload, name, description, rules, schemas, worker_count, sample_size }
    }
  },
  created () {
    this.isSpinner = true
    Promise
      .all([this.getPlan(+this.id), this.getRules(), this.getSchemas()])
      .then(([plan, rules, schemas]) => {
        this.setPayload(plan)
      }).finally(() => { this.isSpinner = false })
  }
}
</script>

<style lang="postcss">
</style>
