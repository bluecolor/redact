<template lang="pug">
t-card
  form.flex.flex-col(autocomplete="off" @submit="onSumbit")
    .form-item
      t-input-group(label='File')
        input(type="file", name="file")
    .form-item
      t-input-group(label='Ignore errors')
        t-toggle(:checked="ignore_errors")
    .form-item.mt-5
      .flex.justify-between.items-center
        .spinner.lds-dual-ring(v-if="isSpinner")
        .flex.gap-x-3(v-else class="w-1/2")
          t-button(type="submit" value="submit" text="Import")
        .end
          t-button(@click="onCancel" type="button" text="Close" variant="error")
</template>

<script>
import { mapActions } from 'vuex'
import * as FilePond from 'filepond'
import 'filepond/dist/filepond.min.css'

export default {
  props: ['connectionId'],
  components: {
  },
  data () {
    return {
      pond: undefined,
      files: [],
      isSpinner: false,
      ignore_errors: false
    }
  },
  methods: {
    ...mapActions('impexp', ['exportSettings']),
    onCancel () {
      window.history.back()
    },
    handleFilePondInit () {

    },
    onSumbit (e) {
      e.preventDefault()
      this.pond.setOptions({
        server: {
          url: `http://localhost:8000/api/v1/connections/${this.connectionId}/settings/import?ignore_errors=${this.ignore_errors}`
        }
      })
      this.pond.processFile().then(file => {
        console.log(file)
      })
    }
  },
  mounted () {
    const inputElement = document.querySelector('input[type="file"]')
    this.pond = FilePond.create(inputElement, {
      credits: false,
      instantUpload: false,
      allowMultiple: false,
      required: true
    })
  }
}
</script>
