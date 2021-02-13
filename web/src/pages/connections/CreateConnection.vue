<template lang="pug">
.page
  .flex.justify-center.flex-col(class="w-1/3")
    form.mt-10(autocomplete="off")
      .form-item
        label Name
        input(name='name' required autofocus)
      .form-item
        label Hostname
        input(name='host')
      .form-item
        label Port
        input(name='port' type='number')
      .form-item
        label Service
        input(name='service')
      .form-item
        label Username
        input(name='username')
      .form-item
        label Password
        input(name='password' type="password")
      .form-item.mt-5
        button.btn(tag="button" type="submit")
          | Create

</template>

<script>

import VSelect from '@/components/Select'
import { PostgreSettings } from '@/components/settings'

export default {
  components: {
    VSelect,
    PostgreSettings
  },
  data () {
    return {
      database: 'postgresql',
      databases: [{
        id: 'snowflake',
        title: 'Snowflake'
      }, {
        id: 'postgresql',
        title: 'Postgre SQL'
      }, {
        id: 'redshift',
        title: 'Redshift'
      }, {
        id: 'bigquery',
        title: 'BigQuery'
      }, {
        id: 'mysql',
        title: 'MySQL'
      }, {
        id: 'oracle',
        title: 'Oracle'
      }, {
        id: 'sqlserver',
        title: 'SQL Server'
      }, {
        id: 'presto',
        title: 'Presto'
      }]
    }
  }
}
</script>

<style lang="postcss">
</style>
