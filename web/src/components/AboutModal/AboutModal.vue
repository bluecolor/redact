<template lang="pug">
t-modal(header='About - Reddact' v-model="v" @closed="onClose" hideCloseButton)
  .flex.flex-col.gap-y-3
    t-alert.alert(v-if="hasNewVersion" variant="warning" show :dismissible="false")
      a(href="https://pypi.org/project/reduck/") New version exists {{pypi.info.version}}. Click here.
    .body.flex.flex-col.justify-center
      p
        |Redact, sensitive data masking and discovery tool.
      p
        | Version: <span class="font-medium">{{version}}</span>
  template(v-slot:footer='')
    .flex.justify-between.align-center
      svg-icon.home(name="marker", addClass="fill-current w-8 h-8 text-gray-500 hover:text-gray-700")
      .flex.justify-end
        .spinner.lds-dual-ring(v-if="isSpinner")
        t-button(v-else type='button' @click="onClose")
          | Ok
</template>

<script>
import axios from 'axios'
import { mapActions } from 'vuex'
import SvgIcon from '@/components/SvgIcon'

export default {
  name: 'AboutModal',
  props: { visible: { type: Boolean, default: false } },
  components: {
    SvgIcon
  },
  data () {
    return {
      v: this.visible,
      version: undefined,
      isSpinner: false,
      pypi: {}
    }
  },
  computed: {
    newVersion () {
      return this.pypi?.info?.version
    },
    hasNewVersion () {
      return (this.newVersion && this.newVersion > this.version)
    }
  },
  methods: {
    ...mapActions('app', ['getVersion']),
    onClose () {
      this.$emit('closed')
    },
    getPackageInfo () {
      return new Promise((resolve) => {
        return axios.get('https://pypi.org/pypi/reduck/json').then(response => {
          this.version = response.data
          return resolve(response.data)
        }).catch(error => {
          console.log(error)
          resolve({})
        })
      })
    }
  },
  created () {
    this.isSpinner = true
    Promise.all([this.getVersion(), this.getPackageInfo()]).then(([{ version }, p]) => {
      this.pypi = p
      this.version = version
    }).catch(e => {
      console.log(e)
    }).finally(() => {
      this.isSpinner = false
    })
  }
}
</script>
