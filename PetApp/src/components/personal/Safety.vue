<template>
<div class = "security-center">
  <header>安全设置</header>
  <div class = "line"></div>
  <div class = "container-fluid">
      <div class = 'row head'>
        <div class = "col-md-12  safety-grade">
          <span>安全级别:</span>
          <div class = "gradecolor"></div>
          <div class = ""></div>
          <div class = ""></div>
          <span class = "grade">初级</span>
          <span>建议您启动全部安全设置，以保障账户及资金安全。</span>
        </div>
      </div>
      <div class = "row safe-item">
        <div class = "col-md-3 col-sm-4 col-xs-4 fore1">
          <div class = "leftimg"></div>
          <span>登入密码</span>
        </div>
        <div class = "col-md-7 col-sm-6 col-xs-6 fontcolor">
          互联网账号存在被盗风险，建议您定期更改密码以保护账户安全。
        </div>
        <div class = "col-md-2 col-sm-2 col-xs-2">
          <router-link to="/modifytel">修改</router-link>
        </div>
      </div>
      <div class = "row safe-item">
      <div class = "col-md-3 col-sm-4 col-xs-4 fore1">
        <div class = "leftimg"></div>
        <span>绑定手机</span>
      </div>
      <div class = "col-md-7 col-sm-6 col-xs-6 fontcolor">
        <p>
        您验证的手机：
        <!--<span>您验证的手机：</span>-->
        <!--<div>-->
          <span>139</span>
          <span>*****</span>
          <span>780</span>
          <span>&nbsp;</span>
        <!--</div>-->
        若已丢失或停用，请立即更换，避免账户被盗
        <!--<span>若已丢失或停用，请立即更换，避免账户被盗</span>-->
        </p>
      </div>
      <div class = "col-md-2 col-sm-2 col-xs-2">
        <router-link to="/modifypwd">修改</router-link>
      </div>
    </div>
      <div class = "row safe-item">
      <div class = "col-md-3 col-sm-4 col-xs-4 fore1">
        <div class = "leftimg"></div>
        <span>绑定邮箱</span>
      </div>
      <div class = "col-md-7 col-sm-6 col-xs-6 fontcolor">
        验证后，可用于快速找回登录密码，接受各种提示信息。
      </div>
      <div class = "col-md-2 col-sm-2 col-xs-2">
        <router-link to="/modifyemail">修改</router-link>
      </div>
    </div>
      <div class = "row safe-item">
      <div class = "col-md-3 col-sm-4 col-xs-4 fore1">
        <div class = "leftimg"></div>
        <span>支付密码</span>
      </div>
      <div class = "col-md-7 col-sm-6 col-xs-6 fontcolor">
        实名认证后您可以开启支付密码，保障虚拟资产安全。
      </div>
      <div class = "col-md-2 col-sm-2 col-xs-2">
        <a href="#" class = "buttonstyle">立即验证</a>
      </div>
    </div>
      <div class = "row safe-item">
      <div class = "col-md-3 col-sm-4 col-xs-4 fore1">
        <div class = "leftimg"></div>
        <span>实名验证</span>
      </div>
      <div class = "col-md-7 col-sm-6 col-xs-6 fontcolor">
        认证后，可通过实名信息找回支付密码，修改手机号等，提高账户安全性
      </div>
      <div class = "col-md-2 col-sm-2 col-xs-2">
        <router-link to="/realname">通过</router-link>
      </div>
    </div>

  </div>
</div>
</template>

