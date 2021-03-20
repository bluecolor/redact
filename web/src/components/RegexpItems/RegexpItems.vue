<template lang="pug">
t-dialog.py-16(name='regexp-items' v-model="model")
  template(slot='title')
    .pb-1
      t-input(placeholder="Search" v-model="search")
  template(slot='default')
    div.bg-white
      template(v-for="item in items" v-if="items.length > 0")
        .flex.justify-between.cursor-pointer(class="rounded-md hover:bg-gray-50")
          .item.flex.px-4.content-center.items-center.p-2 {{item.name}}
  template(slot='buttons')
      .flex.justify-end.w-full.gap-x-2
        t-button(variant="secondary" @click="onClose") Close
</template>

<script>
export default {
  data () {
    return {
      search: '',
      model: true,
      items: [
        { name: 'Phone number', expression: '<phone number>' },
        { name: 'Credit card', expression: '<credit card>' },
        { name: 'Address', expression: '<address>' },
        { name: 'TCKN', expression: '<tckn>' }
      ]
    }
  },
  methods: {
    onClose () {
      this.$emit('close')
    },
    onAdd (item) {
      this.$emit('add', item)
    }
  }
}
</script>
