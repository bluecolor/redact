<template lang="pug">
.flex.flex-col
  .loader.text-gray-600(v-if="isLoading")
  t-card(v-else)
    template(v-slot:default)
      form.flex.flex-col(autocomplete="off" @submit="onSubmit")
        .form-item
          t-input-group(label='Schema')
            t-select(
              v-model="payload.schema_name"
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
              v-model="payload.table_name"
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
              required
            )
        .form-item
          t-input-group(label='Function')
            t-select(
              v-model="payload.func"
              placeholder="Select masking function"
              :options="functions",
              value-attribute='name',
              text-attribute="title",
              @input="onFunctionSelect"
              required
            )
        .form-item(v-if="argsPlaceHolder")
          t-input-group(label='Function parameters')
            t-input(v-model="payload.args" :placeholder="argsPlaceHolder")
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
import _ from 'lodash'
import { loaderMixin } from '@/mixins'
import { mapActions } from 'vuex'

export default {
  props: ['connectionId'],
  components: {
  },
  mixins: [loaderMixin],
  data () {
    return {
      isValid: false,
      columns: [],
      tables: [],
      functions: [],
      schemas: [],
      argsPlaceHolder: undefined,
      payload: {
        func: undefined,
        args: undefined,
        schema_name: '',
        table_name: '',
        column_name: ''
      }
    }
  },
  computed: {
  },
  methods: {
    ...mapActions('md', ['getSchemas', 'getTables', 'getColumns']),
    ...mapActions('mask', ['getMaskingFunctions', 'addMask']),
    onCancel () { window.history.back() },
    onFunctionSelect (name) {
      const { args } = _.find(this.functions, { name })
      this.argsPlaceHolder = args
    },
    onSchemaSelect (schema_name) {
      this.startSpinner()
      this.getTables(schema_name).then(result => {
        this.tables = result
      }).finally(this.stopSpinner)
    },
    onTableSelect () {
      const { schema_name, table_name } = this.payload
      this.startSpinner()
      this.getColumns({ schema_name, table_name }).then(result => {
        this.columns = result
      }).finally(this.stopSpinner)
    },
    onSubmit (e) {
      e.preventDefault()
      this.startSpinner()
      this.addMask(this.payload).then(() => {
        this.$toasted.success('Success. Mask added')
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Error. Failed to add mask')
      }).finally(this.stopSpinner)
    }
  },
  created () {
    this.startLoader()
    Promise.all([this.getSchemas(), this.getMaskingFunctions()]).then(([schemas, functions]) => {
      this.schemas = schemas
      this.functions = functions
    }).finally(this.stopLoader)
  }
}
</script>

<style lang="postcss">
</style>
