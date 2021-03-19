<template lang="pug">
.t-icon-menu.relative(:class="cls.wrapper")
  button(
    @click="isOpen = true",
    :class="`${cls.button} ${cls.icon}`"
  )
    //- .h-full.w-full.object-cover(:class="cls.icon")
  .fixed.inset-0(v-if="isOpen", @click="isOpen = false", tabindex="-1")
  div.bg-white(v-if="isOpen" :class="cls.menu")
    template(v-if="!loading && items.length > 0" v-for="i in items")
      div(:class="cls.menuItem + (i.disabled ? ' disabled' : '')" @click="onItemClick(i)")
        div(v-if="i.icon" :class="`${cls.itemIcon} ${i.icon}`")
        .text-base.block.px-4.py-2.leading-tight {{i[displayProp]}}
    t-simple-spinner(v-if="loading")
    div(v-if="items.length === 0" :class="cls.empty")
      | {{emptyText}}
</template>

<script>

import TSimpleSpinner from '@/components/loaders'
import mixin from '@/components/mixin.js'

export default {
  mixins: [mixin],
  props: {
    displayProp: { type: String, default: 'name' },
    valueProp: { type: String, default: 'name' },
    emitValue: { type: Boolean, default: false },
    loading: { type: Boolean, default: false },
    items: { type: Array, default: () => [] },
    emptyText: { ype: String, default: 'No items found' }
  },
  components: {
    TSimpleSpinner
  },
  data () {
    return {
      isSpinner: false,
      isOpen: false,
      defaultClasses: {
        wrapper: 'relative inline-block icon-btn icon',
        button: 'block rounded-full overflow-hidden focus:outline-none',
        icon: 'las la-ellipsis-v',
        empty: 'empty p-2 text-base',
        menu: 'menu',
        menuItem: 'item flex px-4 content-center items-center',
        itemIcon: 'icon'
      }
    }
  },
  methods: {
    onItemClick (item) {
      this.isOpen = false
      if (this.emitValue) {
        this.$emit('select', item[this.valueProp])
      } else {
        this.$emit('select', item)
      }
    }
  }
}
</script>

<style lang="postcss">
.t-icon-menu .disabled {
  @apply text-gray-400 hover:bg-white cursor-not-allowed;
}
</style>
