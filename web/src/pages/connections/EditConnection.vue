<template lang="pug">
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
              |Cancel

</template>

<script>
import { mapActions } from 'vuex'
import { SimpleSpinner } from '@/components/loaders'

export default {
  props: ['id'],
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
    ...mapActions('connection', ['createConnection', 'testConnection']),
    onSubmit (e) {
      e.preventDefault()
      this.isSpinner = true
    },
    onTest () {
      this.isSpinner = true
      this.testConnection(this.payload).then(result => {
        if (result) {
          this.$toast.success('Success')
        } else {
          this.$toast.error('Error')
        }
      }).catch(error => {
        console.log(error)
        this.$toast.error('Error')
      }).finally(() => {
        this.isSpinner = false
      })
    },
    onCancel () { window.history.back() }
  },
  mounted () {
    const id = +this.id
    console.log(id)
  }
}
</script>

<style lang="postcss">
</style>
