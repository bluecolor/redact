import { mapActions } from 'vuex'

export default {
  data () {
    return {
      isSpinner: false,
      options: {
        search: {
          isFocus: false,
          isSpinner: false,
          schemas: []
        }
      }
    }
  },
  methods: {
    ...mapActions('connection', ['testConnection', 'getSchemasWithPayload']),
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
    onCancel () { window.history.back() },
    onSearchSchemasFocus () {
      this.options.search.isFocus = true
      this.options.search.isSpinner = true
      this.getSchemasWithPayload(this.payload).then(result => {
        this.options.search.schemas = result
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Failed to get schemas list')
      }).finally(() => { this.options.search.isSpinner = false })
    },
    onSearchSchemasBlur () {
      this.options.search.isFocus = false
    }
  }
}
