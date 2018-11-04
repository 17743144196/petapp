<template>
  <div class="container">
    <div class="row card-container">
      <div class="col-md-3 col-md-offset-8 ">
        <div class="user-login-box user-login-header">
          <h2 style="font-weight:lighter">我的狗子</h2>
          <p style="color: #B4B4B4">我的狗子-国内最大的宠物领养送养平台</p>
        </div>
        <div class="user-login-box user-login-body form">
          <div class="form-group">
            <input v-model="ii.telephone" type="text" class="form-control" id="telephone" placeholder="用户名">
          </div>
          <div class="form-group">

            <input v-model="ii.password" type="password" class="form-control" id="password" placeholder="密码">
          </div>
          <div class="login-checkbox">
            <label>
              <div><input type="checkbox"> 记住密码</div>
              <!--<a href="#" style="color: #33ABA0">-->
                <router-link to="/repassword" class="list-group-item">忘记密码？</router-link>
            </label>
          </div>
          <button @click="doLogin" type="button" class="btn btn-primary btn-block btn-color">登陆</button>
        </div>
        <div class="user-login-box user-login-other ">
          <label>社交账号登入</label>
          <a href="#"><i class="icon "><img src="../assets/images/QQ.png" height="26" width="26"/></i></a>
          <a href="#"><i class="icon "><img src="../assets/images/weixin.png" height="26" width="26"/></i></a>
          <a href="#">
            <i class="icon "><img src="../assets/images/weibo.png" height="26" width="26"/></i>

          </a>
          <a class="user-jump-change link-color" href="#/regist">注册帐号</a>


        </div>
      </div>

    </div>
    <div class="mess" v-model="ii.mes" v-text="ii.mes " v-show="ii.mes"></div>

  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'Login',
    data: function () {
      return {
        ii: {
          id:'',
          telephone: '',
          password: '',
          mes: '',
          flag: false
        },
        show: false,
      }
    },

    mounted:function(){
    },
    methods: {
      aa() {

        this.ii.mes = '';
      },
      doLogin() {
        if (this.ii.telephone === '') {
          this.ii.mes = '用户名不能为空';
          return false
        }
        if (this.ii.password === '') {
          this.ii.mes = '密码不能为空';
          return false
        }
        // let dd=new URLSearchParams();
        // dd.append('mobile',this.mobile);
        // dd.append('password',this.password);
        axios.post('http://127.0.0.1:8000/user/login/', JSON.stringify(this.ii), {
          headers: {
            'Content-Type': 'application/json;charset=utf-8',
          }
        })
          .then(res => {
            // console.log(res);
            if (res.data.code === "201") {
              // this.$store.commit('setToken', res.data);
              // localStorage.telephone = this.telephone;
              // localStorage.token_expire = res.data.expire;
              // localStorage.token = res.data.token;
              // alert("seccess");
              // sessionStorage.telephone = res.data.telephone
              // console.log(res.headers.token)  res.headers.token 是用来获取头部的token

              sessionStorage.setItem("tel",res.data.tel)
              sessionStorage.setItem("token",res.headers.token)
              sessionStorage.setItem("id",res.data.user_id);
              sessionStorage.setItem("renovate",true);
              this.$router.push({path: '/'})
            } else {
              alert('用户名或密码错误');
              return false
              // this.ii.mes = '用户名或密码错误';
            }
          })
          // .catch(err => {
          //   console.log(err)
          // })
      }
    },

    watch: {
      ii: {
        handler(newval, oldval) {
          if (this.ii.telephone !== ''&& this.ii.password !== '') {
            this.ii.mes=''
          }
        },
        deep: true,
        // immediate:true
      }


    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  h1, h2, p, span, label, a {
    margin: 0;
    padding: 0;
    font-weight: lighter

  }

  .mess {
    position: fixed;
    width: 150px;
    height: 50px;
    line-height: 50px;
    text-align: center;
    background-color: black;
    font-size: larger;
    color: white;
    z-index: 999;
    left: 45%;
    bottom: 60%;
    opacity: 0.5;

  }

  .container {
    background-image: url(http://www.lazyer.net/static/common/img/banner-login.jpg);
    background-repeat: no-repeat;
    /*background-color: pink;*/
    background-position: top;
    height: 100%;
    width: 100%;
    margin-top: 90px;

  }

  .card-container {
    width: 100%;
    height: 531px;
    padding: 50px 0px;
    /*background-color: pink;*/

  }

  .user-login-box {
    padding: 20px;
    width: 100%;
    background-color: white;

  }

  .user-login-header {
    text-align: center;
    font: 14px Helvetica Neue, Helvetica, PingFang SC, 微软雅黑, Tahoma, Arial, sans-serif;
    font-weight: lighter;

  }

  .user-login-box h2 {
    margin-bottom: 10px;
    margin-top: 0;
  }

  .user-login-body {

  }

  .login-checkbox label {
    display: flex;
    justify-content: space-between;

  }

  .btn-color {
    background-color: #33ABA0;
    border-color: #33ABA0;
  }

  .link-color {
    color: #33ABA0;
  }

  .user-login-other {
    padding-bottom: 25px;

  }

  .icon {
    width: 27px;
    height: 26px;
  }

  .user-jump-change {
    float: right;
    /*justify-content:space-between;*/

  }

</style>
