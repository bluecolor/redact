<template lang="pug">
.flex.justify-center.flex-col
  t-card
    template(v-slot:default)
      form(autocomplete="off" @submit="onSubmit")
        .form-item
          t-input-group(label='Name', required)
            t-input(disabled v-model="policy_expression_name" required autofocus)
        .form-item
          t-input-group(label='Expression', required)
            t-textarea(disabled v-model="expression" required)
        .form-item
          t-input-group(label='Description', required)
            t-textarea(disabled v-model="policy_expression_description")
        .form-item
          t-input-group(label='Schema', required)
            t-select(
              v-model="payload.object_schema"
              placeholder="Select schema"
              :options="policyOwners",
              value-attribute='schema_name',
              text-attribute="schema_name"
              required
              @input="onOwnerSelect"
            )
        .form-item
          t-input-group(label='Table', required)
            t-select(
              v-model="payload.object_name"
              placeholder="Select table"
              :options="policyTables",
              value-attribute='table_name',
              text-attribute="table_name"
              required
              @input="onTableSelect"
            )
        .form-item
          t-input-group(label='Column', required)
            t-select(
              v-model="payload.column_name"
              placeholder="Select column"
              :options="columns",
              value-attribute='column_name',
              text-attribute="column_name"
              required
            )
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
      policyOwners: [],
      policyTables: [],
      columns: [],
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
    ...mapActions('column', { getRedColumns: 'getColumns' }),
    ...mapActions('expression', ['getExpression', 'applyExpressionToColumn']),
    ...mapActions('policy', ['getPolicies', 'getPolicyOwners', 'getPolicyTables']),
    onSubmit (e) {
      e.preventDefault()
      this.isSpinner = true
      const { policy_expression_name } = this
      this.applyExpressionToColumn({ ...this.payload, policy_expression_name }).then(() => {
        this.$toasted.success('Success. Expression applied')
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Error. Failed to appy expression')
      }).finally(() => {
        this.isSpinner = false
      })
    },
    onCancel () { window.history.back() },
    onOwnerSelect (owner) {
      this.isSpinner = true
      this.getPolicyTables(owner).then(result => {
        this.policyTables = result
      }).finally(() => {
        this.isSpinner = false
      })
    },
    onTableSelect (table_name) {
      this.isSpinner = true
      const object_owner = this.payload.object_schema
      const { object_name } = this.payload
      this.getRedColumns({ object_owner, object_name })
        .then(result => { this.columns = result }).finally(() => {
          this.isSpinner = false
        })
    },
    load () {
      const { policy_expression_name } = this
      this.isSpinner = true

      const e = this.getExpression(policy_expression_name)
      const o = this.getPolicyOwners()

      Promise.all([e, o]).then(([exp, owners]) => {
        this.expression = exp.expression
        this.policy_expression_description = exp.policy_expression_description
        this.policyOwners = owners
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
