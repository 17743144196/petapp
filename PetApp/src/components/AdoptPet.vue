<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-md-8 left">
          <div class="row left-top">
            <div class="body-index">
              <div class="index-place">
                <div class="place-md1">
                  位置:
                </div>
                <div class="place-md11">
                  <ul class="city">
                    <li  @click="provinceData" id="1">全部</li>
                    <li v-for="pro in list" :id="pro.pycode" v-text="pro.name" @click="provinceData" v-model.trim="condition"></li>
                  </ul>
                </div>
              </div>
              <div class="index-kind">
                <div class="kind-md1">分类:</div>
                <div class="kind-md11">
                  <ul class="pit">
                    <li href="#" @click="typeData" id="0">全部</li>
                    <li v-for="ty in latr" :id="ty.id" v-text="ty.type" @click="typeData"><a href="#" v-model.trim="type"></a></li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
          <div class="row left-zhong">
            <div class="card-head">
              领养信息
            </div>
          </div>
          <div class="row left-bottom">
            <div>
              <div class="adopt-card" v-for="i in arr" id="i.id" :key="i.id">
                <div class="card-picture">
                  <router-link :to="{name:'AdoptDetail',params:{id:i.id}}">
                    <img :src="i.picone" alt=""
                    >
                    <!--<img alt=""-->
                    <!--src="">-->
                    <div class="uuid layui-hide-md" v-text="i.id"></div>
                  </router-link>
                </div>
                <div class="card-text">
                  <router-link :to="{name:'AdoptDetail',params:{id:i.id}}">
                    <h2 class="text-title" v-text="i.title"></h2>
                  </router-link>
                  <div class="item-attr">
                    <div class="aut">
								        <span>
								            <img :src="i.photo" alt="" width="20" height="20">
                                            <span v-text="i.name"></span>
								        </span>
                    </div>
                    <div class="time" style=" margin: 0 0 0 20px;">
                      <i class="icon-clock"></i>
                      <span v-text="i.date"></span>
                    </div>
                    <div class="tags" style="margin: 0 0 0 20px;">
                      <i class="icon-eye"></i>
                      <span v-text="i.onlooker"></span>
                    </div>
                  </div>
                  <div class="item-desc" v-text="i.introduce"></div>
                </div>
              </div>
            </div>
            <div class="page">
              <paging :asc="alllenght" :currentIndex="pageIndex" @indexclick="getIndex" :count="pagesize" v-show="pagesize>1"></paging>
            </div>
          </div>
        </div>
        <div class="col-md-4 right">
          <article-pet></article-pet>
        </div>
      </div>
    </div>
    <div class="footer">
      <!--<footer-pet></footer-pet>-->
    </div>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: "AdoptPet",
    data () {
      return {
        ImgUrl:'',
        condition: '',
        type:'',
        pageIndex: 1,
        list: [],
        latr:[],
        arr: [],
        more:'',
        pagesize: 1,
        alllenght: 0,
        lengths :""
        // id:''
      }
    },
    mounted: function () {
      this.getProvince();
      this.getType();
      this.getInformation();
      // this.getPageSize();
    },
    methods: {
      getProvince:function(){
        var vm = this
        axios.get('http://localhost:8000/adopt/search/')
          .then(function (response) {
            // console.log(response.data)
            vm.list = response.data
            // vm.imgurl=""+vm.list
            console.log(vm.list)
          })
          .catch(function (error) {
            // vm.answer = 'Error! Could not reach the API. ' + error
            console.log(error)
          })
      },
      getType:function() {
        var vm = this
        axios.get('http://localhost:8000/adopt/pettype/')
          .then(function (response) {
            // console.log(response.data)
            vm.latr = response.data
            // console.log(vm.latr)
          })
          .catch(function (error) {
            // vm.answer = 'Error! Could not reach the API. ' + error
            console.log(error)
          })
      },
      getInformation:function(){
        var vm = this
        var d = vm.type;
        if(d == 0){
          d = ''
        }else{
          d==d
        }
        var vm = this
        var t = vm.condition;
        if(t == 1){
          t = ''
        }else {
          t==t
        }






        // axios.get('http://localhost:8000/adopt/getpets/'+vm.pageIndex+'/')
        axios.get('http://localhost:8000/adopt/getpets/' + vm.pageIndex + '/' + t + '/'+d+'/')
        // axios.get('localhost:8000/adopt/getpets/1///')
          .then(function (response) {
            // console.log(response.data.data)
            vm.arr = response.data.data
            // console.log(response.data.data)
            vm.lengths = response.data.n
            // vm.ImgUrl = 'http://127.0.0.1:8000/media/pic/'+response.data.data[0].photo;
            console.log(vm.ImgUrl)
            vm.getPageSize()
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
      getIndex: function (a) {
        this.pageIndex = a;
        this.getInformation();
        this.getPageSize();

        console.log(this.alllength)
      },
      provinceData:function (event) {
        // var el = event.currentTarget;//复杂的click哈哈
        var el = event.target;//哈哈
        // alert(el.id);
        this.condition=el.id

        // fa = this.target.parentNode;
        var bb = event.target.parentNode;
        var as=bb.querySelectorAll('li');
        for(var a of as){
          a.style.background='white';
          a.style.color='black';

        }
        event.target.style.background='#029789';
        event.target.style.color='white';

        this.pageIndex = 1;
        this.getInformation();
        this.getPageSize();
      },
      typeData:function (event) {
        // var el = event.currentTarget;//复杂的click哈哈
        var el = event.target;//哈哈
        // alert(el.id);
        this.type=el.id

        var bb = event.target.parentNode;
        var as=bb.querySelectorAll('li');
        for(var a of as){
          a.style.background='white';
          a.style.color='black';
        }

        event.target.style.background='#029789';
        event.target.style.color='white';

        console.log(this.condition)
        this.pageindex = 1;
        this.getInformation();
        this.getPageSize();
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
    /*height: 700px;*/
    margin-top: 30px;
  }

  .page{
    background-color: #eeeeee;
  }
  .container .left .left-top {
    width: 780px;
    /*height: 310px;*/
    background-color: #ffffff;
  }
  /*left-top start---------------------------------------------------------------------------*/
  .body-index {
    width: 780px;
    /*height: 313px;*/
    background-color: white;
    padding: 20px;
    box-sizing: border-box;
    border-radius: 0.3%;
  }
  .body-index .index-place {
    width: 100%;
    /*height: 169px;*/
    margin-top: 10px;
    border-bottom: solid 1px #EFF2F7;
    box-sizing: border-box;
    display: flex;
    flex-wrap: wrap;
    /*background-color: #ffbb33;*/
    /*padding-bottom:20px;*/

  }
  .index-place .place-md1, .kind-md1 {
    /*border:solid 1px #EFF2F7 ;*/
    width: 49px;

    /*height: 169px;*/
    font-size: 1.2em;
    /*font-size: small;*/
    color: rgb(102, 102, 102);

  }
  .index-place .place-md11 {
    width: 660px;
    /*height: 168px;*/
    /*padding-bottom: 10px;*/
  }
  .place-md11 .city, .pit {
    display: flex;
    flex-wrap: wrap;

  }

  .place-md11 .city>li:first-child , .pit>li:first-child{
    background-color: #029789;
  }

  .place-md11 .city li, .pit li {
    /*height: 30px;*/
    margin: 0px 5px 13px 9px;
    padding: 0px 15px 2px 15px;
    /*padding: 0px 15px 12px;*/
    font-size: small;
    /*background-color: #bcd8d8;*/
    box-sizing: border-box;
    border-radius: 4%;
    line-height: 30px;
  }
  .place-md11 .city li:hover, .pit li:hover, .page-div a:hover {
     /*background-color: #029789;*/
     cursor: pointer;
   }
  .body-index .index-kind {
    width: 100%;
    /*height: 84px;*/
    margin-top: 10px;
    box-sizing: border-box;
    display: flex;
    flex-wrap: wrap;

  }
  .kind-md11 {
    width: 660px;
    /*height: 84px;*/
    /*padding-bottom: 10px;*/
  }

  .container .left .left-zhong {
    width: 780px;
    /*height: 49px;*/
    background-color: #ffffff;
    margin-top: 20px;

  }
  .container .left .left-bottom {
    width: 780px;
    background-color: #ffffff;
    margin-top: 2px;
  }

  /*left-zhong start---------------------------------------------------------------------------*/
  .left-zhong .card-head {
    /*height: 49px;*/
    width: 780px;
    padding-left: 15px;
    line-height: 49px;
    font-size: 21px;
  }
  /*left-bottom start---------------------------------------------------------------------------*/

  .left-bottom .adopt-card {
    width: 100%;
    /*height: 181px;*/
    box-sizing: border-box;
    padding: 15px;
    border-bottom: solid 1px #D6D6D6;
    display: flex;

  }
  .adopt-card .card-picture {
    max-height: 150px;
    width: 243px;
    /*float: left;*/
    overflow: hidden;
  }
  .adopt-card .card-picture img{
    width: 100%;
  }
  .adopt-card .card-text {
    /*height: 137px;*/
    width: 486px;
    box-sizing: border-box;
    padding: 5px 0px 0px 20px;
    /*background-color: #bcd8d8;*/

  }
  .card-text .text-title {
    width: 100%;
    /*height: 32px;*/
    box-sizing: border-box;
    padding: 0px 10px 10px 10px;
    /*background-color: #393D49;*/
  }
  .card-text .item-attr {
    width: 100%;
    height: 26px;
    padding-top: 15px;
    display: flex;

  }
  .icon-eye, .icon-clock {
    display: block;
    background-image: url("../assets/images/eye.svg");
    width: 18px;
    height: 16px;
    background-position: center center;
    /*z-index: 5;*/
  }
  .card-text .item-attr > div {
    color: #B8B8BC;
    display: flex;
    align-items: center;
    font-size: 13px;
  }
  .icon-clock {
    background-image: url("../assets/images/clock.svg");
  }
  .item-desc {
    font-size: 14px;
    color: #4d4d4d;
    margin-top: 15px;
    line-height: 1.2;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
  }
  .layui-hide-md {
    display: none!important;
  }
</style>
