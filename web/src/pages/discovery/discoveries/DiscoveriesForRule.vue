<template lang="pug">
.policies-container
  .bg-white.empty.w-full(v-if="isDiscoveriesEmpty")
    .text-xl.text-gray-400.text-center There is nothing here!
    .project-logo.flex.justify-center.mt-10.w-full()
      svg-icon(name="box", addClass="fill-current text-gray-300 w-24 h-24")
  .flex.justify-center.w-full(v-else)
    .body.w-full.flex.items-center.flex-col
      .discoveries.gap-y-3.flex.flex-col.w-full
        discoveries-table(:d="items")
</template>

<script>
/* eslint-disable camelcase */
import { mapActions } from 'vuex'
import SvgIcon from '@/components/SvgIcon'
import { dateMixin, paginationMixin } from '@/mixins'
import DiscoveriesTable from '@/components/DiscoveriesTable'

export default {
  mixins: [dateMixin, paginationMixin],
  props: ['connectionId', 'planInstanceId', 'planId', 'ruleId'],
  components: {
    SvgIcon, DiscoveriesTable
  },
  data () {
    return {
      isLoading: false,
      title: 'Discoveries',
      items: [],
      planInstance: {}
    }
  },
  computed: {
    isDiscoveriesEmpty () {
      return this.items.length === 0
    }
  },
  methods: {
    ...mapActions('app', ['setTitle']),
    ...mapActions('discovery', ['getDiscoveriesByRule']),
    ...mapActions('rule', ['getRule']),
    load (q) {
      this.isLoading = true
      const planInstanceId = +this.planInstanceId
      const planId = +this.planId
      const ruleId = +this.ruleId
      const query = q ?? { page: this.page }
      this.getDiscoveriesByRule({ planId, planInstanceId, ruleId, query }).then(result => {
        this.addPage(result)
      }).finally(() => { this.isLoading = false })
    },
    onScroll (e) {
      if (Math.round(window.scrollY + window.innerHeight) >= -200 + Math.round(document.body.scrollHeight)) {
        if (!this.isLoading && this.hasNextPage()) {
          this.nextPage()
          this.load()
        }
      }
    },
    initTitle () {
      const id = +this.ruleId
      this.setTitle({ isLoading: true })
      this.getRule(id).then(result => {
        this.setTitle({ isLoading: false, text: `Discoveries for Rule: ${result.name}` })
      })
    }
  },
  mounted () {
    this.load()
    this.initTitle()
    window.addEventListener('scroll', this.onScroll)
  },
  beforeDestroy () {
    window.removeEventListener('scroll', this.onScroll)
    this.setTitle({ isLoading: false, text: undefined })
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
