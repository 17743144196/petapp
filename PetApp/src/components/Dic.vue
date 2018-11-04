<template>
  <div class="info">
    <ul>
      <li class="items">
        <h3 class="aa">驾照认证</h3>
        <span class="aa3">您的驾照认证未完成，在线认证驾照，可自助取、还车！</span>
      </li>

      <li class="items">
        <span class="aa1">驾照正页图片</span>
        <form id="form3">
          <input type="file" class="aa2" name="usericon" id="upload_file2" @change="update2">
          <div class="img-add">选择文件</div>
          <!--<input type="file" name="usericon" @change="update">-->
        </form>
        <div id="preview"></div>
          <!--<input type="submit" value="提交">-->
        <span class="aa4">请上传小于2M的JPG格式图片</span>
      </li>
      <li class="items">
        <span class="aa1">驾照副页图片</span>
        <form id="form2">
          <input type="file" class="aa2" name="usericon" id="upload_file3" @change="update3">
          <div class="img-add">选择文件</div>
        </form>
        <div id="preview2"></div>
        <span class="aa4">请上传小于2M的JPG格式图片</span>
      </li>
      <div class="bb2">
        <input class="bb1" type="button" value="提交" @click="update1">
      </div>
    </ul>
  </div>
</template>

<script>
import $ from 'jquery'
import axios from 'axios'
export default {

  name: 'Dic',
  data () {
    return {
      btn:false,
      flag:0,
      form1:'',
      form2:'',
      formData:[],
      Positive:"",
      otherSide:""

    }
  },

  methods:{
    update1(){
      console.log(this.formData);
      var config = {
        headers: {'Content-Type': 'multipart/form-data'},

      };
      // 添加请求头
      let vm=this;
      // let otherSideFlag=false;
      // let PositiveFlag=false;
      axios.post('http://127.0.0.1:8000/user/DicLoad/', this.formData[0], {
        headers: {
          'Content-Type': 'application/json',
          token:sessionStorage.getItem("token")
        }
      })
        .then(response => {
          if (response.data.code === 0) {
            vm.ImgUrl = response.data.data;
            console.log(vm.ImgUrl);
          }
          console.log(response.data);
          this.Positive=response.data.name;
          // PositiveFlag=true;
          axios.post('http://127.0.0.1:8000/user/DicLoad/', this.formData[1], config)
            .then(response => {
              if (response.data.code === 0) {
                vm.ImgUrl = response.data.data;
                console.log(vm.ImgUrl);
              }
              console.log(response.data);
              this.otherSide=response.data.name;
              // console.log("11111111111111111111111111",this.otherSide);
              // otherSideFlag=true;
            axios.post('http://127.0.0.1:8000/user/fliename/', {"Positive":this.Positive,"otherSide":this.otherSide}, {
              headers: {
                'Content-Type': 'application/json',
                token:sessionStorage.getItem("token")
              }
            })
                .then(response => {
                  console.log(response.data)
                })
            });
        });



    },
    update2 (e) {  // 上传照片
      var self = this;
      let file = e.target.files[0];
      // console.log(file)
      this.preview1(file);
      // 弹出图片名字
      // alert(file.name);
      /* eslint-disable no-undef */
      let param = new FormData() ;// 创建form对象
      //usericon通常就是file的name属性值
      param.append('usericon', file, file.name) ;// 通过append向form对象添加数据
      param.append('chunk', '0'); // 添加form表单中其他数据
      this.formData.push(param);
      console.log(param.get('file')) // FormData私有类对象，访问不到，可以通过get判断值是否传进去
    },
    update3 (e) {  // 上传照片
      var self = this;
      let file = e.target.files[0];
      // console.log(file)
      this.preview11(file);
      // 弹出图片名字
      // alert(file.name);
      /* eslint-disable no-undef */
      let param = new FormData() ;// 创建form对象
      //usericon通常就是file的name属性值
      param.append('usericon', file, file.name) ;// 通过append向form对象添加数据
      param.append('chunk', '0'); // 添加form表单中其他数据
      this.formData.push(param);
      console.log(param.get('file')) // FormData私有类对象，访问不到，可以通过get判断值是否传进去
    },
    // 图片预览
    preview1(file){
      var img = new Image();
      img.src = URL.createObjectURL(file);
      var url = img.src;
      var $img = $(img);
      $img.css({'width':'150px','height':'69px'});
      img.onload = function () {
        URL.revokeObjectURL(url);
        $('#preview').empty().append($img);
      }
    },
    // 图片预览方法
    preview11(file){
      var img = new Image();
      img.src = URL.createObjectURL(file);
      var url = img.src;
      var $img = $(img);
      $img.css({'width':'150px','height':'69px'});
      img.onload = function () {
        URL.revokeObjectURL(url);
        $('#preview2').empty().append($img);
      }
    },

    }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  ul,li,span{
    margin: 0;
    padding: 0;
  }
  input{
    /*outline: none;*/
  }
  ul{
    list-style: none;
  }
  ul li.items,li.item,li.long-item{
    border-bottom:#e9ebee solid 1px;
  }
  .info{
    width: 924px;
    height:940px;
    border: #e9ebee solid 1px;
    padding: 0px 20px ;
    background-color: white;
  }
  ul li.items:nth-child(1){
    height: 100px;
    width: 100%;
    font-size: 1.5em;
    line-height: 100px;
  }
  ul li.items{
    display: flex;
    height: 70px;
    width: 100%;
    font-size: 1em;
    /*line-height: 70px;*/
  }
 .aa{
   position: relative;
   top: 5px;
   /*color: red;*/
 }
  .items .aa3{
    position: relative;
    top: 10px;
    left: 350px;
    font-size: 16px;
    color: red;
  }
  .items .aa1{
    position: relative;
    top: 0px;
    left: 10px;
    height: 70px;
    line-height: 70px;
    /*background: #22A7F0;*/
  }
  .aa4{
    position: relative;
    height: 70px;
    line-height: 70px;
    left: 215px;
    color: #c6c6ce;
    font-size: 14px;
  }
  .items .aa2{
    position: relative;
    top: 20px;
    left: 130px;
    /*top: 250px;*/
    /*width: 200px;*/
    /*height: 50px;*/
    opacity: 0;
    z-index: 5;
  }
  .bb1{
    position: relative;
    width: 100px;
    height: 50px;
    background: rgba(238, 184, 26, 0.2);
    color: #eeb819;
    border: solid 1px #eeb819;
    left: 150px;
    top: 10px;
  }
  .bb2{
    width: 750px;
    height: 70px;
    background: #f8f8fa;
    margin: auto;
  }
  .img-add{
    position: relative;
    width: 180px;
    height: 50px;
    background: rgba(238, 184, 25, 0.2);
    color: #eeb819;
    top: -16px;
    left: 130px;
    line-height: 50px;
    text-align: center;
    border: solid 1px #eeb819;
  }
  #preview{
    position: relative;
    left: 80px;
    width: 150px;
    height: 70px;
    /*border: 1px solid;*/
    /*background: #22A7F0;*/
  }
  #preview2{
    position: relative;
    left: 80px;
    width: 150px;
    height: 70px;
    /*border: 1px solid;*/
    /*background: #22A7F0;*/
  }

</style>
