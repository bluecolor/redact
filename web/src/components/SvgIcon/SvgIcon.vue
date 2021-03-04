<template>
  <div @click="onClick" v-html="require('!!html-loader!@/svg/' + name + '.svg')"></div>
</template>

<script>
export default {
  props: ['name', 'addClass'],
  mounted () {
    this.$el.querySelector('svg').setAttribute('class', this.addClass)
  },
  methods: {
    onClick () {
      this.$emit('click')
    }
  }
}
</script>
