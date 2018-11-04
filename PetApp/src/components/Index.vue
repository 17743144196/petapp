<template>
  <div class="layui-container layui-row">
    <div class="layui-col-md8 lph-left">
      <div class="layui-col-md12 adopt-index-banner">
        <video autoplay="autoplay"  muted="true"
               src="../assets/images/1477395178197_10556_854x480.mp4"></video>
      </div>
      <div class="layui-card  adopt-index-card layui-col-md12 layui-bg-gray">
        <div class="layui-card-header ">
          <h2>最新领养</h2>
          <span>今日更新<strong class="num">10</strong>篇</span>
        </div>
        <div class="layui-card-body" v-for="i in list" id="i.id" :key="i.id">
          <div class="layui-row  item">
            <div class="layui-col-md4 item-img">
              <router-link :to="{name:'AdoptDetail',params:{id:i.id}}">
                <img :src=i.picone alt="">
              </router-link>
              <div class="uuid layui-hide-md" v-text="i.pet__id"></div>
            </div>
            <div class="layui-col-md8 item-text">
              <router-link :to="{name:'AdoptDetail',params:{id:i.id}}"
                           style="font-size: 16pt">
                <span v-text="i.provid__name"></span><span v-text="i.title"></span>
                <span>-</span>
                <span v-text="i.provid__name"></span><span >宠物领养</span>

              </router-link>

              <div class="item-attr layui-hide-xs">
                <div class="aut" style="float: left; margin: 0;">
									<span>
									  <img :src=i.user__photo alt="" height="20" width="20">
										<span v-text="i.user__name"></span>
									</span>
                </div>
                <div class="time" style="float: left; margin: 0 0 0 20px;">
                  <img src="../assets/images/clock.svg" alt="">
                  <span v-text="i.date"></span>
                </div>
                <div class="tags" style="float: left; margin: 0 0 0 20px;">
                  <img src="../assets/images/eye.svg" alt="">
                  <span v-text="i.onlooker"></span>
                </div>
              </div>
              <div class="item-desc layui-hide-xs" v-text="i.introduce">
              </div>
              <div class="item-attr1 layui-hide-md">
                <div class="layui-col-xs10 time">
                  <span style="">发布于：8小时前</span>
                </div>
                <label class="layui-col-xs2 jump">
                  <a class="right" target="_blank" href="/adopt/12393">查看</a>
                </label>
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>
    <div class="layui-col-md4 lph-right layui-hide-xs">
      <article-pet></article-pet>
    </div>
  </div>


</template>

<script>
  import axios from 'axios';
  export default {
    name: 'Index',
    data: function () {
      return {
        condition: '',
        pageindex: 1,
        list: [],
        pagesize: 0
      }
    },


    mounted: function () {
      this.getData();
      this.getPageSize();
      this.shuaxin();
    },
    methods: {
      getData: function () {
        var vm = this
        axios.get('http://localhost:8000/adopt/adoptpp/'+ vm.pageindex + '/' + vm.condition + '/')
          .then(function (response) {
            vm.list = response.data.name;
            console.log(vm.list)
          })
          .catch(function (error) {
            console.log(error)
          })
      },
      getPageSize: function () {
        var vm = this
        axios.get('http://localhost:8000/adopt/acount/' + vm.condition + '/')
          .then(function (response) {
            vm.pagesize = Math.ceil(response.data.acount / 20);
          })
          .catch(function (error) {
            console.log(error)
          })
      },
      searchData: function () {
        this.pageindex = 1;
        this.getData();
        this.getPageSize();


      },
      getIndex: function (i) {
        this.pageindex = i;
        this.getData();
      },
      created: function () {
        this.msg = this.$route.params.adoptid
      },

      //刷新页面
      shuaxin:function () {
        if(sessionStorage.getItem("renovate") == "true"){
            sessionStorage.setItem("renovate",false)
            location.reload()
        }
      }
    }
  }


