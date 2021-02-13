import { createApp } from 'vue'
import App from './App.vue'
import '@/assets/css/tailwind.css'
import '@/assets/css/line-icons/font-css/LineIcons.css'
import 'line-awesome/dist/line-awesome/css/line-awesome.min.css'
import '@/assets/css/app.scss'
import '@/assets/css/components.scss'

import '@/boot/font-awesome.js'
import router from './router'
import store from './store'

const app = createApp(App)
app.config.productionTip = false

app.use(store).use(router).mount('#app')
