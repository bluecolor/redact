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
        .btns.gap-x-3.flex(v-if="!spinner")
          .icon-btn.las.la-pen
          .icon-btn.las.la-vial
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
        ok: 'Delete'
      }
    }
  },
  methods: {
    ...mapActions('connection', ['deleteConnection']),
    onDelete (id) {
      this.prompt.show = true
      this.isSpinner = true
      this.deleteConnection(id).finally(() => { this.isSpinner = false })
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
