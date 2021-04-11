<template lang="pug">
.policies-container
  .loader.text-gray-600(v-if="isLoading")
  .bg-white.empty.w-full(v-if="!isLoading && isMaskedColumnsEmpty")
    .text-xl.text-gray-400.text-center There is nothing here!
    .flex.justify-center.mt-10.w-full()
      svg-icon(name="box", addClass="fill-current text-gray-300 w-24 h-24")
    .flex.justify-center.mt-10
      t-button.mt-10.w-full.text-center(tagName="a" :href="`/connections/${connectionId}/mssql/masks/columns/create`")
        | Add New Column
  .flex.justify-center.w-full(v-if="!isLoading && !isMaskedColumnsEmpty")
    .body.w-full.flex.items-center.flex-col
      .gap-y-3.flex.flex-col.w-full
        //- policy-card(v-for="i in items" :="i")
      t-button.mt-10.w-full.text-center(tagName="a" :href="`/connections/${connectionId}/mssql/masks/columns/create`")
        | Add New Column
</template>

<script>
import SvgIcon from '@/components/SvgIcon'
import { loaderMixin } from '@/mixins'
import { mapActions } from 'vuex'
export default {
  props: ['connectionId'],
  mixins: [loaderMixin],
  components: {
    SvgIcon
  },
  data () {
    return {
      items: []
    }
  },
  computed: {
    isMaskedColumnsEmpty () {
      return this.items.length === 0
    }
  },
  methods: {
    ...mapActions('mask', ['getMaskedColumns'])
  },
  created () {
    this.startLoader()
    this.getMaskedColumns().then(result => {
      this.items = result
    }).finally(this.stopLoader)
  }
}
</script>
