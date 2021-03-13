import dayjs from 'dayjs'

export default {
  methods: {
    fromNow (d) {
      return dayjs(d).fromNow()
    },
    formatDate (d, f = "MMM D 'YY [at] H:mm") {
      return dayjs(d).format(f)
    }
  }
}
