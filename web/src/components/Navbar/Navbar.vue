<template lang="pug">
header
  search-box(v-if="isSearchBox" @hide="isSearchBox=false")
  .w-full.mx-auto.px-5
    .relative.flex.items-center.justify-between.h-12
      .flex.items-center.gap-x-10
        svg-icon.cursor-pointer.home(@click="onHome" name="marker", addClass="fill-current w-8 h-8 text-gray-500 hover:text-gray-700")
        .connection-title.flex.gap-x-3.items-center
          svg-icon(v-if="vendor" :name="connection.vendor", addClass="fill-current text-gray-300 w-8 h-8")
          router-link.connection.cursor-pointer.text-gray-700(
            v-if="isConnectionLayout"
            :to="`/connections/${connectionId}/${vendor}`"
            class="hover:text-gray-900 hover:font-black"
          ) {{connectionName}}
          .sep(v-if="isConnectionLayout && _title && connectionName") /
          .title.text-gray-500 {{_title}}
      .flex.items-center.pr-2.gap-x-4(class='sm:static sm:inset-auto sm:ml-6 sm:pr-0')
        notifications-menu(v-if="!isNotificationsEmpty")
        .icon-btn.las.la-search(@click="isSearchBox=true")
        t-icon-dropdown(
          :classes="{icon: 'las la-plug'}"
          :items="connectionsWithIcons", displayProp="name", valueProp="id" @select="onSelectConnection")
        t-icon-dropdown(
          :classes="{icon: 'las la-sliders-h'}"
          :emitValue="true" :items="settings", valueProp="path" @select="onSelectSetting")
        t-avatar-menu(:img="current_user.avatar_url")
</template>

<script>

import _ from 'lodash'
import { mapActions, mapGetters } from 'vuex'
import TAvatarMenu from '@/components/TAvatarMenu'
import TIconDropdown from '@/components/TIconDropdown'
import SvgIcon from '@/components/SvgIcon'
import NotificationsMenu from '@/components/NotificationsMenu'
import SearchBox from '@/components/SearchBox'

export default {
  name: 'Navbar',
  components: {
    TAvatarMenu, TIconDropdown, SvgIcon, NotificationsMenu, SearchBox
  },
  data () {
    return {
      isSearchBox: false,
      settings: [{
        path: '/settings/connections',
        icon: 'las la-plug',
        name: 'Connections'
      }, {
        path: '/settings/users',
        icon: 'las la-user',
        name: 'Users'
      }, {
        path: '/settings/notifications',
        icon: 'las la-bell',
        name: 'Notifications'
      }]
    }
  },
  computed: {
    ...mapGetters('user', ['current_user']),
    ...mapGetters('connection', ['connections']),
    ...mapGetters('app', ['connection', 'title']),
    ...mapGetters('notification', ['notifications']),
    vendor () {
      return this.connection?.vendor
    },
    isConnectionLayout () {
      return this.$route.path.startsWith('/connections')
    },
    connectionName () {
      return this.connection?.name
    },
    connectionsWithIcons () {
      return _.map(this.connections, c => {
        const icon = 'las la-circle text-2xl h-full ' + ((status) => {
          if (status) { return 'text-green-400' }
          if (status === false) { return 'text-red-400' }
          if (!status) { return 'text-gray-400' }
        })(c.status)
        const side = c.vendor
        return { ...c, icon, side }
      })
    },
    connectionId () {
      return this.connection?.id
    },
    _title () {
      return this.title?.text ?? this.$route?.meta?.title
    },
    isNotificationsEmpty () {
      return this.notifications.length === 0
    }
  },
  methods: {
    ...mapActions('connection', ['getConnections']),
    ...mapActions('app', ['setConnection']),
    onSelectConnection ({ id, vendor }) {
      this.setConnection(id)
      this.$router.push(`/connections/${id}/${vendor}`)
    },
    onSelectSetting (path) {
      this.$router.push(path)
    },
    onHome () {
      this.$router.push({ path: '/' })
    },
    onKeyDown (e) {
      if (e.key === 'Escape') {
        this.isSearchBox = false
        return
      }
      if (e.ctrlKey && e.key === 'm') {
        this.isSearchBox = !this.isSearchBox
      }
    }
  },
  mounted () {
    document.addEventListener('keydown', this.onKeyDown)
  },
  destroyed () {
    document.removeEventListener('keydown', this.onKeyDown)
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
