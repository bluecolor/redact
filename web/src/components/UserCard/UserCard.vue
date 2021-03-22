<template lang="pug">
t-card.card
  template(v-slot:header)
    .flex.justify-between
      .title
        | {{u.name}}
      .actions.flex.justify-end
        .btns.gap-x-3.flex(v-if="!isSpinner")
          router-link.icon-btn.las.la-pen(:to="`users/${u.id}`" v-slot="{ navigate }")
          .icon-btn.las.la-trash-alt.danger.text-center.items-center(@click="onDelete(u)")
        .spinner.lds-dual-ring(v-else)
  template(v-slot:default)
    | {{u.email}}
</template>

<script>
import { mapActions } from 'vuex'

export default {
  props: { u: { type: Object, default: () => {} } },
  data () {
    return {
      isSpinner: false
    }
  },
  methods: {
    ...mapActions('connection', ['deleteConnection', 'testConnection']),
    onDelete (c) {
      this.isSpinner = true
      this.deleteConnection(c.id).then(() => {
        this.$toasted.success('Success. Deleted connection')
        this.$emit('delete', c)
      }).catch(error => {
        console.log(error)
        this.$$toasted.error('Error. Failed to delete connection')
      }).finally(() => { this.isSpinner = false })
    },
    load () {
      this.isSpinner = true
      this.getConnections().finally(() => { this.isSpinner = false })
    }
  }
}
</script>>
