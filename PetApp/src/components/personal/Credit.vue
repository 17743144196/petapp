<template>
  <div class = "personal">
    <header>账户预览</header>
    <div class = "line"></div>
    <div class = "container">
    <div class = "row">
      <div class = "col-md-3"><img src="../../assets/images/default_avatart.png" alt="#" class = "imgsize"></div>
      <div class = "col-md-9">
        <div class = "row">
          <div class = "col-md-6">
            <span>上次登录时间:</span>
            <span>2018-10-15 21:30:30</span>
          </div>
          <div class = "col-md-6">
            <span>信用等级:</span>
            <span>0</span>
          </div>
        </div>
        <div class = "row">
          <div class = "col-md-6">
            <span>本次登录时间:</span>
            <span>2019-10-15 21:30:30</span>
          </div>
          <div class = "col-md-6">
            <span>访问本网站次数:</span>
            <span>1</span>
          </div>
        </div>
      </div>
    </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PersonalInformation',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .personal {
    width: 100%;
  }

  .personal header {
    font-size: 1.8em;
    font-weight: 400;
  }

  .personal .line {
    margin-top: 20px;
    border:2px solid #c5c5c5;
    border-top-left-radius: 2px;
    border-top-right-radius: 2px;
  }

  .personal .container {
    width: 100%;
    background-color: white;
    padding: 0;
    margin-right: 0;
  }

  .personal .container>.row {
    margin: 40px 0;
    padding: 0 20px;
  }

  .personal .container .row>div:last-child div {
    padding: 0;
    line-height: 75px;
  }

  .personal .imgsize {
    display: block;
    width: 150px;
    height: 150px;
    background-color: #000000;
    border-radius: 50%;
    margin-left: 40px;
  }

  @media (max-width: 768px) {
    .personal .container {
      background-color: rgba(254, 254, 254, 1);
    }

    .personal .imgsize {
      margin: 0 auto
    }

    .personal .container .row>div {
      text-align: center;
    }
  }

  @media (min-width: 768px){
    .personal .imgsize {
      margin: 0 auto
    }

    .personal .container .row>div {
      text-align: center;
    }
  }

</style>
