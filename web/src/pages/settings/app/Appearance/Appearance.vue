<template lang="pug">
.appearance-container.page-container.flex.justify-center
  .w-full
    .title.flex.w-full.justify-between.border-b.border-gray-300.py-5.items-center.pt-0
      .left.flex.items-center
        span.text-gray-500 {{title}}
      i.inline-block.las.la-save.text-2xl.icon-btn
    .body.w-full.flex.justify-center.flex-col.space-y-5.py-5
      .mt-0
        label.block.text-sm.text-gray-500.leading-5(for='#project-name')
          | Theme
        .flex.mt-1
          .flex.items-center.mr-4.mb-2
            input#radio1.hidden(type='radio' name='radio' @click="repositoryType='managed'")
            label.flex.items-center.cursor-pointer(for='radio1')
              span.w-4.h-4.inline-block.mr-1.rounded-full.border.border-grey
              | Dark
          .flex.items-center.mr-4.mb-2
            input#radio2.hidden(type='radio' name='radio' checked @click="repositoryType='gitUrl'")
            label.flex.items-center.cursor-pointer(for='radio2')
              span.w-4.h-4.inline-block.mr-1.rounded-full.border.border-grey
              | Light
</template>

<script>
import SvgIcon from '@/components/SvgIcon'

export default {
  components: {
    SvgIcon
  },
  data () {
    return {
      title: 'Appearance'
    }
  }
}
</script>

<style lang="postcss">
.appearance-container button.create-btn {
  @apply flex justify-center px-4 py-2 text-sm font-medium text-white ring-blue-300
    bg-transparent border border-gray-500 hover:border-gray-800 rounded-md transition duration-150 ease-in-out
    focus:outline-none text-gray-500 hover:text-gray-800;
}

</style>
