<template>
  <div id="app" class="container-fluid" style = "padding: 0" >
    <!--此处可以放导航-->
    <nav-main></nav-main>
    <!--路由容器-->
    <router-view/>
    <footer-pet></footer-pet>
  </div>
</template>

<script>
  export default {
    name: 'App',
    data:function(){
      return{
        fla:false
      }
    },
    methods:{
      show:function () {

      },
    },

  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
  }

</style>
