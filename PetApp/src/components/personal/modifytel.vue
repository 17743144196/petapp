<template>
  <div class="modifytel">
    <header>安全设置</header>
    <div class = "line"></div>
    <div class = "contents">
      <div>
        <div class = "contents-line"></div>
        <div class = "modifytels">修改密码</div>
        <div class = "content-old">
          <input type="text" placeholder="请输入新密码" id = "newpsw" v-model="np"><br>
          <input type="text" placeholder="请输再次输入" id = "opsw" v-model="nnp"><br>
          <div>
          <input type="text" placeholder="输入验证码" id="vc" @change = "yezheng" v-model="yz" >
          <input class="btn btn-default" type="submit" v-model="s" @click = "getc" id = "yzs">
          </div>
          <input class="lastbtn btn-default" type="submit" value="提交" @click = "sbt">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      coeds:"",
      url:"http://127.0.0.1:8000/",
      yz:"", //获取验证码的
      np:"",//获取新密码的
      nnp:"", //新密码的第二次验证
      s:"验证"//读秒
    }
  },

  methods:{

    //产生验证短信
    getc:function () {
      var data = {"phone":sessionStorage.getItem("tel")}
      var vm = this
      $.ajax({
        url: vm.url + "personal/sendcode/",
        type:"POST",
        data:JSON.stringify(data),
        contentType:"aoolication/json",
        success:function(res){

          //验证读秒
          console.log("成功啦")
          document.querySelector("#yzs").style.background = "gray"
          var s =60;
          vm.tt = setInterval(function(){
            vm.s = s + "秒";
            if(s>0){
              s--;
            }else{
              clearInterval(vm.tt)
              vm.s = "验证"
              document.querySelector("#yzs").style.background = "white"
            }

          },1000)
        },
        error:function(){
          console.log("失败啦")
        }
      })
    },

    //保存验新密码
    sbt:function () {
      let d = {
        "telephone":sessionStorage.getItem("tel"),
        "password":this.np,
        "npassword":this.nnp
      }

      let vm = this
      $.ajax({
        url: vm.url + "personal/alterp/",
        type:"POST",
        data:JSON.stringify(d),
        contentType:"aoolication/json",
        success:function(res){
          //如果token过期自动跳转到登录页面
          if(res["code"] == "406"){
            sessionStorage.clear()
            vm.$router.push({path: '/login'})
          }
          alert("密码修改成功")
          vm.np = ""
          vm.nnp = ""
          vm.yz = ""
        },
        error:function(){
          console.log("失败啦")
        }
      })


    },

    //比较验证码
    yezheng:function () {
      var d = {
        "phone":sessionStorage.getItem("tel"),
        "yecode":this.yz,
      }
      let vm = this
      $.ajax({
        url: vm.url + "user/yezheng/",
        type:"POST",
        data:JSON.stringify(d),
        contentType:"aoolication/json",
        success:function(res){
          console.log("成功啦")
        },
        error:function(){
          console.log("失败啦")
        }
      })
    }

    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .modifytel {
    width: 100%;
  }

  .modifytel>header {
    font-size: 1.8em;
    font-weight: 400;
  }

  .modifytel .line {
    margin-top: 20px;
    border:2px solid #c5c5c5;
    border-top-left-radius: 2px;
    border-top-right-radius: 2px;
  }

  @media(min-width: 997px){
    .contents {
      height: 425px;
      background-color: white;
      padding-top: 40px;
      padding-left: 10px;
    }

    .contents .contents-line {
      width: 90%;
      border: 1px solid rgba(157, 157, 157, 0.45);
    }

    .contents .modifytels {
      font-size: 1.5em;
      position: relative;
      top: -15px;
      width: 140px;
      margin-left: 10px;
      text-align: center;
      font-weight: 300;
      background-color: white;
    }

    .contents .content-old {
      /*border: 1px solid red;*/
      text-align: center;
      margin-top: 50px;
    }

    .contents .content-old>div{
      margin:10px auto;
      width: 30%;
      display: flex;
      justify-content: space-between;
    }

    .contents .content-old>input:first-child {
      width: 30%;
      height: 40px;
      border: 1px solid #9AA0A7;
      border-radius: 3px;
      text-align: center;
    }

    .contents .content-old #opsw {
      width: 30%;
      height: 40px;
      margin-top: 10px;
      border: 1px solid #9AA0A7;
      border-radius: 3px;
      text-align: center;
    }

    .contents .content-old>div .btn {
      height: 40px;
      /*margin-left: 50px;*/
      width: 40%;
      margin-right: 0px;
    }

    .contents .content-old .lastbtn {
      width: 30%;
      height: 40px;
      background-color: #E2231A;
      border-radius: 3px;
      color: white;
      border: 0;
    }

    .contents .content-old #vc {
      width: 50%;
      height: 40px;
      border: 1px solid #9AA0A7;
      border-radius: 3px;
      text-align: center;
      position: relative;
    }

  }

</style>
