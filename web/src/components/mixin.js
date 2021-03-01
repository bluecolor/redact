import _ from 'lodash'

export default {
  props: {
    classes: { type: Object, default: () => {} }
  },
  data () {
    return {
      defaultClasses: {}
    }
  },
  computed: {
    cls () {
      return _.extend(this.defaultClasses, this.classes)
    }
  }
}
