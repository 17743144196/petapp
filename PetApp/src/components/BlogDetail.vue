<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-md-8 left" v-for="i in list" id="i.id" :key="i.id">
          <div class="row left-top">
            <div class="lph-list">
              <div class=" col-md-1 lph-list-img">
                <img alt="" :src="i.user__photo" width="46px" height="46px">
              </div>
              <div class=" col-md-11 lph-list-text">
                <div v-text="i.user__name"></div>
                <div>
                  <span>发布于</span>
                  <span v-text="i.date"></span>
                  <span class="pp"><img src="../assets/images/smalleye.svg" alt=""></span>
                  <span class="pp" v-text="i.lookers"></span>
                  <span class="pp"><img src="../assets/images/pinglun.png" alt=""></span>
                  <span class="pp">200</span>
                  <span class="zan"><img src="../assets/images/zan.png" alt=""></span>
                  <span v-text="i.zan"></span>
                </div>
              </div>
            </div>
          </div>
          <div class="row left-zhongjian">
            <div>
              <div class="left-b-t" v-text="i.title"></div>
              <div class="left-b-iph">
                <img :src="i.picture" alt="">
              </div>
              <div class="information">
                <div>
                  <span>联系人:</span>
                  <span v-text="i.contact"></span>
                </div>
                <div>
                  <span>手机号:</span>
                  <span v-text="i.phone"></span>
                </div>
                <div>
                  <span>微信号:</span>
                  <span v-text="i.weixin"></span>
                </div>
                <div>
                  <span>丢失地址:</span>
                  <span v-text="i.address"></span>
                </div>
                <div></div>
                <div></div>
              </div>
            </div>
          </div>
          <div class="row left-bottom">
            <div>
              <textarea class="tt" id="comment" name="comment" placeholder="请输入内容" v-model="content"></textarea>
            </div>
            <div>
              <button class="layui-btn layui-btn-sm dd" id="comment-send" @click="comments"> &nbsp;发表&nbsp;</button>
            </div>
            <div class="layui-col-md12 comment-list" v-for="a in arr" id="a.id" :key="a.id">
              <div class="layui-col-md12 comment-item layui-row">
                <div class="comment-item-header">
                  <img :src="a.user__photo" alt="">
                  <div class="header-attribute layui-col-md11 layui-col-xs9 layui-row">
                    <span class="lph-link-color  nickname" v-text="a.user__name"></span>
                    <span class="layui-col-md4 layui-col-xs11 creattime">发布于:</span>
                    <span class="cr" v-text="a.time"></span>
                    <div class="pinglun" style="float: right; margin: 0 0 0 20px;">
                      <img src="../assets/images/plsmall.png" alt="" style="width: 20px; height: 20px">
                      <span>回复</span>
                    </div>
                    <div class="zan" style="float: right; margin: 0 0 0 20px;">
                      <img src="../assets/images/zan.png" alt="" style="width: 20px; height: 20px">
                      <span v-text="a.like"></span>
                    </div>
                  </div>
                </div>
                <p class="layui-col-md11 layui-col-xs12 comment-item-body" v-text="a.content"></p>
              </div>

            </div>


          </div>
        </div>
        <div class="col-md-4 right">
          <article-pet></article-pet>
        </div>
      </div>
    </div>
    <div class="footer"></div>

  </div>

</template>

<script>
  import axios from 'axios'

  export default {
    name: "BlogDetail",
    data() {
      return {
        list: [],
        content: '',
        arr: [],
        isRouterAlive:true

      }

    },
    created: function () {
      this.id = this.$route.params.id
      // this.user_id=this.$route.params.user__id
      console.log(this.id)
    },

    mounted: function () {
      this.getData();
      this.getComments();
    },
    methods: {
      // 循环上面的
      getData: function () {
        var vm = this;
        var a = this.id
        axios.get(' http://127.0.0.1:8000/forum/search/' + a + '/')
          .then(function (response) {
            // console.log(response.data)
            vm.list = response.data
            console.log(vm.list)
          })
          .catch(function (error) {
            // vm.answer = 'Error! Could not reach the API. ' + error
            console.log(error)
          })

      },

      // 评论
      getComments: function () {
        var vm = this;
        // var pet_id=this.id
        axios.get('http://localhost:8000/forum/forumcomment/' + this.id + '/')
          .then(function (response) {
            // console.log(response.data)
            vm.arr = response.data
            console.log(vm.arr)
          })
          .catch(function (error) {
            // vm.answer = 'Error! Could not reach the API. ' + error
            console.log(error)
          })

      },
      // 发表评论传给数据库
      comments: function () {
        var vm = this;
        var user_id;
        var data = {
          "content": this.content,
          "user_id": sessionStorage.getItem("id"),
          "forum_id": this.id,
        }
        console.log(data)
        if(this.content){
          axios.post('http://127.0.0.1:8000/forum/comment/', data)
            .then(function (res) {
              if (res.data.code === 200) {
                alert("发表成功")
                window.location.reload()
              }else{
                alert("请先登录")
              }
            })
        }else {
          alert("输出的内容不能为空")
        }
      },


    }
  }
