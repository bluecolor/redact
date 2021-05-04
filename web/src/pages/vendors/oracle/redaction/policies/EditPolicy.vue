<template lang="pug">
.flex.flex-col
  t-card
    template(v-slot:default)
      form.flex.flex-col(autocomplete="off" @submit="onSubmit")
        .form-item
          t-input-group(label='Name')
            t-input(v-model="payload.policy_name" required autofocus disabled)
        .form-item
          t-input-group(label='Schema')
            t-select(
              disabled
              v-model="payload.object_schema"
              placeholder="Select schema",
              :options="schemas"
              required
            )
        .form-item
          t-input-group(label='Tables')
            t-select(
              disabled
              :options="tables"
              v-model="payload.object_name"
              placeholder="Select table"
              required
            )
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
          t-input-group(label='Action')
            t-select(
              :disabled="isActionsDisabled"
              placeholder="Select action"
              v-model.number="payload.action"
              :options="actions",
              value-attribute='action',
              text-attribute="name"
            )
        .form-item(v-if="payload.action==3")
          t-input-group(label='Expression')
            t-textarea(v-model="payload.expression" autofocus)
        .form-item(v-if="payload.action==5")
          t-input-group(label='Description')
            t-textarea(v-model="payload.policy_description" autofocus)
        .form-item(v-if="[1, 2, 4, 6].indexOf(+payload.action) > -1")
          t-input-group(label='Column')
            t-select(
              :disabled="isColumnsDisabled"
              placeholder="Select column"
              v-model="payload.column_name"
              :options="calculatedColumns",
              required
            )
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
  props: {
    connectionId: { type: (Number, String) }
  },
  components: {
    TSimpleSpinner
  },
  data () {
    return {
      isSpinner: false,
      isValid: false,
      method: 'custom',
      categoryId: undefined,
      redColumns: [],
      columns: [],
      tables: [],
      schemas: [],
      calculatedColumns: [],
      payload: {
        object_schema: '',
        object_name: '',
        column_name: '',
        policy_name: '',
        action: 3,
        function_type: undefined,
        function_parameters: undefined,
        expression: '',
        policy_description: ''
      }
    }
  },
  watch: {
    'payload.action' (action) {
      if ([1, 2, 4, 6].indexOf(+action) !== -1) {
        const promises = []
        const {
          policy_name, object_name, object_owner
        } = this.$route.query
        if (this.redColumns.length === 0) {
          promises.push(this.getRedColumns({ policy_name, object_name, object_owner }))
        }
        if (this.columns.length === 0) {
          promises.push(this.getColumns({ schema_name: object_owner, table_name: object_name }))
        }
        this.isSpinner = true
        Promise.all([...promises, Promise.resolve()]).then((result) => {
          const [redColumns, columns] = _.take(result, 2)
          this.redColumns = redColumns ?? this.redColumns
          this.columns = columns ?? this.columns
          this.calculateColumns()
        }).finally(() => { this.isSpinner = false })
      }
    }
  },
  computed: {
    ...mapGetters('func', ['actions', 'functionTypes', 'functionParameters']),
    ...mapActions('policy', ['policies']),
    ...mapGetters('category', ['categories']),
    isActionsDisabled () {
      return !_.isEmpty(this.$route.query.action)
    },
    isColumnsDisabled () {
      return !_.isEmpty(this.$route.query.column_name)
    }
  },
  methods: {
    ...mapActions('column', { getRedColumns: 'getColumns' }),
    ...mapActions('md', ['getColumns']),
    ...mapActions('func', ['getActions', 'getFunctionTypes', 'getFunctionParameters']),
    ...mapActions('policy', ['updatePolicy', 'getPolicy']),
    ...mapActions('category', ['getCategories']),
    calculateColumns () {
      switch (+this.payload.action) {
        case 1: // add column
          this.calculatedColumns = _.chain(this.columns).map(c => c.column_name)
            .difference(_.map(this.redColumns, c => c.name))
            .value()
          break
        case 2: // drop column
        case 4: // modify column
        case 6: // set column desciption
          this.calculatedColumns = _.map(this.redColumns, c => c.column_name)
          break
      }
    },
    onSubmit (e) {
      e.preventDefault()
      this.isSpinner = true
      this.updatePolicy(this.payload).then(() => {
        this.$toast.success('Success. Updated policy')
      }).catch(error => {
        console.log(error)
        this.$toast.error('Error. Failed update policy')
      }).finally(() => {
        this.isSpinner = false
      })
    },
    onCancel () { window.history.back() },
    loadColumns () {
      const { object_schema, object_name } = this.payload
      return this.getColumns({ object_schema, object_name })
    },
    getFunctionTypeId (name) {
      // todo
      // in redaction_columns table function type is text
      // all types shoud match an id
      switch (name) {
        case 'FULL REDACTION': return 1
      }
    }
  },
  created () {
    this.isSpinner = true
    const {
      action, column_name, policy_name, object_name, object_owner
    } = this.$route.query
    const promises = [
      this.getPolicy({ policy_name, object_name, object_owner }),
      this.getColumns({ schema_name: object_owner, table_name: object_name }),
      this.getRedColumns({ object_owner, object_name, column_name })
    ]
    promises.push(this.getFunctionTypes())
    promises.push(this.getFunctionParameters())
    promises.push(this.getActions())

    Promise.all(promises).then(([policy, columns, redColumns]) => {
      const { object_owner, ...p } = policy
      let function_type, function_parameters
      if (!_.isEmpty(redColumns)) {
        function_type = this.getFunctionTypeId(redColumns[0].function_type)
        function_parameters = redColumns[0].function_parameters
      }
      this.payload = {
        ...this.payload,
        object_schema: object_owner,
        ...p,
        action,
        column_name,
        function_type,
        function_parameters
      }
      this.schemas.push(object_owner)
      this.tables.push(object_name)
      this.columns = columns
    }).finally(() => {
      this.isSpinner = false
    })
  }
}
</script>

<style lang="postcss">
</style>
