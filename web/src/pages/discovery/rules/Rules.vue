<template lang="pug">
.container
  .empty.w-full.bg-white(v-if="isRulesEmpty")
    .text-xl.text-gray-400.text-center There is nothing here!
    .project-logo.flex.justify-center.mt-10.w-full()
      svg-icon(name="box", addClass="fill-current text-gray-300 w-24 h-24")
    .flex.justify-center.mt-10
      t-button.mt-10.w-full.text-center(tagName="a" :href="`rules/create`")
        | Create New Rule
  .flex.justify-center.w-full(v-else)
    .body.w-full.flex.items-center.flex-col
      .gap-y-3.flex.flex-col.w-full
        rule-card(v-for="r in rules" :r="r")
      t-button.mt-10.w-full.text-center(tagName="a" :href="`rules/create`")
        | Create New Rule

</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import SvgIcon from '@/components/SvgIcon'
import RuleCard from '@/components/RuleCard'

export default {
  components: {
    SvgIcon, RuleCard
  },
  data () {
    return {
      isSpinner: false
    }
  },
  computed: {
    ...mapGetters('rule', ['rules']),
    isRulesEmpty () {
      return this.rules.length === 0
    }
  },
  methods: {
    ...mapActions('rule', ['getRules'])
  },
  created () {
    this.getRules()
  }
}
</script>

<style lang="postcss" scoped>
.empty {
  @apply border-dashed p-3 border-2 rounded-md w-full
}
</style>
