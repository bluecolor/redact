<template lang="pug">
.loading.flex.items-center.gap-x-3
  .lds-dual-ring.h-full.w-full.flex
  .saving {{text}}
</template>

<script>
export default {
  props: { text: { type: String, default: 'Please wait ...' } }
}
</script>
