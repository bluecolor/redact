<template lang="pug">
.flex.justify-center.flex-col(:class="{'pb-64': options.search.isFocus}")
  t-card
    template(v-slot:default)
      form(autocomplete="off" @submit="onSubmit")
        .form-item
          t-input-group(label='Name', required)
            t-input(v-model="payload.name")
        .form-item
          t-input-group(label='Host', required)
            t-input(v-model="payload.host" placeholder="host name or ip address" required)
        .form-item
          t-input-group(label='Port', required)
            t-input(v-model.number="payload.port" required type="number")
        .form-item
          t-input-group(label='Service', required)
            t-input(v-model="payload.service" required)
        .form-item
          t-input-group(label='Username', required)
            t-input(v-model="payload.username" required)
        .form-item
          t-input-group(label='Password', required)
            t-input(v-model="payload.password" required type="password")
        t-input-group(label='Schemas in search', required)
          t-rich-select(v-model="payload.options.search.schemas"
            :options="options.search.schemas"
            valueAttribute="name"
            textAttribute="name"
            multiple
            @focus="onSearchSchemasFocus",
            @blur="onSearchSchemasBlur"
          )
        .form-item.mt-5
          .flex.justify-between.items-center
            .spinner.lds-dual-ring(v-if="isSpinner")
            .flex.gap-x-3(v-else class="w-1/2")
              t-button(type="submit" value="submit")
                span Save
              t-button(@click="onTest" type="button" variant="secondary")
                span Test
            .end
              t-button(@click="onCancel" type="button" variant="error")
                | Close
</template>

<script>
import _ from 'lodash'
import { mapGetters, mapActions } from 'vuex'
import connectionMixin from '@/mixins/connectionMixin'

export default {
  props: ['id'],
  mixins: [connectionMixin],
  data () {
    return {
      isSpinner: false,
      isValid: false,
      options: {
        search: {
          isFocus: false,
          isSpinner: false,
          schemas: []
        }
      },
      payload: {
        name: '',
        host: '',
        port: undefined,
        database: '',
        username: '',
        password: '',
        options: {
          search: {
            schemas: []
          }
        }
      }
    }
  },
  computed: {
    ...mapGetters('connection', ['connections'])
  },
  methods: {
    ...mapActions('connection', [
      'createConnection', 'getConnections', 'getConnection',
      'updateConnection']),
    onSubmit (e) {
      e.preventDefault()
      this.isSpinner = true
      const options = JSON.stringify(this.payload.options)
      this.updateConnection({ ...this.payload, options, vendor: 'mssql' }).then(() => {
        this.$toasted.success('Success. Connection updated')
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Error. Failed to update connection')
      }).finally(() => {
        this.isSpinner = false
      })
    },
    loadConnection (connection) {
      let options = this.payload.options
      try {
        options = JSON.parse(connection.options) ?? {}
        options = _.extend(this.payload.options, options)
        if (!_.isEmpty(options?.search?.schemas)) {
          this.options.search.schemas = _.map(options?.search?.schemas, s => ({ name: s }))
        }
      } catch (e) {
        console.log(e)
      }
      this.payload = { ...this.payload, ...connection, options }
      return connection
    }
  },
  mounted () {
    this.isSpinner = true
    const id = +this.id
    this.getConnection(id).then(result => {
      this.loadConnection(result)
    }).catch(error => {
      console.log(error)
      this.$toasted.error('Failed to find connection')
    }).finally(() => {
      this.isSpinner = false
    })
  }
}
</script>

<style lang="postcss">
</style>
