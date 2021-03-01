const path = require('path')
const Dotenv = require('dotenv-webpack')

const vueSrc = './src'

module.exports = {
  runtimeCompiler: true,
  css: {
    requireModuleExtension: true
  },
  configureWebpack: {
    plugins: [
      new Dotenv()
    ],
    resolve: {
      alias: {
        '@': path.join(__dirname, vueSrc)
      }
    }
  }
}
