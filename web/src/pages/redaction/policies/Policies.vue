<template lang="pug">
.policies-container
  .loader.text-gray-600(v-if="isLoading")
  .bg-white.empty.w-full(v-if="!isLoading && isPoliciesEmpty")
    .text-xl.text-gray-400.text-center There is nothing here!
    .flex.justify-center.mt-10.w-full()
      svg-icon(name="box", addClass="fill-current text-gray-300 w-24 h-24")
    .flex.justify-center.mt-10
      t-button.mt-10.w-full.text-center(tagName="a" :href="`/connections/${connectionId}/policies/create`")
        | Create New Policy
  .flex.justify-center.w-full(v-else)
    .body.w-full.flex.items-center.flex-col
      .gap-y-3.flex.flex-col.w-full
        policy-card(v-for="p in policies" :p="p")
      t-button.mt-10.w-full.text-center(tagName="a" :href="`/connections/${connectionId}/policies/create`")
        | Create New Policy
</template>

<script>
/* eslint-disable camelcase */

import { mapActions } from 'vuex'
import SvgIcon from '@/components/SvgIcon'
import PolicyCard from '@/components/PolicyCard'
import { loaderMixin } from '@/mixins'

export default {
  mixins: [loaderMixin],
  props: ['connectionId'],
  components: {
    SvgIcon, PolicyCard
  },
  data () {
    return {
      title: 'Policies',
      policies: []
    }
  },
  computed: {
    isPoliciesEmpty () {
      return this.policies.length === 0
    }
  },
  methods: {
    ...mapActions('policy', ['getPolicies']),
    load () {
      this.startLoader()
      this.getPolicies().then(result => {
        this.policies = result
      }).finally(this.stopLoader)
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
