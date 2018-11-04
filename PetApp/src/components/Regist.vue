<template>

  <body class="login-body layui-bg-gray" >


  <div class="register-container">
    <div class="row card-container">
      <div class="lph-card-register col-md-4 col-md-offset-4">
        <div class="layadmin-user-login-box layadmin-user-login-header">
          <h2>我的狗子</h2>
          <p>我的狗子-国内最大的宠物领养送养平台</p>
        </div>
        <div class="layadmin-user-login-box layadmin-user-login-body layui-form">
          <div class="layui-form-item">
            <input class="layui-input" placeholder="昵称" @change="checkname" type="text" v-model="name" >
            <span class="mes" v-text="msgame"></span>
          </div>
          <!--<div class="layui-form-item">-->

            <!--<input class="layui-input" id="email"  name="email" placeholder="邮箱" type="text">-->
          <!--</div>-->
          <div class="layui-form-item">
            <input class="layui-input" placeholder="手机"  @change ="checkphone" type="text" v-model = "phone" id="phone">
            <span class="mes" v-text="msgphone"></span>
          </div>
          <div class="layui-form-item">
            <div class="row " style="margin: 0">
              <div class="col-xs-7">
                <input class="layui-input yanzheng" placeholder="验证码" type="text" @change = "yezheng">
              </div>
              <div class="col-xs-4 col-md-offset-1 col-xs-offset-1">
                <div style="margin-left: 10px;">
                  <button class="layui-btn layui-btn-primary layui-btn-fluid nishi"  @click="Zhuce" id="yanzheng11">{{contents}}
                  </button>
                </div>
              </div>
            </div>
          </div>

          <div class="layui-form-item">
            <input class="layui-input" placeholder="密码" @change="checkpassword"  type="password" v-model="password"  id="test">
            <span class="mes" v-text="msgpassword"></span>
          </div>
          <div class="layui-form-item">

            <input class="layui-input" placeholder="确认密码" type="password" @change="checkpwd"  v-model="pwd" id="test1">
            <span class="mes" v-text="msgpwd"></span>
          </div>

          <div class="layui-form-item line">
            <input class="" checked=""   type="checkbox"  style="display: block">
            <div class="layui-unselect  " ><span>同意用户协议</span></div>
          </div>
          <div class="layui-form-item">
            <button class="layui-btn layui-btn-fluid" @click = "sub">注 册</button>
          </div>
          <div class="layui-trans layui-form-item layadmin-user-login-other">
            <label>社交账号注册</label>
            <a href="#"><img src="../assets/images/QQ.png" height="26" width="26"/></a>
            <a href="#"><img src="../assets/images/weixin.png" height="26" width="26"/></a>
            <a href="#"><img src="../assets/images/weibo.png" height="26" width="26"/></a>

            <a class="layadmin-user-jump-change lph-link-color layui-hide-xs" @click="dump">用已有帐号登入</a>

          </div>
        </div>
      </div>
    </div>
  </div>


  </body>
</template>

