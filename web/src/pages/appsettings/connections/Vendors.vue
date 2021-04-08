<template lang="pug">
.grid.grid-cols-3.gap-8.w-full
  vendor-card.w-full(v-for="i in items" :v="i" class="w-1/3")
</template>

<script>
import VendorCard from '@/components/VendorCard'

export default {
  name: 'Vendors',
  components: {
    VendorCard
  },
  data () {
    return {
      items: [{
        name: 'Oracle',
        icon: 'oracle',
        path: ''
      }, {
        name: 'SQL Server',
        icon: 'sqlserver',
        path: ''
      }, {
        name: 'MySQL',
        icon: 'mysql',
        path: ''
      }, {
        name: 'PostgreSQL',
        icon: 'postgresql',
        path: ''
      }]
    }
  },
  methods: {
  }
}
</script>
