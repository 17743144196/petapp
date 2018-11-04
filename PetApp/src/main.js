// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

import NavMain from './components/NavMain'
// 右侧文章
import ArticlePet from './components/ArticlePet'
// 下面
import Footer from './components/Footer'
import Paging from './components/Paging'

import $ from 'jquery'
// import 'bootstrap/dist/css/bootstrap.min.css'
// import 'bootstrap/dist/js/bootstrap.min'

Vue.config.productionTip = false

//注册全局组件
Vue.component('nav-main',NavMain);
Vue.component('article-pet',ArticlePet);
Vue.component('footer-pet',Footer);
Vue.component('paging',Paging);



/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
