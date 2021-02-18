<template lang="pug">
.flex.justify-center.flex-col(class="w-3/4")
  form(autocomplete="off" @submit="onCreate")
    .form-item
      label Name
      input(v-model="payload.name" name='policy_expression_name' required autofocus)
    .form-item
      label Expression
      v-select(
        v-model="payload.policy_expression_name"
        :data="expressions",
        valueProp='policy_expression_name',
        displayProp="policy_expression_name"
        required
      )
    .form-item
      label Function Type
      v-select(
        v-model.number="payload.function_type"
        :data="functionTypes",
        valueProp='function_type',
        displayProp="name"
        required
      )
    .form-item
      label Function Parameters
      v-select(
        v-model="payload.function_parameters"
        :data="functionParameters",
        valueProp='function_parameters',
        displayProp="function_parameters"
      )
    .form-item
      label Description
      textarea(v-model="payload.description" name='description')
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
import VSelect from '@/components/Select'

export default {
  props: ['connectionId'],
  components: {
    SimpleSpinner, VSelect
  },
  data () {
    return {
      isSpinner: false,
      isValid: false,
      payload: {
        name: '',
        policy_expression_name: '',
        function_type: 1,
        function_parameters: '',
        description: ''
      }
    }
  },
  computed: {
    ...mapGetters('redact', ['expressions', 'functionTypes', 'functionParameters'])
  },
  methods: {
    ...mapActions('category', ['createCategory']),
    ...mapActions('redact', ['getExpressions', 'getFunctionTypes', 'getFunctionParameters']),
    onCreate (e) {
      e.preventDefault()
      this.isSpinner = true
      const { connectionId } = this
      this.createCategory({ connectionId, ...this.payload }).then(() => {
        this.$toast.success('Success Category created')
      }).finally(() => {
        this.isSpinner = false
      })
    },
    onCancel () { window.history.back() }
  },
  mounted () {
    this.isSpinner = true
    const promises = []
    if (_.isEmpty(this.expressions)) {
      promises.push(this.getExpressions(this.connectionId))
    }
    if (_.isEmpty(this.functionTypes)) {
      promises.push(this.getFunctionTypes())
    }
    if (_.isEmpty(this.functionParameters)) {
      promises.push(this.getFunctionParameters())
    }
    Promise.all(promises).finally(() => { this.isSpinner = false })
  }
}
</script>

<style lang="postcss">
</style>