</script>

<style scoped>

  body, ul, li, a, p {
    margin: 0;
    padding: 0;
  }

  ul, li {
    list-style: none;
  }

  a:link {
    text-decoration: none;
    color: black;
  }

  a:visited {
    color: black;
  }

  .container {
    width: 1170px;
    margin-top: 30px;
  }

  /*left-top start------------------------------------------------------------------------*/

  .container .left .left-top {
    height: 75px;
    width: 780px;
    background-color: #ffffff;
  }

  .lph-list-img {
    /*background-color: #dbff54;*/
    line-height: 75px;

  }

  .left-top .lph-list-text {
    margin-top: 10px;
    padding-left: 25px;
  }

  .lph-list-text div {
    margin-top: 8px;
  }

  .lph-list-text .pp {
    padding-left: 3px;
  }

  .lph-list-text span {
    font-size: 12px;
    color: #979fa8;
  }

  .lph-list-text .zan {
    margin-left: 440px;
    padding-left: 3px;
  }

  /*left-zhongjian start-----------------------------------------------------------------*/
  .container .left .left-zhongjian {
    background-color: #ffffff;
    margin-top: 1px;
  }

  .left-zhongjian .left-b-iph {
    margin-top: 1px;
    margin-bottom: 40px;
    padding-left: 20px;

  }

  .left-zhongjian .left-b-t {
    margin-left: 8px;
    margin-top: 20px;
    padding-left: 20px;
  }

  .left-zhongjian .left-b-iph img, .left-zhongjian .left-b-iph video {
    max-width: 99%;
    background: #fff;
    padding: 8px;
    border-radius: 3px;
  }

  /*left-bottom start---------------------------------------------------------------*/
  .container .left .left-bottom {
    /*width: 780px;*/
    background-color: #ffffff;
    margin-top: 10px;
  }

  .left .left-bottom .tt {
    width: 720px;
    border: solid 1px #e6e6e6;
    min-height: 100px;
    margin-top: 20px;
    margin-left: 20px;
    color: #767676;
    font-size: 1.1em;
    border: none;
    outline: none;
    border: solid 1px #e6e6e6;

  }

  .left .left-bottom .dd {
    margin-left: 690px;
    margin-top: 5px;
    background-color: #009688;
    color: #fff;
    width: 50px;
    line-height: 30px;
    white-space: nowrap;
    text-align: center;
    border: none;
    border-radius: 2px;
    cursor: pointer;
    margin-bottom: 10px;
  }

  .comment-list {
    padding: 0px 20px 20px 20px;
    border-top: 1px solid hsla(212, 9%, 63%, .2);
  }

  .comment-item:first-child {
    border-top: 0px;
  }

  .comment-item-header img {
    float: left;
    height: 49px;
    width: 49px;
    border-radius: 4px;
  }

  .comment-item-header .header-attribute {
    color: #979fa8;
    float: left;
    font-size: 12px;
    line-height: 24px;
  }

  img {
    vertical-align: middle;
    display: inline-block;
  }

  .comment-item-header .header-attribute .nickname {
    font-size: 14px;
    text-decoration: none;
    cursor: pointer;
    margin-left: 5px;
    float: left;
    padding: 5px 0px 10px;
    line-height: 14px;
  }

  .comment-item-header .header-attribute span {
    margin-right: 8px;
  }

  .lph-link-color {
    color: #029789 !important;
  }

  .comment-item-header .header-attribute .creattime {
    font-size: 12px;
    text-decoration: none;
    cursor: pointer;
    margin-left: 5px;
    float: left;
  }

  .comment-list .comment-item-body {
    line-height: 26px;
    font-size: 14px;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    margin-left: 5px;
  }

  .comment-item {
    padding: 15px 0px 5px 0;
    margin-left: 1px;
    border-top: 1px solid hsla(212, 9%, 63%, .2);
  }

  .comment-item-header .cr {
    margin-left: -190px;
  }
  .information{
    margin: -40px 0 20px 30px;
  }
  .information div{
    padding-top: 20px;
  }
</style>
