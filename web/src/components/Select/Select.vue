<template lang="pug">
.select
  label#select-label
    slot(name="SelectLabel")
  .relative(v-click-outside="closeDropdown")
    span.inline-block.w-full.rounded-md
      button.select-btn(
        type="button",
        @click="openDropdown",
        aria-haspopup="listbox",
        aria-expanded="true",
        aria-labelledby="select-label"
      )
        .flex.items-center.space-x-3.h-5
          span.block.truncate(v-if="selected")
            | {{ selected[displayField] }}
        span.absolute.inset-y-0.right-0.flex.items-center.pr-2.pointer-events-none
          svg.h-5.w-5.text-gray-400(
            viewBox="0 0 20 20",
            fill="none",
            stroke="currentColor"
          )
            path(
              d="M7 7l3-3 3 3m0 6l-3 3-3-3",
              stroke-width="1.5",
              stroke-linecap="round",
              stroke-linejoin="round"
            )
    .absolute.mt-1.w-full.rounded-md.bg-white.shadow-lg(v-show="isOpen")
      ul.max-h-56.rounded-md.py-1.text-base.leading-6.overflow-auto(
        tabindex="-1",
        role="listbox",
        aria-labelledby="select-label",
        aria-activedescendant="listbox-item-3",
        class="focus:outline-none sm:text-sm sm:leading-5"
      )
        li.text-gray-900.cursor-default.select-none.relative.py-2.pl-3.pr-9.cursor-pointer(
          tabindex="0",
          @click="select(i)",
          role="option",
          v-for="i in items",
          v-bind:key="i.title",
          class="hover:bg-gray-200 focus:outline-none focus:bg-gray-200"
        )
          .flex.items-center.space-x-3
            span.block.truncate(
              v-bind:class="{ 'font-normal': !isSelected(i), 'font-semibold': isSelected(i) }"
            )
              | {{ i.title }}
          span.absolute.inset-y-0.right-0.flex.items-center.pr-4(
            v-show="isSelected(i)"
          )
            svg.h-5.w-5(viewBox="0 0 20 20", fill="currentColor")
              path(
                fill-rule="evenodd",
                d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z",
                clip-rule="evenodd"
              )
</template>

<script>
import _ from 'lodash'
import ClickOutside from 'vue-click-outside'

export default {
  name: 'VSelect',
  props: {
    items: { type: Array, required: true },
    value: { type: String, required: false },
    valueField: { type: String, required: false, default: 'id' },
    displayField: { type: String, required: false, default: 'title' }
  },
  components: {},
  data () {
    return {
      isOpen: false,
      selected: undefined
    }
  },
  methods: {
    isSelected (value) {
      return this.value === value
    },
    closeDropdown () {
      this.isOpen = false
    },
    openDropdown () {
      this.isOpen = true
    },
    select (value) {
      this.isOpen = false
      this.selected = value
      this.$emit('input', value[this.valueField])
    }
  },
  directives: {
    ClickOutside
  },
  mounted () {
    if (this.value) {
      this.selected = _.find(this.items, item => item[this.valueField] === this.value)
    }
  }
}
</script>

<style scoped lang="postcss">
.select {
  @apply space-y-1;
}

.select label#select-label {
  @apply block text-sm leading-5 font-medium text-gray-700;
}

.select button.select-btn {
  @apply cursor-pointer relative w-full rounded-md border border-gray-300 bg-white
    pl-3 pr-10 py-2 text-left transition ease-in-out duration-150
    focus:outline-none focus:ring-1 focus:border-blue-300
    sm:text-sm sm:leading-5;
}
</style>
