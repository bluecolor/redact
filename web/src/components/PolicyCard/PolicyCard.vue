<template lang="pug">
t-card.card
  template(v-slot:header)
    .flex.justify-between
      .title
        | {{p.policy_name}}
      .actions.flex.justify-end
        .btns.gap-x-3.flex(v-if="!isSpinner")
          router-link.icon-btn.las.la-columns(
            content="Policy columns" v-tippy='{ placement : "top" }'
            :to="`policies/columns?policy_name=${encodeURI(p.policy_name)}&object_owner=${encodeURI(p.object_owner)}&object_name=${encodeURI(p.object_name)}`")
          router-link.icon-btn.las.la-pen(
            content="Edit policy" v-tippy='{ placement : "top" }'
            :to="`policies/edit?policy_name=${encodeURI(p.policy_name)}&object_owner=${encodeURI(p.object_owner)}&object_name=${encodeURI(p.object_name)}`")
          .icon-btn.las.la-trash-alt.danger(
            content="Delete policy" v-tippy='{ placement : "top" }'
            @click="onDelete(p)"
          )
          t-toggle(:checked="p.enable==='YES'" @change="onToggle(p)")
        .spinner.lds-dual-ring(v-else)
  template(v-slot:default)
    .flex.justify-between
      .start.flex.flex-col.gap-y-2
        .expression.text-gray-600.overflow-ellipsis {{p.expression}}
        .description.text-gray-400.overflow-ellipsis {{p.policy_description}}
      .end.flex.flex-col.justify-end
        .object-full-name {{getFullName(p)}}

</template>

<script>
/* eslint-disable camelcase */
import { mapActions } from 'vuex'

export default {
  props: {
    p: { type: Object, default: () => {} }
  },
  data () {
    return {
      isSpinner: false
    }
  },
  methods: {
    ...mapActions('policy', ['deletePolicy', 'disablePolicy', 'enablePolicy']),
    getFullName (p) {
      const names = []
      p.object_owner && names.push(p.object_owner)
      p.object_name && names.push(p.object_name)
      return names.join('.')
    },
    onToggle (p) {
      const { object_owner } = p
      const policy = { ...p, object_schema: object_owner }
      if (p.enable === 'YES') { this.onDisable(policy) } else { this.onEnable(policy) }
    },
    onDisable (p) {
      this.isSpinner = true
      this.disablePolicy(p).then(() => {
        this.$toasted.success('Success. Disabled policy')
        this.$emit('disable', p)
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Error. Failed to disable policy')
      }).finally(() => {
        this.isSpinner = false
      })
    },
    onEnable (p) {
      this.isSpinner = true
      this.enablePolicy(p).then(() => {
        this.$toasted.success('Success. Enabled policy')
        this.$emit('enable', p)
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Error. Failed to enable policy')
      }).finally(() => {
        this.isSpinner = false
      })
    },
    onDelete (p) {
      this.isSpinner = true
      const { object_owner } = p
      this.deletePolicy({ ...p, object_schema: object_owner }).then(() => {
        this.$toasted.success('Success. Deleted policy')
        this.$emit('delete', p)
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Error. Failed to delete policy')
      }).finally(() => { this.isSpinner = false })
    }
  }
}
</script>
