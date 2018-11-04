<template>
  <div>
    <div class = "container-fluid hc"  >
      <div class="row">
          <div class="col-md-2 col-sm-3 col-xs-12">
            <a href="#">
              <img src="../../assets/images/logo.png" alt="#">
              <span>个人中心</span>
            </a>
          </div>
          <div class="col-md-10 col-sm-9 col-xs-12">
            <nav class="navbar navbar-default">
              <div class="container-fluid">
                <!-- Brand and toggle get grouped for better mobile display -->
                <div class="navbar-header">
                  <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                  </button>
                  <!--<a class="navbar-brand" href="https://www.baidu.com" >-->
                  <router-link to="/" class="navbar-brand">
                    <img src="../../assets/images/home.png" alt="#">
                    <span>返回首页</span>
                  </router-link>
                  <!--</a>-->
                </div>

                <!-- Collect the nav links, forms, and other content for toggling -->
                <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                  <ul class="nav navbar-nav navbar-right clearlia">
                    <li class = "hidden">
                      <div class = "personal">
                        <a href="#"><img :src="touxiang" alt="" id = "showtx"></a>
                        <span v-text="name"></span>
                      </div>
                    </li>
                    <li>
                     <router-link to="/adopt" class = "li">领养信息</router-link>
                    </li>
                    <li class = "li"><router-link to="/foster">寄养信息</router-link></li>
                    <li class = "li"><router-link to="/safety">安全设置</router-link></li>
                    <li class = "li"><router-link to="/credit">信用评级</router-link></li>
                    <li class = "li"><router-link to="/PersonalCenter">个人信息</router-link></li>
                    <li ><a href="#" @click = "exits">退出</a></li>

                  </ul>
                </div><!-- /.navbar-collapse -->
              </div><!-- /.container-fluid -->
            </nav>
          </div>
      </div>
  </div>
    <div class = "container-fluid subject">
      <div class = "row">
        <div class = "col-md-2 col-sm-3 col-xs-12">
          <div class="list-group" >
            <a href="#" class="list-group-item disabled list-group-first clearstate">
              菜单
            </a>
            <!--<a href="#" class="list-group-item">-->
            <router-link to="/adopt" class="list-group-item">
            <div class = "menu-list" >
                <img src="../../assets/images/book.png" alt="">
                <span>领养信息</span>
              </div>
            </router-link>
            <!--</a>-->
            <!--<a href="#" class="list-group-item">-->
            <router-link to="/foster" class="list-group-item">

            <div class = "menu-list">
                <img src="../../assets/images/book.png" alt="">
                <span>寄养信息</span>
              </div>
            </router-link>
            <router-link to="/safety" class="list-group-item">
            <div class = "menu-list">
              <img src="../../assets/images/menu1.png" alt="">
              <span>安全设置</span>
            </div>
            </router-link>
            <!--</a>-->
            <!--<a href="#" class="list-group-item">-->
              <router-link to="/credit" class="list-group-item">
              <div class = "menu-list">
                <img src="../../assets/images/menu1.png" alt="">
                <span>信用评级</span>
              </div>
              </router-link>
            <!--</a>-->
            <!--<a href="#" class="list-group-item">-->
              <router-link to="/PersonalCenter" class="list-group-item">
              <div class = "menu-list">
                <img src="../../assets/images/menu1.png" alt="">
                <span>个人信息</span>
              </div>
              </router-link>
            <!--</a>-->
          </div>
        </div>
        <div class = "col-md-10 col-sm-9 col-xs-12" >
          <div class = "content">
            <!--<router-link to="/pinfromation">Personal</router-link>-->
            <!--<personal-information></personal-information>-->
            <router-view/>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PersonalCenter',
  data () {
    return {
      msg: '我好帅滴',
      height: "",
      name:"",
      url:"http://127.0.0.1:8000/",
      touxiang:""
    }
  },

  mounted: function(){
    document.querySelector(".subject").firstChild.firstChild.style.height = (document.querySelector(".subject").clientHeight) + "px";
    // console.log( document.querySelector(".subject").clientHeight);
    // console.log( document.querySelector(".hc").clientHeight);
      document.querySelector("nav").style.display = "none"
      document.querySelector("footer").style.display = "none"
      sessionStorage.setItem("renovate",true);

      var d = {"id":sessionStorage.getItem("id")}
      var vm = this
      $.ajax({
        url:vm.url + "personal/getnameimg/",
        data:JSON.stringify(d),
        type:"POST",
        contentType:"application/json",
        success:function (res) {
          // console.log(res)
          vm.name = res["name"]
          console.log(res["touxiang"])
          vm.touxiang = res["touxiang"]
        },
        error:function () {
          console.log("出错了")
        }
      })
  },


  updated: function(){
    document.querySelector(".subject").firstChild.firstChild.style.height = "400px";
    document.querySelector(".subject").firstChild.firstChild.style.height = (document.querySelector(".subject").clientHeight) + "px";

  },

  methods:{
    exits:function () {
      sessionStorage.clear();
      sessionStorage.setItem("renovate",true);
      this.$router.push({path: '/'})
    },


  }



}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  #showtx {
    display: block;
    width: 40px;
    height:40px;
    border-radius: 50%;
    /*background-color: red;*/
  }

  .hc {
    padding: 0px;
  }

  .subject {
    padding: 0;
  }

  .hc .row {
    margin-right: 0;
  }



  .subject>.row {
    margin-right: 0;
  }

  .subject>.row>div:first-child {
    padding: 0 0 200px 0;
  }


  .hc .row>div:last-child .navbar {
    padding-right: 0;
  }


  /*subject start*/

  .menu-list {
    display: flex;
    /*justify-content: center;*/
    align-items: center;
  }


  .menu-list img{
    width: 20px;
    height: 20px;
    display: block;
    margin-right: 10px;
  }

  .menu-list span{
    font-size: 1.2em;
  }

  /*subject end*/


  @media (max-width: 768px) {
    /*navigation start*/

    /*navigation left start*/

    .hc .row .col-xs-12:first-child {
      padding: 0;
      height: 40px;
      display: flex;
      justify-content: center;
      align-items: center;
      background-color: #263444;
    }

    .hc .row .col-xs-12:first-child a {
      color: #BEC2C7;
      font-size: 1.4em;
      text-decoration: none;
    }

    .hc .row div:first-child a:hover {
        text-decoration: none;
    }

    .hc .row div a img {
      display: none;
    }

    /*navigation left end*/

    /*navigation right start*/

    .hc .row div:last-child .navbar{
      padding: 0 10px;
    }

    .hc .row div:last-child .navbar a:hover{
      background-color: white;
    }

    .hc .row div:last-child {
      padding: 0 0 0 15px;
    }

    .hc .row>div:last-child nav .clearlia {
      margin-right: 0;
    }

    /*navigation right end*/

    /*navigation end*/


    /*subject start*/


    .subject .row>div:first-child {
      display: none;
    }

    /*content start*/
    .subject .row>div:last-child {
      padding: 0;
    }

    .subject .row>div:last-child .content {
      /*margin-top: 40px;*/
      width: 85%;
      margin: 40px auto 0px;
      /*background-color: chartreuse;*/
    }


    /*content start*/


    /*subject end*/
  }

  @media (min-width: 768px) {
    /*navigation start*/

    /*navigation left start*/
    .hc .row>div:first-child {
      background-color: #263444;
      height: 50px;
      padding: 0;
    }

    .hc .row>div:first-child a  {
      width: 100%;
      height: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      color: #BEC2BF;
      text-decoration: none;
    }



    .hc .row>div:first-child a img {
      display: block;
      height: 30px;
    }

    .hc .row>div:first-child a span {
      margin-left: 10px;
    }

    /*navigation left end*/

    /*navigation right start*/
    .hc .row>.col-sm-9 {
      padding: 0;
      border: 0px;
      height: 50px;
      border-radius: 0;
    }

    .hc .row>.col-sm-9 .navbar {
      border: 0px;
      border-radius: 0;
      padding: 0 20px 0 10px;
      background-color: #393D49;
    }

    .hc .row>.col-sm-9 .navbar-brand {
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .hc .row>.col-sm-9 .navbar-brand span {
      margin-left: 10px;
      color: #BEC2BF;
    }

    .hc .row>.col-sm-9 .navbar-brand span:hover {
      color: rgba(255,255,255,0.8);
    }

    .hc .row>.col-sm-9 div div:last-child ul{
      /*background-color: #9D9D9D;*/
      display: flex;
      align-items: center;
    }

    .hc .row>.col-sm-9 div div:last-child ul .personal {
      display: flex;
      justify-content: center;
      align-items: center;
      color: white;
    }

    .hc .row>.col-sm-9 div div:last-child ul .personal a {
      display: block;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      margin-right: 10px;
      background: url("../../assets/images/man_xiao.png") no-repeat 5px 5px white;
    }

    .hc .row>.col-sm-9 div div:last-child ul li>a {
      color: rgba(255,255,255,1);
    }

    .hc .row>.col-sm-9 div div:last-child ul li>a:hover {
      color: rgba(255,255,255,0.8);
    }

    .hc .row>.col-sm-9 div div:last-child ul .hidden {
      display: inline!important;
    }

    .hc .row>.col-sm-9 div div:last-child ul .li {
      display: none;
    }
    /*navigation right end*/
    /*navigation end*/

    /*subject start*/

    .subject {
      height: 100%;
      background-color: #9D9D9D;
    }

    .subject>div {
      height: 100%;
      /*margin: 0 0px;*/
    }

    .subject .row>div:first-child {
      height: 100%;
      background-color: #EEEEEE;
      padding-left: 0;
      padding-right: 0;
    }
    .subject  .row>div:first-child div .list-group-item {
      border: none;
      border-radius: 0;
      margin-top: 10px;
      border-left: 2px solid rgba(0,0,0,0);
      background-color: #EEEEEE;
    }


    .subject .row>div:first-child div a {
      margin-left: 15px;
    }


    .subject .row>div:first-child div a:hover {
      background-color: #DDDFDF;
      color: white;
      border-left: 2px solid #999999;
    }

    .subject .row>div:first-child div a:first-child {
      background-color: #8E8E8E;
      margin-top: 0px;
      color:black;
      font-weight: 500;
    }

    /*subject end*/

    /*content start*/
    .subject .row>div:last-child {
      padding: 0;
    }

    .subject .row>div:last-child .content {
      /*margin-top: 40px;*/
      width: 85%;
      margin: 40px auto 0;
      /*background-color: chartreuse;*/
    }

    /*content start*/

  }

  @media (min-width: 992px) {
    .hc .row>.col-sm-9 div div:last-child ul .personal span {
      margin-left: 10px;
    }

    /*subject start*/

    .subject {
      /*height: 100%;*/
      background-color: #9D9D9D;
    }


    .subject .row>div:first-child {
      /*height: 100%;*/
      /*height: 700px;*/
      background-color: #EEEEEE;
      padding-left: 0;
      padding-right: 0;
    }
    .subject  .row>div:first-child div .list-group-item {
      border: none;
      border-radius: 0;
      margin-top: 10px;
      border-left: 2px solid rgba(0,0,0,0);
      background-color: #EEEEEE;
    }


    .subject .row>div:first-child div a {
      margin-left: 15px;
    }


    .subject .row>div:first-child div a:hover {
      background-color: #DDDFDF;
      color: white;
      border-left: 2px solid #999999;
    }

    .subject .row>div:first-child div a:first-child {
      background-color: #8E8E8E;
      margin-top: 0px;
      color:black;
      font-weight: 500;
    }

    /*subject end*/

    /*content start*/
    .subject .row>div:last-child {
      padding: 0;
    }

    .subject .row>div:last-child .content {
      /*margin-top: 40px;*/
      width: 85%;
      margin: 40px auto 0;
      /*background-color: chartreuse;*/
    }

    /*content start*/
  }



</style>
