<template lang="pug">
.page-container.page-container.flex.justify-center.py-8
  .space-y-10(class="w-2/4")
    .general
      .sub-title
        | General
      .form-section.mt-5
        .flex.items-center
          label(for='email' class="w-2/4")
            | Name
          .rounded-md.shadow-sm.w-full
            input.text(name='hostname' type='email' required autofocus)
        .flex.items-center.mt-5
          label(for='email' class="w-2/4")
            | Database type
          .rounded-md.shadow-sm.w-full
            v-select(:items="databases" v-model="database")
    postgre-settings
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
