<template lang="pug">
.flex.justify-center.flex-col
  form.mt-10(autocomplete="off" @submit="onCreate")
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
        simple-spinner(v-if="isSpinner")
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
import { mapActions } from 'vuex'
import mixin from './mixin'
import { SimpleSpinner } from '@/components/loaders'

export default {
  mixins: [mixin],
  components: {
    SimpleSpinner
  },
  data () {
    return {
      isSpinner: false,
      isValid: false,
      payload: {
        name: '',
        host: 'localhost',
        port: 1521,
        service: 'orcl',
        username: '',
        password: ''
      }
    }
  },
  methods: {
    ...mapActions('connection', ['createConnection']),
    onCreate (e) {
      e.preventDefault()
      this.isSpinner = true
      this.createConnection(this.payload).then(() => {
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
