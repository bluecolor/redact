<template lang="pug">
.flex.flex-col.justify-center.min-h-screen.py-12.bg-gray-50(class='sm:px-6 lg:px-8')
  div(class='sm:mx-auto sm:w-full sm:max-w-md')
    h2.mt-6.text-3xl.font-extrabold.text-center.text-gray-900.leading-9
      | Sign in
  .mt-8(class='sm:mx-auto sm:w-full sm:max-w-md')
    .px-4.py-8.bg-white.shadow(class='sm:rounded-lg sm:px-10')
      form
        div
          label.block.text-sm.font-medium.text-gray-700.leading-5(for='email')
            | Email
          .mt-1.rounded-md.shadow-sm
            input#email.text(name='email' type='email' required autofocus
              class='focus:outline-none focus:ring-1 focus:border-blue-300 sm:text-sm sm:leading-5'
            )
        .mt-6
          label.block.text-sm.font-medium.text-gray-700.leading-5(for='password')
            | Password
          .mt-1.rounded-md.shadow-sm
            input#password.text(type='password' required
              class='focus:outline-none focus:ring-1 focus:border-blue-300 sm:text-sm sm:leading-5'
            )
        .flex.items-center.justify-between.mt-6
          .flex.items-center
            input#remember(type='checkbox')
            label.block.ml-2.text-sm.text-gray-900.leading-5(for='remember')
              | Remember
          .text-sm.leading-5
            a.font-medium.text-blue-600.transition.ease-in-out.duration-150(href='#' class='hover:text-blue-500 focus:outline-none focus:underline')
              | Forgot your password?
        .mt-6
          span.block.w-full.rounded-md.shadow-sm
            button.submit(type='submit')
              | Sign in

    p.mt-4.text-sm.text-center.text-gray-600.leading-5.max-w
      a.font-medium.text-blue-600.transition.ease-in-out.duration-150(href='#' class='hover:text-blue-500 focus:outline-none focus:underline')
        | Create account

</template>

<script>
export default {

}
</script>

<style scoped lang="postcss">
  input.text {
    @apply appearance-none block w-full px-3 py-2 border border-gray-300 ring-blue-300
      rounded-md placeholder-gray-400 transition duration-150 ease-in-out;
  }

  #remember {
    @apply w-4 h-4 text-indigo-600 transition duration-150 ease-in-out;
  }

  button.submit {
    @apply flex justify-center w-full px-4 py-2 text-sm font-medium text-white ring-blue-300
      bg-green-600 border border-transparent rounded-md transition duration-150 ease-in-out
      hover:bg-green-500 hover:bg-indigo-500 focus:outline-none;
  }
</style>
