<template>
  <nav class="navbar navbar-default navcolor ">
    <div class = "container" >
    <div class="container-fluid">
      <!-- Brand and toggle get grouped for better mobile display -->
      <div class="navbar-header">
        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <!--<a class="navbar-brand cleara" href="#"><img src="../assets/images/logo.png" alt="#" class = "imageset"></a>-->
        <router-link to="/" class="navbar-brand cleara"><img src="../assets/images/logo.png" alt="#" class = "imageset"></router-link>
      </div>

      <!-- Collect the nav links, forms, and other content for toggling -->
      <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
        <ul class="nav navbar-nav">
          <ul class="nav navbar-nav ulpadding">
            <li ><router-link to="/adoptPet">领养</router-link></li>
            <li><router-link to="/Present">寄养</router-link></li>
            <li><router-link to="/Blog">论坛</router-link></li>
            <li ><router-link to="/show">宠物秀</router-link></li>
          </ul>
        </ul>
        <ul class="nav navbar-nav navbar-right" id="loginin" v-if = "!show">
          <li><router-link to="/Login" id="login">登录</router-link></li>
          <li><router-link to="/Regist">注册</router-link></li>
        </ul>
        <!--<ul class="nav navbar-nav navbar-right"  id="logoutout" style="display: none">-->
          <!--<li >个人中心</li>-->
          <!--<li><a href="#" id="logout">退出</a></li>-->
        <!--</ul>-->
        <ul class="nav navbar-nav navbar-right"  id="logoutout" v-if = "show">
          <li class = "touxiang"><router-link to="/PersonalCenter" id="touxiang"><img v-bind:src = "imgss" alt="#" style=" background-color: white"></router-link></li>
          <!--<li ><router-link to="/Regist">{{name}}</router-link></li>-->

          <li class="dropdown personals"><a href="#" class="dropdown-toggle" data-toggle="dropdown" v-text="name"></a>
            <ul class="dropdown-menu">
              <li><router-link to="/PersonalCenter">个人中心</router-link></li>
              <li class = "exit" @click = "exitlogin"><a href="#">退出</a></li>
            </ul>
          </li>
        </ul>
      </div><!-- /.navbar-collapse -->
    </div><!-- /.container-fluid -->
    </div>
  </nav>
</template>

<script>
  import axios from 'axios';
export default {
  name: 'NavMain',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      show:false,
      name:"用户名",
      imgss:""
    }
  },
  mounted:function(){
      var userId = sessionStorage.getItem("id");
      console.log(userId)
      if(userId == null){
        console.log("yes");
      }else{
        this.show = true
        this.showtouxiang()
      }
    },

  methods:{
    bb:function (b) {
      console.log("你好啊")
    },

    // 获取导航栏中，头像和用户名信息    不过后台在传送数据过来时出错了
    showtouxiang:function () {
      var userId = sessionStorage.getItem("id");
      let datas = {"id":userId};
      var vm = this
      if(userId != null){
        $.ajax({
          url:"http://127.0.0.1:8000/user/getNameImg/",
          type:"POST",
          contentType:"application/json",
          data:JSON.stringify(datas),
          success:function (res) {
            vm.name = res.name
            vm.imgss = res.photo
          },
          error:function () {
            console.log("失败了")
          }
        })
      }
    },

    //退出登录状态
    exitlogin:function () {
        this.show = false
        sessionStorage.clear()
        location.reload()
    }
  }
}
</script>

 <!--Add "scoped" attribute to limit CSS to this component only-->
<style scoped>

  .navcolor {
    background-color: #263444;
    height: 60px;
    border-radius: 0;
    border: 0;
  }

  .imageset {
    height: 40px;
  }

  .container {
    padding: 5px 10px;
  }


  .cleara {
    padding: 0px;
  }

  .navbar-default .navbar-nav>li>a {
    color: rgba(255, 255, 255, 0.82);
    background-color: #263444;
  }

  .navbar-default .navbar-nav>li>a:hover {
    color: rgba(255, 255, 255, 1);
    border-bottom: 5px solid #5FB878;
  }

  .navbar-collapse {
    padding: 0;
    background-color: #263444;
  }

  .ulpadding {
    margin-left : 20px;
  }

  .touxiang {
    background-color: red;
    width:40px;
    height: 40px;
    margin-top: 5px;
    border-radius: 50%;
    margin-right: 10px;
  }

  .touxiang a {
    padding: 0px;
  }

  .navbar-default .navbar-nav>.touxiang a:hover{
    border-bottom: 5px solid rgba(95, 184, 120, 0);
  }

  .touxiang a img {
    width: 40px;
    height: 40px;
    display: block;
    border-radius: 50%;
  }

  .navbar-default .navbar-nav>.personals>a{
    border-bottom: 5px solid rgba(95, 184, 120, 0);
    color: #D8DADD;
  }
  .navbar-default .navbar-nav>.personals>a:hover {
    border-bottom: 5px solid rgba(95, 184, 120, 0);
  }

  .navbar-default .navbar-nav>.personals>a:visited{
    background-color: #263444;

  }

  @media (max-width: 768px) {
    .container {
      padding: 5px;
    }

    .container .navbar-header a {
      margin: 0 5px;
    }

    .navbar-nav {
      margin: 0;
      border-top: 1px solid rgba(255, 255, 255, 0.83);
    }


  }
</style>
