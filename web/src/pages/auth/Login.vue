<template lang="pug">
.min-h-screen.flex.items-center.justify-center.bg-gray-50.py-12.px-4(class='sm:px-6 lg:px-8')
  .max-w-md.w-full.space-y-8
    div
      img.mx-auto.h-12.w-auto(src='@/svg/duck.svg' alt='Duck')
      h2.mt-6.text-center.text-3xl.font-extrabold.text-gray-900
        | Sign in to your account
    form.mt-8.space-y-6(autocomplete="off" @submit="onSubmit")
      .space-y-4
        t-input(v-model="payload.username" required autofocus placeholder="Username")
        t-input(v-model="payload.password" required placeholder="Password" type="password")
      t-button(text="Sign In" type="sumbit")
</template>

<script>
import { mapActions } from 'vuex'

export default {
  data () {
    return {
      payload: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    ...mapActions('auth', ['login']),
    onSubmit (e) {
      e.preventDefault()
      this.login(this.payload).then(response => {
        console.log(response)
        this.$router.push({ path: '/' })
      })
    }
  },
  mounted () {
  }
}
</script>
