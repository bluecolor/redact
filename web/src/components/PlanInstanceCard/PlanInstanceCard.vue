<template lang="pug">
t-card.card.plan-instance-card
  template(v-slot:header)
    .flex.justify-between
      .title.flex.gap-x-2.items-center
        .las.la-shipping-fast.text-2xl.text-gray-400
        .text
          | {{p.plan.name}}
      .actions.flex.justify-end
        .btns.gap-x-3.flex(v-if="!isSpinner")
          .icon-btn.las.la-sync-alt(@click="onReload")
          router-link.icon-btn.las.la-chart-bar(
            content="Dashboard" v-tippy='{ placement : "top" }'
            :to="`/connections/${p.plan.connection_id}/${vendor}/discovery/plans/${p.plan.id}/instances/${p.id}/dashboard`"
          )
          .icon-btn.las.la-stop-circle(
            v-if="p.status==='running'"
            content="Stop" v-tippy='{ placement : "top" }'
            @click="onStop(p)")
          .icon-btn.las.la-trash-alt.danger(
            v-if="p.status!=='running'"
            content="Delete" v-tippy='{ placement : "top" }'
            @click="onDelete(p)"
          )
        .spinner.lds-dual-ring(v-else)
  template(v-slot:default)
    .body.flex.flex-col.gap-y-2
      .flex.justify-between
        .flex.flex-col.gap-y-2
          .start-date.text-gray-400
            | started {{fromNow(p.created_on)}}
          .description.flex.flex-col.gap-y-2
            .description {{p.description}}
          .progress
            | {{progress}}
        .end.flex.flex-col.justify-between.gap-y-3
          .status.flex.justify-end
            t-tag.p-1(
              :class="{ 'bg-red-200': p.status==='error',\
                  'bg-blue-200': p.status==='running',\
                  'bg-green-200': p.status==='success'}"
              tag-name="span" variant="badge"
            ) {{p.status}}
          .flex.justify-end
            router-link(
              class="hover:underline"
              :to="`/connections/${p.plan.connection.id}/${vendor}/discovery/plans/${p.plan.id}/instances/${p.id}/discoveries-by-rule`")
              | {{p.discoveries.length}} discoveries
      k-progress.progressbar(v-if="showProgressbar" :percent="progressbar.percent"
        color="#60A5FA"
      )
</template>

<script>
/* eslint-disable camelcase */
import { mapActions, mapGetters } from 'vuex'
import { dateMixin } from '@/mixins'
import KProgress from 'k-progress'
import TIconDropdown from '@/components/TIconDropdown'

export default {
  mixins: [dateMixin],
  props: { p: { type: Object, default: () => {} } },
  components: { KProgress, TIconDropdown },
  data () {
    return {
      isSpinner: false,
      ws: undefined,
      isDestroy: false,
      menu: [
        { name: 'Discoveries by schema', value: 'by-schema', icon: 'las la-map-marker text-green-400' },
        { name: 'Discoveries by rule', value: 'by-rule', icon: 'las la-map-marker text-blue-400' },
        {
          name: 'Dashboard',
          value: 'dashboard',
          icon: 'las la-chart-bar text-yellow-400',
          path: `/connections/${this.p.plan.connection_id}/discovery/plans/${this.p.plan.id}/instances/${this.p.id}/dashboard`
        }
      ],
      progressbar: {
        percent: 0,
        clear: function () {
          this.percent = 0
        }
      },
      searchResult: {
        hit: false,
        table: {},
        clear: function () {
          this.hit = false
          this.table = {}
        }
      }
    }
  },
  computed: {
    ...mapGetters('app', ['connection']),
    vendor () {
      return this.connection?.vendor
    },
    progress () {
      if (this.searchResult?.table?.table_name) {
        return `${this.searchResult?.table?.schema_name}.${this.searchResult.table.table_name}`
      }
      return ''
    },
    showProgressbar () {
      return this.p.status === 'running'
    }
  },
  methods: {
    ...mapActions('planInstance', ['deletePlanInstance', 'stopPlanInstance', 'getPlanInstance']),
    onMenuItem ({ value, path }) {
      if (path) {
        this.$router.push({ path })
      }
    },
    onDelete (p) {
      this.isDestroy = true
      this.isSpinner = true
      this.deletePlanInstance({ id: p.id, planId: p.plan.id }).then(result => {
        this.ws.close()
        this.$toasted.success('Success. Deleted plan run')
        this.$emit('delete', p)
      }).catch(error => {
        this.isDestroy = false
        console.log(error)
        this.$toasted.error('Error. Failed to delete plan run')
      }).finally(() => {
        this.isSpinner = false
      })
    },
    onStop (p) {
      this.isSpinner = true
      this.stopPlanInstance({ id: p.id, planId: p.plan.id }).then(result => {
        this.$toasted.success('Success. Stopped plan')
        this.$emit('stop', result)
      }).catch(error => {
        console.log(error)
        this.$toasted.error('Failed to stop plan')
      }).finally(() => {
        this.isSpinner = false
      })
    },
    onReload () {
      const { id } = this.p
      const planId = this.p.plan.id
      this.isSpinner = true
      this.getPlanInstance({ planId, id }).then(result => {
        this.$emit('reload', result)
      }).finally(() => {
        this.isSpinner = false
      })
    }
  },
  created () {
    const plan_instance_id = this.p.id
    const plan_id = this.p.plan.id
    const conn_id = this.p.plan.connection_id
    const channel = `ws/connections/${conn_id}/discovery/plans/${plan_id}/instances/${plan_instance_id}`
    this.ws = new WebSocket(`ws://localhost:8000/api/v1/${channel}`)
    const sync = () => {
      return this.getPlanInstance({ planId: plan_id, id: plan_instance_id }).then(result => {
        this.$emit('reload', result)
      })
    }
    this.ws.onmessage = (message) => {
      const { data } = message
      try {
        const { done, hit, table, total, progress } = JSON.parse(data)
        this.progressbar.percent = Math.min(100, parseInt((progress * 100 / total).toFixed(2)))
        if (done || this.progressbar.percent >= 100) {
          sync()
          this.searchResult.clear()
        } else {
          this.searchResult = { ...this.searchResult, hit, table }
          if (hit) {
            sync()
          }
        }
      } catch (e) {
        console.log(e)
      }
    }
    this.ws.onclose = () => {
      this.searchResult.clear()
      this.progressbar.clear()
      if (!this.isDestroy) {
        sync()
      }
    }
  },
  beforeDestroy () {
    this.isDestroy = true
    this.ws.close()
  }

}
</script>

<style>
.plan-instance-card .k-progress-outer {
  margin-right: 0 !important;
  padding-right: 0 !important;
}
</style>
