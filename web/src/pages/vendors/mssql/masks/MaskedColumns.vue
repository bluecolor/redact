<template lang="pug">
.policies-container
  .loader.text-gray-600(v-if="isLoading")
  .bg-white.empty.w-full(v-if="!isLoading && isMaskedColumnsEmpty")
    .text-xl.text-gray-400.text-center There is nothing here!
    .flex.justify-center.mt-10.w-full()
      svg-icon(name="box", addClass="fill-current text-gray-300 w-24 h-24")
    .flex.justify-center.mt-10
      t-button.mt-10.w-full.text-center(tagName="a" :href="`/connections/${connectionId}/mssql/masks/columns/create`")
        | Add New
  .flex.justify-center.w-full(v-if="!isLoading && !isMaskedColumnsEmpty")
    .body.w-full.flex.items-center.flex-col
      .gap-y-3.flex.flex-col.w-full
      t-table.d-table(:headers="headers" :data="items" style="overflow:unset;")
        template(slot='row' slot-scope='props')
          tr(:class="[props.trClass, 'hover:bg-gray-50']")
            td.overflow-ellipsis(:class='props.tdClass')
              | {{ props.row.schema_name }}
            td.overflow-ellipsis(:class='props.tdClass')
              | {{ props.row.table_name }}
            td.overflow-ellipsis(:class='props.tdClass')
              | {{ props.row.column_name }}
            td.overflow-ellipsis(:class='props.tdClass')
              | {{ props.row.masking_function }}
            td.flex.gap-x-3.justify-end(:class='props.tdClass')
              t-icon-dropdown(
                :classes="{icon: 'las la-ellipsis-v'}"
                :emitValue="true" :items="menu", valueProp="value"
                @select="(menu) =>  onMenuItemClick(menu, props.row)"
              )
      t-button.mt-10.w-full.text-center(tagName="a" :href="`/connections/${connectionId}/mssql/masks/columns/create`")
        | Add New
</template>

<script>
/* eslint-disable camelcase */

import qs from 'qs'
import _ from 'lodash'
import SvgIcon from '@/components/SvgIcon'
import { loaderMixin } from '@/mixins'
import { mapActions } from 'vuex'
import TIconDropdown from '@/components/TIconDropdown'

export default {
  props: ['connectionId'],
  mixins: [loaderMixin],
  components: {
    SvgIcon, TIconDropdown
  },
  data () {
    return {
      items: [],
      menu: [
        { name: 'Remove mask', value: 'drop-mask', icon: 'las la-trash-alt' },
        { name: 'Edit', value: 'edit', icon: 'las la-pen' },
        { name: 'Grant unmask', value: 'grant-unmask', icon: 'las la-user-secret text-red-400' },
        { name: 'Revoke unmask', value: 'revoke-unmask', icon: 'las la-user text-blue-400' }
      ],
      headers: ['Schema', 'Table', 'Column', 'Function']

    }
  },
  computed: {
    isMaskedColumnsEmpty () {
      return this.items.length === 0
    }
  },
  methods: {
    ...mapActions('mask', ['getMaskedColumns', 'dropMask']),
    onDropMask ({ schema_name, table_name, column_name }) {
      this.startSpinner()
      this.dropMask({ schema_name, table_name, column_name }).then(() => {
        const i = _.findIndex(this.items, { schema_name, table_name, column_name })
        if (i > -1) {
          this.items.splice(i, 1)
        }
        this.$toasted.success('Success. Removed mask from column')
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Error. Failed to remove mask')
      }).finally(this.stopSpinner)
    },
    onEditMask ({ column_name, table_name, schema_name }) {
      const params = { column_name, table_name, schema_name }
      const path = `/connections/${this.connectionId}/mssql/masks/columns/edit?${qs.stringify(params)}`
      this.$router.push({ path })
    },
    onGrantUnnask ({ column_name, table_name, schema_name }) {
      const params = { column_name, table_name, schema_name }
      const path = `/connections/${this.connectionId}/mssql/masks/columns/grant?${qs.stringify(params)}`
      this.$router.push({ path })
    },
    onRevokeUnnask ({ column_name, table_name, schema_name }) {
      const params = { column_name, table_name, schema_name }
      const path = `/connections/${this.connectionId}/mssql/masks/columns/revoke?${qs.stringify(params)}`
      this.$router.push({ path })
    },
    onMenuItemClick (menu, item) {
      switch (menu) {
        case 'drop-mask': this.onDropMask(item); break
        case 'edit': this.onEditMask(item); break
        case 'grant-unmask': this.onGrantUnnask(item); break
        case 'revoke-unmask': this.onRevokeUnnask(item); break
      }
    }
  },
  created () {
    this.startLoader()
    this.getMaskedColumns().then(result => {
      this.items = result
    }).finally(this.stopLoader)
  }
}
</script>

<style lang="postcss" scoped>
.row-action-btn {
  @apply text-gray-400;
}
.d-table, .d-table th, .d-table tr, .d-table td {
  border: 0 !important
}
</style>
