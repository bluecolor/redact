<template lang="pug">
t-card.card.add-conn-card(:classes="classes")
  template.h-full(v-slot:default)
    .flex.justify-center.h-full
      .las.la-plus.text-8xl.h-full.text-gray-400

</template>

<script>
export default {
  data () {
    return {
      classes: {
        wrapper: 'cursor-pointer border-2 border-dashed rounded shadow-sm bg-gray-100 border-gray-400 hover:border-gray-500',
        body: 'p-3 h-full border-dashed'
      }
    }
  }

}
</script>

<style lang="postcss" scoped>
.add-conn-card .p-3 {
  @apply h-full;
}
.add-conn-card:hover .la-plus {
  @apply text-gray-500;
}
</style>
