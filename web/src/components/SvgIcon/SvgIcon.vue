<template>
  <div v-html="require('!!html-loader!@/svg/' + name + '.svg')"></div>
</template>

<script>
export default {
  props: ['name', 'addClass'],
  mounted () {
    this.$el.querySelector('svg').setAttribute('class', this.addClass)
  }
}
</script>
