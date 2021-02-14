<template lang="pug">
.page
  .flex.justify-center.flex-col(class="w-1/3")
    form.mt-10(autocomplete="off" @submit="onCreate")
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
        button.btn(tag="button" type="submit" value="submit")
          .pr-8.lds-dual-ring(v-if="isSpinner")
          |Create

</template>

<script>
import { mapActions } from 'vuex'

export default {
  components: {
  },
  data () {
    return {
      isSpinner: false,
      isValid: false,
      payload: {
        name: '',
        host: '',
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
