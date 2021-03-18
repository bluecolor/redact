<template lang="pug">
t-card.card
  template(v-slot:header)
    .flex.justify-between
      .title
        | {{p.plan.name}}
      .actions.flex.justify-end
        .btns.gap-x-3.flex(v-if="!isSpinner")
          .icon-btn.las.la-sync-alt(@click="onReload")
          router-link.icon-btn.las.la-compass(
            content="Discoveries" v-tippy='{ placement : "top" }'
            :to="`/connections/${p.plan.connection.id}/discovery/plans/${p.plan.id}/instances/${p.id}/discoveries-by-rule`")
          .icon-btn.las.la-stop-circle(
            v-if="p.status==='running'"
            content="Stop" v-tippy='{ placement : "top" }'
            @click="onStop(p)")
          .icon-btn.las.la-trash-alt.danger(
            v-if="p.status!=='running'"
            content="Delete" v-tippy='{ placement : "top" }'
            @click="onDelete(p)"
          )
        .spinner.lds-dual-ring(v-else)
  template(v-slot:default)
    .body.flex.justify-between
      .flex.flex-col
        .start-date.text-gray-400
          | started {{fromNow(p.created_on)}}
        .description.flex.flex-col.gap-y-2
          .description {{p.description}}
      .end.flex.flex-col.justify-between.gap-y-3
        .status.flex.justify-end
          t-tag.p-1(
            :class="{ 'bg-red-200': p.status==='error',\
                'bg-blue-200': p.status==='running',\
                'bg-green-200': p.status==='success'}"
            tag-name="span" variant="badge"
          ) {{p.status}}
        .flex.justify-end
          | {{p.discoveries.length}} discoveries
</template>

<script>
import { mapActions } from 'vuex'
import { dateMixin } from '@/mixins'

export default {
  mixins: [dateMixin],
  props: { p: { type: Object, default: () => {} } },
  data () {
    return { isSpinner: false }
  },
  methods: {
    ...mapActions('planInstance', ['deletePlanInstance', 'stopPlanInstance', 'getPlanInstance']),
    onDelete (p) {
      this.isSpinner = true
      this.deletePlanInstance({ id: p.id, planId: p.plan.id }).then(result => {
        this.$toasted.success('Success. Deleted plan run')
        this.$emit('delete', p)
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Error. Failed to delete plan run')
      }).finally(() => {
        this.isSpinner = false
      })
    },
    onStop (p) {
      this.isSpinner = true
      this.stopPlanInstance({ id: p.id, planId: p.plan.id }).then(result => {
        this.$toasted.success('Success. Stopped plan')
        this.$emit('stop', result)
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Failed to stop plan')
      }).finally(() => {
        this.isSpinner = false
      })
    },
    onReload () {
      const { id } = this.p
      const planId = this.p.plan.id
      this.isSpinner = true
      this.getPlanInstance({ planId, id }).then(result => {
        this.$emit('reload', result)
      }).finally(() => {
        this.isSpinner = false
      })
    }
  }

}
</script>
