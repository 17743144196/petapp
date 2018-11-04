<template>
  <footer>
    <div class="first-footer">
      <div class="container row">
        <div class="col-md-5 col-xs-12 footer-menu">

          <div class="col-md-4 col-xs-6 footer-menu-item">
            <p class="footer-menu-head">关于我们</p>
            <ul class="footer-menu-list">
              <li><a href="#">联系我们</a></li>
              <li><a href="#">网站介绍</a></li>
              <li><a href="#">媒体报道</a></li>
              <li><a href="#">宠物案例</a></li>
            </ul>
          </div>
          <div class="col-md-4 col-xs-6 footer-menu-item">
            <p class="footer-menu-head">产品服务</p>
            <ul class="footer-menu-list">
              <li><a href="#">社区</a></li>
              <li><a href="#">开发宝</a></li>
              <li><a href="#">微信公共号</a></li>
              <li><a href="#">微信公共号</a></li>
            </ul>
          </div>
          <div class="col-md-4 col-xs-6 footer-menu-item">
            <p class="footer-menu-head">帮助</p>
            <ul class="footer-menu-list">
              <li><a href="#">如何关注公共号？</a></li>
              <li><a href="#">如何领养宠物？</a></li>
              <li><a href="#">如何送养宠物？</a></li>
              <li><a href="#">查看更多 &gt;</a></li>
            </ul>
          </div>
        </div>
        <div class="col-md-offset-3 col-md-4 col-xs-12 footer-contact">
          <div class="col-md-6 col-xs-12">
            <div class="footer-list-contact">
              <p class="footer-menu-head"><img class="logo" src="../assets/images/dog.png"></p>
              <ul class="footer-menu-list">
                <li><a href="mailto:pet@lazyer.net">pet@lazyer.net</a></li>
                <li>北京 | 上海 | 广州 | 深圳</li>
                <li><a class="wechat" href="index.html"> <span class="fa-stack">  <img
                  src="../assets/images/xiaoweixin.png" height="20" width="20"/></span> </a>
                  <a href="https://weibo.com/u/2660550167" target="_blank"> <span class="fa-stack">  <img
                    src="../assets/images/xiaoweibo.png" height="20" width="20"/></span> </a>
                  <a class="zhihu" href="index.html" target="_blank"> <span class="fa-stack">  <img
                    src="../assets/images/xiaoqq.png" height="20" width="20"/></span> </a></li>
              </ul>
            </div>
          </div>
          <div class="col-md-6 col-xs-12">
            <img alt="" src="../assets/images/qqerweima.png" width="140px">
            <p class="">加入宠物救助交流群</p>
          </div>

        </div>
      </div>
    </div>


    <div class="second-footer">
      <div class="row  container  footer-copyright">
        <div class="col-md-3">
          <a href="#" target="_blank">
            <img src="../assets/images/xiaodog.png" height="20px"></a>
          <span> 小天才科技旗下品牌 · 狗子宠物 </span>
        </div>
        <div class="col-md-3">
          <span> Copyright&nbsp;©&nbsp;2014-2018&nbsp; </span>
          <a href="http://www.lazyer.net/">lazyer.net</a>
        </div>
      </div>
    </div>
    <div class="fork-bar">Fork</div>
  </footer>

</template>

<script>
  export default {
    name: 'Footer',
    data() {
      return{

      }
    }
  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  div, ul, li, p, span, a {
    padding: 0;
  }

  li,p {
    list-style-type: none;
    color: #8796A8;
    font-size: 14px;
  }

  a:link {
    text-decoration: none;
    color: #8796A8;
  }

  a:visited {
    color: #8796A8;
  }
  .first-footer{
   background-color: #273444;;
  }

  footer .first-footer .container {
    padding-top: 50px;
    padding-bottom: 50px;

  }
  .footer-menu-list {
    margin-top: 1.5rem;
  }
  .footer-menu-list li {
    margin-top: 15px;
  }
/*left```end`````````````````````````````````````````````````````*/
  footer .footer-contact {
    text-align: center;
  }
  .col-md-offset-3 {
    margin-left: 25%;
  }
  .footer-menu-head {
    opacity: .9;
    color: #EFF2F7;
    font-size: 16px;
    line-height: 24px;
  }

  .footer-menu-list li a {
    color: #8796A8;
    font-size: 14px;
    margin-top: 12px;
  }
/*最下面```````````````````````````````````````````````````````*/
  footer .second-footer {
    background: #1f2d3d;
    line-height: 40px;
    height: 60px;
  }
  footer{
    margin-top: 30px;
  }
  footer * {
    color: #8796A8;
  }
  footer .footer-copyright {
    text-align: center;
    padding: 10px 0;
  }

  .container {
    margin: auto;
  }
  footer .fork-bar {
    position: fixed;
    bottom: 0;
    left: 0;
    z-index: 999;
    padding: 8px 0;
    width: 100px;
    background-color: #181a29;
    color: #fff;
    transform: translate3d(-28px, -6px, 0) rotate(45deg);
    text-align: center;
  }

</style>
