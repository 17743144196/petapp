<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-md-8 left">
          <div class="left-top">
            <!--<input type="text" class="left-top-ty" placeholder="秀出你的宠物，做一个爱分享的铲屎官">-->
            <textarea class="left-top-ty" id="cot" name="cot" placeholder="秀出你的宠物，做一个爱分享的铲屎官。"
                      v-model="contents"></textarea>
            <div class="letf-top-p">
              <img src="../assets/images/iph.svg" alt="">
              <input class="mypho" type="file" value="" @change="update2" name="usericon">

            </div>
          </div>
          <div class="img-add"></div>
          <div class="left-zhong">
            <span>
              <button class="layui-btn layui-btn-sm left-z-btn" id="com" name="cot" @click="fabu">发布</button>
            </span>
            <span class="left-z-te">
              亲，最多可以上传9张图片
            </span>
          </div>
          <div class="left-bottom">
            <div class="ttop" v-for="i in list" id="i.id" :key="i.id">
              <router-link :to="{name:'ShowDetail',params:{id:i.id}}">
                <div class="left-b-t" v-text="i.contents"></div>
              </router-link>
              <div class="left-b-iph">
                <router-link :to="{name:'ShowDetail',params:{id:i.id}}"><img :src="i.photo" alt="">
                </router-link>
              </div>
              <div class="left-b-m">
                <span v-text="i.user__name"></span>
                <span><img src="../assets/images/clock.svg" alt=""></span>
                <span v-text="i.time"></span>
                <span><img src="../assets/images/se.svg" alt=""></span>
                <span v-text="i.liulan"></span>
                <span><span><img src="../assets/images/message.svg" alt=""></span></span>
                <span v-text="i.pinglun"></span>
              </div>
            </div>
            <div>
              <paging :asc="alllenght" :currentIndex="pageIndex" @indexclick="getIndex" :count="pagesize"></paging>
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
    name: "PetShow",
    data() {
      return {
        users_id: '',
        contents: '',
        photo: "",
        formData: [],
        list: [],
        ImgUrl:'',
        pageIndex: 1,
        pagesize: 1,
        alllenght: 0,
        condition: '',

      }

    },

    mounted: function () {
      this.getComments();
      this.getPageSize();
    },
    methods: {


      update2(e) {  // 上传照片
        var self = this;
        let file = e.target.files[0];
        // console.log(file)
        this.preview1(file);
        // 弹出图片名字
        // alert(file.name);
        /* eslint-disable no-undef */
        let param = new FormData();// 创建form对象
        //usericon通常就是file的name属性值
        param.append('usericon', file, file.name);// 通过append向form对象添加数据
        param.append('chunk', '0'); // 添加form表单中其他数据
        this.formData.push(param);
        console.log(param.get('file')) // FormData私有类对象，访问不到，可以通过get判断值是否传进去
      },
      preview1(file) {
        var img = new Image();
        img.src = URL.createObjectURL(file);
        var url = img.src;
        var $img = $(img);
        $img.css({'width': '175px', 'height': '175px'});
        img.onload = function () {
          URL.revokeObjectURL(url);
          $('.img-add').empty().append($img);
        }
      },

      fabu() {
        // console.log(this.formData);
        var config = {
          headers: {'Content-Type': 'multipart/form-data'},

        };
        // 添加请求头
        let vm = this;
        // let otherSideFlag=false;
        // let PositiveFlag=false;
        axios.post('http://127.0.0.1:8000/adopt/DicLoad/', this.formData[0], {
          headers: {
            'Content-Type': 'application/json',
            token: sessionStorage.getItem("token")
          }
        })
          .then(response => {
            if (response.data.code === 0) {
              vm.ImgUrl = response.data.data;
              // console.log(vm.ImgUrl);
            }
            // console.log(response.data);
            this.photo = response.data.name;
            var data = {
              "photo": this.photo,
              "contents": this.contents,
              "user_id": sessionStorage.getItem("id"),
            }
            console.log(data)


            axios.post('http://127.0.0.1:8000/petshow/FlieName/', data)
              .then(response => {
                this.user_id = sessionStorage.getItem("id")
                console.log(this.user_id)

                if (this.user_id) {
                  if (response.data.code == 808) {
                    alert("添加成功")
                    this.$router.push({
                      path: '/show'
                    })
                  } else {
                    alert("有内容为空")
                  }

                }
                else {
                  alert("请先登录")
                }
              })
          });

      },



      getComments: function () {
        var vm = this;
        axios.get('http://127.0.0.1:8000/petshow/showp/'+vm.pageIndex+'/')
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

      getPageSize: function () {
        var vm = this
        axios.get('http://localhost:8000/petshow/acountpets/' + vm.condition + '/')
          .then(function (response) {
            /*console.log(response.data)*/
            vm.pagesize = Math.ceil(response.data.acount / 10);
            // console.log(response.data)
          })
          .catch(function (error) {
            // vm.answer = 'Error! Could not reach the API. ' + error
            console.log(error)
          })

      },

      getIndex: function (i) {
        this.pageIndex = i;
        this.getComments();

        // getPhoto: function () {
        //   var vm = this;
        //   var b = this.id
        //   axios.get('http://127.0.0.1:8000/petshow/searchphoto/'+ b + '/')
        //     .then(function (response) {
        //       // console.log(response.data)
        //       // vm.list = response.data
        //       vm.ImgUrl = 'http://127.0.0.1:8000/media/pic/'+response.data.url;
        //       console.log(vm.ImgUrl)
        //
        //       console.log(vm.list)
        //     })
        //     .catch(function (error) {
        //       // vm.answer = 'Error! Could not reach the API. ' + error
        //       console.log(error)
        //     })
        //
        // },

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

  /*left-top-------------------------------------------------------------------------*/
  .left .left-top {
    height: 140px;
    width: 765px;
    /*margin-top: 30px;*/
    background-color: #ffffff;
  }

  .left .left-top .left-top-ty {
    height: 140px;
    width: 100%;
    padding: 10px 0 0 10px;
    border: none;
    outline-style: none;
  }

  .left-top .letf-top-p {
    /*background-color: #dbff54;*/
    height: 16px;
    width: 16px;
    position: relative;
    left: 735px;
    top: -30px;
  }

  /*left-zhong----------------------------------------------------------------------------*/
  .left .left-zhong {
    margin-top: 2px;
    margin-bottom: 2px;
    height: 61px;
    width: 760px;
  }

  .left .left-zhong span {
    float: right;
  }

  .left .left-zhong .left-z-te {
    margin-right: 520px;
    line-height: 61px;
    color: #76808e;
  }

  .left .left-zhong .left-z-btn {
    background-color: #009688;
    color: #fff;
    white-space: nowrap;
    text-align: center;
    border: none;
    font-size: 12px;
    border-radius: 2px;
    cursor: pointer;
    width: 60px;
    height: 30px;
    margin-top: 15px;

  }

  /*left-bottom----------------------------------------------------------------------------------*/
  .left .left-bottom {
    width: 765px;
  }

  .left-bottom .ttop {
    margin-top: 10px;
    padding: 10px 0 0 5px;
    background-color: #ffffff;
    /*margin-top: 10px;*/
  }

  .left-bottom .left-b-m span {
    padding: 10px 0 0 5px;
    font-size: 12px;
    color: #979fa8;

  }

  .left-bottom .left-b-iph {
    margin-top: 0;
  }

  .left-bottom .left-b-iph img, .left-bottom .left-b-iph video {
    max-width: 99%;
    box-sizing: border-box;
    background: #fff;
    padding: 8px;
    border: 1px solid #eee;
    border-radius: 3px;
    box-sizing: border-box;
  }
  .img-add{
    width: 100%;
    height: 100%;
    /*background-color: red;*/
  }
  .letf-top-p .mypho{
    margin-left: -30px;
    margin-top: -20px;
    opacity: 0;


  }


</style>
