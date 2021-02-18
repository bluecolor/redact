<template lang="pug">
select.form-select.mt-1.block.w-full.input(@change="onChange($event)" :value="modelValue")
  option.p-3(v-for="i in data"  :value="i[valueProp]") {{i[displayProp]}}

</template>

<script>
export default {
  name: 'VSelect',
  props: {
    data: { type: Array, default: () => [] },
    displayProp: { type: String },
    valueProp: { type: String },
    modelValue: { type: [Number, String], default: undefined }
  },
  components: {},
  emits: ['update:modelValue'],
  data () {
    return {
      isOpen: false
    }
  },
  watch: {
    value () {
      if (this.value !== this.model) {
        this.model = this.value
      }
    }
  },
  methods: {
    onChange (e) {
      this.$emit('update:modelValue', e.currentTarget.value)
    }
  },
  mounted () {
  }
}
</script>

<style scoped lang="postcss">
</style>
