<template lang="pug">
.echarts.bg-white.w-full.rounded-md
  .content.w-full.h-64(style="width: 100%")
</template>

<script>
import _ from 'lodash'
import { mapActions } from 'vuex'
import * as echarts from 'echarts'

export default {
  props: ['planInstanceId', 'planId'],
  data () {
    return {
      chart: undefined,
      isSpinner: true,
      discoveries: []
    }
  },
  methods: {
    ...mapActions('discovery', ['getDiscoveriesGroupByRule', 'getDiscoveriesGroupBySchema']),
    initChart () {
      this.chart = echarts.init(this.$el.querySelector('.content'), null, {
        renderer: 'svg'
      })
    },
    reloadChart () {
      const option = {
        title: {
          left: 10,
          top: 10,
          textStyle: {
            color: '#9CA3AF',
            fontWeight: 300,
            fontFamily: "'Roboto', sans-serif"
          },
          text: 'Discoveries by Schema'
        },
        tooltip: {
          axisPointer: {
            type: 'shadow'
          }
        },
        legend: {
          orient: 'vertical',
          left: 'right'
        },
        series: [{
          data: _.map(this.discoveries, d => { return { value: d.count, name: d.schema_name } }),
          type: 'pie',
          showBackground: true,
          backgroundStyle: {
            color: 'rgba(180, 180, 180, 0.2)'
          }
        }]
      }
      this.chart.setOption(option)
    },
    fetchData () {
      this.isSpinner = true
      const planId = +this.planId
      const planInstanceId = +this.planInstanceId
      return this.getDiscoveriesGroupBySchema({ planId, planInstanceId }).then(result => {
        this.discoveries = result
        this.reloadChart()
        return result
      })
    }
  },
  created () {
    this.isSpinner = true
  },
  mounted () {
    this.initChart()
    this.fetchData()
  }
}
</script>
