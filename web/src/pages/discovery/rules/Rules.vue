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
            .flex.justify-between
              .start.flex.flex-col.gap-y-2
                .expression.text-gray-600.overflow-ellipsis {{r.expression}}
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
      t-button.mt-10.w-full.text-center(tagName="a" :href="`rules/create`")
        | Create New Rule

</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import SvgIcon from '@/components/SvgIcon'
import { dateMixin } from '@/mixins'

export default {
  mixins: [dateMixin],
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
