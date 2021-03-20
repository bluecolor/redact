<template lang="pug">
.flex.flex-col
  t-card
    template(v-slot:default)
      form.flex.flex-col(autocomplete="off" @submit="onSubmit")
        .form-item
          t-input-group(label='Name')
            t-input(v-model="payload.policy_name" required autofocus)
        .form-item
          t-input-group(label='Object Owners')
            t-select(
              v-model="payload.object_schema"
              placeholder="Select schema"
              :options="objectSchemas",
              value-attribute='name',
              text-attribute="name"
              required
              @input="onOwnerSelect"
            )
        .form-item
          t-input-group(label='Tables')
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
          t-input-group(label='Columns')
            t-select(
              v-model="payload.column_name"
              placeholder="Select column"
              :options="columns",
              value-attribute='column_name',
              text-attribute="column_name"
              required
            )
        .flex
          label.flex.items-center.cursor-pointer
            t-radio(name='options' value='custom'  v-model="method")
            span.ml-2.text-sm Custom
          label.flex.items-center.ml-2.cursor-pointer
            t-radio(name='options' value='category' v-model="method")
            span.ml-2.text-sm From category
        .flex.flex-col.gap-y-5(v-if="method==='category'")
          .form-item
            t-input-group(label='Category')
              t-select(
                v-model.number="categoryId"
                :options="categories",
                value-attribute='id',
                text-attribute="name"
              )
        .flex.flex-col.gap-y-5(v-if="method==='custom'")
          .form-item
            t-input-group(label='Function Type')
              t-select(
                v-model.number="payload.function_type"
                :options="functionTypes",
                value-attribute='function_type',
                text-attribute="name"
                required
              )
          .form-item
            t-input-group(label='Function Parameters')
              t-select(
                placeholder="Select parameters"
                v-model="payload.function_parameters"
                :options="functionParameters",
                value-attribute='function_parameters',
                text-attribute="function_parameters"
              )
          .form-item
            t-input-group(label='Expression')
              t-textarea(v-model="payload.expression" required autofocus)
          .form-item
            t-input-group(label='Description')
              t-textarea(v-model="payload.policy_description" required autofocus)
        .form-item.mt-5
          .flex.justify-between.items-center
            t-simple-spinner(v-if="isSpinner")
            .flex.gap-x-3(v-else class="w-1/2")
              t-button(type="submit" value="submit" text="Save")
            .end
              t-button(@click="onCancel" type="button" text="Close" variant="error")
</template>

<script>
/* eslint-disable camelcase */

import _ from 'lodash'
import { mapActions, mapGetters } from 'vuex'
import TSimpleSpinner from '@/components/loaders'

export default {
  props: ['connectionId', 'object_schema', 'object_name', 'column_name'],
  components: {
    TSimpleSpinner
  },
  data () {
    return {
      isSpinner: false,
      isValid: false,
      method: 'custom',
      categoryId: undefined,
      columns: [],
      tables: [],
      payload: {
        object_schema: this.object_schema,
        object_name: this.object_name,
        column_name: this.column_name,
        policy_name: '',
        function_type: undefined,
        function_parameters: undefined,
        expression: '',
        policy_description: ''
      }
    }
  },
  computed: {
    ...mapGetters('md', ['objectSchemas']),
    ...mapGetters('func', ['functionTypes', 'functionParameters']),
    ...mapGetters('category', ['categories']),
    payload_ () {
      if (this.categoryId) {
        const {
          function_type, function_parameters, policy_expression: {
            expression, policy_description
          }
        } = _.find(this.categories, { id: this.categoryId })
        return {
          ...this.payload,
          function_type,
          function_parameters,
          expression,
          policy_description
        }
      }
      return this.payload
    }
  },
  methods: {
    ...mapActions('md', ['getObjectSchemas', 'getTables', 'getColumns']),
    ...mapActions('policy', ['createPolicy']),
    ...mapActions('func', ['getFunctionTypes', 'getFunctionParameters']),
    ...mapActions('category', ['getCategories']),
    onSubmit (e) {
      e.preventDefault()
      this.isSpinner = true
      this.createPolicy(this.payload_).then(() => {
        this.$toast.success('Success. Policy created')
      }).catch(error => {
        console.log(error)
        this.$toast.error('Error. Failed to create policy')
      }).finally(() => {
        this.isSpinner = false
      })
    },
    onCancel () { window.history.back() },
    loadColumns () {
      const { object_schema, object_name } = this.payload
      this.getColumns({ object_schema, object_name }).then(result => { this.columns = result })
    },
    onOwnerSelect (owner) {
      this.getTables(owner).then(result => { this.tables = result })
    },
    onTableSelect (table) {
      this.loadColumns()
    }
  },
  created () {
    this.isSpinner = true
    const promises = [
      this.getObjectSchemas(),
      this.getFunctionTypes(),
      this.getFunctionParameters(),
      this.getCategories()
    ]

    if (this.object_name) {
      promises.push(this.onOwnerSelect(this.object_schema))
    }
    if (this.column_name) {
      promises.push(this.onTableSelect(this.object_name))
    }

    Promise.all(promises).finally(() => { this.isSpinner = false })
  }
}
</script>

<style lang="postcss">
</style>
