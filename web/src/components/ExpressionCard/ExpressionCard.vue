<template lang="pug">
t-card.card
  template(v-slot:header)
    .flex.justify-between
      .title
        | {{e.policy_expression_name}}
      .actions.flex.justify-end
        .btns.gap-x-3.flex(v-if="!isSpinner")
          router-link.icon-btn.las.la-columns(
            content="Apply to column" v-tippy='{ placement : "top" }'
            :to="`expressions/${encodeURI(e.policy_expression_name)}/apply-to-column`"
          )
          router-link.icon-btn.las.la-pen(:to="`expressions/${encodeURI(e.policy_expression_name)}`")
          .icon-btn.las.la-trash-alt.danger(@click="onDelete(e)")
        .spinner.lds-dual-ring(v-else)
  template(v-slot:default)
    .flex.justify-between
      .start.flex.flex-col.gap-y-2
        .expression.text-gray-600.overflow-ellipsis {{e.expression}}
        .description.text-gray-400.overflow-ellipsis {{e.policy_expression_description}}
      .end.flex.flex-col.justify-end
        .object-full-name {{getFullName(e)}}

</template>

<script>
/* eslint-disable camelcase */
import { mapActions } from 'vuex'

export default {
  props: { e: { type: Object, default: () => {} } },
  data () {
    return {
      isSpinner: false
    }
  },
  methods: {
    ...mapActions('expression', ['deleteExpression']),
    getFullName (e) {
      const names = []
      e.object_owner && names.push(e.object_owner)
      e.object_name && names.push(e.object_name)
      e.column_name && names.push(e.column_name)
      return names.join('.')
    },
    onDelete (e) {
      const { policy_expression_name } = e
      this.deleteExpression({ policy_expression_name }).then(() => {
        this.$toast.success('Success. Dropped expression')
        this.$emit('delete', e)
      }).catch(error => {
        console.log(error)
        this.$toast.error('Error. Failed to drop expression')
      })
    }
  }
}
</script>
