<template lang="pug">
header
  .w-full.mx-auto.px-5
    .relative.flex.items-center.justify-between.h-12
      .flex.items-center
        svg-icon.cursor-pointer.home(name="duck", addClass="fill-current w-8 h-8 text-gray-500 hover:text-gray-900")
      .flex.items-center.pr-2.gap-x-4(class='sm:static sm:inset-auto sm:ml-6 sm:pr-0')
        .icon-btn.las.la-search
        t-icon-dropdown(
          :classes="{icon: 'las la-plug'}"
          :emitValue="true" :items="connections", displayProp="name", valueProp="id" @select="onSelectConnection")
        t-icon-dropdown(
          :classes="{icon: 'las la-sliders-h'}"
          :emitValue="true" :items="settings", valueProp="path" @select="onSelectSetting")
        t-avatar-menu
</template>

<script>

import { mapActions, mapGetters } from 'vuex'
import TAvatarMenu from '@/components/TAvatarMenu'
import TIconDropdown from '@/components/TIconDropdown'
import SvgIcon from '@/components/SvgIcon'

export default {
  name: 'Navbar',
  components: {
    TAvatarMenu, TIconDropdown, SvgIcon
  },
  data () {
    return {
      settings: [{
        path: '/settings/connections',
        icon: 'las la-plug',
        name: 'Connections'
      }, {
        path: '/',
        icon: 'las la-user',
        name: 'Users'
      }]
    }
  },
  computed: {
    ...mapGetters('connection', ['connections'])
  },
  methods: {
    ...mapActions('connection', ['getConnections']),
    onSelectConnection (id) {
      this.$router.push(`/connections/${id}`)
    },
    onSelectSetting (path) {
      this.$router.push(path)
    }
  },
  created () {
    this.getConnections()
  }
}
</script>

<style lang="postcss" scoped>
header {
  @apply fixed border-b border-gray-300 px-0 bg-white;
  top: 0;
  margin-top: 0;
  position: fixed;
  top: 0;
  width: 100%;
}
header .container {
  @apply px-0 mx-4 flex flex-wrap items-center justify-between;
}

header .container .w-full {
  @apply relative flex justify-between px-0;
}

header i.icon {
  @apply text-2xl text-gray-800 opacity-75 cursor-pointer;
}
</style>
