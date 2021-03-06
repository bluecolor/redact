<template lang="pug">
div
  .bg-white.empty.w-full(v-if="isCategoriesEmpty")
    .text-xl.text-gray-400.text-center There is nothing here!
    .project-logo.flex.justify-center.mt-10.w-full()
      svg-icon(name="cloud-computing", addClass="fill-current text-gray-300 w-24 h-24")
    .flex.justify-center.mt-10
      t-button.mt-10.w-full.text-center(tagName="a"
        :href="`/connections/${connectionId}/categories/create`" text="Create New Category")
  .connections-container.flex.justify-center.w-full(v-else)
    .body.w-full.flex.items-center.flex-col
      .connections.gap-y-3.flex.flex-col.w-full
        t-card.card(v-for="c in categories" :header='c.name')
          template(v-slot:header)
            .flex.justify-between
              .title
                | {{c.name}}
              .actions.flex.justify-end
                .btns.gap-x-3.flex(v-if="!isSpinner")
                  router-link.icon-btn.las.la-pen(
                    :to="`categories/${c.id}`")
                  .icon-btn.las.la-trash-alt.danger(@click="onDelete(c)")
                .spinner.lds-dual-ring(v-else)
          template(v-slot:default)
            .flex.justify-between
              .start
                .description {{c.description}}
              .end.flex.flex-col.justify-between
                .function-type {{c.function_type_name}}
                .date.text-sm.text-gray-400 {{fromNow(c.updated_on)}}

      t-button.mt-10.w-full.text-center(tagName="a"
        :href="`/connections/${connectionId}/categories/create`" text="Create New Category")

</template>

<script>
import dayjs from 'dayjs'
import relativeTime from 'dayjs/plugin/relativeTime'
import { mapActions, mapGetters } from 'vuex'
import SvgIcon from '@/components/SvgIcon'

dayjs.extend(relativeTime)

export default {
  props: ['connectionId'],
  components: {
    SvgIcon
  },
  data () {
    return {
      isSpinner: false,
      title: 'Connections'
    }
  },
  computed: {
    ...mapGetters('category', ['categories', 'isCategoriesEmpty'])
  },
  methods: {
    ...mapActions('category', ['getCategories', 'deleteCategory']),
    load () {
      this.isSpinner = true
      this.getCategories(this.connectionId).finally(() => { this.isSpinner = false })
    },
    fromNow (d) {
      return dayjs(d).fromNow()
    },
    onDelete ({ id }) {
      this.isSpinner = true
      this.deleteCategory({ id }).then(() => {
        this.$toast.success('Success. Deleted category')
      }).catch(error => {
        console.log(error)
        this.$toast.error('Error. Failed to delete category')
      }).finally(() => { this.isSpinner = false })
    }
  },
  mounted () {
    this.load()
  }
}
</script>

<style lang="postcss" scoped>
.empty {
  @apply border-dashed p-3 border-2 rounded-md w-full
}
.page {
}

</style>
