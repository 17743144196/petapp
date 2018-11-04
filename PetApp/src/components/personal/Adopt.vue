<template>
  <div class = "adopt">
    <header>领养记录</header>
    <div class = "line"></div>
    <div class = "container-fluid record">
      <div class = "row">
        <div class = "col-md-12">
          寄养记录每页记录5条，我们将在本页为您每一次寄养宠物类型、寄养时间、结束时间、寄养状态和您对此次寄养的评价。如果需要查看其中一条信息的消息内容
          通过点击该条记录，即可进入该条寄养信息的详情页。
        </div>
      </div>
      <div class = "row navs" >
        <div class = "col-md-2 col-sm-2 col-xs-2" >寄养人</div>
        <div class = "col-md-2 col-sm-2 col-xs-2" >宠物名</div>
        <div class = "col-md-2 col-sm-2 col-xs-2" >宠物类型</div>
        <div class = "col-md-2 col-sm-2 col-xs-2" >开始时间</div>
        <div class = "col-md-2 col-sm-2 col-xs-2" >结束时间</div>
        <div class = "col-md-2 col-sm-2 col-xs-2" >状态</div>
      </div>
      <div class = "recordheight" >
        <div class = "row rrecord" id = "002" v-for="i in list">
          <div class = "col-md-2 col-sm-2 col-xs-2" v-text="i.name"></div>
          <div class = "col-md-2 col-sm-2 col-xs-2" v-text="i.contact"></div>
          <div class = "col-md-2 col-sm-2 col-xs-2" v-text="i.type"></div>
          <div class = "col-md-2 col-sm-2 col-xs-2" v-text="i.stat_time"></div>
          <div class = "col-md-2 col-sm-2 col-xs-2" v-text="i.end_time"></div>
          <div class = "col-md-2 col-sm-2 col-xs-2" v-text="i.state"></div>
        </div>

      </div>
    </div>
    <div class = "page">
      <nav aria-label="Page navigation">
        <ul class="pagination">
          <li>
            <a href="#" aria-label="Previous">
              <span aria-hidden="true">&laquo;</span>
            </a>
          </li>
          <li><a href="#">1</a></li>
          <li><a href="#">2</a></li>
          <li><a href="#">3</a></li>
          <li><a href="#">4</a></li>
          <li><a href="#">5</a></li>
          <li>
            <a href="#" aria-label="Next">
              <span aria-hidden="true">&raquo;</span>
            </a>
          </li>
        </ul>
      </nav>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';
export default {
  name: 'PersonalInformation',
  data () {
    return {
      condition: '',
      pageindex: 1,
      list: [],
      pagesize: 0,
      user:"",
      d:"",//用于获取存放截取的7个数据

    }
  },
  mounted: function () {
    this.getData();
  },
  methods:{
    getData: function () {
      var vm = this
      this.user_id={"id":sessionStorage.getItem("id")}

      axios.post('http://localhost:8000/personal/getpets/',this.user_id)
        .then(function (response) {
          console.log(response.data)
          vm.list = response.data
        })
        .catch(function (error) {
          console.log(error)
        })
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .adopt header {
    font-size: 1.8em;
    font-weight: 400;
  }

  .adopt .line {
    margin-top: 20px;
    border:2px solid #c5c5c5;
    border-top-left-radius: 2px;
    border-top-right-radius: 2px;
  }

  /*.adopt header {*/

  @media(max-width: 768px){

    .adopt header {
      font-size: 1.8em;
      font-weight: 400;
    }

    .adopt .line {
      margin-top: 18px;
      border:2px solid #c5c5c5;
      border-top-left-radius: 2px;
      border-top-right-radius: 2px;
    }
    /*foster-record start*/
    .record {
      background-color: white;
      padding: 10px 20px 15px;
    }

    .record > .row:first-child > div:first-child {
      width: 80%;
      font-size: 12px;
      font-weight: 300;
      padding: 10px 0 20px;
    }

    .record .navs {
      background-color: #F5F5F5;
      padding: 5px 0;
      text-align: center;
    }


    .record .rrecord {
      padding: 10px 0;
      font-size: 5px;
      text-align: center;
    }

    .record .rrecord:hover {
      background-color: gainsboro;
      cursor: pointer;
    }

    .recordheight {
      height: 200px;
    }

    .page {
      text-align: center;
      background-color: white;
      border-bottom-right-radius: 3px;
      border-bottom-left-radius: 3px;
    }
  }

  @media(min-width: 768px){
    /*foster-record start*/
    .record {
      background-color: white;
      padding: 10px 20px 50px;
    }

    .record > .row:first-child > div:first-child {
      width: 80%;
      font-size: 12px;
      font-weight: 300;
      padding: 10px 0 20px;
    }

    .record .navs {
      background-color: #F5F5F5;
      padding: 5px 0;
      text-align: center;
    }


    .record .rrecord {
      padding: 10px 0;
      text-align: center;
    }

    .record .rrecord:hover {
      background-color: gainsboro;
      cursor: pointer;
    }

    .recordheight {
      height: 200px;
    }

    .page {
      text-align: center;
      background-color: white;
      border-bottom-right-radius: 3px;
      border-bottom-left-radius: 3px;
    }
  }

  @media(min-width: 992px) {

    /*foster-record start*/
    .record {
      background-color: white;
      padding: 10px 20px 50px;
    }

    .record > .row:first-child > div:first-child {
      width: 80%;
      font-size: 12px;
      font-weight: 300;
      padding: 10px 0 20px;
    }

    .record .navs {
      background-color: #F5F5F5;
      padding: 5px 0;
      font-size: 12px;
      text-align: center;
    }


    .record .rrecord {
      padding: 10px 0;
      text-align: center;
    }

    .record .rrecord:hover {
      background-color: gainsboro;
      cursor: pointer;
    }

    .recordheight {
      height: 200px;
    }

    .page {
      text-align: center;
      background-color: white;
      border-bottom-right-radius: 3px;
      border-bottom-left-radius: 3px;
    }

  }


</style>
