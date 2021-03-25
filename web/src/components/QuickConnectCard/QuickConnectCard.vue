<template lang="pug">
t-card.card.cursor-pointer.hover-animate
  template(v-slot:header)
    .title.text-center.w-full
      | {{c.name}}
  template(v-slot:default)
    .flex.justify-center
      svg-icon(name="oracle", addClass="fill-current text-gray-300 w-24 h-24")
</template>

<script>
import SvgIcon from '@/components/SvgIcon'

export default {
  components: { SvgIcon },
  props: { c: { type: Object, default: () => {} } },
  data () {
    return {
    }
  },
  methods: {
  }
}
</script>>
