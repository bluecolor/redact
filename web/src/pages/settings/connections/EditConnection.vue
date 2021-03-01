<template lang="pug">
.page
  //- page-loader(v-if="isPageLoader")
  .flex.justify-center.flex-col(class="w-1/3")
    form.mt-10(autocomplete="off" @submit="onSubmit")
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
      .form-item.mt-5
        .flex.justify-between.items-center
          t-simple-spinner(v-if="isSpinner")
          .flex.gap-x-3(v-else class="w-1/2")
            t-button(type="submit" value="submit" variant="secondary")
              span Save
            t-button(@click="onTest" variant="secondary")
              span Test
          .end
            t-button(@click="onCancel" variant="error")
              | Close
</template>

<script>
import _ from 'lodash'
import { mapGetters, mapActions } from 'vuex'
import TSimpleSpinner from '@/components/loaders'
import mixin from './mixin'

export default {
  props: ['id'],
  mixins: [mixin],
  components: {
    TSimpleSpinner
  },
  data () {
    return {
      isPageLoader: false,
      isSpinner: false,
      isValid: false,
      payload: {
        name: '',
        host: '',
        port: undefined,
        service: '',
        username: '',
        password: ''
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
      this.updateConnection(this.payload).then(() => {
        this.$toasted.success('Success. Connection updated')
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Error. Failed to update connection')
      }).finally(() => {
        this.isSpinner = false
      })
    },
    loadConnection (c) {
      if (_.isObject(c)) {
        this.payload = { ...c }
        return c
      } else {
        const connection = _.find(this.connections, { c })
        if (connection) {
          this.payload = { ...connection }
          return connection
        }
      }
    }
  },
  mounted () {
    this.isPageLoader = true
    const id = +this.id
    if (!this.loadConnection(id)) {
      this.isPageLoader = true
      this.getConnection(id).then(result => {
        this.loadConnection(result)
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Failed to find connection')
      }).finally(() => {
        this.isPageLoader = false
      })
    }
  }
}
</script>

<style lang="postcss">
</style>
