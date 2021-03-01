<template lang="pug">
div
  .empty.w-full(v-if="isExpressionsEmpty")
    .text-xl.text-gray-400.text-center There is nothing here!
    .project-logo.flex.justify-center.mt-10.w-full()
      svg-icon(name="cloud-computing", addClass="fill-current text-gray-300 w-24 h-24")
    .flex.justify-center.mt-10
      t-button.mt-10.w-full.text-center(tagName="a"
        :href="`/connections/${connectionId}/expressions/create`" text="Create New Expression")
  .connections-container.flex.justify-center.w-full(v-else)
    .body.w-full.flex.items-center.flex-col
      .gap-y-3.flex.flex-col.w-full
        t-card.card(v-for="e in expressions")
          template(v-slot:header)
            .flex.justify-between
              .title
                | {{e.policy_expression_name}}
              .actions.flex.justify-end
                .btns.gap-x-3.flex(v-if="!isSpinner")
                  router-link.icon-btn.las.la-pen(:to="`expressions/${encodeURI(e.policy_expression_name)}`")
                  .icon-btn.las.la-trash-alt.danger(@click="onDelete()")
                .spinner.lds-dual-ring(v-else)
          template(v-slot:default)
            | Content of the card.

      t-button.mt-10.w-full.text-center(tagName="a"
        :href="`/connections/${connectionId}/expressions/create`" text="Create New Expression")
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import SvgIcon from '@/components/SvgIcon'

export default {
  props: ['connectionId'],
  components: {
    SvgIcon
  },
  data () {
    return {
      isSpinner: false,
      title: 'Connections'
    }
  },
  computed: {
    ...mapGetters('redact', ['expressions', 'isExpressionsEmpty'])
  },
  methods: {
    ...mapActions('redact', ['getExpressions']),
    load () {
      this.isSpinner = true
      this.getExpressions(this.connectionId).finally(() => { this.isSpinner = false })
    }
  },
  mounted () {
    this.load()
  }
}
</script>

<style lang="postcss" scoped>
.empty {
  @apply border-dashed p-3 border-2 rounded-md w-full
}
.page {
}

</style>
