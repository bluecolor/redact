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
        path: '/settings/connections/create/oracle'
      }, {
        name: 'SQL Server',
        icon: 'sqlserver',
        path: '/settings/connections/create/mssql'
      }, {
        name: 'MySQL',
        icon: 'mysql',
        path: '',
        disabled: true
      }, {
        name: 'PostgreSQL',
        icon: 'postgresql',
        path: '',
        disabled: true
      }]
    }
  },
  methods: {
  }
}
</script>
