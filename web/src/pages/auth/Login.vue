<template lang="pug">
.login-page
  .min-h-screen.flex.items-center.justify-center.bg-gray-50.py-12.px-4(class='sm:px-6 lg:px-8')
    .max-w-md.w-full.space-y-8
      div
        img.mx-auto.h-16.w-auto(src='@/svg/marker.svg' alt='Redact')
        h2.mt-6.text-center.text-3xl.font-extrabold.text-gray-900
          | Sign in to your account
      form.mt-8.space-y-6(autocomplete="off" @submit="onSubmit")
        .space-y-4
          t-input(v-model="payload.username" required autofocus placeholder="Username")
          t-input(v-model="payload.password" required placeholder="Password" type="password")
        t-button(text="Sign In" type="sumbit")
  .login-footer
    .flex.justify-between.items-center.h-full.pl-3.pr-3
      .left.flex
        .footer-item.company © {{year}} SCF & Blue
      .right.flex.gap-x-3
        a(href="https://github.com/bluecolor/redact")
          .footer-item.help.lab.la-github.icon-btn(
            content="Source code" v-tippy='{ placement : "top" }'
          )
        a(href="https://bluecolor.github.io/redact/")
          .footer-item.help.las.la-question-circle.icon-btn
        a(href="https://github.com/bluecolor/redact/issues")
          .footer-item.bug.las.la-bug.icon-btn(
            content="Issues" v-tippy='{ placement : "top" }'
          )
        a(href="https://github.com/bluecolor/redact/issues")
          .footer-item.mail.las.la-envelope.icon-btn
</template>

<script>
import dayjs from 'dayjs'
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
  computed: {
    year () {
      return dayjs().year()
    }
  },
  methods: {
    ...mapActions('user', ['login']),
    onSubmit (e) {
      e.preventDefault()
      this.login(this.payload).then(response => {
        this.$router.push({ path: '/' })
      })
    }
  },
  mounted () {
  }
}
</script>

<style lang="postcss">
.login-page .login-footer {
  bottom: 0;
  position: fixed;
  background-color: transparent;
  height: 50px;
  width: 100%;
  border-top: 1px solid #ccc;
}
.login-page .login-footer .right .footer-item {
  @apply text-gray-400 hover:text-gray-700;
}
.login-page .login-footer .footer-item.company {
  @apply text-blue-500 hover:text-blue-700 cursor-pointer;
}
</style>
