<template lang="pug">
aside(class="w-3/12")
  .bg-white.rounded.w-full.pt-10
    ul.space-y-1
      li(v-for="i in items")
        .sidebar-menu-item(class="hover:bg-gray-200 focus:shadow-outline")
          span.text-gray-600
            i.text-lg.leading-lg.text-gray-700.opacity-75.text-xl(
              :class="i.icon"
            )
          span {{ i.title }}
</template>

<script>
export default {
  data () {
    return {
      items: [
        {
          icon: 'las la-home',
          title: 'Home'
        }, {
          icon: 'las la-cube',
          title: 'Environments'
        }, {
          icon: 'las la-play-circle',
          title: 'Jobs'
        }, {
          icon: 'las la-list',
          title: 'Run History'
        }, {
          icon: 'lab la-codepen',
          title: 'Develop'
        }
      ]
    }
  }
}
</script>

<style lang="postcss" scoped>
aside {
  @apply transform left-0 w-64 bg-white fixed h-full overflow-auto
  ease-in-out transition-all duration-300 z-30 border-r border-gray-400
}
aside .sidebar-menu-item {
  @apply cursor-pointer flex items-center space-x-4 text-gray-600 p-2
  font-medium pl-6;
}
</style>
