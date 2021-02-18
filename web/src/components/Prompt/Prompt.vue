<template lang="pug">
teleport(to="body")
  .fixed.z-10.inset-0.overflow-y-auto.z-50
    .flex.items-end.justify-center.min-h-screen.pt-4.px-4.pb-20.text-center(class='sm:block sm:p-0')
      .fixed.inset-0.transition-opacity(aria-hidden='true')
        .absolute.inset-0.bg-gray-500.opacity-25.z-10
      // This element is to trick the browser into centering the modal contents.
      span.hidden(class='sm:inline-block sm:align-middle sm:h-screen' aria-hidden='true')
      .z-50.inline-block.align-bottom.bg-white.rounded-lg.text-left.overflow-hidden.shadow-xl.transform.transition-all(class='sm:my-8 sm:align-middle sm:max-w-lg sm:w-full' role='dialog' aria-modal='true' aria-labelledby='modal-headline')
        .bg-white.px-4.pt-5.pb-4(class='sm:p-6 sm:pb-4')
          div(class='sm:flex sm:items-start')
            .mx-auto.flex-shrink-0.flex.items-center.justify-center.h-12.w-12.rounded-full.bg-red-100(class='sm:mx-0 sm:h-10 sm:w-10')
              // Heroicon name: outline/exclamation
              svg.h-6.w-6.text-red-600(xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke='currentColor' aria-hidden='true')
                path(stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z')
            .mt-3.text-center(class='sm:mt-0 sm:ml-4 sm:text-left')
              h3#modal-headline.text-lg.leading-6.font-medium.text-gray-900
                | {{prompt.title}}
              .mt-2
                p.text-sm.text-gray-500
                  | {{prompt.description}}
        .bg-gray-50.px-4.py-3(class='sm:px-6 sm:flex sm:flex-row-reverse')
          button.w-full.inline-flex.justify-center.rounded-md.border.border-transparent.shadow-sm.px-4.py-2.bg-red-600.text-base.font-medium.text-white(
            @click="onOk"
            type='button' class='hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 sm:ml-3 sm:w-auto sm:text-sm')
            | {{prompt.ok}}
          button.mt-3.w-full.inline-flex.justify-center.rounded-md.border.border-gray-300.shadow-sm.px-4.py-2.bg-white.text-base.font-medium.text-gray-700(
            @click="onCancel"
            type='button' class='hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm')
            | {{prompt.cancel}}

</template>

<script>
import _ from 'lodash'

export default {
  props: {
    params: { type: Object, default: () => {} }
  },
  emits: ['hide'],
  data () {
    return {
      prompt: _.extend({
        title: 'Are you sure?',
        description: 'Are you sure you want to do this.',
        cancel: 'Cancel',
        ok: 'Ok'
      }, this.params)
    }
  },
  methods: {
    onOk () {
      if (this.params.cb?.ok) {
        Promise.resolve(this.params.cb.ok()).finally(() => {
          this.$emit('hide')
        })
      }
    },
    onCancel () {
      if (this.params.cb?.cancel) {
        Promise.resolve(this.params.cb.cancel()).finally(() => {
          this.$emit('hide')
        })
      } else {
        this.$emit('hide')
      }
    }
  }
}
</script>
