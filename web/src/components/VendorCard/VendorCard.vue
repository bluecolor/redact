<template lang="pug">
.cursor-pointer.vendor-card(@click="onNav" :class="{'hover-animate': !v.disabled, 'disabled': v.disabled}")
  t-card.card
    template(v-slot:header)
      .title.text-center.w-full
        | {{v.name}}
    template.relative(v-slot:default)
      .flex.justify-center
        svg-icon(:name="v.icon", addClass="fill-current text-gray-300 w-24 h-24")
</template>

<script>
import SvgIcon from '@/components/SvgIcon'

export default {
  components: { SvgIcon },
  props: { v: { type: Object, default: () => {} } },
  methods: {
    onNav () {
      const { path } = this.v
      if (path) { this.$router.push({ path }) }
    }
  },
  created () {
  }
}
</script>>

<style scoped lang="postcss">
.vendor-card.disabled .card{
  @apply bg-gray-100;
}
</style>
