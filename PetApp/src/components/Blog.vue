<template>
  <div class="layui-container layui-row">
    <div class="layui-col-md8 lph-left">
      <div class="layui-card blog-index-card layui-col-md12">
        <div class="layui-card-header card-header-first">
          <div class="card-header-attribute layui-row" @click="typefc">
            <a href="#">全部文章</a>
            <span v-for="a in list" i="a.id" :key="a.id"  >
              <a href="#" v-text="a.type" v-model.trim="type" :id = "a.id"></a>
            </span>
          </div>
        </div>
        <div class="layui-card-header card-header-second layui-row">
          <a class="lph-link-color" href="javascript:void(0)">最新主题</a>
          <a href="javascript:void(0)" id="like">推荐</a>
          <span style="float: right">
					<button class="layui-btn layui-btn-sm" id="blog-create">发布主题</button>
				</span>
        </div>
        <div class="layui-card-body card-body">
          <div class="layui-row  card-body-item">
            <div class="layui-col-md7 card-body-title">
              <span class="layui-badge layui-bg-orange">置顶</span>
              <!--<p>宠物领养协议(合同)模版下载</p>-->
              <router-link :to="{ path: '/template'}">
              <p>宠物领养协议(合同)模版下载</p>
              </router-link>
            </div>
            <div class="layui-col-md5 card-body-attribute">
              <span class="username">admin</span>
              <span class="datetime">2018-02-28</span>
              <span class="count">
							<span><img src="../assets/images/eye.svg" alt=""></span>
              <span class="num-SHda6">332</span>
              <span><img src="../assets/images/pinglun.png" alt=""></span>
              <span class="num-SHda6">3</span>
              </span>
            </div>
          </div>
          <span v-for="i in arr" id="i.id" :key="i.id">
            <div class="layui-row  card-body-item">
            <div class="layui-col-md7 card-body-title">
              <router-link :to="{name:'BlogDetail',params:{id:i.id}}">
                <p class="text-title" v-text="i.title"></p>
              </router-link>
              <!--<a target="_blank" href="/blog/103434" v-text="i.title"></a>-->
            </div>
            <div class="layui-col-md5 card-body-attribute">
              <span class="username" v-text="i.name"></span>
              <span class="datetime" v-text="i.data"></span>
              <span class="count">
							<span><img src="../assets/images/eye.svg" alt=""></span>
              <span class="num-SHda6" v-text="i.zan"></span>
              <span><img src="../assets/images/pinglun.png" alt=""></span>
              <span class="num-SHda6" v-text="i.lookers"></span>
              </span>
            </div>
          </div>
          </span>

        </div>
        <div class="page">
          <paging :asc="alllenght" :currentIndex="pageIndex" :count="pagesize" @indexclick="getIndex" v-show="pagesize>1"></paging>
        </div>

      </div>

    </div>
    <div class="layui-col-md4 lph-right layui-hide-xs" style="padding-left: 15px">
      <article-pet></article-pet>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    name: "Blog",
    data () {
      return {
        condition: '',
        type:'',
        pageIndex: 1,
        list: [],
        arr: [],
        pagesize: "",
        alllenght: 0,
        lengths :"",

      }
    },
    mounted: function () {
      this.forumType();
      this.getInformation();
    },
    methods: {
      forumType: function () {
        var vm = this
        axios.get('http://localhost:8000/forum/forumtype/')
          .then(function (response) {

            vm.list = response.data
            console.log(vm.list)
          })
          .catch(function (error) {
            console.log(error)
          })
      },
      getInformation: function () {
        var vm = this
        axios.get('http://localhost:8000/forum/getforum/' + vm.pageIndex + '/' + vm.type + '/')
          .then(function (response) {
            // console.log(response.data)
            vm.arr = response.data.data
            console.log( vm.arr)
            vm.lengths = response.data.n
            vm.getPageSize()
            // console.log(vm.arr)
          })
          .catch(function (error) {
            // vm.answer = 'Error! Could not reach the API. ' + error
            console.log(error)
          })
      },
      getPageSize: function () {
        // var vm = this
        // vm.alllength = response.data.acount;
        // this.pagesize = Math.ceil(response.data.acount/10);
        this.pagesize = Math.ceil(this.lengths/10);
      },

      //获取点击事件内的标签元素
      typefc:function (e) {
        if(e.target.text == "全部文章"){
          this.type = ""
          var bb = event.target.parentNode
          var as=bb.querySelectorAll('a');
          for(var a of as){
            a.style.background='white';
            a.style.color='black';
          }

          event.target.style.background='#029789';
          event.target.style.color='white';
          this.runs()
          this.runs()
        }else{
          if(e.target.id != ""){
            this.type = e.target.id
            var bb = event.target.parentNode.parentNode;
            var as=bb.querySelectorAll('a');
            for(var a of as){
              a.style.background='white';
              a.style.color='black';
            }

            event.target.style.background='#029789';
            event.target.style.color='white';
            this.runs()
          }

        }

      },

      runs:function(){
        this.pageIndex = 1
        this.getInformation();
      },

      getIndex: function (a) {
        console.log(a)
        this.pageIndex = a;
        this.getInformation();
        }
      },

    // },
    // typeData:function (event) {
    //   // var el = event.currentTarget;//复杂的click哈哈
    //   var el = event.target;//哈哈
    //   // alert(el.id);
    //   this.type=el.id
    //
    //   var bb = event.target.parentNode;
    //   var as=bb.querySelectorAll('li');
    //   for(var a of as){
    //     a.style.background='white';
    //     a.style.color='black';
    //   }
    //
    //   event.target.style.background='#029789';
    //   event.target.style.color='white';
    //
    //   console.log(this.condition)
    //   this.pageindex = 1;
    //   this.getInformation();
    //   this.getPageSize();
    // }

  }
