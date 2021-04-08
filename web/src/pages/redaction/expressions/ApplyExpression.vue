<template lang="pug">
.flex.justify-center.flex-col
  t-card
    template(v-slot:default)
      form(autocomplete="off" @submit="onSubmit")
        .form-item
          t-input-group(label='Name', required)
            t-select(
              v-model="payload.policy_expression_name"
              placeholder="Select expression"
              :options="expressions",
              value-attribute='policy_expression_name',
              text-attribute="policy_expression_name"
              required
            )
        .form-item
          t-input-group(label='Schema', required)
            t-select(
              v-model="payload.object_schema"
              placeholder="Select schema"
              :options="policyOwners",
              value-attribute='name',
              text-attribute="name"
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
            .spinner.lds-dual-ring(v-if="isSpinner")
            .flex.gap-x-3(v-else class="w-1/2")
              t-button(type="submit" value="submit" text="Save")
            .end
              t-button(@click="onCancel" type="button" text="Close" variant="error")
</template>

<script>
/* eslint-disable camelcase */

import { mapActions } from 'vuex'

export default {
  props: ['connectionId'],
  components: {
  },
  data () {
    return {
      isSpinner: false,
      isValid: false,
      policy_expression_description: '',
      expressions: [],
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
    ...mapActions('expression', ['getExpressions', 'applyExpressionToColumn']),
    ...mapActions('policy', ['getPolicies', 'getPolicyOwners', 'getPolicyTables']),
    onSubmit (e) {
      e.preventDefault()
      this.isSpinner = true
      const { policy_expression_name } = this.payload
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
      this.isSpinner = true
      const { schema_name, table_name, column_name } = this.$route.query
      const promises = []
      promises.push(this.getExpressions())
      promises.push(this.getPolicyOwners())
      if (schema_name) {
        promises.push(this.getPolicyTables(this.schema_name))
      }
      if (table_name) {
        promises.push(this.getRedColumns({
          object_owner: this.schema_name,
          object_name: this.table_name
        }))
      }

      return Promise.all(promises).then(([expressions, owners, ...others]) => {
        this.expressions = expressions
        this.policyOwners = owners
        if (schema_name) {
          this.payload.object_schema = schema_name
        }
        if (table_name) {
          this.payload.object_name = table_name
        }
        if (column_name) {
          this.payload.column_name = column_name
        }
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
