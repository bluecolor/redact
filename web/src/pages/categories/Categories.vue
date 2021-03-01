<template lang="pug">
div
  .empty.w-full(v-if="isCategoriesEmpty")
    .text-xl.text-gray-400.text-center There is nothing here!
    .project-logo.flex.justify-center.mt-10.w-full()
      svg-icon(name="cloud-computing", addClass="fill-current text-gray-300 w-24 h-24")
    .flex.justify-center.mt-10
      t-button.mt-10.w-full.text-center(tagName="a"
        :href="`/connections/${connectionId}/categories/create`" text="Create New Category")
  .connections-container.flex.justify-center.w-full(v-else)
    .body.w-full.flex.items-center.flex-col
      .connections.gap-y-3.flex.flex-col.w-full
        t-card(v-for="c in categories" :header='c.name')
          | Content of the card.

      t-button.mt-10.w-full.text-center(tagName="a"
        :href="`/connections/${connectionId}/categories/create`" text="Create New Category")

</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import SvgIcon from '@/components/SvgIcon'

export default {
  props: ['connectionId'],
  components: {
    SvgIcon
  },
  data () {
    return {
      isSpinner: false,
      title: 'Connections'
    }
  },
  computed: {
    ...mapGetters('category', ['categories', 'isCategoriesEmpty'])
  },
  methods: {
    ...mapActions('category', ['getCategories']),
    load () {
      this.isSpinner = true
      this.getCategories(this.connectionId).finally(() => { this.isSpinner = false })
    }
  },
  mounted () {
    this.load()
  }
}
</script>

<style lang="postcss" scoped>
.empty {
  @apply border-dashed p-3 border-2 rounded-md w-full
}
.page {
}

</style>
