<template lang="pug">
t-card.card
  template(v-slot:header)
    .flex.justify-between
      .title.flex.gap-x-2.items-center
        .las.la-ruler.text-2xl.text-gray-400
        .text
          | {{r.name}}
      .actions.flex.justify-end
        .btns.gap-x-3.flex(v-if="!isSpinner")
          router-link.icon-btn.las.la-pen(:to="`rules/${r.id}`")
          .icon-btn.las.la-trash-alt.danger(
            content="Delete rule" v-tippy='{ placement : "top" }'
            @click="onDelete(r)"
          )
        .spinner.lds-dual-ring(v-else)
  template(v-slot:default)
    .flex.justify-between
      .start.flex.flex-col.gap-y-2
        .expression.text-gray-600.overflow-ellipsis.text-red-400
          |{{r.expression}}
        .description.text-gray-400.overflow-ellipsis {{r.description}}
      .end.flex.flex-col.justify-end.gap-y-3
        .rule-type.flex.justify-end
          .flex.gap-x-2
            t-tag.p-1(
              content="Rule type" v-tippy='{ placement : "left" }'
              :class="{ 'bg-yellow-100': r.type==='metadata',\
                  'bg-green-100': r.type==='data'}"
              tag-name="span" variant="badge"
            ) {{r.type}}
            t-tag.p-1(
              content="Severity" v-tippy='{ placement : "left" }'
              :class="{ 'bg-gray-100': r.severity==='low',\
                  'bg-indigo-100': r.severity==='medium',\
                  'bg-red-100': r.severity==='high'}"
              tag-name="span" variant="badge"
            ) {{r.severity}}
        .text-gray-400.text-sm.flex.justify-end {{formatDate(r.created_on)}}
</template>

<script>
import { mapActions } from 'vuex'
import { dateMixin } from '@/mixins'

export default {
  mixins: [dateMixin],
  props: { r: { type: Object, default: () => {} } },
  data () {
    return {
      isSpinner: false
    }
  },
  methods: {
    ...mapActions('rule', ['deleteRule']),
    onDelete (r) {
      this.isSpinner = true
      this.deleteRule(r.id).then(() => {
        this.$toasted.success('Success. Deleted rule')
        this.$emit('delete', r)
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Error. Failed to delete rule')
      }).finally(() => {
        this.isSpinner = false
      })
    }
  }
}
</script>
