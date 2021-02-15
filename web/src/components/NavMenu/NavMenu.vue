<template lang="pug">
.relative.inline-block
  button.block.h-8.w-8.rounded-full.overflow-hidden(
    @click="isOpen = true",
    class="focus:outline-none"
  )
    .las.la-sliders-h.h-full.w-full.object-cover
  .fixed.inset-0(v-if="isOpen", @click="isOpen = false", tabindex="-1")
  .menu(v-if="isOpen")
      template(v-for="i in items")
        router-link.item.flex.px-2.content-center.items-center(:to="i.path")
          .icon(:class="i.icon")
          .text-base.block.px-4.py-2.leading-tight(v-if="i !== '-'" to="#") {{i.title}}
        .border-t.border-gray-200(v-if="i === '-'")
</template>

<script>

export default {
  props: {
  },
  data () {
    return {
      isOpen: false,
      items: [{
        path: '/connections',
        icon: 'las la-plug',
        title: 'Connections'
      }, {
        path: '/',
        icon: 'las la-user',
        title: 'Users'
      }]
    }
  }
}
</script>

<style lang="scss">
</style>
