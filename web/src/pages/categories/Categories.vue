<template lang="pug">
page-loader(v-if="isSpinner")
.empty.w-full(v-if="isCategoriesEmpty")
  .text-xl.text-gray-400.text-center There is nothing here!
  .project-logo.flex.justify-center.mt-10.w-full()
    svg-icon(name="cloud-computing", addClass="fill-current text-gray-300 w-24 h-24")
  .flex.justify-center.mt-10
    router-link.btn.create-btn.mt-10(tag="button" class="w-2/3" :to="`/connections/${connectionId}/categories/create`")
      | Create New Category
.connections-container.flex.justify-center.w-full(v-else)
  .body.w-full.flex.items-center.flex-col
    .connections.gap-y-3.flex.flex-col.w-full
      category-card(v-for="c in categories" :category="c")
    router-link.btn.create-btn.mt-10.w-full(tag="button"
      :to="`/connections/${connectionId}/categories/create`"
    )
      | Create New Category
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import SvgIcon from '@/components/SvgIcon'
import PageLoader from '@/components/loaders'
import CategoryCard from '@/components/CategoryCard'

export default {
  props: ['connectionId'],
  components: {
    SvgIcon, PageLoader, CategoryCard
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
