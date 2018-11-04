<template>
  <div class="modifytel">
    <header>安全设置</header>
    <div class = "line"></div>
    <div class = "contents">
      <div>
        <div class = "contents-line"></div>
        <div class = "modifytels">绑定邮箱</div>
        <div class = "content-old">
          <input type="text" :placeholder="show" id = "newpsw" @change = "yanzheng" v-model="email"><br>
          <!--<input type="text" placeholder="请输再次输入" id = "opsw"><br>-->
          <div>
          <input type="text" placeholder="输入邮箱验证码" id="vc" v-model="codes">
          <input class="btn btn-default" type="submit" value="验证" @click = "sendcode">
          </div>
          <input class="lastbtn btn-default" type="submit" value="提交" @click = "sub">
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
      email:"",//获取邮箱码
      codes:"",//获取验证码
      show:"请输入邮箱",//显示提示信息
      url:"http://127.0.0.1:8000/",
      savacode:""
    }
  },


  methods:{
    //判断是否为邮箱
    yanzheng:function () {
      //利用正则表达式判断是否是信箱
      var reg = new RegExp("^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$");
      console.log( reg.test(this.email))
      if( !reg.test(this.email)){
        this.email = ""
        this.show = "请输入正确的邮箱"
      }
    },

    //获取邮箱验证码
    sendcode:function () {
      if(this.email == ""){
        this.show = "请输入正确的邮箱"
        return
      }

      var vm = this
      var d = {"email":this.email}
      $.ajax({
        url:vm.url + "user/sendEmail/",
        data:JSON.stringify(d),
        type:"POST",
        contentType:"appliction/json",
        success:function (res) {
            vm.savacode = res.codes
        },
        error:function () {
          alert("程序出错 请刷新页面重新输入")
        }
      })
    },

    //提交绑定邮箱
    sub:function () {
      if(this.email == "" && this.codes == ""){
        this.show = "请输入正确的邮箱"
        return
      }

      if(this.savacode == this.codes){
        var vm = this
        var d = {"email":this.email,"user_id":sessionStorage.getItem("id")}
        $.ajax({
          url:vm.url + "user/addemail/",
          data:JSON.stringify(d),
          type:"POST",
          contentType:"appliction/json",
          success:function (res) {
              alert("邮箱绑定成功")
              vm.email = ""
              vm.codes = ""
              vm.savacode = ""
          },
          error:function () {
            alert("程序出错 请刷新页面重新输入")
          }
        })
      }else{
         this.email = ""
         this.codes = ""
         this.savacode = ""
         this.show = "验证码错误 请重新发送"
      }


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
      margin-top: 30px;
    }

    .contents .content-old>div{
      margin:30px auto;
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
