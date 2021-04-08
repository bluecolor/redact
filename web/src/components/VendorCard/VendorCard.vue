<template lang="pug">
.cursor-pointer.hover-animate(@click="onNav")
  t-card
    template(v-slot:header)
      .title.text-center.w-full
        | {{v.name}}
    template.relative(v-slot:default)
      .flex.justify-center
        svg-icon(:name="v.icon", addClass="fill-current text-gray-300 w-24 h-24")
</template>

<script>
import { mapActions } from 'vuex'
import SvgIcon from '@/components/SvgIcon'

export default {
  components: { SvgIcon },
  props: { v: { type: Object, default: () => {} } },
  methods: {
    ...mapActions('app', ['setConnection']),
    onNav () {
      const { path } = this.v
      this.$router.push({ path })
    }
  },
  created () {
  }
}
</script>>
