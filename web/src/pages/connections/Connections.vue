<template lang="pug">
.page
  .connections-container.flex.justify-center(class="w-2/4")
    .body.w-full.flex.items-center.flex-col.py-10
      .empty
        .text-xl.text-gray-400.text-center There is nothing here!
        .project-logo.flex.justify-center.mt-10(class="h-1/4 ")
          svg-icon(name="cloud-computing", addClass="fill-current text-gray-300 w-24 h-24")
        .flex.justify-center.mt-10
          router-link.btn.create-btn.mt-10(tag="button" class="w-2/3" to="/connections/create")
            | Create New Connection
</template>

<script>
import SvgIcon from '@/components/SvgIcon'

export default {
  components: {
    SvgIcon
  },
  data () {
    return {
      title: 'Connections'
    }
  }
}
</script>

<style lang="postcss">
.connections-container .empty {
  @apply border-dashed p-3 border-2 w-2/4 rounded-md
}

</style>
