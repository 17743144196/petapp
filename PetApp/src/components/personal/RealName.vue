<template>
  <div class="modifytel">
    <header>安全设置</header>
    <div class="line"></div>
    <div class="contents">
      <div>
        <div class="contents-line"></div>
        <div class="modifytels">实名认证</div>
        <div class="content-old">
          <!--<div class = "name">-->
          <!--<label for = "name">真是姓名:</label>-->
          <!--<input type="text" name = "name" id = "name">-->
          <!--<span></span>-->
          <!--</div>-->
          <!--<div class = "name">-->
          <!--<label for = "types">证件类型:</label>-->
          <!--<input type="text" name = "name" id = "types">-->
          <!--<span></span>-->
          <!--</div>-->
          <!--<div class = "name">-->
          <!--<label for = "number">证件号码:</label>-->
          <!--<input type="text" name = "name" id = "number">-->
          <!--<span></span>-->
          <!--</div>-->
          <!--<div class = "name">-->
          <!--<label for = "bank-card">银行卡号:</label>-->
          <!--<input type="text" name = "name" id = "bank-card">-->
          <!--<span></span>-->
          <!--</div>-->
          <!--<div class = "name">-->
          <!--<label for = "tel">银行卡号:</label>-->
          <!--<input type="text" name = "name" id = "tel">-->
          <!--<span></span>-->
          <!--</div>-->
          <!--<div class = "name">-->
          <!--<label for = "telc">短信验证码:</label>-->
          <!--<input type="text" name = "name" id = "telc">-->
          <!--<span></span>-->
          <!--</div>-->
          <div class="row name">
            <div class="col-md-2 xingming" style="text-align: right">真实姓名:</div>
            <div class="col-md-1 zhenshi"><input type="text" class="nd" name="name" id="name" v-model="name"></div>
            <div class="col-md-9 auth" style="text-align: left">
              <!--<span class="extra" style="display: none;">为确保您的账户安全，请填写您本人的实名认证信息</span>-->
              <span class="error">请输入姓名</span>
            </div>
          </div>
          <div class="row name">
            <div class="col-md-2 zjleixing" style="text-align: right">证件类型:</div>
            <!--<div class = "col-md-2 zhenshi">-->
            <div class="col-md-2 dropdown">
              <!--<div class="layui-input-inline">-->
              <select lay-verify="required" name="type" v-model="type" id="type" class="leixing">
                <option value="身份证">身份证</option>
                <option value="外籍护照">外籍护照</option>
                <option value="台胞证">台胞证</option>
                <option value="回乡证">回乡证</option>
              </select>

              <!--</div>-->
            </div>
            <div class="col-md-8 auth" style="text-align: left"></div>
          </div>
          <div class="row name">
            <div class="col-md-2 xingming" style="text-align: right">证件号码:</div>
            <div class="col-md-2 zhenshi"><input type="text" v-model="num"></div>
            <div class="col-md-8 auth" style="text-align: left"></div>
          </div>
          <div class="row name">
            <div class="col-md-2 xingming" style="text-align: right">银行卡号:</div>
            <div class="col-md-2 zhenshi"><input type="text" v-model="banknumber"></div>
            <div class="col-md-8 auth" style="text-align: left">
              <span class="blu">支持银行</span>
              <span>仅支持您本人名下的银行卡，输入卡号自动识别银行卡种</span>
            </div>
          </div>
          <div class="row name">
            <div class="col-md-2 xingming" style="text-align: right">手机号码:</div>
            <div class="col-md-2 zhenshi"><input type="text" v-model="tel"></div>
            <div class="col-md-8 auth" style="text-align: left">
              <span>请填写该卡在银行预留的手机号码，验证该银行卡是否真实属于您本人 </span>
            </div>
          </div>
          <!--<div class="row name">-->
            <!--<div class="col-md-2 xingming" style="text-align: right">短信验证码:</div>-->
            <!--<div class="col-md-1 zhenshi"><input type="text" class="nd" name="name" id="name" v-model="verification_code"></div>-->
            <!--<div class="col-md-9 auth" style="text-align: left">-->
              <!--<span class="code">获取验证码</span>-->
              <!--<span class="blu">没有收到短信?</span>-->
              <!--<span class="error" style="color: red">请输入验证码</span>-->
            <!--</div>-->
          <!--</div>-->
          <div class="row name">
            <div class="col-md-2 xingming"></div>

          </div>
          <div class="row name">
            <button class="btn btn-default" type="submit" @click="Real">提交</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: "realname",
    data() {
      return {
        name: '',
        type: '',
        num: '',
        banknumber: '',
        tel: '',
        verification_code:''
      }
    },
    methods: {
      Real: function () {
        var vm = this;
        var data = {
          "name": this.name,
          "type": this.type,
          "num": this.num,
          "banknumber": this.banknumber,
          "tel": this.tel,
          "user_id": sessionStorage.getItem("id"),
        }
        console.log(data)
        if(this.name && this.type && this.num && this.banknumber && this.tel){
          axios.post('http://127.0.0.1:8000/user/realname/', data)
            .then(function (res) {
              if (res.data.code === 200) {
                alert("成功")
                // window.location.reload()
              } else {
                alert("error")
              }
            })
        }else{
          alert("有内容为空")
        }


      },


    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .modifytel {
    width: 100%;
  }

  .modifytel > header {
    font-size: 1.8em;
    font-weight: 400;
  }

  .modifytel .line {
    margin-top: 20px;
    border: 2px solid #c5c5c5;
    border-top-left-radius: 2px;
    border-top-right-radius: 2px;
  }

  @media (min-width: 997px) {
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
      margin-top: 20px;
      height: 200px;
      /*border: 1px solid red;*/
    }

    .contents .content-old div {
      margin-top: 10px;
      /*background-color: chartreuse;*/
    }

    .zhenshi input {
      height: 32px;
      line-height: 32px;
      margin-top: -8px;
      /*width: 110px;*/
      border: 1px solid #e6e6e6;
      font-size: 14px;
      vertical-align: middle;
      color: #5e5e5e;
    }

    /*.name .auth .extra{*/
    /*color: #ff5256;*/
    /*font-size: 12px;*/
    /*padding-left: 10px;*/
    /*}*/
    .zhenshi .nd {
      width: 90px;
    }

    .auth .error {
      color: red;
      font-size: 12px;
    }

    .blu {
      font-size: 12px;
      color: #5b9fe2;

    }

    .name .dropdown {
      width: 100px;
      /*background-color: #EEEEEE;*/
    }

    .auth .code {
      display: inline-block;
      height: 32px;
      line-height: 32px;
      margin-top: -8px;
      text-align: center;
      border: 1px solid #e6e6e6;
      background: #f5f5f5;
      vertical-align: middle;
      color: #5e5e5e;
      /*margin-left: 1px;*/
      padding: 0 8px;
    }
  }
  .leixing{
    height: 35px;
    width: 90px;
  }
  .zjleixing{
    line-height: 30px;
  }

</style>
