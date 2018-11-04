<template>
  <div id="app" class="container-fluid" style = "padding: 0">
    <!--此处可以放导航-->
    <nav-main></nav-main>
    <!--路由容器-->
    <router-view/>
    <footer-pet></footer-pet>
  </div>
</template>

<script>
  // $(function () {
  //   alert('ok')
  // });
  export default {
    name: 'App',
    methods:{
      show:function () {

      }
    },
    mounted:function () {
      document.querySelector("nav").style.display = "none"
      document.querySelector("footer").style.display = "none"
    }

  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
  }

</style>
