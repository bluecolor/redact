<template lang="pug">
.flex.flex-col.pb-5(class="w-3/4")
  form.flex.flex-col(autocomplete="off" @submit="onAddColumn")
    .form-item
      t-input-group(label='Policy Name')
        t-input(v-model="payload.policy_name" disabled)
    .form-item
      t-input-group(label='Object Schema')
        t-input(v-model="payload.object_schema" disabled)
    .form-item
      t-input-group(label='Object Name')
        t-input(v-model="payload.object_name" disabled)
    .form-item
      t-input-group(label='Column Name')
        t-input(v-model="payload.column_name" disabled)
    .form-item
      t-input-group(label='Expression')
        t-textarea(v-model="payload.expression" required autofocus)
    .form-item.mt-5
      .flex.justify-between.items-center
        t-simple-spinner(v-if="isSpinner")
        .flex.gap-x-3(v-else class="w-1/2")
          t-button(type="submit" value="submit" text="Save")
        .end
          t-button(@click="onBack" text="Back" variant="secondary")
</template>

<script>
/* eslint-disable camelcase */

import { mapActions } from 'vuex'
import TSimpleSpinner from '@/components/loaders'
import { PolicyActions } from '@/utils'

export default {
  props: ['connectionId'],
  components: {
    TSimpleSpinner
  },
  data () {
    return {
      isSpinner: false,
      isValid: false,
      method: 'custom',
      categoryId: undefined,
      payload: {
        object_schema: '',
        object_name: '',
        column_name: '',
        policy_name: '',
        action: PolicyActions.MODIFY_EXPRESSION,
        expression: ''
      }
    }
  },
  computed: {
  },
  methods: {
    ...mapActions('redact', ['alterPolicy']),
    onAddColumn (e) {
      e.preventDefault()
      this.isSpinner = true
      this.alterPolicy(this.payload).then(() => {
        this.$toast.success('Success. Column added')
      }).catch(error => {
        console.log(error)
        this.$toast.error('Error. Failed ad column')
      }).finally(() => {
        this.isSpinner = false
      })
    },
    onBack () { window.history.back() }
  },
  created () {
    const {
      policy_name, object_owner, object_name, column_name
    } = this.$route.query
    this.payload = {
      ...this.payload,
      policy_name,
      object_schema: object_owner,
      object_name,
      column_name
    }
  }
}
</script>

<style lang="postcss">
</style>
