const MonacoWebpackPlugin = require('monaco-editor-webpack-plugin')

// vue.config.js
module.exports = {
  lintOnSave: false,
  chainWebpack: (config) => {
    // Pug Loader
    config.module
      .rule('pug')
      .test(/\.pug$/)
      .use('pug-plain-loader')
      .loader('pug-plain-loader')
      .end()

    config.plugin('monaco-editor').use(MonacoWebpackPlugin, [{
      // Languages are loaded on demand at runtime
      languages: ['json', 'javascript', 'html', 'xml', 'sql']
    }])
  }
}
