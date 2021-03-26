<template lang="pug">
.flex.justify-center.flex-col.edit-user
  t-card
    template(v-slot:default)
      form(autocomplete="off" @submit="onSumbit")
        .form-item
          t-input-group(label='Name', required)
            t-input(v-model="payload.name")
        .form-item
          t-input-group(label='Username', required)
            t-input(v-model="payload.username"  required)
        .form-item
          t-input-group(label='Email', required)
            t-input(v-model="payload.email" required)
        .form-item
          t-input-group(label='Password', required)
            t-input(v-model="payload.password" required type="password")
        .form-item
          t-input-group(label='API Key', required)
            .api-key-wrapper.relative
              t-input.api-key-input#api-key-input(@focus="onCopyApiKey" v-model="payload.api_key" required readonly)
              .api-sync.icon-btn.las.la-sync-alt(@click="onRegenerateApiKey")
        .form-item.mt-5
          .flex.justify-between.items-center
            .spinner.lds-dual-ring(v-if="isSpinner")
            .flex.gap-x-3(v-else class="w-1/2")
              t-button(type="submit" value="submit")
                span Save
            .end
              t-button(@click="onCancel" type="button" variant="error")
                | Close
</template>

<script>
/* eslint-disable camelcase */
import { mapActions } from 'vuex'

export default {
  props: ['id'],
  components: {
  },
  data () {
    return {
      isSpinner: false,
      isValid: false,
      payload: {
        name: '',
        username: '',
        email: '',
        password: '',
        api_key: ''
      }
    }
  },
  computed: {
  },
  methods: {
    ...mapActions('user', ['getMe', 'updateUser', 'getUser', 'regenerateApiKey']),
    onCopyApiKey () {
      const copyText = document.getElementById('api-key-input')
      copyText.select()
      copyText.setSelectionRange(0, 99999)
      document.execCommand('copy')
      this.$toasted.success('Copied to clipboard')
    },
    onRegenerateApiKey () {
      let id = +this.id
      if (this.$route.name === 'profile') {
        id = this.payload.id
      }
      this.regenerateApiKey(id).then(({ api_key }) => {
        this.payload.api_key = api_key
        this.$toasted.success('Success. Regerated API key')
      })
    },
    onCancel () {
      window.history.back()
    },
    onSumbit (e) {
      e.preventDefault()
      this.isSpinner = true
      console.log(this.payload)
      this.updateUser(this.payload).then(() => {
        this.$toast.success('Success. User updated')
      }).finally(() => {
        this.isSpinner = false
      })
    },
    load () {
      this.isSpinner = true
      this.getUser(+this.id).then(result => {
        this.payload = result
      }).finally(() => {
        this.isSpinner = false
      })
    }
  },
  created () {
    if (this.$route.name) {
      this.getMe().then(result => {
        this.payload = { ...result }
      })
    } else if (this.id) { this.load() }
  }
}
</script>

<style lang="postcss">
.edit-user .api-sync {
  position: absolute;
  right: 10px;
  bottom: 0.5rem;
  @apply text-gray-400;
}
.edit-user .api-sync:hover {
  @apply text-gray-600;
}
.edit-user .api-key-input {
  @apply cursor-pointer text-gray-400 hover:bg-green-50;
}
</style>
