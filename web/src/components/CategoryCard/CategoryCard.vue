<template lang="pug">
t-card.card
  template(v-slot:header)
    .flex.justify-between
      .title.flex.gap-x-2.items-center
        .las.la-tag.text-2xl.text-gray-400
        .text
          | {{c.name}}
      .actions.flex.justify-end
        .btns.gap-x-3.flex(v-if="!isSpinner")
          router-link.icon-btn.las.la-pen(
            :to="`categories/${c.id}`")
          .icon-btn.las.la-trash-alt.danger(@click="onDelete(c)")
        .spinner.lds-dual-ring(v-else)
  template(v-slot:default)
    .flex.justify-between
      .start.flex.flex-col.gap-y-2
        .expression-name.overflow-ellipsis {{policy_expression_name}}
        .description.text-gray-400.overflow-ellipsis {{c.description}}
      .end.flex.flex-col.justify-between
        .function-type {{c.function_type_name}}
        .date.text-sm.text-gray-400 {{fromNow(c.updated_on)}}
</template>

<script>
import { mapActions } from 'vuex'
import { dateMixin } from '@/mixins'

export default {
  mixins: [dateMixin],
  props: { c: { type: Object, default: () => {} } },
  data () {
    return {
      isSpinner: false
    }
  },
  computed: {
    policy_expression_name () {
      return this.c.policy_expression?.policy_expression_name
    }
  },
  methods: {
    ...mapActions('category', ['deleteCategory']),
    onDelete (c) {
      this.isSpinner = true
      this.deleteCategory(c.id).then(() => {
        this.$toast.success('Success. Deleted category')
        this.$emit('delete', c)
      }).catch(error => {
        console.log(error)
        this.$toast.error('Error. Failed to delete category')
      }).finally(() => { this.isSpinner = false })
    }
  },
  created () {
  }
}
</script>
