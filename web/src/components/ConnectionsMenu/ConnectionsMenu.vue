<template lang="pug">
.relative.inline-block
  button.block.h-8.w-8.rounded-full.overflow-hidden(
    @click="isOpen = true",
    class="focus:outline-none"
  )
    .las.la-plug.h-full.w-full.object-cover
  .fixed.inset-0(v-if="isOpen", @click="isOpen = false", tabindex="-1")
  .menu(v-if="isOpen")
    template(v-if="!isSpinner && connections.length > 0" v-for="c in connections")
      router-link.item.flex.px-2.content-center.items-center(:to="'/connections/' + c.id")
        .text-base.block.px-4.py-2.leading-tight {{c.name}}
    SimpleSpinner(v-else)
    .empty.p-2.text-base(v-if="connections.length === 0")
      |No connections found
</template>

<script>
import _ from 'lodash'
import { mapActions, mapGetters } from 'vuex'
import { SimpleSpinner } from '@/components/loaders'

export default {
  components: {
    SimpleSpinner
  },
  data () {
    return {
      isSpinner: false,
      isOpen: false
    }
  },
  computed: {
    ...mapGetters('connection', ['connections'])
  },
  methods: {
    ...mapActions('connection', ['getConnections'])
  },
  mounted () {
    if (_.isEmpty(this.connections)) {
      this.isSpinner = true
      this.getConnections().finally(() => {
        this.isSpinner = false
      })
    }
  }
}
</script>

<style lang="scss">
</style>
