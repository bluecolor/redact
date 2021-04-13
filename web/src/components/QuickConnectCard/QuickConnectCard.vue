<template lang="pug">
.cursor-pointer.hover-animate.quick-connect-card(@click="onNav")
  t-card
    template(v-slot:header)
      .title.text-center.w-full
        | {{c.name}}
    template.relative(v-slot:default)
      .flex.justify-center
        svg-icon(:name="icon", addClass="fill-current text-gray-300 w-24 h-24")
      .status.las.la-circle.text-2xl.h-full(:class="{'text-green-400': c.status, 'text-red-400': c.status === false, 'text-gray-400': c.status===undefined}")
</template>

<script>
import { mapActions } from 'vuex'
import SvgIcon from '@/components/SvgIcon'

export default {
  components: { SvgIcon },
  props: { c: { type: Object, default: () => {} } },
  data () {
    return {
    }
  },
  computed: {
    icon () {
      return this.c.vendor
    }
  },
  methods: {
    ...mapActions('connection', ['testConnection']),
    ...mapActions('app', ['setConnection']),
    onNav () {
      const { id, vendor } = this.c
      const path = `/connections/${id}/${vendor}`
      this.setConnection(id)
      this.$router.push({ path })
    }
  },
  created () {
  }
}
</script>>

<style>
.quick-connect-card .status {
  position: absolute;
  bottom: 0;
  left: 0;
}
</style>
