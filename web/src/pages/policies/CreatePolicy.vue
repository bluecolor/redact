<template lang="pug">
.flex.flex-col(class="w-3/4")
  t-card
    template(v-slot:default)
      form.flex.flex-col(autocomplete="off" @submit="onCreate")
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
          label.flex.items-center
            t-radio(name='options' value='custom'  v-model="method")
            span.ml-2.text-sm Custom
          label.flex.items-center.ml-2
            t-radio(name='options' value='category' v-model="method")
            span.ml-2.text-sm From category
        .category.flex.flex-col.gap-y-5(v-if="method==='category'")
          .form-item
            t-input-group(label='Category')
              t-select(
                v-model.number="categoryId"
                :options="categories",
                value-attribute='id',
                text-attribute="name"
              )
        .custom.flex.flex-col.gap-y-5(v-if="method==='custom'")
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
              t-textarea(v-model="payload.policy_expression_description" required autofocus)
        .form-item.mt-5
          .flex.justify-between.items-center
            t-simple-spinner(v-if="isSpinner")
            .flex.gap-x-3(v-else class="w-1/2")
              t-button(type="submit" value="submit" text="Save")
            .end
              t-button(@click="onCancel" text="Canlcel" variant="error")
</template>

<script>
/* eslint-disable camelcase */

import _ from 'lodash'
import { mapActions, mapGetters } from 'vuex'
import TSimpleSpinner from '@/components/loaders'

export default {
  props: ['connectionId'],
  components: {
    TSimpleSpinner
  },
  data () {
    return {
      isSpinner: false,
      isValid: false,
      method: 'custom',
      categoryId: undefined,
      payload: {
        object_schema: '',
        object_name: '',
        column_name: '',
        policy_name: '',
        function_type: undefined,
        function_parameters: undefined,
        expression: '',
        policy_expression_description: ''
      }
    }
  },
  computed: {
    ...mapGetters('md', ['objectSchemas', 'tables', 'columns']),
    ...mapGetters('redact', ['functionTypes', 'functionParameters']),
    ...mapGetters('category', ['categories']),
    payload_ () {
      if (this.categoryId) {
        const {
          function_type, function_parameters, policy_expression: {
            expression, policy_expression_description
          }
        } = _.find(this.categories, { id: this.categoryId })
        return {
          ...this.payload,
          function_type,
          function_parameters,
          expression,
          policy_expression_description
        }
      }
      return this.payload
    }
  },
  methods: {
    ...mapActions('md', ['getObjectSchemas', 'getTables', 'getColumns']),
    ...mapActions('redact', ['createPolicy', 'getFunctionTypes', 'getFunctionParameters']),
    ...mapActions('category', ['getCategories']),
    onCreate (e) {
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
      this.getColumns({ object_schema, object_name })
    },
    onOwnerSelect (owner) {
      this.getTables({ owner })
    },
    onTableSelect (table) {
      this.loadColumns()
    }
  },
  created () {
    this.getObjectSchemas()
    this.getFunctionTypes()
    this.getFunctionParameters()
    this.getCategories()
  }
}
</script>

<style lang="postcss">
</style>
