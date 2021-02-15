import { mapActions } from 'vuex'

export default {
  data () {
    return {
      isSpinner: false
    }
  },
  methods: {
    ...mapActions('connection', ['testConnection']),
    onTest () {
      this.isSpinner = true
      this.testConnection(this.payload).then(result => {
        if (result) {
          this.$toast.success('Success')
        } else {
          this.$toast.error('Error')
        }
      }).catch(error => {
        console.log(error)
        this.$toast.error('Error')
      }).finally(() => {
        this.isSpinner = false
      })
    },
    onCancel () { window.history.back() }
  }
}
