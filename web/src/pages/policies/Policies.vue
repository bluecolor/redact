<template lang="pug">
.policies-container
  .bg-white.empty.w-full(v-if="isPoliciesEmpty")
    .text-xl.text-gray-400.text-center There is nothing here!
    .flex.justify-center.mt-10.w-full()
      svg-icon(name="box", addClass="fill-current text-gray-300 w-24 h-24")
    .flex.justify-center.mt-10
      t-button.mt-10.w-full.text-center(tagName="a" :href="`/connections/${connectionId}/policies/create`")
        | Create New Policy
  .flex.justify-center.w-full(v-else)
    .body.w-full.flex.items-center.flex-col
      .gap-y-3.flex.flex-col.w-full
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
                    @click="onDelete(p)"
                  )
                  t-toggle(:checked="p.enable==='YES'" @change="onToggle(p)")
                .spinner.lds-dual-ring(v-else)
          template(v-slot:default)
            .flex.justify-between
              .start.flex.flex-col.gap-y-2
                .expression.text-gray-600.overflow-ellipsis {{p.expression}}
                .description.text-gray-400.overflow-ellipsis {{p.policy_description}}
              .end.flex.flex-col.justify-end
                .object-full-name {{getFullName(p)}}

      t-button.mt-10.w-full.text-center(tagName="a" :href="`/connections/${connectionId}/policies/create`")
        | Create New Policy
</template>

<script>
/* eslint-disable camelcase */

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
    ...mapGetters('policy', ['policies']),
    isPoliciesEmpty () {
      return this.policies.length === 0
    }
  },
  methods: {
    ...mapActions('policy', ['getPolicies', 'deletePolicy', 'disablePolicy', 'enablePolicy']),
    getFullName (p) {
      const names = []
      p.object_owner && names.push(p.object_owner)
      p.object_name && names.push(p.object_name)
      return names.join('.')
    },
    onToggle (p) {
      const { object_owner } = p
      const policy = { ...p, object_schema: object_owner }
      if (p.enable === 'YES') { this.onDisable(policy) } else { this.onEnable(policy) }
    },
    onDisable (p) {
      this.isSpinner = true
      this.disablePolicy(p).then(() => {
        this.$toasted.success('Success. Disabled policy')
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Error. Failed to disable policy')
      }).finally(() => {
        this.isSpinner = false
      })
    },
    onEnable (p) {
      this.isSpinner = true
      this.enablePolicy(p).then(() => {
        this.$toasted.success('Success. Enabled policy')
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Error. Failed to enable policy')
      }).finally(() => {
        this.isSpinner = false
      })
    },
    onDelete (p) {
      this.isSpinner = true
      const { object_owner } = p
      this.deletePolicy({ ...p, object_schema: object_owner }).then(() => {
        this.$toasted.success('Success. Deleted policy')
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Error. Failed to delete policy')
      }).finally(() => { this.isSpinner = false })
    },
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
