<template lang="pug">
.flex.justify-center.flex-col
  .loader.text-gray-600(v-if="isLoading")
  t-card(v-else)
    template(v-slot:default)
      form(autocomplete="off" @submit="onSubmit")
        .form-item
          t-input-group(label='Category')
            t-input(v-model="category.name" required disabled)
        .form-item
          t-input-group(label='Expression Name')
            t-input(
              v-model="category.policy_expression_name"
              required
              disabled
            )
        .form-item
          t-input-group(label='Expression')
            t-textarea(
              v-if="category"
              v-model="category.expression"
              required
              disabled
            )
        .form-item
          t-input-group(label='Function Type')
            t-select(
              v-model.number="category.function_type"
              :options="functionTypes",
              value-attribute='function_type',
              text-attribute="name"
              disabled
            )
        .form-item
          t-input-group(label='Function Parameters')
            t-input(
              v-model="category.function_parameters"
              required
              disabled
            )
        .form-item
          t-input-group(label='Schema')
            t-select(
              v-model="payload.object_schema"
              placeholder="Select schema"
              :options="schemas",
              value-attribute='schema_name',
              text-attribute="schema_name"
              required
              @input="onSchemaSelect"
            )
        .form-item
          t-input-group(label='Table')
            t-select(
              v-model="payload.object_name"
              placeholder="Select table"
              :options="tables",
              value-attribute='table_name',
              text-attribute="table_name"
              required
              @input="onTableSelect"
            )
        .form-item
          t-input-group(label='Column')
            t-select(
              v-model="payload.column_name"
              placeholder="Select column"
              :options="columns",
              value-attribute='column_name',
              text-attribute="column_name"
              @input="onColumnSelect"
              required
            )
        .form-item(v-if="policy===null")
          t-alert(variant="warning" show :dismissible="false")
            | This table does not have a policy.
            | Supply policy name as well to create it.
        .form-item(v-if="expression")
          t-alert(variant="info" show :dismissible="false")
            | This column has an expression on it.
            | Saving will overwrite this expression.
        .form-item(v-if="policy===null")
          t-input-group(label='Policy Name')
            t-input(v-model="policy_name" required)
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
  props: ['connectionId', 'id'],
  components: {
    SimpleSpinner
  },
  data () {
    return {
      isLoading: false,
      isSpinner: false,
      isValid: false,
      category: {
        policy_expression_name: undefined,
        expression: undefined,
        function_type: undefined,
        function_parameters: ''
      },
      schemas: [],
      tables: [],
      columns: [],
      policy: undefined,
      policy_name: undefined,
      expression: undefined,
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
    ...mapActions('func', ['getFunctionTypes']),
    ...mapActions('policy', ['updatePolicy', 'createPolicy']),
    ...mapActions('expression', ['applyExpressionToColumn', 'getExpression']),
    ...mapActions('redaction', ['askRedactionPolicy', 'askRedactionExpression']),
    ...mapActions('md', ['getSchemas', 'getTables', 'getColumns']),
    ...mapActions('category', ['getCategory']),
    onSubmit (e) {
      e.preventDefault()
      if (!this.policy && !this.policy_name) {
        this.$toasted.info('Supply policy name.')
      }
      if (this.policy && !this.expression) {
        this.addColumnWithCategory()
      } else if (this.policy && this.expression) {
        this.applyExpressionWithCategory()
      } else if (!this.policy) {
        this.createPolicyWithCategory()
      }
    },
    onCancel () { window.history.back() },
    onSchemaSelect (s) {
      this.isSpinner = true
      return Promise.all(([
        this.getTables(s).then(result => { this.tables = result }),
        this.checkPolicy(),
        this.checkExpression()
      ])).finally(() => {
        this.isSpinner = false
      })
    },
    onTableSelect (t) {
      this.isSpinner = true
      return Promise.all([
        this.loadColumns(),
        this.checkPolicy(),
        this.checkExpression()
      ]).finally(() => {
        this.isSpinner = false
      })
    },
    loadColumns () {
      const { object_schema: schema_name, object_name: table_name } = this.payload
      this.getColumns({ schema_name, table_name }).then(result => { this.columns = result })
    },
    onColumnSelect (column_name) {
      return this.checkExpression()
    },
    checkPolicy () {
      const { object_schema: schema_name, object_name: table_name } = this.payload
      if (!table_name || !schema_name) {
        return
      }
      return this.askRedactionPolicy({ schema_name, table_name }).then(({ policy }) => {
        console.log(policy)
        this.policy = policy
        return policy
      })
    },
    checkExpression () {
      const { object_schema: schema_name, object_name: table_name, column_name } = this.payload
      if (!schema_name || !table_name || !column_name) {
        return
      }
      this.isSpinner = true
      return this.askRedactionExpression({ schema_name, table_name, column_name }).then(({ expression }) => {
        this.expression = expression
        return expression
      }).finally(() => { this.isSpinner = false })
    },
    applyExpressionWithCategory () {
      const { policy_expression_name } = this.category
      const { object_schema, object_name, column_name } = this.payload
      this.isSpinner = true
      this.applyExpressionToColumn({ policy_expression_name, object_schema, object_name, column_name }).then(result => {
        this.$toasted.success('Success. Category applied to column')
      }).catch(error => {
        this.$toasted.error('Error. Failed to add column to category')
        console.log(error)
      }).finally(() => { this.isSpinner = false })
    },
    createPolicyWithCategory () {
      const { object_schema, object_name, column_name } = this.payload
      const { policy_name } = this
      const { function_type, function_parameters } = this.category
      const { expression } = this.category
      if (!policy_name) {
        this.$toasted.info('Policy name must be given')
        return
      }
      this.isSpinner = true
      this.createPolicy({
        expression,
        object_schema,
        object_name,
        column_name,
        policy_name,
        function_type,
        function_parameters
      }).then(() => {
        this.$toasted.success('Success. Policy created with category')
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Error. Failed to create policy with given category')
      }).finally(() => { this.isSpinner = false })
    },
    addColumnWithCategory () {
      const action = 1 // add column
      const { object_schema, object_name, column_name } = this.payload
      const { policy_name } = this.policy
      const { expression, function_type, function_parameters } = this.category
      this.isSpinner = false
      this.updatePolicy({
        action,
        object_schema,
        object_name,
        column_name,
        policy_name,
        expression,
        function_type,
        function_parameters
      }).then(() => {
        this.$toasted.success('Success. Category applied to column')
      }).catch(error => {
        this.$toasted.error('Error. Failed to add column to category')
        console.log(error)
      }).finally(() => {
        this.isSpinner = false
      })
    }
  },
  created () {
    this.isLoading = true
    const promises = []
    promises.push(this.getCategory(+this.id))
    promises.push(this.getSchemas())
    promises.push(this.getFunctionTypes())
    Promise.all(promises).then(([category, schemas, functionTypes]) => {
      this.category = category
      this.functionTypes = functionTypes
      const { policy_expression_name, function_parameters, function_type } = JSON.parse(category.options)
      this.category = { ...this.category, function_parameters, function_type }
      this.getExpression(policy_expression_name).then(({ expression, function_type }) => {
        this.category = { ...this.category, policy_expression_name, expression, function_type, function_parameters }
      })
      this.schemas = schemas
    }).finally(() => { this.isLoading = false })
  }
}
</script>

<style lang="postcss">
</style>
