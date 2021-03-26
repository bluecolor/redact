<template lang="pug">
.t-icon-menu.relative.relative.inline-block.icon-btn.icon
  .icon-btn.las.la-bell.danger.relative(@click="isOpen = true")
    t-tag(
      style="color:red;position:absolute;top:-5px;right:-10px;padding-left:0.25rem;padding-right:0.25rem"
      class="bg-red-100"
      tag-name="span" variant="badge"
    ) {{items.length}}

  .fixed.inset-0(v-if="isOpen", @click="isOpen = false", tabindex="-1")
  .menu.bg-white(v-if="isOpen")
    .heading.p-2.text-xl.text-gray-700.border-b(class="")
      | Notifications
    template(v-if="!loading && items.length > 0" v-for="i in items")
      .item.flex.px-4.content-center.items-center(:class="(i.disabled ? ' disabled' : '')" @click="onItemClick(i)")
        .icon(v-if="i.icon" :class="i.icon")
        .text-base.block.px-4.py-2.leading-tight {{i.text}}
    t-simple-spinner(v-if="loading")
    .empty.p-2.text-base(v-if="items.length === 0")
      | {{emptyText}}
    .footer.p-2.text-gray-700.border-t.flex.gap-x-3(class="hover:bg-green-50")
      .las.la-angle-double-right
      .text-base.block.leading-tight See all
</template>

<script>

import TSimpleSpinner from '@/components/loaders'
import { mapGetters } from 'vuex'

export default {
  props: {
    displayProp: { type: String, default: 'name' },
    valueProp: { type: String, default: 'name' },
    emitValue: { type: Boolean, default: false },
    loading: { type: Boolean, default: false },
    emptyText: { ype: String, default: 'No items found' }
  },
  components: {
    TSimpleSpinner
  },
  data () {
    return {
      isSpinner: false,
      isOpen: false
    }
  },
  computed: {
    ...mapGetters('notification', ['notifications']),
    isNotificationsEmpty () {
      return this.notifications.length === 0
    },
    items () {
      return this.notifications
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
