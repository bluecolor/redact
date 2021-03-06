<template lang="pug">
.container
  .empty.w-full.bg-white(v-if="isPlansEmpty")
    .text-xl.text-gray-400.text-center There is nothing here!
    .project-logo.flex.justify-center.mt-10.w-full()
      svg-icon(name="cloud-computing", addClass="fill-current text-gray-300 w-24 h-24")
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
                    content="Run plan" v-tippy='{ placement : "top" }'
                    @click="onRun(p)"
                  )
                  router-link.icon-btn.las.la-pen(
                    :to="`plans/${p.id}`")
                  .icon-btn.las.la-trash-alt.danger(
                    content="Delete plan" v-tippy='{ placement : "top" }'
                    @click="onDelete()"
                  )
                .spinner.lds-dual-ring(v-else)
          template(v-slot:default)
            | {{p.description}}

      t-button.mt-10.w-full.text-center(tagName="a" :href="`/connections/${connectionId}/discovery/plans/create`")
        | Create New Plan

</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import SvgIcon from '@/components/SvgIcon'

export default {
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
    ...mapGetters('discovery', ['plans']),
    isPlansEmpty () {
      return this.plans.length === 0
    }
  },
  methods: {
    ...mapActions('discovery', ['getPlans']),
    onDelete () {},
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