</script>

<style scoped>
  .layui-card:last-child {
    margin-bottom: 0;
  }
  .layui-card {
    border-radius: 2px;
    background-color: #fff;
    box-shadow: 0 1px 2px 0 rgba(0,0,0,.05);
  }
  .blog-index-card .card-header-first {
    padding: 10px 20px;
    height: auto;
  }
  .layui-card-header {
    line-height: 42px;
    border-bottom: 1px solid #f6f6f6;
    color: #333;
    border-radius: 2px 2px 0 0;
    font-size: 14px;
  }
  .blog-index-card .card-header-first .card-header-attribute a {
    padding: 6px 10px;
    margin-right: 5px;
    border-radius: 5px;
    cursor: pointer;
    border: 1px solid transparent;
    transition: all .3s;
    text-decoration: none;
    color: #333;
  }
  .blog-index-card .card-header-second {
    padding: 5px 20px;
    overflow: hidden;
    background: #f0f2f5;
  }
  .blog-index-card .card-header-second {
    padding: 5px 20px;
    padding-top: 5px;
    padding-right: 20px;
    padding-bottom: 5px;
    padding-left: 20px;
    overflow: hidden;
    background: #f0f2f5;
  }
  .blog-index-card .card-header-second {
    padding: 5px 20px;
    padding-top: 5px;
    padding-right: 20px;
    padding-bottom: 5px;
    padding-left: 20px;
    overflow: hidden;
    background: #f0f2f5;
  }
  .layui-card-header {
    height: 42px;
    line-height: 42px;
    padding: 0 15px;
    border-bottom: 1px solid #f6f6f6;
    color: #333;
    border-radius: 2px 2px 0 0;
    font-size: 14px;
  }
  .blog-index-card .card-header-second a {
    padding: 6px 10px;
    margin-right: 5px;
  }
  lph-link-color {
    color: #029789 !important;
  }
  a{
    text-decoration: none;
  }
  .layui-btn-sm {
    height: 30px;
    line-height: 30px;
    padding: 0 10px;
    font-size: 12px;
  }
  .layui-btn {
    display: inline-block;
    height: 38px;
    padding: 0 18px;
    background-color: #009688;
    color: #fff;
    white-space: nowrap;
    text-align: center;
    font-size: 14px;
    border: none;
    border-radius: 2px;
    cursor: pointer;
  }
  .blog-index-card .card-body {
    padding: 0px 15px 10px 15px;
  }
  .blog-index-card .layui-card-body .card-body-item {
    margin-left: 10px;
    border-bottom: 1px solid hsla(212, 9%, 63%, .2);
    padding: 10px 5px 10px 5px;
  }
  .layui-badge {
    height: 18px;
    line-height: 18px;
  }
  .blog-index-card .layui-card-body .card-body-item .card-body-attribute {
    font-size: 12px;
    color: #979fa8;
    text-align: right;
  }
  .blog-index-card .layui-card-body .card-body-item .card-body-attribute span {
    margin: 0px 2px;
  }
  .blog-index-card .layui-card-body .card-body-item .card-body-attribute .count {
    margin-right: 5px;
    /*background: #f0f2f5;*/
    line-height: 5px;
    padding: 0px 5px 0px 5px;
    color: #979fa8;
  }
  .layui-row:after, .layui-row:before {
    content: '';
    display: block;
    clear: both;
  }
  .aside-card-2 .layui-card-header {
    border-bottom: solid 2px #D6D6D6;
    position: relative;
    line-height: 37px;
    padding: 0;
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
  .aside-card-2 .layui-card-header h3 {
    display: inline-block;
  }
  .aside-card-2 .layui-card-header a {
    float: right;
    font-size: 12px;
    padding-top: 5px;
    color: #9d9d9d;
  }
  a{
    text-decoration: none;
  }

  .aside-card-1 .lph-list-img img {
    width: 100%;
  }
  layui-inline, img {
    display: inline-block;
  }

  .lph-link-color {
    color: #029789 !important;
  }
</style>
