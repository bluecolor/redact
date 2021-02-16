<template lang="pug">
page-loader(v-if="isPageLoader")
.page
  .flex.justify-center.flex-col(class="w-1/3")
    form.mt-10(autocomplete="off" @submit="onSubmit")
      .form-item
        label Name
        input(v-model="payload.name" name='name' required autofocus)
      .form-item
        label Host
        input(v-model="payload.host" name='host' required)
      .form-item
        label Port
        input(v-model.number="payload.port" name='port' required type='number')
      .form-item
        label Service
        input(v-model="payload.service" name='service' required)
      .form-item
        label Username
        input(v-model="payload.username" name='username' required)
      .form-item
        label Password
        input(v-model="payload.password" name='password' type="password" required)
      .form-item.mt-5
        .flex.justify-between.items-center
          simple-spinner(v-if="isSpinner")
          .flex.gap-x-3(v-else class="w-1/2")
            button.btn(tag="button" type="submit" value="submit")
              span Save
            button.btn(tag="button" @click="onTest")
              span Test
          .end
            button.btn(tag="button" @click="onCancel")
              | Close

</template>

<script>
import _ from 'lodash'
import { mapGetters, mapActions } from 'vuex'
import PageLoader, { SimpleSpinner } from '@/components/loaders'
import mixin from './mixin'

export default {
  props: ['id'],
  mixins: [mixin],
  components: {
    SimpleSpinner, PageLoader
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
        this.$toast.success('Success. Connection updated')
      }).catch(error => {
        console.log(error)
        this.$toast.error('Error. Failed to update connection')
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
        this.$toast.error('Failed to find connection')
      }).finally(() => {
        this.isPageLoader = false
      })
    }
  }
}
</script>

<style lang="postcss">
</style>
