<template lang="pug">
.loading(:class="classes.wrapper")
  .lds-dual-ring.h-full.w-full.flex
  .saving(:class="classes.text") {{text}}
</template>

<script>
export default {
  props: {
    text: { type: String, default: 'Please wait ...' },
    classes: {
      type: Object,
      default () {
        return {
          wrapper: 'flex items-center gap-x-3',
          text: ''
        }
      }
    }
  }
}
</script>

<style lang="scss">
.lds-dual-ring {
  display: inline-block;
  width: 20px;
  height: 20px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 16px;
  height: 16px;
  margin-right: 8px;
  border-radius: 50%;
  border: 2px solid #888;
  border-color: #888 transparent #888 transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
