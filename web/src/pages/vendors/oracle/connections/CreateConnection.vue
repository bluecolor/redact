<template lang="pug">
.flex.justify-center.flex-col(:class="{'pb-64': options.search.isFocus}")
  t-card
    template(v-slot:default)
      form(autocomplete="off" @submit="onCreate")
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
            t-input(v-model="payload.database" required)
        .form-item
          t-input-group(label='Username', required)
            t-input(v-model="payload.username" required)
        .form-item
          t-input-group(label='Password', required)
            t-input(v-model="payload.password" required type="password")
        .form-item
          t-input-group(label='Schemas in search', required)
            t-rich-select(v-model="payload.options.search.schemas" required
              :options="options.search.schemas"
              valueAttribute="schema_name"
              textAttribute="schema_name"
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
              t-button(@click="onTest" variant="secondary")
                span Test
            .end
              t-button(@click="onCancel" type="button" variant="error")
                | Close
</template>

<script>
import { mapActions } from 'vuex'
import connectionMixin from '@/mixins/connectionMixin'

export default {
  mixins: [connectionMixin],
  components: {
  },
  data () {
    return {
      isSpinner: false,
      isValid: false,
      payload: {
        vendor: 'oracle',
        name: '',
        host: 'localhost',
        port: 1521,
        database: 'orcl',
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
  methods: {
    ...mapActions('connection', ['createConnection']),
    onCreate (e) {
      e.preventDefault()
      this.isSpinner = true
      const options = JSON.stringify(this.payload.options)
      this.createConnection({ ...this.payload, options, vendor: 'oracle' }).then(() => {
        this.$toast.success('Success Connection created')
      }).finally(() => {
        this.isSpinner = false
      })
    }
  }
}
</script>

<style lang="postcss">
</style>
