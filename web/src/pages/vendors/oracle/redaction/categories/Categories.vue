<template lang="pug">
div
  .bg-white.empty.w-full(v-if="isCategoriesEmpty")
    .text-xl.text-gray-400.text-center There is nothing here!
    .flex.justify-center.mt-10.w-full()
      svg-icon(name="box", addClass="fill-current text-gray-300 w-24 h-24")
    .flex.justify-center.mt-10
      t-button.mt-10.w-full.text-center(tagName="a"
        :href="`categories/create`" text="Create New Category")
  .flex.justify-center.w-full(v-else)
    .body.w-full.flex.items-center.flex-col
      .gap-y-3.flex.flex-col.w-full
        category-card.card(v-for="c in categories" :c='c')
      t-button.mt-10.w-full.text-center(tagName="a"
        :href="`categories/create`" text="Create New Category")

</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import SvgIcon from '@/components/SvgIcon'
import CategoryCard from '@/components/vendors/oracle/CategoryCard'

export default {
  props: ['connectionId'],
  components: {
    SvgIcon, CategoryCard
  },
  data () {
    return {
      isSpinner: false,
      title: 'Categories'
    }
  },
  computed: {
    ...mapGetters('category', ['categories']),
    isCategoriesEmpty () {
      return this.categories.length === 0
    }
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
