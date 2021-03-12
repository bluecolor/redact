<template lang="pug">
.container
  .empty.w-full.bg-white(v-if="isRulesEmpty")
    .text-xl.text-gray-400.text-center There is nothing here!
    .project-logo.flex.justify-center.mt-10.w-full()
      svg-icon(name="cloud-computing", addClass="fill-current text-gray-300 w-24 h-24")
    .flex.justify-center.mt-10
      t-button.mt-10.w-full.text-center(tagName="a" :href="`rules/create`")
        | Create New Rule
  .flex.justify-center.w-full(v-else)
    .body.w-full.flex.items-center.flex-col
      .gap-y-3.flex.flex-col.w-full
        t-card.card(v-for="r in rules")
          template(v-slot:header)
            .flex.justify-between
              .title
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
            | {{r.description}}

      t-button.mt-10.w-full.text-center(tagName="a" :href="`rules/create`")
        | Create New Rule

</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import SvgIcon from '@/components/SvgIcon'

export default {
  components: {
    SvgIcon
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
    ...mapActions('rule', ['getRules', 'deleteRule']),
    onDelete ({ id }) {
      this.isSpinner = true
      this.deleteRule(id).then(() => {
        this.$toasted.success('Success. Deleted rule')
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Error. Failed to delete rule')
      }).finally(() => {
        this.isSpinner = false
      })
    }
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
