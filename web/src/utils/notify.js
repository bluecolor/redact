export default {
  toast: {
    success (msg = 'Success') {
      this.$toasted.success(msg)
    },
    error (msg = 'Error') {
      this.$toasted.error(msg)
    }
  }
}
