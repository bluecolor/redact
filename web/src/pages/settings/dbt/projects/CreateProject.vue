<template lang="pug">
.create-project-page
  .w-full
    .title.flex.w-full.justify-between.border-b.border-gray-300.py-5.items-center.pt-0
      .left.flex.items-center
        span.text-gray-500 Create Project
      i.inline-block.las.la-save.text-2xl.icon-btn
  .body.w-full.flex.justify-center.flex-col.py-5.space-y-5
    .mt-0
      label.block.text-sm.text-gray-500.leading-5(for='#project-name')
        | Name
      input#project-name.text.mt-1(
        required
        placeholder="Project name"
        class='focus:outline-none focus:ring-1 focus:border-blue-300 sm:text-sm sm:leading-5'
      )
    .mt-5
      label.block.text-sm.text-gray-500.leading-5(for='#project-name')
        | Repository
      .flex.mt-1
        .flex.items-center.mr-4.mb-2
          input#radio1.hidden(type='radio' name='radio' checked @click="repositoryType='managed'")
          label.flex.items-center.cursor-pointer(for='radio1')
            span.w-4.h-4.inline-block.mr-1.rounded-full.border.border-grey
            | Managed
        .flex.items-center.mr-4.mb-2
          input#radio2.hidden(type='radio' name='radio' @click="repositoryType='gitUrl'")
          label.flex.items-center.cursor-pointer(for='radio2')
            span.w-4.h-4.inline-block.mr-1.rounded-full.border.border-grey
            | Git Url
      input.text(
        v-if="repositoryType==='gitUrl'"
        required
        placeholder="Git url"
        class='focus:outline-none focus:ring-1 focus:border-blue-300 sm:text-sm sm:leading-5'
      )
</template>

<script>
export default {
  data () {
    return {
      repositoryType: 'managed'
    }
  }

}
</script>

<style lang="postcss">

</style>
