<template lang="pug">
.tab(v-show="selected")
  .toolbar.flex.justify-between
    slot(name="toolbar")
  slot
</template>

<script>
export default {
  name: 'Tab',
  props: {
    path: { type: String, required: false },
    selected: { type: Boolean, required: false, default: false }
  },
  computed: {
    name () {
      return this.path.split('/').pop()
    }
  }

}
</script>

<style lang="postcss">
.tabs-container .tab .toolbar {
  @apply border-b border-gray-200;
  padding: .4em .5em;
}
</style>
