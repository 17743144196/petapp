<template>
  <div class="zzc">
    <div class="bd">
      <form class="form-horizontal">
        <div class="form-group ">
          <label for="inputEmail3" class="col-sm-3 control-label">姓名:</label>
          <div class="col-sm-9">
            <input type="name" class="form-control" id="inputEmail3" placeholder="Name" v-model="name">
          </div>
        </div>
        <div class="form-group ">
          <label for="inputPassword3" class="col-sm-3 control-label">手机号:</label>
          <div class="col-sm-9">
            <input type="telephone" class="form-control" id="inputPassword3" placeholder="Telephone" v-model="telephone">
          </div>
        </div>
        <div class="form-group ">
          <label for="inputPassword3" class="col-sm-3 control-label">领养原因:</label>
          <div class="col-sm-9">
            <textarea class="form-control" rows="4" v-model="causes"></textarea>
          </div>
        </div>
        <div class="form-group">
          <div class=" col-md-6 form-group">
            <div class="col-sm-offset-9 col-sm-3">
              <button type="submit" class="btn btn-default" @click="tijiao">提交</button>
            </div>
          </div>
          <div class=" col-md-6 form-group">
            <div class="col-sm-offset-8 col-sm-4">
              <button type="submit" class="btn btn-default" @click="toExit">退出</button>
            </div>
          </div>
        </div>
      </form>
    </div>

  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    props:['ll'],
    name: "Kuang",
    data() {
      return {
        name:'',
        telephone:'',
        causes:'',
        user_id:'',
        pet_id:''

      }
    },
    // created:function () {
    //   this.user_id=this.$route.params.user__id
    //   console.log(id)
    // },
    methods: {
      // 关闭模态框
      toExit: function () {
        this.$emit('adoptclick')
      },
      closeMyself: function () {
        this.status = ''
        this.$emit('on-close')
      },
      tijiao:function () {
        let vm = this
        // this.adopt_user_id=el.i
        var data={
          "name":this.name,
          "telephone":this.telephone,
          "causes":this.causes,
          "user_id":sessionStorage.getItem("id"),
          "pet_id":this.ll
        }
        console.log(data)
        // alert(data)
        if(this.name && this.telephone && this.causes){
          axios.post("http://127.0.0.1:8000/lingyang/xinxi/",data)
            .then(function(res){
              if(res.data.code==200){
                // alert("成功")
                // vm.$router.push({path:"/xinxi"})
                vm.$emit('adoptclick')
                alert("提交成功")

              }else{
                // vm.contents = "错误";
                alert("提交失败")

              }
            })
            .catch(function (error) {

              console.log(2)
            })
        }else{
          alert("有内容为空")
        }


      }
    },


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

  .zzc {
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.6);
    position: fixed;
    z-index: 999;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
  }

  a:visited {
    color: black;
  }

  .bd {
    width: 30%;
    margin: auto;
    padding-top: 20px;
    padding-right: 30px;
    /*background-image: url("../assets/images/u=4276688522,3150880084&fm=200&gp=0.jpg");*/
    /*background-repeat: repeat;*/
    /*background-position: center;*/
    position: absolute;
    /*left: 50%;*/
    transform: translate(120%, 80%);
    border-radius: 20px;
    border: solid 1px black;
    background-color: #9fcdff;
  }
  .zzc {
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.6);
    position: fixed;
    z-index: 999;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
  }


</style>
