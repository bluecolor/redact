<template lang="pug">
t-dialog.py-16(name='named-dialog' v-model="model")
  template(slot='title')
    .pb-1
      t-input(placeholder="Search or add" v-on:keydown="onEnter" v-model="search")
  template(slot='default')
    div.bg-white
      template(v-for="item in items" v-if="items.length > 0")
        .flex.justify-between(class="rounded-md hover:bg-gray-50")
          .item.flex.px-4.content-center.items-center.p-2 {{item}}
          .icon.las.la-times.flex.justify-end.icon-btn(@click="onRemove(item)")
  template(slot='buttons')
      .flex.justify-end.w-full.gap-x-2
        t-button(variant="secondary" @click="onClose") Close
</template>

<script>
export default {
  props: { items: { type: Array, default: () => [] } },
  data () {
    return {
      search: '',
      model: true
    }
  },
  methods: {
    onClose () {
      this.$emit('close')
    },
    onRemove (item) {
      this.$emit('remove', item)
    },
    onEnter ({ key }) {
      if (key === 'Enter') {
        this.$emit('add', this.search)
      }
    }
  }
}
</script>
