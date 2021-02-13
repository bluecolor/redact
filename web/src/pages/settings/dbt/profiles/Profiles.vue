<template lang="pug">
.profiles-container
  .w-full
    .title.flex.w-full.justify-between.border-b.border-gray-300.py-5.items-center.pt-0.mt-0
      .left.flex.items-center
        span.text-gray-500 Profiles
      .right.space-x-4
        i.inline-block.las.text-2xl.icon-btn(
          :class="{'la-magic': isFileEditor, 'la-file-alt': !isFileEditor }"
          @click="isFileEditor = !isFileEditor"
        )
        i.inline-block.las.la-save.text-2xl.icon-btn
    .body.w-full.flex.justify-center.flex-col.py-4
      profiles-file.mt-0
</template>

<script>
import ProfilesFile from './ProfilesFile'

export default {
  components: {
    ProfilesFile
  },
  data () {
    return {
      isFileEditor: true
    }
  },
  mounted () {
    console.log('sasa')
  }
}
</script>

<style lang="postcss">
.profile-page .toolbar {
  @apply border-b border-gray-200 items-center;
  padding: .4em 1em;
}
</style>
