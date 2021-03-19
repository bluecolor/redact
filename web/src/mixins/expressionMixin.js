import _ from 'lodash'

export default {
  data () {
    return {
      isExpressionItems: false
    }
  },
  computed: {
    canTabulate () {
      const e = this.payload.expression?.toLowerCase()
      return e.includes(' in ')
    },
    expressionItems () {
      const e = this.payload.expression
      const tokens = e.split('(')
      if (tokens.length === 0) {
        return []
      }
      const items = tokens[tokens.length - 1].replace(')', '')
      return _.chain(items.split(',')).map(i => i.replaceAll("'", '').trim()).value()
    },
    expressionPrefix () {
      const e = this.payload.expression
      const tokens = e.split('(')
      if (tokens.length === 0) {
        return []
      }
      tokens.pop()
      return tokens.join('(')
    }
  },
  methods: {
    onTabulate () {
      this.isExpressionItems = true
    },
    onAddItemToExpression (item) {
      const items = this.expressionItems
      items.push(item)
      const expression = [this.expressionPrefix]
      const tail = _.map(items, i => `'${i}'`).join(',')
      expression.push(`(${tail})`)
      this.payload.expression = expression.join(' ')
    },
    onRemoveItemFromExpression (item) {
      const items = this.expressionItems
      const i = items.indexOf(item)
      if (i > -1) {
        items.splice(i, 1)
      }
      const expression = [this.expressionPrefix]
      const tail = _.map(items, i => `'${i}'`).join(',')
      expression.push(`(${tail})`)
      this.payload.expression = expression.join(' ')
    }
  }
}
