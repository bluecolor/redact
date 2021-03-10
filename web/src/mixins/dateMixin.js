import dayjs from 'dayjs'

export default {
  methods: {
    fromNow (d) {
      return dayjs(d).fromNow()
    }
  }
}
