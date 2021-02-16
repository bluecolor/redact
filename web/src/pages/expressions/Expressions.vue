<template lang="pug">
page-loader(v-if="isSpinner")
.empty.w-full(v-if="isExpressionsEmpty")
  .text-xl.text-gray-400.text-center There is nothing here!
  .project-logo.flex.justify-center.mt-10.w-full()
    svg-icon(name="cloud-computing", addClass="fill-current text-gray-300 w-24 h-24")
  .flex.justify-center.mt-10
    router-link.btn.create-btn.mt-10(tag="button" class="w-2/3" to="/connections/create")
      | Create New Expression
.connections-container.flex.justify-center.w-full(v-else)
  .body.w-full.flex.items-center.flex-col
    .connections.gap-y-3.flex.flex-col.w-full
      expression-card(v-for="e in expressions" :expression="e")
    router-link.btn.create-btn.mt-10.w-full(tag="button"
      :to="`/connections/${connectionId}/expressions/create`"
    )
      | Create New Expression
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import SvgIcon from '@/components/SvgIcon'
import PageLoader from '@/components/loaders'
import ConnectionCard from '@/components/ConnectionCard'
import ExpressionCard from '@/components/ExpressionCard'

export default {
  props: ['connectionId'],
  components: {
    SvgIcon, PageLoader, ConnectionCard, ExpressionCard
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
      this.getExpressions(this.connectionId).then(r => {
        console.log(r)
      }).finally(() => { this.isSpinner = false })
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
