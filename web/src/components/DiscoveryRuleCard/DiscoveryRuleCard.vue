<template lang="pug">
t-card.card
  template(v-slot:header)
    .flex.justify-between
      .title.flex.gap-x-2.items-center
        .las.la-ruler.text-2xl.text-gray-400
        .text
          | {{d.rule.name}}
      .actions.flex.justify-end
        .btns.gap-x-3.flex(v-if="!isSpinner")
          router-link.icon-btn.las.la-info-circle(
            content="Details" v-tippy='{ placement : "top" }'
            :to="`/`"
          )
        .spinner.lds-dual-ring(v-else)
  template(v-slot:default)
    .flex.justify-between
      .flex.gap-x-3
        t-tag.p-1(
          content="Rule type" v-tippy='{ placement : "left" }'
          :class="{ 'bg-yellow-100': d.rule.type==='metadata',\
              'bg-green-100': d.rule.type==='data'}"
          tag-name="span" variant="badge"
        ) {{d.rule.type}}
        t-tag.p-1(
          content="Severity" v-tippy='{ placement : "left" }'
          :class="{ 'bg-gray-100': d.rule.severity==='low',\
              'bg-indigo-100': d.rule.severity==='medium',\
              'bg-red-100': d.rule.severity==='high'}"
          tag-name="span" variant="badge"
        ) {{d.rule.severity}}
      .result
        router-link(
          class="hover:underline"
          :to="`rules/${d.rule.id}/discoveries`"
        ) {{d.count}} findings

</template>

<script>
import { dateMixin } from '@/mixins'

export default {
  mixins: [dateMixin],
  props: { d: { type: Object, default: () => {} } },
  data () {
    return {
      isSpinner: false
    }
  }
}
</script>
