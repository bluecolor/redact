<template lang="pug">
.monaco-editor
</template>

<script>
import * as monaco from 'monaco-editor/esm/vs/editor/editor.api'

export default {
  data () {
    return {}
  },
  mounted () {
    const el = this.$el
    this.editor = monaco.editor.create(el, {
      value: '',
      language: 'sql',
      automaticLayout: true
    })
  }
}
</script>

<style>
.monaco-editor {
  height: 100vh;
  overflow: hidden;
}
</style>
