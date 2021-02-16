<template lang="pug">
.connections-container.page-container.flex.justify-center
  .w-full
    .title.flex.w-full.justify-between.border-b.border-gray-300.py-5.items-center.pt-0
      .left.flex.items-center
        span.text-gray-500 Connections
      i.inline-block.las.la-plus.text-2xl.icon-btn
    .body.w-full.flex.justify-center.flex-col.py-10
      .text-xl.text-gray-400.text-center There is nothing here!
      .project-logo.flex.justify-center.mt-10(class="h-1/4 ")
        svg-icon(name="cloud-computing", addClass="fill-current text-gray-300 w-24 h-24")
      .flex.justify-center
        router-link.create-btn.mt-10(tag="button" class="w-1/3" to="/settings/projects/create")
          | Create New
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
.connections-container button.create-btn {
  @apply flex justify-center px-4 py-2 text-sm font-medium text-white ring-blue-300
    bg-transparent border border-gray-500 hover:border-gray-800 rounded-md transition duration-150 ease-in-out
    focus:outline-none text-gray-500 hover:text-gray-800;
}

</style>
