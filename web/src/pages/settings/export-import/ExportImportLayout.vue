<template lang="pug">
.container.flex.flex-col.gap-y-3
  .toolbar.flex.flex-col.gap-y-2.p-5.w-full.bg-gray-50.rounded-md
    .flex.flex-row.justify-between
      .flex.gap-x-4
        label.flex.items-center.cursor-pointer
          t-radio(name='options' value='export'  v-model="ei")
          span.ml-2.text-sm Export
        label.flex.items-center.ml-2.cursor-pointer
          t-radio(name='options' value='import' v-model="ei")
          span.ml-2.text-sm Import
  .body
    router-view
</template>

<script>

export default {
  props: ['connectionId'],
  data () {
    return {
      ei: undefined
    }
  },
  watch: {
    ei (v, o) {
      if (!o) { return }
      const path = `/connections/${this.connectionId}/settings/export-import/${v}`
      this.$router.push({ path })
    }
  },
  created () {
    switch (this.$route.name) {
      case 'exportSettings': this.ei = 'export'; break
      case 'importSettings': this.ei = 'import'; break
    }
  }
}
</script>

<style lang="postcss">
</style>
