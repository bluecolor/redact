<template lang="pug">
t-card.card
  template(v-slot:header)
    .flex.justify-between
      .title.flex.gap-x-2.items-center
        .text-2xl.text-gray-400(:class="n.icon")
        .text
          | {{n.type}}
      .actions.flex.justify-end
        .btns.gap-x-3.flex(v-if="!isSpinner")
        .spinner.lds-dual-ring(v-else)
  template(v-slot:default)
    |{{n.text}}
</template>

<script>

export default {
  props: { n: { type: Object, default: () => {} } },
  data () {
    return {
      isSpinner: false
    }
  },
  methods: {
  }
}
</script>>
