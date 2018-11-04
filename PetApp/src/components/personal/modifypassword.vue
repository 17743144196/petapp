<template>
  <div class="modifypwd">
    <header>安全设置</header>
    <div class = "line"></div>
    <div class = "contents">
      <div>
        <div class = "contents-line"></div>
        <div class = "modifytel">修改绑定手机号</div>
        <div class = "content-old">
              <input type="text" placeholder="请输入您的旧手机号"><br>
              <input class="btn btn-default" type="submit" value="确定" @click = "verification">
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
      msg: 'Welcome to Your Vue.js App'
    }
  },

  methods : {
    verification : function(){
      alert("123")
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  .modifypwd {
    width: 100%;
  }

  .modifypwd>header {
    font-size: 1.8em;
    font-weight: 400;
  }

  .modifypwd .line {
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

  .contents .modifytel {
    font-size: 1.5em;
    position: relative;
    top: -15px;
    width: 160px;
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

  .contents .content-old>input:first-child {
    width: 30%;
    height: 40px;
    border: 1px solid #9AA0A7;
    border-radius: 3px;
    text-align: center;
  }

  .contents .content-old .btn {
    margin-top: 20px;
    width: 10%;
  }

}

</style>
