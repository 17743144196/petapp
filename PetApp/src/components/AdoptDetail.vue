<template>
  <div>
    <div class="container">
      <div class="row" v-for="a in list" id="a.id" :key="a.id">
        <div class="col-md-8 left">
          <div class="row left-top">
            <div class="headline">
              <div v-text="a.title">
                <!--肇庆麻烦-肇庆宠物领养-->
              </div>
              <div><a href="#" v-text="a.state_type__type"></a></div>
            </div>
            <div class="left-top-t">
              <span class="left-top-num">{{id}}</span>
              <span v-text="a.provid__name"></span>
            </div>
            <div class="introduce">
              <div class="col-md-2">
                类型:<strong style="color: #2D3238;" v-text="a.pet_type__type"></strong></div>
              <div class="col-md-2">
                性别:<strong style="color: #2D3238;" v-text="a.pet_sex__sex"></strong></div>
              <div class="col-md-2">
                免费:<strong style="color: #2D3238;" v-text="a.isFree"></strong>
              </div>
              <div class="col-md-2 money">
                金额:<strong style="color: #2D3238;" v-text="a.price"></strong>
              </div>
              <div class="col-md-4">
                <button @click="myadopt">我要领养</button>

              </div>

            </div>
          </div>
          <div class="row left-zhong">
            <div class="col-md-12 middle">
              <div class="col-md-2">
                <span class="f"><img src="../assets/images/read.png" alt=""></span>
                <span>阅读</span>
                <span v-text="a.onlooker"></span>

              </div>
              <div class="col-md-2">
                <span class="f" @click="zanzan"><img src="../assets/images/zan.png" alt=""></span>
                <span>喜欢</span>
                <span v-text="a.like"></span>
              </div>
              <div class="col-md-2">
                <span class="f"><img src="../assets/images/pinglun.png" alt=""></span>
                <span>评论</span>
                <span v-text="a.com_num"></span>
              </div>
              <div class="col-md-2">
                <span class="f"><img src="../assets/images/fenxiang.png" alt=""></span>
                <span>分享</span>
                <span v-text="a.share"></span>
              </div>
              <div class="col-md-4">
                <!--<span class="adm">意向领养</span>-->
                <!--<span>0</span>-->
              </div>
            </div>
          </div>
          <div class="row left-main">
            <div class="picture">
              <div class="left-pic-pet">宠物相册</div>
              <div><img :src="a.picone" alt=""></div>
              <div><img :src="a.pictwo" alt=""></div>
              <!--<div class="ee"><img :src="a.user" alt=""></div>-->
              <!--<div class="ee"><img :src="a.pic_name" alt=""></div>-->
            </div>
            <div class="require">
              <div class="left-r">宠物介绍</div>
              <p v-text="a.introduce"></p>

            </div>
            <div class="require">
              <div class="left-r">领养要求</div>
              <p v-text="a.yaoqiu"></p>

            </div>
          </div>
          <div class="pet-comment layui-row">
            <div class="layui-col-md12">
              <div class="comment-textarea" style="overflow: hidden;">
                <textarea class="layui-textarea" id="comment" name="comment" placeholder="请输入内容" v-model="content"></textarea>
              </div>
              <div class="comment-button">
                <button class="layui-btn layui-btn-sm " id="comment-send" @click="comments"> &nbsp;发表&nbsp; </button>
              </div>
            </div>
            <div class="layui-col-md12 comment-list" v-for="i in arr" id="i.a" :key="i.a">
              <div class="layui-col-md12 comment-item layui-row">
                <div class="comment-item-header">
                  <img :src="i.user_id__photo" alt="">
                  <div class="header-attribute layui-col-md11 layui-col-xs9 layui-row">
                    <span class="lph-link-color  nickname" v-text="i.user_id__name"></span>
                    <span class="layui-col-md4 layui-col-xs11 creattime">发布于:</span>
                    <span class="cr" v-text="i.time"></span>
                    <div class="pinglun" style="float: right; margin: 0 0 0 20px;">
                      <img src="../assets/images/plsmall.png" alt="" style="width: 20px; height: 20px">
                      <span>回复</span>
                    </div>
                    <div class="zan" style="float: right; margin: 0 0 0 20px;">
                      <img src="../assets/images/zan.png" alt="" style="width: 20px; height: 20px">
                      <span v-text="i.like"></span>
                    </div>
                  </div>
                </div>
                <p class="layui-col-md11 layui-col-xs12 comment-item-body" v-text="i.content"></p>
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
    <Kuang v-if="showexit" :ll=id @adoptclick="myadopt"></Kuang>
  </div>

