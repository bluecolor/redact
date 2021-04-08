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
  TTable,
  TTag,
  TDatepicker,
  TToggle,
  TDialog,
  TCheckboxGroup,
  TAlert,
  TModal
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
  TDatepicker,
  TToggle,
  TDialog,
  TCheckboxGroup,
  TModal,
  't-alert': {
    component: TAlert,
    props: {
      fixedClasses: {
        wrapper: 'relative flex items-center p-4 border-l-4  rounded shadow-sm',
        body: 'flex-grow',
        close: 'absolute relative flex items-center justify-center ml-4 flex-shrink-0 w-6 h-6 transition duration-100 ease-in-out rounded  focus:ring-2 focus:ring-blue-500 focus:outline-none focus:ring-opacity-50',
        closeIcon: 'fill-current h-4 w-4'
      },
      classes: {
        wrapper: 'bg-blue-50 border-blue-500',
        body: 'text-blue-700',
        close: 'text-blue-500 hover:bg-blue-200'
      },
      variants: {
        danger: {
          wrapper: 'bg-red-50 border-red-500',
          body: 'text-red-700',
          close: 'text-red-500 hover:bg-red-200'
        },
        success: {
          wrapper: 'bg-green-50 border-green-500',
          body: 'text-green-700',
          close: 'text-green-500 hover:bg-green-200'
        },
        warning: {
          wrapper: 'bg-yellow-50 border-yellow-500',
          body: 'text-yellow-700',
          close: 'text-yellow-500 hover:bg-yellow-200'
        },
        info: {
          wrapper: 'bg-blue-50 border-blue-500',
          body: 'text-blue-700',
          close: 'text-blue-500 hover:bg-blue-200'
        }
      }
    }
  },
  't-tag': {
    component: TTag,
    props: {
      fixedClasses: '',
      classes: '',
      variants: {
        title: 'text-2xl leading-8 font-extrabold text-gray-900 tracking-tight',
        subtitle: 'text-lg leading-6 font-medium text-gray-900',
        error: 'text-red-500',
        badge: 'inline-flex items-center px-3 rounded-full text-xs font-medium leading-4 bg-gray-100 text-gray-800',
        avatar: 'inline-flex items-center justify-center h-10 w-10 rounded-full bg-gray-500 overflow-hidden leading-none text-center'
      }
    }
  },
  't-table': {
    component: TTable,
    props: {
      classes: {
        table: 'rounded-sm overflow-hidden min-w-full divide-y divide-gray-100 shadow-sm border-gray-200 border',
        thead: '',
        theadTr: '',
        theadTh: 'px-3 py-2 font-medium text-left bg-gray-100 border-b',
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
