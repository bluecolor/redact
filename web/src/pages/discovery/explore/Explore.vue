<template lang="pug">
.flex.justify-center.w-full
  .body.w-full.flex.items-center.flex-col
    .gap-y-3.flex.flex-col.w-full
      .flex.gap-x-5
        t-input(v-model="search" placeholder="Search")
    .flex.justify-center.mt-5.w-full()
      .empty.flex.flex-col.justify-between.gap-y-6(v-if="isEmpty")
        .flex.justify-center.mt-10.w-full
          svg-icon(name="box", addClass="fill-current text-gray-300 w-24 h-24")
        .text.text-center.text-gray-400
          | Start typing to search database
      .flex.justify-center.w-full(v-else)
        .body.w-full.flex.items-center.flex-col
          .gap-y-3.flex.flex-col.w-full
            metadata-card(v-for="m in items" :m="m")

</template>

<script>
import _ from 'lodash'
import { mapActions } from 'vuex'
import SvgIcon from '@/components/SvgIcon'
import MetadataCard from '@/components/MetadataCard'

export default {
  props: ['connectionId', 's'],
  components: {
    SvgIcon, MetadataCard
  },
  data () {
    return {
      isSpinner: false,
      search: '',
      items: []
    }
  },
  watch: {
    search (q) {
      if (q.length >= 3) {
        this.doSearch(q)
      }
    },
    s (q) {
      this.doSearch(q)
    }
  },
  computed: {
    isEmpty () { return this.items.length === 0 }
  },
  methods: {
    ...mapActions('md', ['searchMetadata']),
    doSearch (q) {
      this.isSpinner = true
      this.searchMetadata(q).then(result => {
        this.items = result
      }).finally(() => {
        this.isSpinner = false
      })
    }
  },
  created () {
    this.load = _.debounce(this.searchMetadata, 300)
    if (this.s) {
      this.doSearch(this.s)
    }
  }
}
</script>
