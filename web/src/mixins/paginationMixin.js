export default {
  data () {
    return {
      items: [],
      total: 0,
      page: 0,
      size: 20
    }
  },
  methods: {
    initPagination ({ page, size }) {
      this.page = page ?? this.page
      this.size = size ?? this.size
    },
    addPage ({ items, page, size, total }) {
      this.items.push(...items)
      this.total = total
    },
    nextPage () {
      if (this.page * this.size < this.total) {
        this.page++
      }
    },
    prevPage () {
      if (this.page > 0) {
        this.page--
      }
    },
    hasNextPage () {
      return (this.page * this.size < this.total)
    },
    hasPrevPage () {
      return (this.page > 0)
    }
  }
}
