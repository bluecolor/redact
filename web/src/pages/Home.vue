<template lang="pug">
.home-container.flex.justify-center.pt-10
    .grid.grid-cols-3.gap-10.pa-10(class="w-6/12")
      t-card.text-center(header="John Doe")
        template(v-slot:default)
          img(:src="img", alt="avatar")
        template(v-slot:footer)
          t-button.w-full(text="Profile")
      t-card.text-center(header="Connections" :classes="card.classes")
        template(v-slot:default)
          t-button.w-full(v-for="c in connections" variant="secondary" :text="c.name")
        template(v-slot:footer)
          t-button.w-full(text="See All")
      t-card.text-center(header="Settings" :classes="card.classes")
        template(v-slot:default)
          t-button.w-full(v-for="s in settings" variant="secondary")
            .flex.gap-x-5.items-center
              .icon.text-2xl(:class="s.icon")
              .text {{s.title}}
        template(v-slot:footer)
          t-button.w-full(text="General Settings")
      t-card.text-center(header="Discover" :classes="card.classes")
        template(v-slot:default)
          .flex.justify-center
            svg-icon(name="telescope", addClass="fill-current text-gray-300 w-24 h-24")
        template(v-slot:footer)
          t-button.w-full(text="Define & Find Sensitve Data")
      t-card.text-center(header="Search" :classes="card.classes")
        template(v-slot:default)
          .flex.justify-center
            svg-icon(name="search", addClass="fill-current w-24 h-24")
        template(v-slot:footer)
          t-button.w-full(text="Search Everywhere")
      t-card.text-center(header="Help" :classes="card.classes")
        template(v-slot:default)
          .flex.justify-center
            svg-icon(name="lifesaver", addClass="fill-current  w-24 h-24")
        template(v-slot:footer)
          t-button.w-full(text="Documentation")

</template>

<script>

import { v4 as uuidv4 } from 'uuid'
import { mapGetters } from 'vuex'
import SvgIcon from '@/components/SvgIcon'

export default {
  name: 'Home',
  components: {
    SvgIcon
  },
  data () {
    return {
      img: `https://avatars.dicebear.com/4.5/api/identicon/${uuidv4()}.svg?r=50&m=15`,
      options: {},
      card: {
        classes: {
          wrapper: 'flex flex-col border rounded shadow-sm bg-white border-gray-100',
          body: 'p-3 flex-grow flex flex-col gap-y-3',
          header: 'border-b border-gray-100 p-3 rounded-t',
          footer: 'border-gray-100 border-t p-3 rounded-b'
        }
      },
      settings: [{
        title: 'Connections',
        icon: 'las la-plug'
      }, {
        title: 'Users',
        icon: 'las la-user'
      }, {
        title: 'Customize',
        icon: 'las la-pencil-ruler'
      }, {
        title: 'Discovery',
        icon: 'las la-compass'
      }]
    }
  },
  computed: {
    ...mapGetters('connection', ['connections'])
  },
  methods: {
    onResize () {},
    onChange () {}
  }
}
</script>
