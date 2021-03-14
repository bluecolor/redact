<template lang="pug">
div
  .bg-white.empty.w-full(v-if="isExpressionsEmpty")
    .text-xl.text-gray-400.text-center There is nothing here!
    .flex.justify-center.mt-10.w-full()
      svg-icon(name="box", addClass="fill-current text-gray-300 w-24 h-24")
    .flex.justify-center.mt-10
      t-button.mt-10.w-full.text-center(tagName="a"
        :href="`expressions/create`" text="Create New Expression")
  .container.flex.justify-center.w-full(v-else)
    .body.w-full.flex.items-center.flex-col
      .gap-y-3.flex.flex-col.w-full
        expression-card(v-for="e in expressions" :e="e")
      t-button.mt-10.w-full.text-center(tagName="a"
        :href="`expressions/create`" text="Create New Expression")
</template>

<script>
/* eslint-disable camelcase */
import { mapActions, mapGetters } from 'vuex'
import SvgIcon from '@/components/SvgIcon'
import ExpressionCard from '@/components/ExpressionCard'

export default {
  props: ['connectionId'],
  components: {
    SvgIcon, ExpressionCard
  },
  data () {
    return {
      isSpinner: false,
      title: 'Connections'
    }
  },
  computed: {
    ...mapGetters('expression', ['expressions']),
    isExpressionsEmpty () {
      return this.expressions.length === 0
    }
  },
  methods: {
    ...mapActions('expression', ['getExpressions', 'deleteExpression']),
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
