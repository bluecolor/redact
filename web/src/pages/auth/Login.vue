<template lang="pug">
.min-h-screen.flex.items-center.justify-center.bg-gray-50.py-12.px-4(class='sm:px-6 lg:px-8')
  .max-w-md.w-full.space-y-8
    div
      img.mx-auto.h-12.w-auto(src='@/svg/duck.svg' alt='Duck')
      h2.mt-6.text-center.text-3xl.font-extrabold.text-gray-900
        | Sign in to your account
    form.mt-8.space-y-6(action='#' method='POST')
      .space-y-4
        t-input(v-model="payload.usernanme" required autofocus placeholder="Username")
        t-input(v-model="payload.password" required placeholder="Password" type="password")
      t-button(text="Sign In")
</template>

<script>
export default {
  data () {
    return {
      payload: {}
    }
  },
  mounted () {
    console.log('login')
  }
}
</script>
