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
    '$route.name' (v) {
      this.setEI()
    },
    ei (v, o) {
      if (!o || v === o) { return }
      const path = `/connections/${this.connectionId}/settings/export-import/${v}`
      if (path !== this.$route.path) {
        this.$router.push({ path })
      }
    }
  },
  methods: {
    setEI () {
      switch (this.$route.name) {
        case 'exportSettings': this.ei !== 'export' && (this.ei = 'export'); break
        case 'importSettings': this.ei !== 'import' && (this.ei = 'import'); break
      }
    }
  },
  created () {
    this.setEI()
  }
}
</script>

<style lang="postcss">
</style>
