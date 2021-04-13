/* eslint-disable camelcase */
import _ from 'lodash'
import qs from 'qs'
import { mapActions } from 'vuex'
import { loaderMixin } from '@/mixins'

export default {
  mixins: [loaderMixin],
  data () {
    return { info: {} }
  },
  computed: {
    hasExpression () {
      return this.info?.expressions?.length > 0
    },
    hasPolicy () {
      return this.info?.policies?.length > 0
    },
    menu () {
      switch (this.vendor) {
        case 'oracle': return this.menuOracle
        case 'mssql': return this.menuSqlServer
      }
    },
    menuSqlServer () {
      return [{
        name: 'Add masking',
        value: 'add-masking',
        icon: 'las la-theater-masks',
        path: `masks/columns/edit?${qs.stringify(this.info)}`,
        disabled: this.m.type !== 'column' || !_.isEmpty(this.info)
      }, {
        name: 'Edit masking',
        value: 'edit-masking',
        icon: 'las la-pen',
        path: 'masks/columns/create',
        disabled: this.m.type !== 'column' || _.isEmpty(this.info)
      }]
    },
    menuOracle () {
      return [
        {
          name: 'Apply expression',
          value: 'apply-expression',
          icon: 'las la-stamp',
          disabled: !this.hasExpression,
          path: (() => {
            const { schema_name, table_name, column_name } = this.m
            const params = { schema_name, table_name, column_name }
            return `/connections/${this.connectionId}/oracle/expressions/apply?${qs.stringify(params)}`
          })()
        },
        {
          name: 'Add to policy',
          value: 'add-column',
          icon: 'las la-plus',
          disabled: this.hasExpression || !this.hasPolicy,
          path: (() => {
            const { schema_name: object_owner, table_name: object_name, column_name } = this.m
            if (this.info?.policies?.length > 0) {
              const { policy_name } = this.info.policies[0]
              const params = { policy_name, object_owner, object_name, column_name, action: 1 }
              return `/connections/${this.connectionId}/oracle/policies/edit?${qs.stringify(params)}`
            }
          })()
        },
        {
          name: 'Remove from policy',
          value: 'drop-column',
          icon: 'las la-minus',
          disabled: !this.hasExpression,
          path: (() => {
            const { schema_name: object_owner, table_name: object_name, column_name } = this.m
            if (this.info?.policies[0]) {
              const { policy_name } = this.info.policies[0]
              const params = { policy_name, object_owner, object_name, column_name, action: 2 }
              return `/connections/${this.connectionId}/oracle/policies/edit?${qs.stringify(params)}`
            }
          })()
        },
        {
          name: 'Create policy',
          value: 'create-policy',
          icon: 'las la-certificate',
          disabled: this.hasPolicy,
          path: (() => {
            return `/connections/${this.connectionId}/oracle/policies/create`
          })()
        }
      ]
    }
  },
  methods: {
    ...mapActions('redaction', ['askRedactionInfo']),
    ...mapActions('mask', ['getMaskedColumns']),
    askMaskingOracle (params) {
      this.startSpinner()
      this.askRedactionInfo(params)
        .then(result => { this.info = result })
        .finally(this.stopSpinner)
    },
    askMaskingSqlServer (params) {
      this.startSpinner()
      this.getMaskedColumns(params).then(result => {
        if (result.length > 0) {
          this.info = result[0]
        }
      }).finally(this.stopSpinner)
    },
    askMasking () {
      const { vendor } = this
      const { schema_name, table_name, column_name } = this.m
      const params = { schema_name, table_name, column_name }
      switch (vendor) {
        case 'oracle': this.askMaskingOracle(params); break
        case 'mssql': this.askMaskingSqlServer(params); break
      }
    }
  }
}