<script>
export default {
  name: 'Safety',
  data () {
    return {
      msg: 'safety'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
 .security-center {
    width: 100%;
  }

  .security-center header {
    font-size: 1.8em;
    font-weight: 400;
  }

  .security-center .line {
    margin-top: 20px;
    border:2px solid #c5c5c5;
    border-top-left-radius: 2px;
    border-top-right-radius: 2px;
  }

  .security-center .container-fluid {
    width: 100%;
    background-color: white;
    padding: 10px 0 20px 0;
    border-bottom-left-radius: 2px;
    border-bottom-right-radius: 2px;
  }

  /*.security-center .container>.row {*/
    /*margin: 40px 0;*/
    /*padding: 0 20px;*/
  /*}*/

 .security-center .container-fluid .row {
   margin: 0;
 }


  .security-center .safety-grade {
    margin-top: 5px;
    background-color: #FFFDEE;
    display: flex;
    align-items: center;
    /*border-bottom: 1px solid ;*/
  }

 .security-center .safety-grade span:first-child {
   font-weight: 700;
   padding-right: 10px;
 }

 .security-center .safety-grade div {
   width: 30px;
   height: 12px;
   background-color: gainsboro;
 }

 .security-center .safety-grade .grade {
   padding: 0 15px 0 10px;
   color: #FF6C00;
 }

 .security-center .safety-grade .gradecolor {
   background-color: #FF6C00;
 }

 .security-center .safety-grade span:last-child {
   color: #FF6C00;
 }

 .security-center .container-fluid .safe-item {
   padding: 30px 0;
   margin: 0 10px;
   border-bottom: 1px solid #E6E6E6;
 }

 .security-center .container-fluid .fore1 {
   display: flex;
   /*justify-content: center;*/
   align-items: center;
   padding-right: 0;
   border-right: 1px solid #E6E6E6;
 }

 .security-center .safe-item .fore1 .leftimg {
   width: 33px;
   height: 33px;
   margin-right: 20px;
   margin-left: 10px;

   background:url("../../assets/images/icon-msg2013.png") no-repeat 0 0;
 }

 .security-center .safe-item .fore1 span {
   font-size: 1.5em;
   font-weight: bold;
 }

 .security-center .safe-item  .fontcolor {
   /*height: 33px;*/
   line-height: 33px;
   display: flex;
   font-size: 0.8em;
 }

 .security-center .safe-item  .fontcolor>div {
   padding: 0;
 }



 .security-center .safe-item>div:last-child .buttonstyle {
   display: block;
   line-height: 33px;
   text-decoration: none;
 }


  @media(max-width: 768px){

    .security-center .container-fluid {
      background-color: rgba(255, 255, 255, 1);
    }
    .security-center .safety-grade {
      margin-top: 5px;
      font-size: 0.5em;
      background-color: #FFFDEE;
      display: flex;
      align-items: center;
      /*border-bottom: 1px solid ;*/
    }

    .security-center .safety-grade span:first-child {
      font-weight: 700;
      padding-right: 10px;
      font-size: 0.8em;
    }

    .security-center .safety-grade div {
      width: 20px;
      height: 12px;
      background-color: gainsboro;
    }

    .security-center .safety-grade .grade {
      padding: 0 15px 0 10px;
      color: #FF6C00;
    }

    .security-center .safety-grade .gradecolor {
      background-color: #FF6C00;
    }

    .security-center .safety-grade span:last-child {
      color: #FF6C00;
    }


    .security-center .container-fluid .safe-item {
      padding: 20px 0;
      margin: 0 10px;
      border-bottom: 1px solid #E6E6E6;
    }

    .security-center .safe-item .fore1 span {
      font-size: 1.3em;
      font-weight: bold;
    }


    .security-center .safe-item  .fontcolor {
      /*height: 33px;*/
      line-height: 16px;
      display: flex;
      font-size: 0.8em;
    }

    .security-center .safe-item>div:last-child .buttonstyle {
      display: block;
      line-height: 33px;
      font-size: 0.8em;
      text-decoration: none;
    }

    .security-center .safe-item .fore1 .leftimg {
      width: 33px;
      height: 33px;
      margin-right: 10px;
      margin-left: 5px;
      background:url("../../assets/images/gantanhao.png") no-repeat 0 5px ;
    }

  }

  @media (min-width: 768px) {

    .security-center .safety-grade {
      margin-top: 5px;
      font-size: 0.8em;
      background-color: #FFFDEE;
      display: flex;
      align-items: center;
      /*border-bottom: 1px solid ;*/
    }

    .security-center .safety-grade span:first-child {
      font-weight: 700;
      padding-right: 10px;
      font-size: 0.8em;
    }

    .security-center .safety-grade div {
      width: 20px;
      height: 12px;
      background-color: gainsboro;
    }

    .security-center .safety-grade .grade {
      padding: 0 15px 0 10px;
      color: #FF6C00;
    }

    .security-center .safety-grade .gradecolor {
      background-color: #FF6C00;
    }

    .security-center .safety-grade span:last-child {
      color: #FF6C00;
    }


    .security-center .container-fluid .safe-item {
      padding: 20px 0;
      margin: 0 10px;
      border-bottom: 1px solid #E6E6E6;
    }

    .security-center .safe-item .fore1 span {
      font-size: 1.3em;
      font-weight: bold;
    }


    .security-center .safe-item  .fontcolor {
      /*height: 33px;*/
      line-height: 16px;
      display: flex;
      font-size: 0.8em;
    }

    .security-center .safe-item>div:last-child .buttonstyle {
      display: block;
      line-height: 33px;
      font-size: 0.8em;
      text-decoration: none;
    }
  }

  @media (min-width: 992px) {

    .security-center .safe-item>div:last-child .buttonstyle {
      display: block;
      line-height: 33px;
      font-size: 1em;
      text-decoration: none;
    }

    .security-center .container-fluid .safe-item {
      padding: 30px 0;
      margin: 0 10px;
      border-bottom: 1px solid #E6E6E6;
    }

    .security-center .safe-item .fore1 span {
      font-size: 1.5em;
      font-weight: bold;
    }


    .security-center .safe-item  .fontcolor {
      /*height: 33px;*/
      line-height: 33px;
      display: flex;
      font-size: 0.8em;
    }

  }
</style>
