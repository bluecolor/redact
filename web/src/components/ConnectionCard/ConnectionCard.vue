<template lang="pug">
t-card.card
  template(v-slot:header)
    .flex.justify-between
      .title
        | {{c.name}}
      .actions.flex.justify-end
        .btns.gap-x-3.flex(v-if="!isSpinner")
          router-link.icon-btn.las.la-pen(:to="`connections/${c.id}`" v-slot="{ navigate }")
          .icon-btn.las.la-vial(
            content="Test connection" v-tippy='{ placement : "top" }'
            @click="onTest(c.id)"
          )
          .icon-btn.las.la-trash-alt.danger.text-center.items-center(@click="onDelete(c)")
          t-icon-dropdown(
            :classes="{icon: 'las la-ellipsis-v'}"
            :emitValue="true" :items="menu", valueProp="path")
        .spinner.lds-dual-ring(v-else)
  template(v-slot:default)
    |{{c.host}}:{{c.port}}/{{c.service}}
</template>

<script>
import { mapActions } from 'vuex'
import TIconDropdown from '@/components/TIconDropdown'

export default {
  components: { TIconDropdown },
  props: { c: { type: Object, default: () => {} } },
  data () {
    return {
      menu: [
        { name: 'Export', value: 'export', icon: 'las la-download' },
        { name: 'Import', value: 'import', icon: 'las la-upload' }],
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
    },
    load () {
      this.isSpinner = true
      this.getConnections().finally(() => { this.isSpinner = false })
    }
  }
}
</script>>