<script>
  import axios from 'axios'

  export default {
    name: "Regist",
    data: function () {
      return {
        msgame: "",
        msgpassword: "",
        msgpwd: "",
        msgphone: "",
        name: "",
        password: "",
        pwd: "",
        phone: "",
        contents:"验证密码",
        tt: ""
      }
    },
    methods:{
      dump:function(){
        this.$router.push({
          name:'login'
        })
      },
      Zhuce:function(){
        // console.log(this.phone);

        var vm = this;
        axios.post('http://127.0.0.1:8000/user/sendcode/',{"phone":this.phone})
          .then(function (res) {
              if(res.data.code === 200){
                // alert('发送成功')
                // console.log(document.querySelector(".nishi"))

                document.querySelector(".nishi").style.background = "gray"
                // console.log("12345")
                var s =60;
                 vm.tt = setInterval(function(){
                  vm.contents = s + "秒";
                  if(s>0){
                    s--;
                  }else{
                    clearInterval(vm.tt)
                    vm.contents = "验证密码"
                    document.querySelector(".nishi").style.background = "#009688"
                  }

                },1000)
              }
          })
          .catch(function (error) {
            console.log(2)
          })
      },

      checkname:function(){
        if(this.name===""){
          this.msgame = "用户名不能为空";

        }else{
          this.msgame ="";
        }
      },

      checkpassword:function(){
        var pwdReg = /^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{8,16}$/;
        var value = $('#test').val();
        if(this.password===""){
          this.msgpassword = "密码不能为空"
        }else if(!pwdReg.test(value)){
          this.msgpassword = "密码为8-16位，需要有数字字母组成";
        }else{
          this.msgpassword = "";
        }
      },

      checkpwd:function(){
        if(this.pwd===""){
          this.msgpassword ="密码不能为空"
        }else if(this.pwd !==this.password){
          this.msgpwd = "两次输入的密码不一致"
        }else{
          this.msgpwd =""
        }
      },
      checkphone:function(){
        var myreg = /^1[34578]\d{9}$/;
        if(this.phone===""){
          this.msgphone="手机号不能为空";
          return false
        }else if(!myreg.test($("#phone").val())){
          this.msgphone="请输入有效的手机号码";
          return false
        }else{
          var data = {
            "telephone":this.phone,
          };
          var vm = this;
          axios.post('http://127.0.0.1:8000/user/chackphone/',data)
            .then(function(res){
              console.log(res.data.code === 200);
              if(res.data.code===200){

                vm.msgphone="该手机号已存在";
                console.log(6666666666666666666);
                // $('input[value="Hot Fuzz"]')
                $('#yanzheng11').attr('disabled',"true")
                // $('#yanzheng11')[0].disabled="true";


              }if(res.data.code===202){
                console.log(22222222222);
                vm.msgphone="";
                // $("#button_id").attr('disabled',false);
                $('#yanzheng11').removeAttr('disabled')
                console.log($('#yanzheng11')[0].disabled,33333);
              }
            })
        }
      },

      yezheng:function(){


        // data = {
        //   "phnoe":this.phnoe,
        //   // "yanzhengma":document.querySelector(".yanzheng").value()
        // };


        var dc = document.querySelector(".yanzheng").value
        var vm = this;
        axios.post('http://127.0.0.1:8000/user/yezheng/',{"phone":this.phone,"yecode":dc})
          .then(function(res){
            if(res.data.code===200){
              document.querySelector(".nishi").style.background = "#009688";
              vm.contents = "验证通过";
              clearInterval(vm.tt)
            }else{
              vm.contents = "验证错误";
            }
          })
          .catch(function (error) {

            console.log(2)
          })
      },

      sub: function(){
        var vm = this;

        var data = {
          "name":this.name,
          "telephone":this.phone,
          "password":this.password,
          "npassword":this.pwd
        };

        axios.post('http://127.0.0.1:8000/user/regist/',data)
          .then(function(res){
            if(res.data.code===200){
              alert("注册成功")
              vm.$router.push({path:"/login"})
            }else{
              vm.contents = "验证错误";
            }
          })
          .catch(function (error) {
            console.log(2)
          })

      },




      // chackphone: function(){
      //
      //
      //   var vm = this;
      //
      //   var data = {
      //     "telephone":this.phone,
      //
      //   };
      //
      //
      //
      //     .catch(function (error) {
      //
      //       console.log(2)
      //     })
      //
      // },











    },
    // methods: {
    //   aa() {
    //
    //     this.ii.mes = '';
    //   },
    //   doLogin() {
    //     if (this.ii.telephone === '') {
    //       this.ii.mes = '用户名不能为空';
    //       return false
    //     }
    //     if (this.ii.password === '') {
    //       this.ii.mes = '密码名不能为空';
    //       return false
    //     }
    //     // let dd=new URLSearchParams();
    //     // dd.append('mobile',this.mobile);
    //     // dd.append('password',this.password);
    //     axios.post('http://127.0.0.1:8000/user/login/', JSON.stringify(this.ii), {
    //       headers: {
    //         'Content-Type': 'application/json;charset=utf-8'
    //       }
    //     })
    //       .then(res => {
    //         console.log(res);
    //         if (res.data.code === "201") {
    //           // this.$store.commit('setToken', res.data);
    //           // localStorage.telephone = this.telephone;
    //           // localStorage.token_expire = res.data.expire;
    //           // localStorage.token = res.data.token;
    //           // alert("seccess");
    //           this.$router.push({path: '/'})
    //         } else {
    //           alert('用户名或密码错误');
    //         }
    //       })
    //     .catch(err => {
    //       console.log(err)
    //     })
    //   }
    // },
    // //
    //
    // //
    // //
    // // }
  }

</script>

<style scoped>

  blockquote, body, button, dd, div, dl, dt, form, h1, h2, h3, h4, h5, h6, input, li, ol, p, pre, td, textarea, th, ul {

    padding: 0;}
  body{
    height: 100%;
    font-family: "Helvetica Neue",Helvetica,Arial,sans-serif;
    font-size: 14px;
    line-height: 1.42857143;

  }
  p{
    margin: 0;
  }

  .mes{
  font-size: medium ;
    color: #009688;
    padding-left: 8px

  }
  .yanzheng{
    width: 75% !important;
  }
  .line{
    display: flex;
  }
  .layui-bg-gray {
    background-color: #eee !important;
    color: #666 !important;
  }
  .card-container {
    padding: 50px 0;
    margin: 0;
  }
  .lph-card-register {
    padding: 20px 45px;
  }
  .layadmin-user-login-header {
    text-align: center;
  }
  .layadmin-user-login-box {
    padding: 20px;
  }
  .layadmin-user-login-header h2 {
    margin-bottom: 10px;
    font-weight: 300;
    font-size: 30px;
    color: #000;
  }
  .layadmin-user-login-box {
    padding: 20px;
  }
  /*1111111111111111111111111111111111111111111111111*/
  .layadmin-user-login-body .layui-form-item {
    position: relative;
  }
  .layui-form-item {
    margin-bottom: 23px;
    height: 38px;
  }
  .layui-input, .layui-textarea {
    display: block;
    width: 100%;}
  .layui-input, .layui-select, .layui-textarea {
    height: 38px;
    line-height: 1.3;
    /*line-height: 38px\9;*/
    border-width: 1px;
    border-style: solid;
    padding: 0 9px;
    background-color: #fff;
    border-radius: 2px;
  }
  .layui-btn-fluid {
    width: 100%;
  }
  .layui-btn-fluid {
    width: 100%;
  }
  .layui-btn {
    display: inline-block;
    height: 38px;
    line-height: 38px;
    padding: 0 18px;
    background-color: #009688;
    color: #fff;
    white-space: nowrap;
    text-align: center;
    font-size: 14px;
    border: none;
    border-radius: 2px;
    cursor: pointer;
  }
  .layui-unselect{
    padding:10px 0 0 10px;

  }
  /*.................社交.*/
  .layadmin-user-login-other {
    position: relative;
    /*font-size: 0;*/
    line-height: 38px;
    padding-top: 20px;
  }
  .lph-link-color {
    color: #029789 !important;
  }
  .layadmin-user-jump-change {
    float: right;
  }

</style>
