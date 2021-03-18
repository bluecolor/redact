<template lang="pug">
  t-card.card
    template(v-slot:header)
      .flex.justify-between
        .title
          | {{d.rule.name}}
        .actions.flex.justify-end
          .btns.gap-x-3.flex(v-if="!isSpinner")
            .icon-btn.las.la-info-circle(
              content="Details" v-tippy='{ placement : "top" }'
            )
          .spinner.lds-dual-ring(v-else)
    template(v-slot:default)
      | {{d.schema_name}}.{{d.table_name}}.{{d.column_name}}

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
