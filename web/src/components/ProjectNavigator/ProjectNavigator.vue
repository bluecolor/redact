<template lang="pug">
.project-navigator.h-full
  .toolbar.flex.justify-between.items-center
    .project-title
      | Project Name
    .actions
      i.las.la-code-branch.text-2xl.icon-btn
  .file-tree
    tree(:value='treeData' ref="tree")
      span.boreder-0(slot-scope='{node, index, path, tree}')
        span.fitem.flex.items-center.cursor-pointer(@click='tree.toggleFold(node, path)')
          i.text-lg.text-gray-500.mr-2.las(v-if="node.children" :class="{'la-folder': node.$folded, 'la-folder-open': !node.$folded}")
          i.text-lg.text-gray-500.mr-2.las.la-file-alt(v-else)
          span.fname.text-gray-500.text-sm {{node.text}}

</template>

<script>
import 'he-tree-vue/dist/he-tree-vue.css'
import { Tree, Fold, foldAll } from 'he-tree-vue'

export default {
  components: { Tree: Tree.mixPlugins([Fold]) },
  data () {
    return {
      treeData: [
        {
          text: 'Project Name',
          children: [
            { text: 'analysis', children: [{ text: 'node 2-1' }] },
            { text: 'data', children: [{ text: 'node 2-1' }] },
            { text: 'dbt_modules', children: [{ text: 'node 2-1' }] },
            { text: 'logs', children: [{ text: 'node 2-1' }] },
            { text: 'macros', children: [{ text: 'node 2-1' }] },
            { text: 'models', children: [{ text: 'node 2-1' }] },
            { text: 'snapshots', children: [{ text: 'node 2-1' }] },
            { text: 'target', children: [{ text: 'node 2-1' }] },
            { text: 'tests', children: [{ text: 'node 2-1' }] },
            { text: '.gitignore' },
            { text: 'dbt_project.yml' },
            { text: 'README.md' }

          ]
        }
      ]
    }
  },
  mounted () {
    foldAll(this.treeData)
    const root = this.$refs.tree.getNodeByPath([0])
    this.$refs.tree.unfold(root)
  }
}
</script>

<style lang="postcss">
.project-navigator .toolbar {
  @apply border-b border-gray-200;
  padding: .4em .5em;
}
.project-navigator .file-tree .tree-node  {
  @apply border-0 mb-0;
}
.project-navigator .file-tree .tree-node-back  {
  @apply hover:bg-gray-200;
}
</style>
