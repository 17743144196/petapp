<template>
  <div style="padding:20px;" id="app">
    <div class="panel panel-primary">
      <div class="panel-heading"><h1>领养者信息</h1></div>
      <table class="table table-bordered table-striped text-center">
        <thead>
        <tr>
          <th>序号</th>
          <th>姓名</th>
          <th>手机号</th>
          <th>地址</th>
          <th class="yy">原因</th>
          <th>操作</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(i,index) in list" :id = "i.id">
          <td>{{index+1}}</td>
          <td v-text="i.name"></td>
          <td v-text="i.telepthone"></td>
          <td v-text="i.address"></td>
          <td v-text="i.reason"></td>
          <td v-if = "!isf"><button type="button" class="btn btn-primary btn-sm" @click = "tongyi(i.id)" >同意</button></td>
          <td v-if = "!isf"><button type="button" class="btn btn-primary btn-sm" @click = "jujue(i.id)" >不同意</button></td>
          <td v-if = "!isf"><button type="button" class="btn btn-primary btn-sm" v-on:click="remove(index,i.id)">删除</button></td>
          <td v-if = "isf" v-text="i.state"></td>
        </tr>

        <!--<tr v-for ="(user,index) in list">-->
          <!--<td>{{index+1}}</td>-->
          <!--<td>{{user.name}}</td>-->
          <!--<td>{{user.age}}</td>-->
          <!--<td>{{user.school}}</td>-->
          <!--<td>{{user.school}}</td>-->
          <!--<td><button type="button" class="btn btn-primary btn-sm">同意</button></td>-->
          <!--<td><button type="button" class="btn btn-primary btn-sm">不同意</button></td>-->
          <!--<td><button type="button" class="btn btn-primary btn-sm" v-on:click="remove(index)">删除</button></td>-->
        <!--</tr>-->


        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'Fan',
    data () {
      return {
        pet_id:'',
        id:'',
        list:[],
        url:"http://127.0.0.1:8000/",
        isf:false,
        content:""

      }
    },

    mounted:function(){
      this.id = this.$route.params.id
      console.log(this.id)
      this.bb()
    },

    methods:{

      //获取申请者者的基本信息
      bb:function() {
        var data = {
          "pet_id": this.id,
        }
        console.log(data)
        var vm = this;

        axios.post(this.url + 'lingyang/showlingyang/',data)
          .then(function (res) {
            if (res.data.code === 201) {

              if(res.data.lingyang_user.length){
                  console.log(res.data.lingyang_user)
                  vm.list = res.data.lingyang_user
                  // console.log(vm.list[0].state == "已领养")
                  if(vm.list[0].state == "已领养" || vm.list[0].state == "被领养"){
                      for(var i=0;i<vm.list.length; i++){
                         if(vm.list[i].state == "已领养"){
                           vm.list[i].state = "同意"
                         }else{
                           vm.list[i].state = "拒绝"
                         }
                      }
                      vm.isf = true
                  }

              }else{
                console.log("没长度")
              }
            } else {
             console.log("失败")
            }
          })
      },

      //删除记录
      remove: function (index,id) {
        console.log(id)
        var d = {"id":id}
        this.list.splice(index, 1)
        var vm = this
        $.ajax({
          url: vm.url + "lingyang/dellingyang/",
          data:JSON.stringify(d),
          contentType:"application/json",
          type:"POST",
          success:function (res) {
            console.log(res)
          },
          error:function () {
            console.log("错误")
          }

        })

      },

      //同意领养
      tongyi:function (num) {
        var d = {"pet_id":this.id,"num":num}
        var vm = this
        $.ajax({
          url: vm.url + "lingyang/confirm/",
          data:JSON.stringify(d),
          contentType:"application/json",
          type:"POST",
          success:function (res) {
            console.log(res)
          },
          error:function () {
            console.log("错误")
          }

        })
      },

      //拒绝领养
      jujue:function (num) {
        var d = {"pet_id":this.id,"num":num}
        var vm = this
        $.ajax({
          url: vm.url + "lingyang/cancel/",
          data:JSON.stringify(d),
          contentType:"application/json",
          type:"POST",
          success:function (res) {
            console.log(res)
          },
          error:function () {
            console.log("错误")
          }

        })
      }



    }

  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
    text-align: center;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  a {
    color: #42b983;
  }
  tr,th{
    text-align:center;
  }
  .yy{
    width: 40%;
  }
</style>
