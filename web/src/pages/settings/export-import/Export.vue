<template lang="pug">
t-card
  form.flex.flex-col(autocomplete="off" @submit="onSumbit")
    .form-item
      t-input-group(label='Select items to export:')
        t-checkbox-group(v-model="payload.options" :options="options" autofocus)
    .form-item.mt-5
      .flex.justify-between.items-center
        t-simple-spinner(v-if="isSpinner")
        .flex.gap-x-3(v-else class="w-1/2")
          t-button(type="submit" value="submit" text="Export")
        .end
          t-button(@click="onCancel" type="button" text="Close" variant="error")
</template>

<script>
import { mapActions } from 'vuex'

export default {
  data () {
    return {
      isSpinner: false,
      options: [
        { text: 'Expressions', value: 'expressions' },
        { text: 'Categories', value: 'categories' },
        { text: 'Policies', value: 'policies' },
        { text: 'Rules', value: 'rules' },
        { text: 'Plans', value: 'plans' }
      ],
      payload: {
        options: []
      }
    }
  },
  methods: {
    ...mapActions('impexp', ['exportSettings']),
    onCancel () {},
    onSumbit (e) {
      e.preventDefault()
      this.exportSettings(this.payload).then((result) => {
        const url = window.URL.createObjectURL(new Blob([result]))
        const link = document.createElement('a')
        link.href = url
        link.setAttribute('download', 'file.json')
        document.body.appendChild(link)
        link.click()
      })
    }
  }
}
</script>
