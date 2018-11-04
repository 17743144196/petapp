<template>
  <div class="register-container">
    <div class="layui-row card-container">
      <div class="lph-card-register layui-col-md4 layui-col-md-offset4">
        <div class="layadmin-user-login-box layadmin-user-login-header">
          <h2>我的狗子</h2>
          <p>我的狗子-国内最大的宠物领养送养平台</p>
        </div>
        <div class="layadmin-user-login-box layadmin-user-login-body layui-form">
          <div class="layui-form-item">
            <label class="layadmin-user-login-icon layui-icon layui-icon-cellphone" ></label>
            <input class="layui-input" v-model="phone" id="phone" lay-verify="phone" name="phone" placeholder="请输入注册时的手机号" type="text">
          </div>
          <div class="layui-form-item">
            <div class="layui-row">
              <div class="layui-col-xs7">
                <label class="layadmin-user-login-icon layui-icon layui-icon-vercode" for="LAY-user-login-vercode"></label>
                <input class="layui-input"  @change = "yezheng" v-model="yanzhengcode" id="LAY-user-login-vercode" lay-verify="required" name="verifyCode" placeholder="验证码" type="text">
              </div>
              <div class="layui-col-xs5">
                <div style="margin-left: 10px;">
                  <button class="layui-btn layui-btn-primary layui-btn-fluid" @click="Zhuce" id="send-verify" type="button">获取验证码</button>
                </div>
              </div>
            </div>
          </div>
          <div class="layui-form-item">
            <label class="layadmin-user-login-icon layui-icon layui-icon-password" for="LAY-user-login-password"></label>
            <input class="layui-input" v-model="newpassword" id="LAY-user-login-password" lay-verify="required" name="passwordNew" placeholder="新密码" type="password">
          </div>
          <div class="layui-form-item">
            <label class="layadmin-user-login-icon layui-icon layui-icon-password" for="LAY-user-login-repass"></label>
            <input class="layui-input" v-model="again" id="LAY-user-login-repass" lay-verify="required" name="repassword" placeholder="确认新密码" type="password">
          </div>

          <div class="layui-form-item">
            <button class="layui-btn layui-btn-fluid" @click="getdata" lay-filter="forget-submit" lay-submit="">重置新密码</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';
    export default {
        name: "repassword",
      data: function () {
        return {
          phone: "",
          yanzhengcode: "",
          newpassword: "",
          again: "",

        }

      },
      methods:{
        getdata:function () {
          var value=this.phone;
          var phoneReg = /^1[34578]\d{9}$/;
          var data = {
            "phone": this.phone,
            "yanzhengcode": this.yanzhengcode,
            "newpassword":this.newpassword,

          }
          if(phoneReg.test(value)&&this.yanzhengcode&&this.newpassword&&this.newpassword===this.again){
            axios.post('http://127.0.0.1:8000/user/repassword/', data)
              .then(response => {

                  if (response.data.code === 808) {
                    alert("修改成功");
                    this.$router.push({
                      path: 'Login'
                    })
                  }else{
                    alert("两次密码不一致");
                  }

              })
          }
          },

        Zhuce:function(){
          // console.log(this.phone);

          var vm = this;
          axios.post('http://127.0.0.1:8000/user/sendcode/',{"phone":this.phone})
            .then(function (res) {
              if(res.data.code === 200){
                // alert('发送成功')
                // console.log(document.querySelector(".nishi"))

                document.querySelector("#send-verify").style.background = "gray"
                // console.log("12345")
                var s =60;
                vm.tt = setInterval(function(){
                  vm.contents = s + "秒";
                  if(s>0){

                    $('#send-verify').attr('disabled',"true")
                    s--;
                  }else{
                    clearInterval(vm.tt)
                    $('#send-verify').removeAttr('disabled')
                    vm.contents = "获取验证码"
                    document.querySelector(".send-verify").style.background = "#009688"
                  }

                },1000)
              }
            })
            .catch(function (error) {
              console.log(2)
            })
        },

        yezheng:function(){
          var dc = document.querySelector("#LAY-user-login-vercode").value
          var vm = this;
          axios.post('http://127.0.0.1:8000/user/yezheng/',{"phone":this.phone,"yecode":dc})
            .then(function(res){
              if(res.data.code===200){
                document.querySelector(".send-verify").style.background = "#009688";
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
        }

    }
</script>

<style scoped>
  blockquote, body, button, dd, div, dl, dt, form, h1, h2, h3, h4, h5, h6, input, li, ol, p, pre, td, textarea, th, ul {

    margin: 0;
    padding: 0;
  }

  .layui-bg-gray {

    color: #666 !important;

  }
  .card-container {

    padding: 50px 0px;

  }

  .lph-card-register {

    padding: 20px 45px;

  }

  .layui-col-md-offset4 {

    margin-left: 33.33333333%;

  }
  .layui-col-md4 {

    width: 33.33333333%;

  }
  .layui-col-md1, .layui-col-md10, .layui-col-md11, .layui-col-md12, .layui-col-md2, .layui-col-md3, .layui-col-md4, .layui-col-md5, .layui-col-md6, .layui-col-md7, .layui-col-md8, .layui-col-md9 {

    float: left;

  }
  .layui-col-lg1, .layui-col-lg10, .layui-col-lg11, .layui-col-lg12, .layui-col-lg2, .layui-col-lg3, .layui-col-lg4, .layui-col-lg5, .layui-col-lg6, .layui-col-lg7, .layui-col-lg8, .layui-col-lg9, .layui-col-md1, .layui-col-md10, .layui-col-md11, .layui-col-md12, .layui-col-md2, .layui-col-md3, .layui-col-md4, .layui-col-md5, .layui-col-md6, .layui-col-md7, .layui-col-md8, .layui-col-md9, .layui-col-sm1, .layui-col-sm10, .layui-col-sm11, .layui-col-sm12, .layui-col-sm2, .layui-col-sm3, .layui-col-sm4, .layui-col-sm5, .layui-col-sm6, .layui-col-sm7, .layui-col-sm8, .layui-col-sm9, .layui-col-xs1, .layui-col-xs10, .layui-col-xs11, .layui-col-xs12, .layui-col-xs2, .layui-col-xs3, .layui-col-xs4, .layui-col-xs5, .layui-col-xs6, .layui-col-xs7, .layui-col-xs8, .layui-col-xs9 {

     position: relative;
     display: block;
     box-sizing: border-box;

   }
  .layadmin-user-login-header {

    text-align: center;

  }
  .layadmin-user-login-box {

    padding: 20px;

  }
  .layadmin-user-login-header {

    text-align: center;

  }
  .layadmin-user-login-box {

    padding: 20px;

  }

  .layadmin-user-login-body .layui-form-item {

    position: relative;

  }
  .layui-form-item {

    margin-bottom: 15px;
    clear: both;


  }


  .layadmin-user-login-icon {

    position: absolute;
    left: 1px;
    top: 1px;
    width: 38px;
    line-height: 36px;
    text-align: center;
    color: #d2d2d2;

  }
  .layui-icon {

    font-family: layui-icon !important;
    font-size: 16px;
    font-style: normal;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;

  }
  .layui-btn, .layui-disabled, .layui-icon, .layui-unselect {

    -webkit-user-select: none;
    -ms-user-select: none;
    -moz-user-select: none;

  }

  .layadmin-user-login-body .layui-form-item .layui-input {

    padding-left: 38px;

  }
  .layui-input, .layui-textarea {

    display: block;
    width: 100%;
    padding-left: 10px;

  }
  .layui-input, .layui-select, .layui-textarea {

    height: 38px;
    line-height: 1.3;
    line-height: 38px\9;
    border-width: 1px;
    border-style: solid;
    background-color: #fff;
    border-radius: 2px;

  }
  .layui-badge-rim, .layui-colla-content, .layui-colla-item, .layui-collapse, .layui-elem-field, .layui-form-pane .layui-form-item[pane], .layui-form-pane .layui-form-label, .layui-input, .layui-layedit, .layui-layedit-tool, .layui-quote-nm, .layui-select, .layui-tab-bar, .layui-tab-card, .layui-tab-title, .layui-tab-title .layui-this::after, .layui-textarea {

    border-color: #e6e6e6;

  }
  .layui-btn, .layui-input, .layui-select, .layui-textarea, .layui-upload-button {

    outline: 0;
    -webkit-appearance: none;
    transition: all .3s;
    -webkit-transition: all .3s;
    box-sizing: border-box;

  }
  button, input, optgroup, option, select, textarea {

    font-family: inherit;
    font-size: inherit;
    font-style: inherit;
    font-weight: inherit;
    outline: 0;

  }

  .lph-card-register {

    padding: 20px 45px;

  }

</style>