</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .adopt-index-banner video {
    width: 100%;
    height: auto;
  }

  video {
    object-fit: contain;
  }

  .adopt-index-card {
    margin-top: 20px;
  }

  .layui-card:last-child {
    margin-bottom: 0;
  }

  .adopt-index-card .layui-card-header {
    height: 37px;
    border-bottom: solid 2px #D6D6D6;
    position: relative;
    line-height: 37px;
    background-color: #fff;
    padding: 5px 15px;
  }

  .adopt-index-card .layui-card-header h2 {
    display: inline-block;
  }

  .adopt-index-card .layui-card-header span {
    float: right;
    font-size: 15px;
    padding-top: 5px;
    color: #666;
  }

  .adopt-index-card .layui-card-header span .num {
    margin: 0 5px;
    color: #4289db;
  }

  .adopt-index-card .layui-card-body {
    padding: 0;
  }

  .adopt-index-card .layui-card-body .item {
    height: auto;
    line-height: 22px;
    border-bottom: 1px dotted #e2e2e2;
    background-color: #fff;
    padding: 15px 15px;
    margin: 0px 0px 0px 0px;
  }

  .adopt-index-card .layui-card-body .item-img {
    overflow: hidden;
    max-height: 150px;
  }

  a {
    color: #333;
    text-decoration: none;
  }

  .adopt-index-card .layui-card-body .item-img img {
    width: 100%;
  }

  .adopt-index-card .layui-card-body .item-img .uuid {
    position: absolute;
    left: 10px;
    top: 10px;
    padding: 3px 5px;
    background: rgba(91, 91, 91, .6);
    color: #fff;
    font-size: 12px;
    border-radius: 2px;
    font-weight: 700;
  }

  .adopt-index-card .layui-card-body .item-text {
    padding-top: 5px;
    padding-left: 20px;
  }

  .adopt-index-card .layui-card-body .item-text .title {
    padding: 0px 10px 10px 10px;
  }

  .adopt-index-card .layui-card-body .item-attr {
    height: 26px;
    line-height: 25px;
    font-size: 13px;
    color: #b8b8b8;
    padding-top: 15px;
  }

  .adopt-index-card .layui-card-body .item-desc {
    font-size: 14px;
    line-height: 1.6;
    margin-top: 15px;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
  }

  .lph-right {
    padding-left: 15px;
  }

  .aside-card-2 {
    margin-bottom: 20px;
    background: #FFFFFF;
    padding: 10px 20px 20px 20px;
  }

  .aside-card-2 .layui-card-header {
    border-bottom: solid 2px #D6D6D6;
    position: relative;
    line-height: 37px;
    padding: 0;
  }

  .aside-card-2 .layui-card-header h3 {
    display: inline-block;
  }

  .aside-card-2 .layui-card-header a {
    float: right;
    font-size: 12px;
    padding-top: 5px;
    color: #9d9d9d;
  }

  .aside-card-2 .layui-card-body {
    padding: 0;
  }

  .aside-card-2 .lph-list {
    height: auto;
    line-height: 22px;
    padding: 10px 0;
    border-bottom: 1px dotted #e2e2e2;
  }

  .aside-card-2 .lph-list-img {
    overflow: hidden;
    max-height: 80px;
  }

  .aside-card-2 .lph-list-text {
    padding-left: 10px;
  }

  .aside-card-2 .lph-list-name {
    font-size: 14px;
    overflow: hidden;
    padding-right: 5px;
  }

  .aside-card-2 .lph-list-title {
    margin-top: 5px;
    color: #888;
    font-size: 12px;
    line-height: 20px;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 1;
    -webkit-box-orient: vertical;
  }

  .aside-card-2 .lph-list-desc {
    margin-top: 5px;
    font-size: 12px;
    line-height: 20px;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    color: #272322;
  }

  .layui-card:last-child {
    margin-bottom: 0;
  }

  .aside-card-1 .layui-card-header {
    border-bottom: solid 2px #D6D6D6;
    position: relative;
    line-height: 37px;
    padding: 0;
  }

  .aside-card-1 .layui-card-header h3 {
    display: inline-block;
  }

  .aside-card-1 .layui-card-header a {
    float: right;
    font-size: 12px;
    padding-top: 5px;
    color: #9d9d9d;
  }

  .aside-card-1 .lph-list {
    height: auto;
    line-height: 22px;
    padding: 10px 0;
    border-bottom: 1px dotted #e2e2e2;
  }

  .aside-card-1 .lph-list-img {
    overflow: hidden;
    max-height: 80px;
  }

  .aside-card-1 .lph-list-img img {
    width: 100%;
  }

  .aside-card-1 .lph-list-text {
    padding-top: 5px;
    padding-left: 20px;
  }

  .aside-card-1 .lph-list-title {
    color: #333333;
    font-size: 14px;
    line-height: 35px;
    height: 35px;
    overflow: hidden;
  }

  .aside-card-1 .lph-list-desc {
    color: #888;
    font-size: 12px;
    line-height: 20px;
    height: 40px;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
  }

</style>
