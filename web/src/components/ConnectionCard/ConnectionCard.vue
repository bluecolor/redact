<template lang="pug">
prompt(:params="prompt" v-if="prompt.show" @hide="prompt.show=false")
.card.w-full
  .overflow-hidden.border.rounded-md.w-full
    // card header
    .card-heder.px-3.py-3.bg-white.border-b.border-gray-200.uppercase.flex.justify-between
      .title
        | {{connection.name}}
      .actions.flex.justify-end
        // button link
        .btns.gap-x-3.flex(v-if="!isSpinner")
          router-link.icon-btn.las.la-pen(:to="`/connections/${connection.id}/edit`")
          .icon-btn.las.la-vial(@click="onTest(connection.id)")
          .icon-btn.las.la-trash-alt.danger(@click="onDelete(connection.id)")
        .spinner.lds-dual-ring(v-else)
    // card body
    .p-3.bg-white.border-gray-200
      |{{connection.host}}:{{connection.port}}/{{connection.service}}
</template>

<script>
import { mapActions } from 'vuex'
import Prompt from '@/components/Prompt'

export default {
  props: {
    connection: { type: Object, default: () => {} }
  },
  components: { Prompt },
  data () {
    return {
      isSpinner: false,
      prompt: {
        show: false,
        title: 'Delete Connection?',
        description: 'This will only delete connection. All redactions will be kept on database.',
        ok: 'Delete',
        cb: { ok: () => {}, cancel: () => {} }
      }
    }
  },
  methods: {
    ...mapActions('connection', ['deleteConnection', 'testConnection']),
    onDelete (id) {
      this.isSpinner = true
      this.prompt.cb.ok = () => {
        this.deleteConnection(id).finally(() => { this.isSpinner = false })
      }
      this.prompt.show = true
    },
    onTest (id) {
      this.isSpinner = true
      this.testConnection(id).then(result => {
        if (result) {
          this.$toast.success('Success')
        } else {
          this.$toast.success('Error')
        }
      }).catch(e => {
        console.log(e)
        this.$toast.error('Error!')
      }).finally(() => {
        this.isSpinner = false
      })
    }
  }

}
</script>

<style lang="scss" scoped>
.card {
  .actions {
    .icon-btn { visibility: hidden;}
  }
  &:hover {
    .border {
      @apply border-blue-600;
    }
    .actions {
      .icon-btn { visibility: visible;}
    }
  }
}

</style>
