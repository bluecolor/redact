<template lang="pug">
.t-avatar-menu(:class="classes.wrapper")
  button(
    :class="classes.button"
    @click="isOpen = true",
    class="focus:outline-none"
  )
    img(:src="img", alt="avatar" :class="classes.img")
  .fixed.inset-0(v-if="isOpen", @click="isOpen = false", tabindex="-1")
  div(v-if="isOpen" :class="classes.menuWrapper")
      template(v-for="i in items")
        a(v-if="i !== '-'" href="#", :class="classes.menuItem") {{i.title}}
        div(v-if="i === '-'" :class="classes.separator")
</template>

<script>

import { v4 as uuidv4 } from 'uuid'

export default {
  props: {
    img: { type: String, required: false, default: `https://avatars.dicebear.com/4.5/api/identicon/${uuidv4()}.svg?r=50&m=15` },
    classes: {
      type: Object,
      default () {
        return {
          wrapper: 'relative inline-block',
          button: 'block h-8 w-8 rounded-full overflow-hidden',
          img: 'h-full w-full object-cover',
          menuWrapper: 'ring-1 ring-black ring-opacity-5 shadow-lg w-64 rounded-md mt-3 absolute right-0 origin-top-right text-left',
          menuItem: 'text-base block px-4 py-2 leading-tight hover:bg-gray-200',
          separator: 'border-t border-gray-200'
        }
      }
    }
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
