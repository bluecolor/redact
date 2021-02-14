<template lang="pug">
nav
  .w-full.mx-auto.px-5
    .relative.flex.items-center.justify-between.h-12
      .flex.items-center
        svg-icon.cursor-pointer.home(name="duck", addClass="fill-current w-8 h-8 text-gray-500 hover:text-gray-900")
      .flex.items-center.pr-2(class='sm:static sm:inset-auto sm:ml-6 sm:pr-0')
        .icon-btn.las.la-search.mr-4
        nav-menu.icon-btn.icon.mr-4(to="/settings/projects")
        profile-menu
</template>

<script>
import ProfileMenu from '@/components/ProfileMenu'
import NavMenu from '@/components/NavMenu'
import SvgIcon from '@/components/SvgIcon'

export default {
  name: 'Navbar',
  components: {
    ProfileMenu,
    NavMenu,
    SvgIcon
  },
  data () {
    return {
    }
  },
  methods: {
    onHome () {
      this.$router.push('/projects')
    }
  }
}
</script>

<style lang="postcss">
nav {
  @apply border-b border-gray-300 relative px-0 bg-white;
}
nav .container {
  @apply px-0 mx-4 flex flex-wrap items-center justify-between;
}

nav .container .w-full {
  @apply relative flex justify-between px-0;
}

nav i.icon {
  @apply text-2xl text-gray-800 opacity-75 cursor-pointer;
}
</style>
