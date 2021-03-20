<template lang="pug">
.container.flex.flex-col.gap-y-3
  .toolbar.flex.flex-col.gap-y-2.p-5.w-full.bg-gray-50.rounded-md
    .flex.flex-row.justify-between
      .flex.gap-x-4
        label.flex.items-center.cursor-pointer
          t-radio(name='options' value='export'  v-model="ei")
          span.ml-2.text-sm Export
        label.flex.items-center.ml-2.cursor-pointer
          t-radio(name='options' value='category' v-model="ei")
          span.ml-2.text-sm Import
  .body
    router-view
</template>

<script>

export default {
  data () {
    return {
      ei: 'export'
    }
  },
  components: {
  },
  methods: {
  },
  watch: {
  }
}
</script>

<style lang="postcss">
</style>
