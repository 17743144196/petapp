import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Index from '@/components/Index'
import Present from '@/components/Present'
import Login from '@/components/Login'
import Regist from '@/components/Regist'
import Blog from '@/components/Blog'
import AdoptPet from '@/components/AdoptPet'
import PetShow from '@/components/PetShow'
import AdoptDetail from '@/components/AdoptDetail'
import ShowDetail from '@/components/ShowDetail'
import test from "@/components/test/test"
import test1 from "@/components/test/test1"
import PersonalCenter from "@/components/personal/PersonalCenter"
import PersonalInformation from "@/components/personal/PersonalInformation"
import Credit from "@/components/personal/Credit"
import Safety from "@/components/personal/Safety"
import Adopt from "@/components/personal/Adopt"
import Foster from "@/components/personal/Foster"
import modifypassword from "@/components/personal/modifypassword"
import modifyemail from "@/components/personal/modifyemail"
import modifytel from "@/components/personal/modifytel"
import RealName from "@/components/personal/RealName"
import Template from '@/components/Template'
import BlogDetail from '@/components/BlogDetail'
import repassword from '@/components/repassword'
import Fan from '@/components/Fan'










Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index
    },
    {
      path: '/hello',
      name: 'helloworld',
      component: HelloWorld
    },
    {
      path: '/present',
      name: 'present',
      component: Present
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/regist',
      name: 'regist',
      component: Regist
    },
    {
      path: '/blog',
      name: 'blog',
      component: Blog
    },
    {
      path: '/adoptPet',
      name: 'AdoptPet',
      component: AdoptPet
    },
    {
      path: '/show',
      name: 'PetShow',
      component: PetShow
    },
    {
      path: '/adopts/:id',
      name: 'AdoptDetail',
      component: AdoptDetail
    },
    {
      path: '/showdetail/:id',
      name: 'ShowDetail',
      component: ShowDetail
    },
    {
      path:"/test",
      name:"test",
      component:test,
      children:[{
        path:"/",
        name:"test1",
        component: test1
      }]

    },
    {
      path:"/PersonalCenter",
      name:"PersonalCenter",
      component:PersonalCenter,
      children:[
        {path:"/", name:"PersonalInformation", component:PersonalInformation},
        {path:"/Credit",name:"Credit",component:Credit},
        {path:"/Safety",name:"Safety",component:Safety},
        {path:"/adopt",name:"adopt",component:Adopt},
        {path:"/Foster",name:"Foster",component:Foster},
        {path:"/modifypwd",name:"modifypwd",component:modifypassword},
        {path:"/modifyemail",name:"modifyemail",component:modifyemail},
        {path:"/modifytel",name:"modifytel",component:modifytel},
        {path:"/RealName",name:"RealName",component:RealName},
        ]
    },
    {
      path: '/template',
      name: 'Template',
      component: Template
    },

    {
      path: '/blogdetail/:id',
      name: 'BlogDetail',
      component: BlogDetail
  },
    {
      path: '/repassword',
      name: 'repassword',
      component: repassword
    },
    {
      path: '/fan/:id',
      name: 'Fan',
      component: Fan
    },
    {
      path:"/repassword",
      name:"repassword",
      component:repassword
    }

  ]
})
