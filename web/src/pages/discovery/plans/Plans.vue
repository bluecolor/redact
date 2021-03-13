<template lang="pug">
.container
  .empty.w-full.bg-white(v-if="isPlansEmpty")
    .text-xl.text-gray-400.text-center There is nothing here!
    .project-logo.flex.justify-center.mt-10.w-full()
      svg-icon(name="box", addClass="fill-current text-gray-300 w-24 h-24")
    .flex.justify-center.mt-10
      t-button.mt-10.w-full.text-center(tagName="a" :href="`/connections/${connectionId}/discovery/plans/create`")
        | Create New Plan
  .flex.justify-center.w-full(v-else)
    .body.w-full.flex.items-center.flex-col
      .gap-y-3.flex.flex-col.w-full
        t-card.card(v-for="p in plans")
          template(v-slot:header)
            .flex.justify-between
              .title
                | {{p.name}}
              .actions.flex.justify-end
                .btns.gap-x-3.flex(v-if="!isSpinner")
                  .icon-btn.las.la-play(
                    v-if="p.rules.length > 0"
                    content="Run plan" v-tippy='{ placement : "top" }'
                    @click="onRun(p)"
                  )
                  router-link.icon-btn.las.la-shipping-fast(:to="`plans/${p.id}/instances`")
                  router-link.icon-btn.las.la-pen(:to="`plans/${p.id}`")
                  .icon-btn.las.la-trash-alt.danger(
                    content="Delete plan" v-tippy='{ placement : "top" }'
                    @click="onDelete(p)"
                  )
                .spinner.lds-dual-ring(v-else)
          template(v-slot:default)
            .flex.justify-between
              .start.flex.flex-col.gap-y-2
                .description.text-gray-400.overflow-ellipsis {{p.description}}
                .text-gray-600(v-if="p.rules.length!==0") {{p.rules.length}} rule{{p.rules.length>1?'s':''}}
                .text-red-300(v-if="p.rules.length==0") Does not have rules
              .end.flex.flex-col.justify-end.gap-y-3
                .flex.justify-end
                  t-tag.p-1.bg-blue-100(v-if="p.status==='running'" tag-name="span" variant="badge") {{p.status}}
                .text-gray-400.text-sm.flex.justify-end {{formatDate(p.created_on)}}

      t-button.mt-10.w-full.text-center(tagName="a" :href="`/connections/${connectionId}/discovery/plans/create`")
        | Create New Plan

</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import SvgIcon from '@/components/SvgIcon'
import { dateMixin } from '@/mixins'

export default {
  mixins: [dateMixin],
  props: ['connectionId'],
  components: {
    SvgIcon
  },
  data () {
    return {
      isSpinner: false
    }
  },
  computed: {
    ...mapGetters('plan', ['plans']),
    isPlansEmpty () {
      return this.plans.length === 0
    }
  },
  methods: {
    ...mapActions('plan', ['getPlans', 'deletePlan']),
    onDelete ({ id }) {
      this.isSpinner = true
      this.deletePlan(id).then(() => {
        this.$toast.success('Success. Plan deleted')
      }).catch(error => {
        console.log(error)
        this.$toast.error('Error. Failed to delete plan')
      }).finally(() => {
        this.isSpinner = false
      })
    },
    onRun (p) {}
  },
  created () {
    this.getPlans()
  }
}
</script>

<style lang="postcss" scoped>
.empty {
  @apply border-dashed p-3 border-2 rounded-md w-full
}
</style>
