<template lang="pug">
#profile-menu.relative.inline-block
  button.block.h-8.w-8.rounded-full.overflow-hidden(
    @click="isOpen = true",
    class="focus:outline-none"
  )
    img.h-full.w-full.object-cover(:src="img", alt="avatar")
  .fixed.inset-0(v-if="isOpen", @click="isOpen = false", tabindex="-1")
  .ring-1.ring-black.ring-opacity-5.shadow-lg.w-64.rounded-md.mt-3.absolute.right-0.origin-top-right.text-left(v-if="isOpen")
      template(v-for="i in items")
        a.text-base.block.px-4.py-2.leading-tight(v-if="i !== '-'" href="#", class="hover:bg-gray-200") {{i.title}}
        .border-t.border-gray-200(v-if="i === '-'")
</template>

<script>

import { v4 as uuidv4 } from 'uuid'

export default {
  props: {
    img: { type: String, required: false, default: `https://avatars.dicebear.com/4.5/api/identicon/${uuidv4()}.svg?r=50&m=15` }
  },
  data () {
    return {
      isOpen: false,
      items: [{
        title: 'Profile'
      }, '-', {
        title: 'Sign out'
      }]
    }
  }
}
</script>

<style lang="scss">
</style>
