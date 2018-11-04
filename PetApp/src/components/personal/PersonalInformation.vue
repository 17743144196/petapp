<template>
  <div class="personal">
    <header>个人信息</header>
    <div class="line"></div>
    <div class="container-fluid">
      <div class="row portrait">
        <div class="col-md-2 col-sm-2 col-xs-3">
          头像
        </div>
        <div class="col-md-2 col-sm-2 col-xs-9 peimg">
          <!--<img src="../assets/images/default_avatart.png" alt="">-->
          <!--<div class = "showimg"></div>-->
          <div class="divimg">
            <img src="../../assets/images/default_avatart.png" alt="#" class="userimg" id="nameimg">
          </div>
          <form id="myform">
            <input type="file" name="usericon" id="upload" class="upload" @change="uploads">
          </form>
        </div>
        <div class="col-md-8 col-sm-8 col-xs-12">
          <div class="row">
            <div class="col-md-12 col-sm-12 col-xs-6">
              <button class="cancel" @click="quxiao">取消选着</button>
            </div>
            <div class="col-md-12 col-sm-12 col-xs-6">
              <button class="confirm" @click="confirm">确定选着</button>
            </div>
          </div>
        </div>
      </div>
      <div class="row email">
        <div class="col-md-2">邮箱</div>
        <div class="col-md-10 inputs"><input type="text" placeholder="请绑定邮箱" v-model="email"></div>
      </div>
      <div class="row nickname">
        <div class="col-md-2">昵称</div>
        <div class="col-md-10 inputs"><input type="text" placeholder="请输入昵称" v-model="name"></div>
      </div>
      <div class="row telephone">
        <div class="col-md-2">手机</div>
        <div class="col-md-10 inputs"><input type="text" placeholder="修改手机号，请前往安全设置" v-model="tel"></div>
      </div>
      <div class="row birthday" v-if="!f">
        <div class="col-md-2">生日</div>
        <div class="col-md-10">
          <select name="year" id="year" v-model="years">
            <option v-for="i in y" v-bind:value="i">{{i}}</option>
          </select>

          <select name="month" id="month" v-model="mounth">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
            <option value="6">6</option>
            <option value="7">7</option>
            <option value="8">8</option>
            <option value="9">9</option>
            <option value="10">10</option>
            <option value="11">11</option>
            <option value="12">12</option>
          </select>

          <select name="day" id="day" v-model="day">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
            <option value="6">6</option>
            <option value="7">7</option>
            <option value="8">8</option>
            <option value="9">9</option>
            <option value="10">10</option>
            <option value="11">11</option>
            <option value="12">12</option>
            <option value="13">13</option>
            <option value="14">14</option>
            <option value="15">15</option>
            <option value="16">16</option>
            <option value="17">17</option>
            <option value="18">18</option>
            <option value="19">19</option>
            <option value="20">20</option>
            <option value="21">21</option>
            <option value="22">22</option>
            <option value="23">23</option>
            <option value="24">24</option>
            <option value="25">25</option>
            <option value="26">26</option>
            <option value="27">27</option>
            <option value="28">28</option>
            <option value="29">29</option>
            <option value="30">30</option>
            <option value="31">31</option>
          </select>
        </div>
      </div>
      <div class="row birthday" v-if="f">
        <div class="col-md-2">生日</div>
        <div class="col-md-10">

          <!--显示出生你年 月  日-->
          <input type="text" v-model="years">
          <input type="text" v-model="mounth">
          <input type="text" v-model="day">


        </div>
      </div>
      <div class="row address" v-if="!af">
        <div class="col-md-2">居住地址</div>
        <div class="col-md-10">
          <select name="province" id="province" @change="cityc">
            <option v-for="item in p" v-bind:value="item.addressId">{{item.province}}</option>
          </select>

          <select name="month" id="city" @change="areas">
            <option v-for="item in c" v-bind:value="item.addressId">{{item.city}}</option>
          </select>

          <select name="area" id="area">
            <option v-for="item in a" v-bind:value="item.addressId">{{item.area}}</option>

          </select>
        </div>
      </div>
      <div class="row address" v-if="af">
        <div class="col-md-2">居住地址</div>
        <div class="col-md-10">
          <!--显示居住地-->
          <input type="text" v-model="province">
          <input type="text" v-model="city">
          <input type="text" v-model="area">
        </div>
      </div>
      <div class="row addressdetails">
        <div class="col-md-2">详细地址</div>
        <div class="col-md-10">
          <textarea name="" id="details" cols="50" rows="5" placeholder="请输入你现在固定居住的地址"
                    v-model="addressDiscribe"></textarea>
        </div>
      </div>
      <div class="row tijiao" v-if="!f">
        <div class="col-md-2"></div>
        <div class="col-md-10">
          <button @click="tijiao">提交</button>
          <span>生日日期提交后无法更改，住址信息每6个月可更改一次</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'PersonalInformation',
    data() {
      return {
        name: "", //昵称
        email: "", //邮箱地址
        tel: "", //手机号
        years: "",//年
        mounth: "", //月
        day: "", //日
        f: "flase", //出生日期kai关
        af: "flase", //住址开关
        province: "",//省
        city: "",//市
        area: "", //区或县
        p: "",//用以保存省份循环用
        c: '',//用来存储市信息
        a: "",//用来存储区域信息
        addressDiscribe: "",// 地址的详细描述
        y: [1, 2, 3, 4, 5, 6, 7, 8],//用以输出年份信息
        file: "",
        qw: "",
        imgs: "",
        formData: "",
        url: "http://127.0.0.1:8000/",
        qiniu: require("qiniu-js"),  //添加七牛
        urlimg: "http://ph1v7yp7b.bkt.clouddn.com/",
        telephone: sessionStorage.getItem("tel")
      }
    },

    methods: {
      preview: function (f) {
        let img = new Image()
        img.src = URL.createObjectURL(f)
        let url = img.src
        let $img = $(img)
        img.onload = function () {
          URL.revokeObjectURL(url)

          //由于添加的标签无法绑定以写的css样式，所以在创建img属性的时候要在次给img标签绑定样式
          $img.css('width', '100%').css('height', '100%').css('object-fit', 'cover').css('border-radius', '50%')
          $('.peimg .divimg').empty().append($img)
        }
      },


      //对input type = "file" 设置事件
      uploads: function (e) {
        var file = e.target.files[0];
        this.file = file;
        // console.log(file.name);
        this.preview(file);   //将获取的值传输到preview 函数中
      },

      //上传图片到后台或七牛云
      confirm: function () {
        //将对象转换成FormData数据（二进制数据）
        // var formData = new FormData($( "#myform" )[0]);
        // var vm = this
        // $.ajax({
        //   url: 'http://127.0.0.1:8000/personal/upload/' ,
        //   type: 'POST',
        //   data: formData,
        //   async: false,
        //   cache: false,
        //   contentType: false,
        //   processData: false,
        //   success: function (returndata) {
        //     console.log(returndata);
        //   },
        //   error: function (returndata) {
        //     console.log(returndata);
        //   }
        // });


        //将图片上传到七牛云
        let file = this.file

        if (file) {
          // 上传头像点击确定时执行
          let that = this

          $.ajax({
            url: that.url + 'personal/qiniu/?key=' + file.name,
            success: function (res) {
              var newname = res.filename
              var token = res.token;
              var newfile = new File([file], newname)

              // console.log(newfile.name)

              // 使得ESLint不检查以下代码
              /* eslint-disable */
              let observable


              var config = {
                useCdnDomain: false,
                disableStatisticsReport: true,
                retryCount: 6,
                region: that.qiniu.region.z0
              };

              var putExtra = {
                fname: '',
                params: {},
                mimeType: ['image/png', 'image/jpeg', 'image/gif', 'image/jpg']
              };

              var key = newfile.name
              // 添加上传dom面板
              putExtra.params['x:name'] = key.split('.')[0]
              var subscription

              observable = that.qiniu.upload(file, key, token, putExtra)


              subscription = observable.subscribe({
                next(res) {
                },
                error(err) {
                  alert("error!")
                },
                complete(res) {
                  var data = {
                    "telephone": that.telephone,
                    "imagsname": that.urlimg + newname
                  }

                  $.ajax({
                    url: "http://127.0.0.1:8000/personal/uploadimg/",
                    type: "POST",
                    data: JSON.stringify(data),
                    contentType: "application/json",
                    success: function (res) {
                      alert("上传头像成功")
                    },
                    error: function () {
                      console.log("失败啦")
                    }
                  })
                  console.log(data)

                }
              })
            }
          })
        }
      },

      //取消头像上传
      quxiao: function () {
        console.log(document.querySelector(".divimg"))
        this.file = ""
        document.querySelector(".divimg").querySelector("img").src = this.imgs
      },

      //获取市信息
      cityc: function () {
        var vm = this
        var id = document.querySelector("#province").value
        var d = {"Province": id}
        $.ajax({
          url: "http://127.0.0.1:8000/personal/getCity/",
          type: "POST",
          data: JSON.stringify(d),
          contentType: "appliction/json",
          success: function (res) {
            console.log(res.p)
            vm.c = res.p
          },
          error: function () {
            console.log("错了")
          }
        })

      },

      //获取区域信息
      areas: function () {
        var vm = this
        var id = document.querySelector("#city").value
        var d = {"cityid": id}
        $.ajax({
          url: "http://127.0.0.1:8000/personal/getAare/",
          type: "POST",
          data: JSON.stringify(d),
          contentType: "appliction/json",
          success: function (res) {
            vm.a = res.p
          },
          error: function () {
            console.log("错了")
          }
        })

      },

      //提交信息
      tijiao: function () {
        var d = {
          "telephone": this.telephone,
          "year": this.years,
          "mounth": this.mounth,
          "day": this.day,
          "province": document.querySelector("#province").value,
          "city": document.querySelector("#city").value,
          "area": document.querySelector("#area").value,
          "addressdetails": this.addressDiscribe
        }

        $.ajax({
          url: "http://127.0.0.1:8000/personal/savasd/",
          data: JSON.stringify(d),
          type: 'POST',
          contentType: "appliction.json",
          success: function (res) {
            alert("提交成功");
            location.reload()
          },
          error: function () {
            alert("错误")
          }
        })


      }


    },

    mounted: function () {
      //该ajax用户获取，用户中心初始化的信息
      var d = {"telephone": this.telephone,"token":sessionStorage.getItem("token")}
      var vm = this
      $.ajax({
        url: vm.url + "personal/getInformation/",
        type: "POST",
        data: JSON.stringify(d),
        contentType: "application/json",
        success: function (res) {
          // console.log(res["code"])

          //如果token过期自动跳转到登录页面
          if(res["code"] == "406"){
            sessionStorage.clear()
            vm.$router.push({path: '/login'})
          }
          //获取头像href，并给头像添加云连接
          vm.imgs = res["datas"]["photo"]
          document.querySelector("#nameimg").src = res["datas"]["photo"]

          //给文本添加邮箱
          vm.email = res["datas"]["email"]

          //给文本赋值
          vm.name = res["datas"]["name"]
          vm.tel = res["datas"]["telephone"]

          //填写出生日期
          if (res["datas"]["datetime"]) {
            var time = res["datas"]["datetime"].split("T")[0].split("-")
            vm.years = time[0]
            vm.mounth = time[1]
            vm.day = time[2]

            vm.f = true
          } else {
            vm.f = false
          }

          //填写住址信息
          if (res["datas"]["province"]) {
            vm.province = res["datas"]["city"]
            vm.city = res["datas"]["province"]
            vm.area = res["datas"]["area"]
            vm.addressDiscribe = res["datas"]["addressDiscribe"]
            vm.af = true
          } else {
            vm.af = false
            var t = vm
            $.ajax({
              url: t.url + "personal/getProvince/",
              type: "POST",
              data: "",
              contentType: "application/json",
              success: function (res) {
                t.p = res.p
              },
              error: function () {
                alert("错了")
              }
            })
          }

        },
        error: function () {
          alert("错啦")
        }

      })
    },

    created: function () {
      var p = []
      for (var i = 0; i < 150; i++) {
        p.push(2018 - i)
      }
      this.y = p
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  /*修改input file 的样式*/
  .upload {
    display: block;
    width: 100%;
    height: 100%;
    opacity: 0;
    top: 0px;
    position: absolute;
  }

  .peimg {
    padding: 0px;
    border: 0px;
  }

  .peimg .divimg {
    width: 100%;
    height: 100%;
    border: 1px solid gainsboro;
    border-radius: 50%;
    overflow: hidden;
    /*box-shadow: 1px 1px 1px;*/
  }

  .peimg img {
    display: block;
    height: 100px;
    width: 100px;
    object-fit: cover;
  }



  @media (max-width: 768px) {
    /*presonal start*/
    .personal {
      margin-bottom: 20px;
    }

    .personal header {
      font-size: 1.8em;
      font-weight: 400;
    }

    .personal .line {
      margin-top: 20px;
      border: 2px solid #c5c5c5;
      border-top-left-radius: 2px;
      border-top-right-radius: 2px;
    }

    .personal .container-fluid {
      padding: 50px 15px 20px 30px;
      background-color: white;
      border-bottom-left-radius: 3px;
      border-bottom-right-radius: 3px;
    }

    /*presonal end*/
    /*portrait start*/
    .personal .portrait {
      padding: 20px 0;
    }

    .personal .portrait > div:first-child {
      font-size: 1.3em;
      font-weight: 300;
    }

    .personal .portrait .peimg {
      width: 100px;
      height: 100px;
      border: 1px solid rgba(220, 220, 220, 0);
      border-radius: 3px;
    }

    .personal .portrait > div:last-child {
      padding-left: 30px;
    }

    .personal .portrait > div:last-child div {
      height: 50px;
    }

    .personal .portrait > div:last-child .cancel {
      border: 1px solid gainsboro;
      background-color: white;
      border-radius: 2px;
      font-size: 0.9em;
      padding: 8px;
      margin-top: 10px;
    }

    .personal .portrait > div:last-child .confirm {
      background-color: #029789;
      border-radius: 2px;
      font-size: 0.9em;
      padding: 8px;
      color: white;
      margin-top: 10px;
      border: 0;
    }

    /*portrait end*/
    /*portrait start*/
    .personal .email {
      padding: 20px 0;
    }

    .personal .email > div:first-child {
      margin-top: 6px;
      font-size: 1.3em;
      font-weight: 300;
      padding: 0 15px 0 0px;
    }

    .personal .email .inputs {
      padding: 10px 0 0 0;
    }

    .personal .email .inputs input {
      width: 80%;
      height: 40px;
      border: 1px solid gainsboro;
      border-radius: 3px;
      padding-left: 5px;
    }

    /*portrait end*/
    /*nickname start*/
    .personal .nickname {
      padding: 20px 0;
    }

    .personal .nickname > div:first-child {
      margin-top: 6px;
      font-size: 1.3em;
      font-weight: 300;
      padding: 0 15px 0 0px;
    }

    .personal .nickname .inputs {
      padding: 10px 0 0 0;
    }

    .personal .nickname .inputs input {
      width: 80%;
      height: 40px;
      border: 1px solid gainsboro;
      border-radius: 3px;
      padding-left: 5px;
    }

    /*nickname end*/
    /*telephone start*/
    .personal .telephone {
      padding: 20px 0;
    }

    .personal .telephone > div:first-child {
      margin-top: 6px;
      font-size: 1.3em;
      font-weight: 300;
      padding: 0 15px 0 0px;
    }

    .personal .telephone .inputs {
      padding: 10px 0 0 0;
    }

    .personal .telephone .inputs input {
      width: 80%;
      height: 40px;
      border: 1px solid gainsboro;
      border-radius: 3px;
      padding-left: 5px;
    }

    /*telephone end*/
    /*birthday start*/
    .personal .birthday {
      padding: 20px 0;
    }

    .personal .birthday > div:first-child {
      margin-top: 6px;
      font-size: 1.3em;
      font-weight: 300;
      padding: 0 15px 0 0px;
    }

    .personal .birthday > div:last-child {
      padding: 10px 0 0 0;
    }

    .personal .birthday > div:last-child select {
      height: 25px;
      width: 25%;
      font-size: 1.2em;
      margin-right: 10px;
      padding: 0 15px 0 0px;
    }

    /*birthday end*/
    /*address start*/
    .personal .address {
      padding: 20px 0;
    }

    .personal .address > div:first-child {
      margin-top: 1px;
      font-size: 1.3em;
      font-weight: 300;
      padding: 0 15px 0 0px;
    }

    .personal .address > div:last-child {
      padding: 10px 0 0 0;

    }

    .personal .address > div:last-child select {
      height: 25px;
      width: 25%;
      font-size: 1.2em;
      margin-right: 10px;
    }

    /*address end*/
    /*addressdetails start*/
    .personal .addressdetails {
      padding: 20px 0;
    }

    .personal .addressdetails > div:first-child {
      margin-top: 1px;
      font-size: 1.3em;
      font-weight: 300;
      padding: 0 15px 0 0px;
    }

    .personal .addressdetails > div:last-child {
      padding: 10px 0 0 0;
    }

    .personal .addressdetails > div:last-child textarea {
      resize: none;
      width: 90%;
    }

    /*addressdetails end*/

  }

  @media (min-width: 768px) {
    /*presonal start*/
    .personal {
      margin-bottom: 20px;
    }

    .personal header {
      font-size: 1.8em;
      font-weight: 400;
    }

    .personal .line {
      margin-top: 20px;
      border: 2px solid #c5c5c5;
      border-top-left-radius: 2px;
      border-top-right-radius: 2px;
    }

    .personal .container-fluid {
      padding: 50px 15px 20px 30px;
      background-color: white;
      border-bottom-left-radius: 3px;
      border-bottom-right-radius: 3px;
    }

    /*presonal end*/
    /*portrait start*/
    .personal .portrait {
      padding: 20px 0;
    }

    .personal .portrait > div:first-child {
      font-size: 1.3em;
      font-weight: 300;
    }

    .personal .portrait .peimg {
      width: 100px;
      height: 100px;
      border: 1px solid rgba(220, 220, 220, 0);
      border-radius: 3px;
    }

    .personal .portrait > div:last-child {
      padding-left: 30px;
    }

    .personal .portrait > div:last-child div {
      height: 50px;
    }

    .personal .portrait > div:last-child .cancel {
      border: 1px solid gainsboro;
      background-color: white;
      border-radius: 2px;
      font-size: 0.9em;
      padding: 8px;
      margin-top: 10px;
    }

    .personal .portrait > div:last-child .confirm {
      background-color: #029789;
      border-radius: 2px;
      font-size: 0.9em;
      padding: 8px;
      color: white;
      margin-top: 10px;
      border: 0;
    }

    /*portrait end*/
    /*portrait start*/
    .personal .email {
      padding: 20px 0;
    }

    .personal .email > div:first-child {
      margin-top: 6px;
      font-size: 1.3em;
      font-weight: 300;
    }

    .personal .email .inputs {
      padding: 0;
    }

    .personal .email .inputs input {
      width: 350px;
      height: 40px;
      border: 1px solid gainsboro;
      border-radius: 3px;
      padding-left: 5px;
    }

    /*portrait end*/
    /*nickname start*/
    .personal .nickname {
      padding: 20px 0;
    }

    .personal .nickname > div:first-child {
      margin-top: 6px;
      font-size: 1.3em;
      font-weight: 300;
    }

    .personal .nickname .inputs {
      padding: 0;
    }

    .personal .nickname .inputs input {
      width: 350px;
      height: 40px;
      border: 1px solid gainsboro;
      border-radius: 3px;
      padding-left: 5px;
    }

    /*nickname end*/
    /*telephone start*/
    .personal .telephone {
      padding: 20px 0;
    }

    .personal .telephone > div:first-child {
      margin-top: 6px;
      font-size: 1.3em;
      font-weight: 300;
    }

    .personal .telephone .inputs {
      padding: 0;
    }

    .personal .telephone .inputs input {
      width: 350px;
      height: 40px;
      border: 1px solid gainsboro;
      border-radius: 3px;
      padding-left: 5px;
    }

    /*telephone end*/
    /*birthday start*/
    .personal .birthday {
      padding: 20px 0;
    }

    .personal .birthday > div:first-child {
      margin-top: 6px;
      font-size: 1.3em;
      font-weight: 300;
    }

    .personal .birthday > div:last-child {
      padding: 0px;
    }

    .personal .birthday > div:last-child select {
      height: 40px;
      width: 80px;
      font-size: 1.2em;
      margin-right: 10px;
    }

    /*birthday end*/
    /*address start*/
    .personal .address {
      padding: 20px 0;
    }

    .personal .address > div:first-child {
      margin-top: 1px;
      font-size: 1.3em;
      font-weight: 300;
    }

    .personal .address > div:last-child {
      padding: 0px;
    }

    .personal .address > div:last-child select {
      height: 30px;
      width: 80px;
      font-size: 1.2em;
      margin-right: 10px;
    }

    /*address end*/
    /*addressdetails start*/
    .personal .addressdetails {
      padding: 20px 0;
    }

    .personal .addressdetails > div:first-child {
      margin-top: 1px;
      font-size: 1.3em;
      font-weight: 300;
    }

    .personal .addressdetails > div:last-child {
      padding: 0px;
    }

    .personal .addressdetails > div:last-child textarea {
      resize: none
    }

    /*addressdetails end*/

  }

  @media (min-width: 992px) {
    /*presonal start*/
    .personal {
      margin-bottom: 20px;
    }

    .personal header {
      font-size: 1.8em;
      font-weight: 400;
    }

    .personal .line {
      margin-top: 20px;
      border: 2px solid #c5c5c5;
      border-top-left-radius: 2px;
      border-top-right-radius: 2px;
    }

    .personal .container-fluid {
      padding: 50px 15px 20px 30px;
      background-color: white;
      border-bottom-left-radius: 3px;
      border-bottom-right-radius: 3px;
    }

    /*presonal end*/
    /*portrait start*/
    .personal .portrait {
      padding: 20px 0;
    }

    .personal .portrait > div:first-child {
      font-size: 1.3em;
      font-weight: 300;
    }

    .personal .portrait .peimg {
      width: 100px;
      height: 100px;
      border: 1px solid rgba(220, 220, 220, 0);
      border-radius: 3px;
    }

    .personal .portrait > div:last-child {
      padding-left: 30px;
    }

    .personal .portrait > div:last-child div {
      height: 50px;
    }

    .personal .portrait > div:last-child .cancel {
      border: 1px solid gainsboro;
      background-color: white;
      border-radius: 2px;
      font-size: 0.9em;
      padding: 8px;
      margin-top: 10px;
    }

    .personal .portrait > div:last-child .confirm {
      background-color: #029789;
      border-radius: 2px;
      font-size: 0.9em;
      padding: 8px;
      color: white;
      margin-top: 10px;
      border: 0;
    }

    /*portrait end*/
    /*portrait start*/
    .personal .email {
      padding: 20px 0;
    }

    .personal .email > div:first-child {
      margin-top: 6px;
      font-size: 1.3em;
      font-weight: 300;
    }

    .personal .email .inputs {
      padding: 0;
    }

    .personal .email .inputs input {
      width: 350px;
      height: 40px;
      border: 1px solid gainsboro;
      border-radius: 3px;
      padding-left: 5px;
    }

    /*portrait end*/
    /*nickname start*/
    .personal .nickname {
      padding: 20px 0;
    }

    .personal .nickname > div:first-child {
      margin-top: 6px;
      font-size: 1.3em;
      font-weight: 300;
    }

    .personal .nickname .inputs {
      padding: 0;
    }

    .personal .nickname .inputs input {
      width: 350px;
      height: 40px;
      border: 1px solid gainsboro;
      border-radius: 3px;
      padding-left: 5px;
    }

    /*nickname end*/
    /*telephone start*/
    .personal .telephone {
      padding: 20px 0;
    }

    .personal .telephone > div:first-child {
      margin-top: 6px;
      font-size: 1.3em;
      font-weight: 300;
    }

    .personal .telephone .inputs {
      padding: 0;
    }

    .personal .telephone .inputs input {
      width: 350px;
      height: 40px;
      border: 1px solid gainsboro;
      border-radius: 3px;
      padding-left: 5px;
    }

    /*telephone end*/
    /*birthday start*/
    .personal .birthday {
      padding: 20px 0;
    }

    .personal .birthday > div:first-child {
      margin-top: 6px;
      font-size: 1.3em;
      font-weight: 300;
    }

    .personal .birthday > div:last-child {
      padding: 0px;
    }

    .personal .birthday > div:last-child select {
      height: 40px;
      width: 80px;
      font-size: 1.2em;
      margin-right: 10px;
    }

    .personal .birthday input {
      width: 9%;
      height: 35px;
      text-align: center;
      margin-right: 8px;
    }

    /*birthday end*/
    /*address start*/
    .personal .address {
      padding: 20px 0;
    }

    .personal .address > div:first-child {
      margin-top: 1px;
      font-size: 1.3em;
      font-weight: 300;
    }

    .personal .address > div:last-child {
      padding: 0px;
    }

    .personal .address > div:last-child select {
      height: 30px;
      width: 80px;
      font-size: 1.2em;
      margin-right: 10px;
    }

    .personal .address input {
      width: 9%;
      margin-right: 9px;
    }

    /*address end*/
    /*addressdetails start*/
    .personal .addressdetails {
      padding: 20px 0;
    }

    .personal .addressdetails > div:first-child {
      margin-top: 1px;
      font-size: 1.3em;
      font-weight: 300;
    }

    .personal .addressdetails > div:last-child {
      padding: 0px;
    }

    .personal .addressdetails > div:last-child textarea {
      resize: none
    }

    /*addressdetails end*/
    /*设置提交按钮的样式*/
    .personal .tijiao > div:last-child {
      padding: 0;
    }

    .personal .tijiao > div:last-child button {
      width: 10%;
      border: none;
      border-radius: 3px;
      padding: 5px;
      color: white;
      background-color: #029789;
    }

    .personal .tijiao > div:last-child span {
      font-size: 0.7em;
      padding-left: 10px;
      color: red;
    }

  }

</style>
