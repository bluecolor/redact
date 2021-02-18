<template lang="pug">
prompt(:params="prompt" v-if="prompt.show" @hide="prompt.show=false")
.card.w-full
  .overflow-hidden.border.rounded-md.w-full
    // card header
    .card-heder.px-3.py-3.bg-white.border-b.border-gray-200.uppercase.flex.justify-between
      .title
        | {{category.policy_expression?.policy_expression_name}}
      .actions.flex.justify-end
        // button link
        .btns.gap-x-3.flex(v-if="!isSpinner")
          router-link.icon-btn.las.la-pen(:to="`expressions/${encodeURI(category.policy_expression_name)}`")
          .icon-btn.las.la-trash-alt.danger(@click="onDelete()")
        .spinner.lds-dual-ring(v-else)
    // card body
    .p-3.bg-white.border-gray-200
      span(v-if="category.policy_expression_description")
        |{{category.policy_expression_description}}
      span(v-else) No description
</template>

<script>
import { mapActions } from 'vuex'
import Prompt from '@/components/Prompt'

export default {
  props: {
    category: { type: Object, default: () => {} }
  },
  components: { Prompt },
  data () {
    return {
      isSpinner: false,
      prompt: {
        show: false,
        title: 'Delete Category',
        description: 'This will only delete category definition. Related expression will remain.',
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
