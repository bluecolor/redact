<template lang="pug">
.policies-container
  .bg-white.empty.w-full(v-if="isPoliciesEmpty")
    .text-xl.text-gray-400.text-center There is nothing here!
    .project-logo.flex.justify-center.mt-10.w-full()
      svg-icon(name="cloud-computing", addClass="fill-current text-gray-300 w-24 h-24")
    .flex.justify-center.mt-10
      t-button.mt-10.w-full.text-center(tagName="a" :href="`/connections/${connectionId}/policies/create`")
        | Create New Policy
  .flex.justify-center.w-full(v-else)
    .body.w-full.flex.items-center.flex-col
      .connections.gap-y-3.flex.flex-col.w-full
        t-card.card(v-for="p in policies" :header='p.policy_name')
          template(v-slot:header)
            .flex.justify-between
              .title
                | {{p.policy_name}}
              .actions.flex.justify-end
                .btns.gap-x-3.flex(v-if="!isSpinner")
                  router-link.icon-btn.las.la-columns(
                    content="Policy columns" v-tippy='{ placement : "top" }'
                    :to="`policies/columns?policy_name=${encodeURI(p.policy_name)}&object_owner=${encodeURI(p.object_owner)}&object_name=${encodeURI(p.object_name)}`")
                  router-link.icon-btn.las.la-pen(
                    content="Edit policy" v-tippy='{ placement : "top" }'
                    :to="`policies/edit?policy_name=${encodeURI(p.policy_name)}&object_owner=${encodeURI(p.object_owner)}&object_name=${encodeURI(p.object_name)}`")
                  .icon-btn.las.la-trash-alt.danger(
                    content="Delete policy" v-tippy='{ placement : "top" }'
                    @click="onDelete()"
                  )
                .spinner.lds-dual-ring(v-else)
          template(v-slot:default)
            | Content of the card.

      t-button.mt-10.w-full.text-center(tagName="a" :href="`/connections/${connectionId}/policies/create`")
        | Create New Policy
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
      title: 'Policies'
    }
  },
  computed: {
    ...mapGetters('redact', ['policies']),
    isPoliciesEmpty () {
      return this.policies.length === 0
    }
  },
  methods: {
    ...mapActions('redact', ['getPolicies']),
    load () {
      this.isSpinner = true
      this.getPolicies().finally(() => { this.isSpinner = false })
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
