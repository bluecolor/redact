<template lang="pug">
.home-containe.h-full
//- split-pane(v-on:resize='onResize' :min-percent='20' :default-percent='20' split='vertical')
//-   template(slot='paneL')
//-     project-navigator
//-   template(slot='paneR')
//-     .container
//-       tabs
//-         template(v-slot:items)
//-           tab.h-full(path='model_1_name.sql' :selected='true')
//-             template(v-slot:toolbar)
//-               .left.actions.space-x-2
//-                 i.las.la-cog.text-2xl.icon-btn
//-                 i.las.la-play.text-2xl.icon-btn
//-               .right
//-                 i.las.la-save.text-2xl.icon-btn
//-             monaco-editor()
//-           tab(path='model_2_name.sql' )
//-             template(v-slot:toolbar)
//-               .left
//-               .right
//-                   i.las.la-save.text-2xl.icon-btn
//-           tab(path='model_3_name.sql')
//-             span Content 3

</template>

<script>
import {
  defineComponent
} from 'vue'
import splitPane from 'vue-splitpane'
import { Tab, Tabs } from '@/components/Tabs'
import MonacoEditor from '@/components/MonacoEditor'
import ProjectNavigator from '@/components/ProjectNavigator'

export default defineComponent({
  name: 'Home',
  components: {
    splitPane,
    Tab,
    Tabs,
    MonacoEditor,
    ProjectNavigator
  },
  data () {
    return {
      options: {}
    }
  },
  methods: {
    onResize () {},
    onChange () {}
  }
})
</script>
