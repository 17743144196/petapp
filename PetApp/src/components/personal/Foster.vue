<template>
   <div class = "foster">
    <header>寄养记录</header>
    <div class = "line"></div>
    <div class = "container-fluid record">
      <div class = "row">
        <div class = "col-md-12">
        寄养记录每页记录5条，我们将在本页为您每一次寄养宠物类型、寄养时间、结束时间、寄养状态和您对此次寄养的评价。如果需要查看其中一条信息的消息内容
          通过点击该条记录，即可进入该条寄养信息的详情页。
        </div>
      </div>
      <div class = "row navs">
        <div class = "col-md-2 col-sm-2 col-xs-2">寄养宠物名</div>
        <div class = "col-md-2 col-sm-2 col-xs-2">寄养宠物</div>
        <div class = "col-md-2 col-sm-2 col-xs-2">寄养时间</div>
        <div class = "col-md-2 col-sm-2 col-xs-2">结束时间</div>
        <div class = "col-md-2 col-sm-2 col-xs-2">寄养状态</div>
        <div class = "col-md-2 col-sm-2 col-xs-2">评价</div>
      </div>
      <div class = "recordheight">
      <div class = "row rrecord" v-for = "item in d">
        <div class = "col-md-2 col-sm-2 col-xs-2">{{item.name}}</div>
        <div class = "col-md-2 col-sm-2 col-xs-2">{{item.pettype}}</div>
        <div class = "col-md-2 col-sm-2 col-xs-2">{{item.stime}}</div>
        <div class = "col-md-2 col-sm-2 col-xs-2" v-text = "item.etime"></div>
        <div class = "col-md-2 col-sm-2 col-xs-2"  v-bind:data-adoptid="item.adoptid">
          <router-link :to="{name:'Fan',params:{id:item.adoptid}}" v-text = "item.adopttype">
          </router-link>
        </div>
        <div class = "col-md-2 col-sm-2 col-xs-2" >评价</div>
      </div>
      </div>
    </div>
     <div class = "page" v-if = "n.length>1" @click = "fenye">
       <nav aria-label="Page navigation">
         <ul class="pagination">
           <li :data-bb = "0">
             <a href="#" aria-label="Previous">
               &laquo;
             </a>
           </li>
           <li v-for = "i in n" :data-bb = "i">
             <a href="#" v-text="i" ></a>
           </li>
           <li :data-bb = "1000">
             <a href="#" aria-label="Next">
               &raquo;
             </a>
           </li>
         </ul>
       </nav>
     </div>

  </div>
</template>

<script>
export default {
  name: 'PersonalInformation',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      url:"http://127.0.0.1:8000/",
      d:"",//用于获取存放截取的7个数据
      n:"",//用于存放获取到的分页书
      index:1,
      dds:""//用于获取整个数据

    }
  },
  mounted:function () {
    //获取7条记录信息
    var vm = this
    var d = {"id":sessionStorage.getItem("id"),"index":(this.index),"token":sessionStorage.getItem("token")}
    $.ajax({
      url:vm.url + 'personal/getadopt/',
      type:"POST",
      data:JSON.stringify(d),
      contentType:"aoolication/json",
      success:function (res) {
        //如果token过期自动跳转到登录页面
        if(res["code"] == "406"){
          sessionStorage.clear()
          vm.$router.push({path: '/login'})
        }

        //渲染数据
        console.log(res)
        vm.dds = res.slice(0,-1)
        vm.d = res.slice(0,-1)
        vm.d = vm.d.slice(0,7)
        let b = Math.ceil((res[res.length-1]["p"])/7)
        let bb = []
        for(var i = 1 ; i <= b; i++){
          bb.push(i)
        }

        vm.n = bb

      },
      error:function () {
        console.log("寄养获取数据错误")
      }

    })
  },

  methods:{
    fenye:function (e) {
      console.log(e.target.parentNode.dataset["bb"])
      let bs = parseInt(e.target.parentNode.dataset["bb"])
      if(bs != 0 && bs != 1000 ){
        this.index = bs
        this.d = this.dds.slice((bs-1 )*7,bs * 7)
      }else if(bs == 0){
        if(this.index != 1){
            this.index = this.index -1
            this.d = this.dds.slice((this.index-1 )*7,this.index * 7)
        }
      }else if(this.index == 1000){
          if(this.index != (this.n).length){
            this.index = this.index +1
            this.d = this.dds.slice((this.index-1 )*7,this.index * 7)
          }
      }

    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .foster header {
    font-size: 1.8em;
    font-weight: 400;
  }

  .foster .line {
    margin-top: 20px;
    border:2px solid #c5c5c5;
    border-top-left-radius: 2px;
    border-top-right-radius: 2px;
  }

  @media(max-width: 768px){

    .foster header {
      font-size: 1.8em;
      font-weight: 400;
    }

    .foster .line {
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
  /*foster-record start*/

</style>
