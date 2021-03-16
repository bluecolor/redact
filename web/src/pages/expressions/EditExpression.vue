<template lang="pug">
.flex.justify-center.flex-col
  t-card
    template(v-slot:default)
      form(autocomplete="off" @submit="onSubmit")
        .form-item
          t-input-group(label='Name', required)
            t-input(disabled v-model="payload.policy_expression_name" required autofocus)
        .form-item
          t-input-group(label='Expression', required)
            t-textarea(v-model="payload.expression" required)
        .form-item
          t-input-group(label='Description', required)
            t-textarea(v-model="payload.policy_expression_description")
        .form-item.mt-5
          .flex.justify-between.items-center
            simple-spinner(v-if="isSpinner")
            .flex.gap-x-3(v-else class="w-1/2")
              t-button(type="submit" value="submit" text="Save")
            .end
              t-button(@click="onCancel" type="button" text="Close" variant="error")
</template>

<script>

import _ from 'lodash'
import { mapActions, mapGetters } from 'vuex'
import SimpleSpinner from '@/components/loaders'

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
    ...mapGetters('expression', ['expressions'])
  },
  methods: {
    ...mapActions('expression', ['updateExpression', 'getExpression']),
    onSubmit (e) {
      e.preventDefault()
      this.isSpinner = true
      this.updateExpression(this.payload).then(() => {
        this.$toast.success('Success Expression updated')
      }).finally(() => {
        this.isSpinner = false
      })
    },
    onCancel () {
      window.history.back()
    }
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
