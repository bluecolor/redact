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
          this.$toasted.success('Success')
        } else {
          this.$toasted.error('Error')
        }
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Error')
      }).finally(() => {
        this.isSpinner = false
      })
    },
    onCancel () { window.history.back() }
  }
}
