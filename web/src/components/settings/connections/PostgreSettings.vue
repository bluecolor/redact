<template lang="pug">
.database-connection
  .section
    .sub-title
      | Postgre Settings
    form.form-section.mt-5
      .flex.items-center
        label(for='email' class="w-2/4")
          | Hostname
        .rounded-md.shadow-sm.w-full
          input.text(name='hostname' type='email' required autofocus
            class='focus:outline-none focus:ring-1 focus:border-blue-300 sm:text-sm sm:leading-5'
          )
      .flex.items-center.mt-5
        label(for='email' class="w-2/4")
          | Port
        .rounded-md.shadow-sm.w-full
          input.text(name='port' type='number' required autofocus
            class='focus:outline-none focus:ring-1 focus:border-blue-300 sm:text-sm sm:leading-5'
          )
      .flex.items-center.mt-5
        label(for='email' class="w-2/4")
          | Database
        .rounded-md.shadow-sm.w-full
          input.text(name='hostname' type='email' required autofocus
            class='focus:outline-none focus:ring-1 focus:border-blue-300 sm:text-sm sm:leading-5'
          )
      .flex.items-center.mt-5
        label(for='email' class="w-2/4")
          | Username
        .rounded-md.shadow-sm.w-full
          input.text(name='hostname' type='email' required autofocus
            class='focus:outline-none focus:ring-1 focus:border-blue-300 sm:text-sm sm:leading-5'
          )
      .flex.items-center.mt-5
        label(for='email' class="w-2/4")
          | Password
        .rounded-md.shadow-sm.w-full
          input.text(name='port' type='password' required autofocus
            class='focus:outline-none focus:ring-1 focus:border-blue-300 sm:text-sm sm:leading-5'
          )
      .flex.items-center.mt-5
        label(for='email' class="w-2/4")
          | Schema
        .rounded-md.shadow-sm.w-full
          input.text(name='hostname' type='email' required autofocus
            class='focus:outline-none focus:ring-1 focus:border-blue-300 sm:text-sm sm:leading-5'
          )
</template>

<script>
export default {

}
</script>

<style scoped lang="postcss">
  .ssh-tunnel {
    @apply w-4 h-4 text-blue-600 transition duration-150 ease-in-out;
  }

</style>
