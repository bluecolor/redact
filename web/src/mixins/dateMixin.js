import dayjs from 'dayjs'
import relativeTime from 'dayjs/plugin/relativeTime'
dayjs.extend(relativeTime)

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
