<template lang="pug">
.search-box-container(@click="onHide" style='position: absolute;z-index:99999999999;width: 100vw; height: 100vh; top:0;' )
  div.search-box.p-1(v-on:mouseenter="onMouseEnter" autofocus @click.stop="" style='position: relative; z-index: 1; box-shadow: rgba(15, 15, 15, 0.05) 0px 0px 0px 1px, rgba(15, 15, 15, 0.1) 0px 5px 10px, rgba(15, 15, 15, 0.2) 0px 15px 40px; border-radius: 3px; background: white; top: 90px; overflow: hidden; width: 75%; max-width: 600px;')
    .relative
      t-input.w-full(autofocus v-model="q" placeholder='A place to search everything  🔖…' type='text' style='text-overflow: ellipsis;')
      .search-icon.icon-btn.las.la-search(v-if="!isSearching")
      .spinner.search-icon.icon-btn.lds-dual-ring(v-if="isSearching")
    div(v-if="items.length > 0" style='display: flex; align-items: center; line-height: 120%; width: 100%; user-select: none; min-height: 0px; font-size: 14px;')
      .flex.flex-col.pt-2.w-full
        template(v-for="i in items")
          .w-full.item.flex.px-4.content-center.items-center(class="hover:bg-gray-200 cursor-pointer")
            .text-2xl.text-gray-400(v-if="i.icon" :class="i.icon")
            .text-base.block.px-4.py-2.leading-tight {{i.name}}
    footer(style='flex-shrink: 0;')

</template>

<script>
/* eslint-disable camelcase */
import { mapActions, mapGetters } from 'vuex'
import _ from 'lodash'

export default {
  data () {
    return {
      q: '',
      isSearching: false,
      items: [],
      focusIndex: -1,
      static: [{
        path: '/',
        name: 'Home',
        type: 'static',
        icon: 'las la-home',
        tags: ['home', 'index', 'menu']
      }, {
        path: '/settings/connections',
        name: 'Settings',
        type: 'static',
        icon: 'las la-sliders-h',
        tags: ['settings', 'users', 'connections', 'profile', 'prefenreces']
      }, {
        path: '/settings/connections',
        type: 'static',
        name: 'Connections',
        icon: 'las la-plug',
        tags: ['connections']
      }, {
        path: '/settings/users',
        name: 'Users',
        type: 'static',
        icon: 'las la-user',
        tags: ['users']
      }, {
        path: '/settings/profile',
        name: 'Profile',
        type: 'static',
        icon: 'las la-id-card',
        tags: ['profile']
      }, {
        path: '/settings/preferences',
        name: 'Preferences',
        type: 'static',
        icon: 'las la-cog',
        tags: ['preferences']
      }]
    }
  },
  watch: {
    q (q) {
      if (q) {
        this.search(q)
      } else {
        this.isSearching = false
        this.items = []
      }
    }
  },
  computed: {
    ...mapGetters('app', ['connectionId'])
  },
  methods: {
    ...mapActions('md', ['searchMetadata']),
    onClear () {
      this.q = ''
      this.items = []
    },
    onHide () {
      this.$emit('hide')
    },
    onMenuItem ({ path }) {
      if (path) {
        this.$router.push({ path })
        this.$emit('hide')
      }
    },
    search (q) {
      if (!q?.length) {
        this.items = []
        return
      }

      q = q.toLowerCase()
      this.isSearching = true

      this.items = _.filter(this.static, s => {
        for (const i in s.tags) {
          if (s.tags[i]?.toLowerCase()?.includes(q.toLowerCase())) {
            return true
          }
        }
        return false
      })

      if (this.connectionId && q?.length > 3) {
        this.searchMetadata(q).then(result => {
          this.items.push(..._.map(result, r => {
            const fullName = (m) => {
              const { type, owner, table_name, column_name } = m
              if (type === 'column') {
                return `${owner}.${table_name}.${column_name}`
              }
              return `${owner}.${table_name}`
            }
            const icon = (m) => {
              const { type } = m
              switch (type) {
                case 'column': return 'las la-columns text-blue-200'
                case 'table': return 'las la-border-all text-red-200'
              }
              return 'text-gray-200'
            }
            return {
              path: '/explore/x',
              name: fullName(r),
              type: r.type,
              icon: icon(r)
            }
          }))
        }).finally(() => { this.isSearching = false })
      } else { this.isSearching = false }
    },
    onKeyDown (e) {
      if (e.code === 'Enter' && this.focusIndex !== -1) {
        const item = this.items[this.focusIndex]
        if (item) { this.onMenuItem(item) }
      }
      if (e.code === 'ArrowUp') {
        this.focusIndex = this.focusIndex ? --this.focusIndex : 0
      } else if (e.code === 'ArrowDown') {
        this.focusIndex = this.focusIndex === this.items.length - 1 ? 0 : ++this.focusIndex
      }
      if (['ArrowDown', 'ArrowUp'].includes(e.code)) {
        let el = this.$el.querySelector('.result-list .focus')
        if (el) {
          el.classList.remove('focus')
        }
        el = this.$el.querySelector(`.result-list .result-item-${this.focusIndex}`)
        if (el) {
          el.classList.add('focus')
        }
      }
    },
    bindNav (bind) {
      if (!bind) { document.removeEventListener('keydown', this.onKeyDown); return }
      document.addEventListener('keydown', this.onKeyDown)
    },
    onMouseEnter () {
      this.focusIndex = -1
      const el = this.$el.querySelector('.result-list .focus')
      if (el) {
        el.classList.remove('focus')
      }
    }
  },
  mounted () {
    setTimeout(() => {
      this.$el.querySelector('input').select()
      this.bindNav(true)
    }, 100)
  },
  created () {
    this.search = _.debounce(this.search, 200)
  },
  destroyed () {
    this.bindNav(false)
  }
}
</script>

<style lang="postcss">
.search-box-container .search-icon {
  position: absolute;
  right: 10px;
  bottom: 0.5rem;
  @apply text-gray-400;
}
.search-box-container .search-icon:hover {
  @apply text-gray-600;
}
</style>

<style lang="scss">
.search-box-container {
  background-color: rgba(15, 15, 15, 0.7);
  .search-box {
    background-color: white;
    left: 50%;
    margin-left: -300px;
    input:focus {
      outline: none;
    }
    .focus {
      background-color: #ccc;
    }
  }
}
</style>
