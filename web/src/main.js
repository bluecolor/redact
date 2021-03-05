import Vue from 'vue'
import App from './App.vue'

import './assets/css/index.css'
import './assets/css/app.scss'

import router from './router'
import store from './store'
import VueTailwind from 'vue-tailwind'
import 'line-awesome/dist/line-awesome/css/line-awesome.min.css'
import Toast from '@/plugins/toast'

import {
  TInput,
  TButton,
  TInputGroup,
  TCard,
  TTextarea,
  TRichSelect,
  TSelect,
  TRadio,
  TTable
} from 'vue-tailwind/dist/components'
import VueTippy, { TippyComponent } from 'vue-tippy'

import 'tippy.js/themes/light.css'
import 'tippy.js/themes/light-border.css'
import 'tippy.js/themes/google.css'
import 'tippy.js/themes/translucent.css'

Vue.config.productionTip = false

const settings = {
  TInput,
  TInputGroup,
  TCard,
  TTextarea,
  TRichSelect,
  TSelect,
  TRadio,
  't-table': {
    component: TTable,
    props: {
      classes: {
        table: 'rounded-sm overflow-hidden min-w-full divide-y divide-gray-100 shadow-sm border-gray-200 border',
        thead: '',
        theadTr: '',
        theadTh: 'px-3 py-2 font-semibold text-left bg-gray-100 border-b',
        tbody: 'bg-white divide-y divide-gray-100',
        tr: '',
        td: 'px-3 py-2 whitespace-no-wrap',
        tfoot: '',
        tfootTr: '',
        tfootTd: ''
      },
      variants: {
        thin: {
          td: 'p-1 whitespace-no-wrap text-sm',
          theadTh: 'p-1 font-semibold text-left bg-gray-100 border-b text-sm'
        }
      }
    }
  },
  't-button': {
    component: TButton,
    props: {
      fixedClasses: 'block px-4 py-2 transition duration-100 ease-in-out focus:border-blue-500 focus:ring-2 focus:ring-blue-500 focus:outline-none focus:ring-opacity-50 disabled:opacity-50 disabled:cursor-not-allowed',
      classes: 'text-white bg-blue-500 border border-transparent shadow-sm rounded hover:bg-blue-600',
      variants: {
        secondary: 'rounded text-gray-800 bg-white border border-gray-300 shadow-sm hover:text-gray-600',
        error: 'text-white bg-red-500 border border-transparent rounded shadow-sm hover:bg-red-600',
        success: 'text-white bg-green-500 border border-transparent rounded shadow-sm hover:bg-green-600',
        link: 'text-blue-500 underline hover:text-blue-600'
      }
    }
  }
}

Vue.use(VueTailwind, settings)
Vue.use(Toast, {
  theme: 'toasted-primary',
  position: 'bottom-right',
  duration: 5000
})

Vue.use(VueTippy, {
  directive: 'tippy', // => v-tippy
  flipDuration: 0,
  popperOptions: {
    // modifiers: {
    //   preventOverflow: {
    //     enabled: false
    //   }
    // }
  }
})

Vue.component('tippy', TippyComponent)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