</template>

<script>
  import axios from 'axios'
  import Kuang from './Kuang'

  export default {
    name: "AdoptPet",
    data() {
      return {
        id:'',
        list:[],
        showexit: false,
        users_id:'',
        arr:[],
        a:'',
        pet_id:'',
        content:'',
        ImgUrl:''

      }

    },
    components: {
      Kuang
    },
    created:function () {
      this.id = this.$route.params.id
      // this.user_id=this.$route.params.user__id
      // console.log(id)
    },
    mounted: function(){
      var vm = this;
      var a=this.id
      console.log(this.id)
      axios.get('http://localhost:8000/adopt/adopts/'+a+'/')
        .then(function (response) {
          console.log(response.data)
          vm.list = response.data
          console.log(vm.list)
          // if(vm.list.state_type__type== 2){
          //   vm.list.state_type__type='已领养'
          // }
          // vm.ImgUrl = 'http://127.0.0.1:8000/media/pic/'+response.data.picone;
          // console.log(vm.ImgUrl)
        })
        .catch(function (error) {
          // vm.answer = 'Error! Could not reach the API. ' + error
          console.log(error)
        })
      this.getComments();
    },

    methods: {
      // 评论
      getComments:function() {
        var vm = this;
        // var pet_id=this.id
        axios.get('http://localhost:8000/adopt/showcomment/' + this.id + '/')
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

      zanzan:function () {
        var vm = this;
        var user_id;

        var data = {
          "user_id": sessionStorage.getItem("id"),
          "pet_id": this.id,
        }
        console.log(data)
        axios.post('http://127.0.0.1:8000/adopt/dianzan/', data)
          .then(function (res) {
            if (res.data.code === 200) {
              alert("成功")
            } else {
              alert("失败")
            }
          })
      },




      comments:function () {
        var vm = this;
        var user_id;

        var data = {

          "content": this.content,
          "user_id": sessionStorage.getItem("id"),
          "pet_id": this.id,
        }
        console.log(data)
        axios.post('http://127.0.0.1:8000/adopt/comment/', data)
          .then(function (res) {
            if (res.data.code === 200) {
              alert("发表成功")
            } else {
              alert("发表失败")
            }
          })
      },



      myadopt: function () {
        // var data={
        //   "users_id":sessionStorage.getItem("id")
        // }
        this.users_id=sessionStorage.getItem("id")
        // console.log(data)
        // alert(data)
        if(this.users_id){
          this.showexit = !this.showexit
          console.log(this.showexit)
          // alert("登录")
        }
        else{
          alert("请先登录")
        }

      }
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
    height: 185px;
    width: 780px;
    background-color: #ffffff;
  }

  .left-top .headline {
    width: 95%;
    margin: auto;
    line-height: 42px;
    margin-top: 30px;
    display: flex;
    justify-content: space-between;
  }

  .left-top .headline div {
    font-size: 2em;
  }

  .left-top .headline a {
    color: #029789;
    font-size: 15px;
  }

  .left-top .left-top-t {
    width: 95%;
    margin: auto;
    line-height: 43px;
  }

  .left-top-t .left-top-num {
    border-radius: 3px;
    background-color: #8796A8;
    color: #fff;
    font-size: 10px;
    padding: 3px 4px;
    margin-right: 6px;
  }

  .introduce div {
    padding-left: 50px;
    border-right: solid 1px #D9D9D9;
    height: 25px;
    margin-top: 20px;
    line-height: 25px;
    text-align: center;
    color: #979FA8;
  }

  .introduce div button {
    margin-left: 70px;
    background-color: #009688;
    color: #fff;
    white-space: nowrap;
    text-align: center;
    border: none;
    border-radius: 2px;
    cursor: pointer;
    height: 30px;
    width: 120px;
    line-height: 30px;
    font-size: 12px;
  }

  .introduce .money {
    border-right: none;
  }

  /*left-zhong start-------------------------------------------------------------------*/
  .left-zhong .middle {
    background-color: #ffffff;
    margin-top: 1px;
  }

  .left-zhong .middle div {
    line-height: 42px;
  }

  .left-zhong .middle span:last-child {
    color: #979FA8;
  }

  .left-zhong .middle .f {
    margin-right: 7px;
  }
  .left-zhong .middle .adm{
    margin-left: 120px;
  }

  /*left-main start--------------------------------------------------------------------------*/
  .container .left .left-main {
    /*height: 1000px;*/
    /*width: 780px;*/
    background-color: #ffffff;
    margin-top: 2px;
  }

  .left-main .picture {
    width: 680px;
    border-top: solid 1px #e6e6e6;
    margin: auto;
    margin-top: 60px;
    position: relative;
  }

  .left-main .picture div {
    max-width: 100%;
    margin-left: 5px;
    margin-top: 30px;
  }

  .left-main .picture .left-pic-pet {
    line-height: 22px;
    background: white;
    position: absolute;
    left: 15px;
    top: -40px;
    text-align: center;
    font-size: 20px;
    font-weight: 300;
    width: 100px;
  }
  .left-main .picture img{
    width: 100%;
  }

  .left-main .require {
    width: 680px;
    border-top: solid 1px #e6e6e6;
    margin: auto;
    height: 100px;
    margin-top: 30px;
    position: relative;
    margin-bottom: 20px;

  }

  .left-main .require p {
    width: 680px;
    margin-top: 40px;
    color: #666;
    font-size: 0.9em;
  }

  .left-main .require .left-r {
    line-height: 22px;
    background: white;
    position: absolute;
    left: 80px;
    top: -10px;
    text-align: center;
    font-size: 20px;
    font-weight: 300;
    width: 100px;
  }

  /*left-bottom start-----------------------------------------------------------------------------*/
  .container .left .left-bottom {
    /*width: 780px;*/
    background-color: #ffffff;
    margin-top: 15px;
  }
  .left .left-bottom .tt{
    width: 720px;
    border:solid 1px #e6e6e6 ;
    min-height: 100px;
    margin-top: 20px;
    margin-left: 20px;
    color: #767676;
    font-size: 1.1em;
    border: none;
    outline: none;
    border:solid 1px #e6e6e6 ;

  }
  .left .left-bottom .dd{
    margin-left: 690px;
    margin-top: 10px;
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


  /*left-bottom start-----------------------------------------------------------------------------*/
  .pet-comment {
    background: #fff;
    height: auto;
    margin-top: 10px;
    width: 104%;
    position: relative;
    left: -15px;
  }
  .pet-comment .comment-textarea {
    padding: 20px 20px 10px;
  }
  .layui-textarea {
    min-height: 100px;
    height: auto;
    line-height: 20px;
    padding: 6px 10px;
    resize: vertical;
  }
  .pet-comment .comment-button {
    padding: 0px 20px 10px;
    overflow: hidden;
  }
  .pet-comment .comment-button button {
    float: right;
  }
  .layui-btn-sm {
    height: 30px;
    line-height: 30px;
    padding: 0 10px;
    font-size: 12px;
  }
  .pet-comment .comment-list {
    padding: 0px 20px 20px 20px;
    border-top: 1px solid hsla(212, 9%, 63%, .2);
  }
  .pet-comment .comment-item:first-child {
    border-top: 0px;
  }
  .pet-comment .comment-item-header img {
    float: left;
    height: 49px;
    width: 49px;
    border-radius: 4px;
  }
  .pet-comment .comment-item-header .header-attribute {
    color: #979fa8;
    float: left;
    font-size: 12px;
    line-height: 24px;
  }
  img{
    vertical-align: middle;
    display: inline-block;
  }
  .pet-comment .comment-item-header .header-attribute .nickname {
    font-size: 14px;
    text-decoration: none;
    cursor: pointer;
    margin-left: 5px;
    float: left;
    padding: 5px 0px 10px;
    line-height: 14px;
  }
  .pet-comment .comment-item-header .header-attribute span {
    margin-right: 8px;
  }
  .lph-link-color {
    color: #029789 !important;
  }
  .pet-comment .comment-item-header .header-attribute .creattime {
    font-size: 12px;
    text-decoration: none;
    cursor: pointer;
    margin-left: 5px;
    float: left;
  }
  .pet-comment .comment-list .comment-item-body {
    line-height: 26px;
    font-size: 14px;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    margin-left: 5px;
  }
  .pet-comment .comment-item {
    padding: 15px 0px 5px 0;
    margin-left: 1px;
    border-top: 1px solid hsla(212, 9%, 63%, .2);
  }
  .comment-item-header .cr{
    margin-left: -190px;
  }

  /*right start-----------------------------------------------------------------------------*/

</style>
