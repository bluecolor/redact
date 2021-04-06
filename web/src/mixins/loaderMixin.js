
export default {
  data () {
    return { isSpinner: false, isLoading: false }
  },
  methods: {
    startSpinner () {
      this.isSpinner = true
      return this
    },
    stopSpinner () {
      this.isSpinner = false
      return this
    },
    startLoader () {
      this.isLoading = true
    },
    stopLoader () {
      this.isLoading = false
    }
  }
}
