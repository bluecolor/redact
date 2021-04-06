<template lang="pug">
.t-avatar-menu(v-click-outside="onHide" :class="classes.wrapper")
  button(
    :class="classes.button"
    @click="isOpen = true",
    class="focus:outline-none"
  )
    img(:src="img", alt="avatar" :class="classes.img")
  .fixed.inset-0(v-if="isOpen", @click="isOpen = false", tabindex="-1")
  div.bg-white(v-if="isOpen" :class="classes.menuWrapper")
    template(v-if="items.length > 0" v-for="i in items")
      .cursor-pointer(v-if="i !== '-'"  :class="classes.menuItem" @click="onItemClick(i)")
        div(v-if="i.icon" :class="`${classes.itemIcon} ${i.icon}`")
        .text-base.block.px-4.py-2.leading-tight {{i.title}}
      div(v-if="i === '-'" :class="classes.separator")
</template>

<script>

import { v4 as uuidv4 } from 'uuid'
import { mapActions } from 'vuex'
import ClickOutside from 'vue-click-outside'

export default {
  directives: {
    ClickOutside
  },
  props: {
    img: { type: String, required: false, default: `https://avatars.dicebear.com/4.5/api/identicon/${uuidv4()}.svg?r=50&m=15` },
    classes: {
      type: Object,
      default () {
        return {
          wrapper: 'relative inline-block',
          button: 'block h-8 w-8 rounded-full overflow-hidden',
          img: 'h-full w-full object-cover',
          itemIcon: 'icon icon-btn',
          menuWrapper: 'ring-1 ring-black ring-opacity-5 shadow-lg w-64 rounded-md mt-3 absolute right-0 origin-top-right text-left',
          menuItem: 'flex items-center text-base block px-4 py-1 leading-tight hover:bg-gray-200',
          separator: 'border-t border-gray-200'
        }
      }
    }
  },
  data () {
    return {
      isOpen: false,
      items: [{
        name: 'profile',
        title: 'Profile',
        icon: 'las la-user'
      }, {
        name: 'preferences',
        title: 'Preferences',
        icon: 'las la-cog'
      }, '-', {
        name: 'signout',
        title: 'Sign out',
        icon: 'danger las la-sign-out-alt'
      }, '-', {
        name: 'help',
        title: 'Help',
        icon: 'las la-life-ring'
      }, {
        name: 'about',
        title: 'About',
        icon: 'las la-feather-alt'
      }]
    }
  },
  computed: {
  },
  methods: {
    ...mapActions('user', ['logout']),
    onHide () {
      this.isOpen = false
    },
    onItemClick (i) {
      switch (i.name) {
        case 'signout':
          this.logout()
          this.$router.push({ path: '/auth/login' })
          break
        case 'profile':
          this.$router.push({ path: '/settings/profile' })
          break
        case 'preferences':
          this.$router.push({ path: '/settings/preferences' })
          break
        case 'help':
          window.location = 'https://bluecolor.github.io/duck/'
          break
      }
      this.isOpen = false
    }
  }
}
</script>

<style lang="scss">
</style>
