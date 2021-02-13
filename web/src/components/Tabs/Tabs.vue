<template lang="pug">
.tabs-container
  .tabs
    .flex.tab-title-content.flex-grow(v-for='tab in items' @click='onSelectTab(tab)' :class="{ selected: tab.selected }")
        .inline-block.title {{ tab.name }}
        i.inline-block.close.las.la-times.ml-2
    .flex.flex-grow
      .tab-title-content.last-item.h-full
        i.las.la-plus.text-2xl.icon-btn
  .tabs-details.h-full
    slot(name='items')
</template>

<script>
export default {
  name: 'Tabs',
  data () {
    return {
      items: []
    }
  },
  computed: {
  },
  methods: {
    onSelectTab (selected) {
      this.items.forEach(tab => {
        tab.isActive = (tab.path === this.selected.path)
      })
    }
  },
  mounted () {
    this.items = this.$children
  }
}
</script>

<style lang="postcss">
.tabs-container .tabs {
  @apply flex flex-grow items-center justify-start
}

.tabs-container .tabs {
  @apply flex flex-grow items-center justify-start;
}

.tabs-container .tabs .tab-title-content {
  @apply border-b border-gray-200 items-center flex border-r border-gray-200 hover:bg-gray-50 w-40 justify-between
    cursor-pointer;
  padding: .5em .5em;
}

.tabs-container .tabs .tab-title-content.last-item {
  @apply flex flex-grow justify-end border-b border-gray-200 cursor-default hover:bg-transparent;
}

.tabs-container .tabs .tab-title-content.selected {
  @apply border-b-0 hover:bg-transparent;
}

.tabs-container .tabs .tab-title-content i.close {
  visibility: hidden;
}

.tabs-container .tabs .tab-title-content:hover i.close {
  visibility: visible;
}
.tab-title-content:not(.selected) {
  @apply text-gray-400;
}
</style>
