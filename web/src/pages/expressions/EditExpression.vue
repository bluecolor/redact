<template lang="pug">
.flex.justify-center.flex-col(class="w-3/4")
  form(autocomplete="off" @submit="onUpdate")
    .form-item
      label Name
      input(v-model="payload.policy_expression_name" name='policy_expression_name' required autofocus)
    .form-item
      label Expression
      textarea(v-model="payload.expression" name='expression' required)
    .form-item
      label Description
      textarea(v-model="payload.policy_expression_description" name='policy_expression_description' required)
    .form-item.mt-5
      .flex.justify-between.items-center
        simple-spinner(v-if="isSpinner")
        .flex.gap-x-3(v-else class="w-1/2")
          button.btn(tag="button" type="submit" value="submit")
            span Save
        .end
          button.btn(tag="button" @click="onCancel")
            | Close
</template>

<script>

import _ from 'lodash'
import { mapActions, mapGetters } from 'vuex'
import { SimpleSpinner } from '@/components/loaders'

export default {
  props: ['connectionId', 'policy_expression_name'],
  components: {
    SimpleSpinner
  },
  data () {
    return {
      isSpinner: false,
      isValid: false,
      payload: {
        policy_expression_name: '',
        expression: '',
        policy_expression_description: ''
      }
    }
  },
  computed: {
    ...mapGetters('redact', ['expressions'])
  },
  methods: {
    ...mapActions('redact', ['updateExpression', 'getExpression']),
    onUpdate (e) {
      e.preventDefault()
      this.isSpinner = true
      const { connectionId } = this
      this.updateExpression({ connectionId, ...this.payload }).then(() => {
        this.$toast.success('Success Expression updated')
      }).finally(() => {
        this.isSpinner = false
      })
    },
    onCancel () { window.history.back() }
  },
  mounted () {
    /* eslint-disable camelcase */
    const { policy_expression_name } = this
    if (_.isEmpty(this.expressions)) {
      this.isSpinner = true
      const { connectionId } = this
      this.getExpression({ connectionId, policy_expression_name }).then(result => {
        this.payload = { ...result }
      }).catch(() => {
        this.$toast.error('Failed to find expression')
      }).finally(() => { this.isSpinner = false })
    } else {
      const expression = _.find(this.expressions, { policy_expression_name })
      this.payload = { ...expression }
    }
  }
}
</script>

<style lang="postcss">
</style>
