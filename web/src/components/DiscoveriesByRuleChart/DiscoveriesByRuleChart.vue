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
    ...mapActions('discovery', ['getDiscoveriesGroupByRule']),
    initChart () {
      this.chart = echarts.init(this.$el.querySelector('.content'), null, {
        renderer: 'svg'
      })
    },
    reloadChart () {
      const labelOption = {
        show: true,
        position: 'insideLeft',
        distance: 15,
        formatter: '{b} - {value|{c}}',
        fontSize: 14,
        color: '#fff',
        rich: {
          value: {
            alignSelf: '',
            textAlign: 'right',
            fontSize: 14,
            fontWeight: 600,
            color: '#fff'
          }
        }
      }

      const option = {
        title: {
          left: 10,
          top: 10,
          textStyle: {
            color: '#9CA3AF',
            fontWeight: 300,
            fontFamily: "'Roboto', sans-serif"
          },
          text: 'Discoveries by Rule'
        },
        grid: {
          left: '3%',
          right: '3%',
          bottom: '3%',
          containLabel: true
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        xAxis: {
          type: 'value',
          interval: 1,
          axisTick: {
            interval: 1
          }
        },
        yAxis: {
          type: 'category',
          axisLabel: {
            inside: true
          },
          data: _.map(this.discoveries, d => d.rule.name)
        },
        series: [{
          label: labelOption,
          color: '#60A5FA',
          data: _.map(this.discoveries, d => d.count),
          type: 'bar',
          showBackground: true
          // backgroundStyle: {
          //   color: 'rgba(180, 180, 180, 0.2)'
          // }
        }]
      }
      this.chart.setOption(option)
    },
    fetchData () {
      this.isSpinner = true
      const planId = +this.planId
      const planInstanceId = +this.planInstanceId
      return this.getDiscoveriesGroupByRule({ planId, planInstanceId }).then(result => {
        this.discoveries = result
        this.reloadChart()
        return result
      }).finally(() => { this.isSpinner = false })
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
