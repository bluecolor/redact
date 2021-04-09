<template lang="pug">
.relative.flex.justify-center.flex-col
  expression-items(
    @close="isExpressionItems=false"
    v-if="isExpressionItems"
    :items="expressionItems"
    @add="onAddItemToExpression"
    @remove="onRemoveItemFromExpression"
  )
  t-card
    template(v-slot:default)
      form(autocomplete="off" @submit="onSumbit")
        .form-item
          t-input-group(label='Name', required)
            t-input(v-model="payload.policy_expression_name" required autofocus)
        .form-item.relative.expression
          t-input-group(label='Expression', required)
            t-textarea(v-model="payload.expression" required)
          .tabulate.icon-btn.las.la-table(v-if="canTabulate" @click="onTabulate")
        .form-item
          t-input-group(label='Description', required)
            t-textarea(v-model="payload.policy_expression_description")
        .form-item.mt-5
          .flex.justify-between.items-center
            simple-spinner(v-if="isSpinner")
            .flex.gap-x-3(v-else class="w-1/2")
              t-button(type="submit" value="submit" text="Save")
            .end
              t-button(@click="onCancel" text="Close" variant="error")
</template>

<script>

import { mapActions } from 'vuex'
import SimpleSpinner from '@/components/loaders'
import ExpressionItems from '@/components/oracle/ExpressionItems'
import { expressionMixin } from '@/mixins'

export default {
  mixins: [expressionMixin],
  props: ['connectionId'],
  components: {
    SimpleSpinner, ExpressionItems
  },
  data () {
    return {
      isSpinner: false,
      isValid: false,
      payload: {
        policy_expression_name: '',
        expression: "sys(*) in ('a', 'b')",
        policy_expression_description: ''
      }
    }
  },
  methods: {
    ...mapActions('expression', ['createExpression']),
    onSumbit (e) {
      e.preventDefault()
      this.isSpinner = true
      this.createExpression(this.payload).then(() => {
        this.$toasted.success('Success. Expression created')
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Error. Failed to create expression')
      }).finally(() => {
        this.isSpinner = false
      })
    },
    onCancel () { window.history.back() }
  }
}
</script>

<style lang="postcss">
.expression .tabulate {
  position: absolute;
  top: 0;
  right: 0;
  margin-top: 24px;
  @apply text-gray-300 hover:text-gray-600
}
</style>
