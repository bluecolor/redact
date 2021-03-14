<template lang="pug">
t-card.card
  template(v-slot:header)
    .flex.justify-between
      .title
        | {{p.name}}
      .actions.flex.justify-end
        .btns.gap-x-3.flex(v-if="!isSpinner")
          .icon-btn.las.la-play(
            v-if="p.rules.length > 0"
            content="Run plan" v-tippy='{ placement : "top" }'
            @click="onRun(p)"
          )
          router-link.icon-btn.las.la-shipping-fast(:to="`plans/${p.id}/instances`")
          router-link.icon-btn.las.la-pen(:to="`plans/${p.id}`")
          .icon-btn.las.la-trash-alt.danger(
            content="Delete plan" v-tippy='{ placement : "top" }'
            @click="onDelete(p)"
          )
        .spinner.lds-dual-ring(v-else)
  template(v-slot:default)
    .flex.justify-between
      .start.flex.flex-col.gap-y-2
        .description.text-gray-400.overflow-ellipsis {{p.description}}
        .text-gray-600(v-if="p.rules.length!==0") {{p.rules.length}} rule{{p.rules.length>1?'s':''}}
        .text-red-300(v-if="p.rules.length==0") Does not have rules
      .end.flex.flex-col.justify-end.gap-y-3
        .flex.justify-end
          t-tag.p-1.bg-blue-100(v-if="p.status==='running'" tag-name="span" variant="badge") {{p.status}}
        .text-gray-400.text-sm.flex.justify-end {{formatDate(p.created_on)}}
</template>

<script>
import { mapActions } from 'vuex'
import { dateMixin } from '@/mixins'

export default {
  mixins: [dateMixin],
  props: { p: { type: Object, default: () => {} } },
  data () {
    return {
      isSpinner: false
    }
  },
  methods: {
    ...mapActions('plan', ['deletePlan']),
    onDelete (p) {
      this.isSpinner = true
      this.deletePlan(p.id).then(() => {
        this.$toast.success('Success. Plan deleted')
        this.$emit('delete', p)
      }).catch(error => {
        console.log(error)
        this.$toast.error('Error. Failed to delete plan')
      }).finally(() => {
        this.isSpinner = false
      })
    },
    onRun (p) {}
  }
}
</script>
