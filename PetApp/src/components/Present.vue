<template>
  <body class="layui-bg-gray" cz-shortcut-listen="true">
  <div class="layui-container layui-row">
    <div class="layui-col-md10 layui-col-md-offset1 lph-left">
      <div class="layui-card adopt-create-card layui-col-md12">
        <div class="layui-card-header card-header">
          <h2 class="title">请输入宠物的信息 信息越完整,送出率越高</h2>
        </div>

        <div class="layui-card-body card-body">
          <form action="" class="layui-form" method="post">
            <div class="layui-row layui-col-md12 card-body-group">
              <div class="card-form-label layui-col-md2 layui-col-xs12">送养名</div>
              <div class="layui-col-md10">
                <div class="layui-form-item layui-form-pane layui-col-md12 no-label">
                  <div class="layui-input-block">
                    <input autocomplete="off" class="layui-input"  name="title" placeholder="请输入标题"
                           type="text" v-model="title">
                  </div>
                </div>
              </div>
            </div>

            <div class="layui-row layui-col-md12 card-body-group">
              <div class="card-form-label layui-col-md2 layui-col-xs12">宠物介绍</div>
              <div class="layui-col-md10">
                <div class="layui-form-item layui-form-pane layui-col-md12 no-label">
                  <div class="layui-input-block">
                    <textarea class="layui-textarea"  name="introduce" placeholder="请输入内容"
                              v-model="introduce"></textarea>
                  </div>
                </div>
              </div>
            </div>
            <div class="layui-row layui-col-md12 card-body-group">
              <div class="card-form-label layui-col-md2 layui-col-xs12">领养要求</div>
              <div class="layui-col-md10">
                <div class="layui-form-item layui-form-pane layui-col-md12 no-label">
                  <div class="layui-input-block">
                    <textarea class="layui-textarea" name="require" placeholder="请输入内容"
                              v-model="yaoqiu"></textarea>
                  </div>
                </div>
              </div>
            </div>
            <div class="layui-row layui-col-md12 card-body-group">
              <div class="card-form-label layui-col-md2 layui-col-xs12">联系人信息</div>
              <div class="layui-col-md10">
                <div class="layui-form-item layui-form-pane layui-col-md12">
                  <label class="layui-form-label">送养人</label>
                  <div class="layui-input-block">
                    <input autocomplete="off" class="layui-input" lay-verify="required" name="contact"
                           placeholder="请输入姓名" type="text" v-model="contact">
                  </div>
                </div>
                <div class="layui-form-item layui-form-pane layui-col-md12">
                  <label class="layui-form-label">手机号</label>
                  <div class="layui-input-block">
                    <input autocomplete="off" class="layui-input" name="phone" placeholder="联系方式三选一" type="text"
                           v-model="phone">
                  </div>
                </div>
                <div class="layui-form-item layui-form-pane layui-col-md12">
                  <label class="layui-form-label">微信号</label>
                  <div class="layui-input-block">
                    <input autocomplete="off" class="layui-input" name="weixin" placeholder="联系方式三选一" type="text"
                           v-model="weixin">
                  </div>
                </div>
                <div class="layui-form-item layui-form-pane layui-col-md12">
                  <label class="layui-form-label">QQ号</label>
                  <div class="layui-input-block">
                    <input autocomplete="off" class="layui-input" name="qq" placeholder="联系方式三选一" type="text"
                           v-model="qq">
                  </div>
                </div>
              </div>
            </div>
            <div class="layui-row layui-col-md12 card-body-group">
              <div class="card-form-label layui-col-md2 layui-col-xs12">领养时间段</div>
              <div class="layui-col-md10">
                <div class="layui-form-item layui-form-pane layui-col-md12">
                  <label class="layui-form-label">开始时间</label>
                  <div class="layui-input-block">
                    <input autocomplete="off" class="layui-input" lay-verify="required" name="contact"
                           placeholder="请输入姓名" type="date" v-model="stat_time">
                  </div>
                </div>
                <div class="layui-form-item layui-form-pane layui-col-md12">
                  <label class="layui-form-label">结束时间</label>
                  <div class="layui-input-block">
                    <input autocomplete="off" class="layui-input" name="phone" placeholder="联系方式三选一" type="date"
                           v-model="end_time">
                  </div>
                </div>
              </div>

            </div>


            <div class="layui-row layui-col-md12 card-body-group">
              <div class="card-form-label layui-col-md2 layui-col-xs12">宠物信息</div>
              <div class="layui-col-md10">
                <div class="layui-form-item layui-form-pane layui-col-md12">
                  <label class="layui-form-label">分类</label>
                  <div class="layui-input-inline">
                    <select lay-verify="required" name="cateId" id="type" v-model="pet_type_id">
                      <option value="">选择分类</option>
                      <option value="01">小狗</option>
                      <option value="02">小猫</option>
                      <option value="03">龙猫</option>
                      <option value="04">宠物鼠</option>
                      <option value="05">鱼</option>
                      <option value="06">虾</option>
                      <option value="07">松鼠</option>
                      <option value="08">鸟</option>
                      <option value="09">豚鼠</option>
                      <option value="10">宠物貂</option>
                      <option value="11">龟</option>
                      <option value="12">兔子</option>
                      <option value="13">蛇</option>
                      <option value="14">蜥蜴</option>
                      <option value="15">其他</option>
                    </select>
                  </div>
                  <label class="layui-form-label">性别</label>
                  <div class="layui-input-inline">
                    <select lay-verify="required" name="sex" v-model="pet_sex_id" id="sex">
                      <option value="0">选择性别</option>
                      <option value="1">公</option>
                      <option value="2">母</option>
                    </select>
                  </div>
                </div>
                <div class="layui-form-item layui-form-pane layui-col-md12">
                  <label class="layui-form-label">是否免费</label>
                  <div class="layui-input-inline">
                    <select lay-verify="required" name="isFree" v-model="isFree" id="isFree">
                      <option selected="" value="1">免费</option>
                      <option value="0">有偿</option>
                    </select>
                  </div>
                  <label class="layui-form-label">价格</label>
                  <div class="layui-input-inline">
                    <input autocomplete="off" class="layui-input" name="price"  type="text"
                           v-model="price" placeholder="0" value="0">
                  </div>
                </div>
              </div>
            </div>
            <div class="layui-row layui-col-md12 card-body-group">
              <div class="card-form-label layui-col-md2 layui-col-xs12">所在城市</div>
              <div class="layui-col-md10">
                <div class="layui-form-item layui-form-pane layui-col-md12">
                  <label class="layui-form-label">请选择省</label>
                  <div class="layui-input-inline">
                    <select id="provid" lay-filter="provid" lay-verify="required" name="provid" v-model="provid_id">
                      <option value="">请选择</option>
                    </select>
                  </div>
                  <label class="layui-form-label">请选择市</label>
                  <div class="layui-input-inline">
                    <select id="cityid" lay-filter="cityid" lay-verify="required" name="cityid" v-model="citys">
                      <option value="">请选择</option>
                    </select>
                  </div>
                </div>
                <div class="layui-form-item layui-form-pane layui-col-md12">
                  <label class="layui-form-label">请选择县</label>
                  <div class="layui-input-inline">
                    <select id="areaid" lay-filter="areaid" lay-verify="required" name="areaid" v-model="areas">
                      <option value="">请选择</option>
                    </select>
                  </div>
                </div>
              </div>
            </div>


            <div class="layui-row layui-col-md12 card-body-group">
              <div class="card-form-label layui-col-md2 layui-col-xs12">宠物靓照</div>
              <div class="layui-col-md10">
                <div class="card-form-upload layui-col-md6 layui-col-xs12">
                  <div class="layui-upload-drag image-upload layui-col-md11 layui-col-xs12" id="image-upload-1">
                    <img alt="" class="layui-hide" id="image-upload-view-1" src="" width="100%">
                    <div id="image-upload-icon-1" style="width: 100%;height: 100%">
                      <div style=" height: 50%; margin-bottom: -40px;"></div>
                      <i class="layui-icon"></i>
                      <input type="file" class="mdc" value="点击上传，或将文件拖拽到此处" @change="update2" name="usericon">
                      <p class="img-add1">点击上传，或将文件拖拽到此处</p>
                    </div>
                  </div>
                  <input class="layui-upload-file" type="file" accept="undefined" name="file">
                </div>

                <div class="card-form-upload layui-col-md6  layui-col-xs12">
                  <div class="layui-upload-drag image-upload layui-col-md11 layui-col-xs12" id="image-upload-2">
                    <img alt="" class="layui-hide" id="image-upload-view-2" src="" width="100%">
                    <div id="image-upload-icon-2" style="width: 100%;height: 100%">
                      <div style=" height: 50%; margin-bottom: -40px;"></div>
                      <i class="layui-icon"></i>
                      <input type="file" class="mdc" value="点击上传，或将文件拖拽到此处" @change="update3" name="usericon">
                      <p class="img-add2">点击上传，或将文件拖拽到此处</p>
                    </div>
                  </div>
                  <input class="layui-upload-file" type="file" accept="undefined" name="file">
                </div>
              </div>
              <input id="input-image-1" name="images[]" type="hidden">
              <input id="input-image-2" name="images[]" type="hidden">
            </div>
            <div class="layui-row layui-col-md12 card-body-submit">
              <div class="layui-col-md4 layui-col-md-offset7">
                <button class="layui-btn" id="btn-upload" lay-filter="adopt-submit" type="button"
                        @click="update1">立即提交
                </button>
                <button class="layui-btn layui-btn-primary" id="reset-img" type="button">重置图片</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
  </body>
</template>

<script>
  import axios from 'axios';

  export default {
    name: 'Present',
    data: function () {
      return {
        title: "",
        introduce: "",
        yaoqiu: "",
        pet_type_id: "",
        pet_sex_id: "",
        isFree: "",
        price: "",
        provid_id: "",
        citys: "",
        areas: "",
        contact: "",
        phone: "",
        weixin: "",
        qq: "",
        user_id: "",
        stat_time:"",
        end_time:"",
        Positive: "",
        otherSide: "",
        formData: [],

      }
    },

    mounted: function () {
      if(sessionStorage.getItem("id") == null){
        this.$router.push({path: '/login'})
      }

      var defaults = {
        s1: 'provid',
        s2: 'cityid',
        s3: 'areaid',
        v1: null,
        v2: null,
        v3: null
      };
      var $form;
      var form;
      var $;
      layui.define(['jquery', 'form'], function () {
        $ = layui.jquery;
        form = layui.form;
        $form = $('form');
        treeSelect(defaults);
      });

      function treeSelect(config) {
        config.v1 = config.v1 ? config.v1 : 110000;
        config.v2 = config.v2 ? config.v2 : 110100;
        config.v3 = config.v3 ? config.v3 : 110101;
        $.each(threeSelectData, function (k, v) {
          appendOptionTo($form.find('select[name=' + config.s1 + ']'), k, v.val, config.v1);
        });
        form.render();
        cityEvent(config);
        areaEvent(config);
        form.on('select(' + config.s1 + ')', function (data) {
          cityEvent(data);
          form.on('select(' + config.s2 + ')', function (data) {
            areaEvent(data);
          });
        });

        function cityEvent(data) {
          $form.find('select[name=' + config.s2 + ']').html("");
          config.v1 = data.value ? data.value : config.v1;
          $.each(threeSelectData, function (k, v) {
            if (v.val == config.v1) {
              if (v.items) {
                $.each(v.items, function (kt, vt) {
                  appendOptionTo($form.find('select[name=' + config.s2 + ']'), kt, vt.val, config.v2);
                });
              }
            }
          });
          form.render();
          config.v2 = $('select[name=' + config.s2 + ']').val();
          areaEvent(config);
        }

        function areaEvent(data) {
          $form.find('select[name=' + config.s3 + ']').html("");
          config.v2 = data.value ? data.value : config.v2;
          $.each(threeSelectData, function (k, v) {
            if (v.val == config.v1) {
              if (v.items) {
                $.each(v.items, function (kt, vt) {
                  if (vt.val == config.v2) {
                    $.each(vt.items, function (ka, va) {
                      appendOptionTo($form.find('select[name=' + config.s3 + ']'), ka, va, config.v3);
                    });
                  }
                });
              }
            }
          });
          form.render();
          form.on('select(' + config.s3 + ')', function (data) {
          });
        }

        function appendOptionTo($o, k, v, d) {
          var $opt = $("<option>").text(k).val(v);
          if (v == d) {
            $opt.attr("selected", "selected")
          }
          $opt.appendTo($o);
        }
      }
      $('#layui-upload-file').click(function () {
        var formData = new FormData($("#myform")[0]);
        $.ajax({
          url: 'http://127.0.0.1:8000/send/upload/',
          type: 'POST',
          data: formData,
          async: false,
          cache: false,
          contentType: false,
          processData: false,
          success: function (returndata) {
            console.log(returndata);
          },
          error: function (returndata) {
            console.log(returndata);
          }
        });
      })


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
          $('.img-add1').empty().append($img);
        }
      },
      update3(e) {  // 上传照片
        var self = this;
        let file = e.target.files[0];
        // console.log(file)
        this.preview11(file);
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
      preview11(file) {
        var img = new Image();
        img.src = URL.createObjectURL(file);
        var url = img.src;
        var $img = $(img);
        $img.css({'width': '175px', 'height': '175px'});
        img.onload = function () {
          URL.revokeObjectURL(url);
          $('.img-add2').empty().append($img);
        }
      },
      update1() {
        console.log(this.formData);
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
              console.log(vm.ImgUrl);
            }
            console.log(response.data);
            this.Positive = response.data.name;
            // PositiveFlag=true;
            axios.post('http://127.0.0.1:8000/adopt/DicLoad/', this.formData[1], config)
              .then(response => {
                if (response.data.code === 0) {
                  vm.ImgUrl = response.data.data;
                  console.log(vm.ImgUrl);
                }
                console.log(response.data);
                this.otherSide = response.data.name;
                var data = {
                  "title": this.title,
                  "introduce": this.introduce,
                  "yaoqiu": this.yaoqiu,
                  "pet_type_id": document.querySelector("#type").value,
                  "pet_sex_id": document.querySelector("#sex").value,
                  "isFree": document.querySelector("#isFree").value,
                  "price": this.price,
                  "provid_id": document.querySelector("#provid").value,
                  "citys": document.querySelector("#cityid").value,
                  "areas": document.querySelector("#areaid").value,
                  "contact": this.contact,
                  "phone": this.phone,
                  "weixin": this.weixin,
                  "qq": this.qq,
                  "user_id": sessionStorage.getItem("id"),
                  "Positive": this.Positive,
                  "otherSide": this.otherSide,
                  "stat_time": this.stat_time,
                  "end_time": this.end_time
                }

                axios.post('http://127.0.0.1:8000/adopt/FlieName/', data)
                  .then(response => {
                    console.log(123)
                    // console.log(res.data)
                    this.user_id = sessionStorage.getItem("id")
                    console.log(this.user_id)

                    if (this.user_id) {
                      if (response.data.code == 808) {
                        alert("添加成功")
                        this.$router.push({
                          path: '/'
                        })
                      } else {
                        alert("有内容为空")
                      }

                    }
                    else {
                      alert("请先登录")
                    }
                    // if (response.data.code==808) {
                    //   alert("添加成功")
                    //   this.$router.push({
                    //     path: '/'
                    //   })
                    // } else {
                    //   alert("denglu")
                    // }
                  })
              });
          });
      },


    }
  }

</script>
<style scoped>
  .adopt-create-card .card-body .card-body-group {
    border-bottom: 2px solid #f6f6f6;
    padding: 30px 0px 20px 0px;
  }

  .adopt-create-card .card-form-label {
    float: left;
    display: block;
    padding: 9px 15px;
    font-weight: 400;
    line-height: 20px;
  }

  .layui-form-pane .layui-input-block {
    margin: 0;
    left: -1px;
    min-height: 36px;
    position: relative;
    width: 100%;
  }

  .layui-btn {
    position: relative;
    left: -180px;
    margin-left: 30px;
  }

  .layui-form-pane .layui-form-label {
    width: 110px;
    padding: 8px 15px;
    height: 38px;
    line-height: 20px;
    border-width: 1px;
    border-style: solid;
    border-radius: 2px 0 0 2px;
    text-align: center;
    background-color: #FBFBFB;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
    box-sizing: border-box;
  }

  .layui-form-pane .layui-input {
    border-radius: 0 2px 2px 0;
  }

  .layui-input, .layui-textarea {
    display: block;
    width: 70%;
    padding-left: 10px;
  }

  .layui-upload-drag {
    position: relative;
    padding: 30px;
    border: 1px dashed #e2e2e2;
    background-color: #fff;
    text-align: center;
    cursor: pointer;
    color: #999;
  }
  .mdc{
    opacity: 0;
    /*background-color: red;*/
    margin-bottom: -25px;
  }
  .adopt-create-card .card-header {
    padding: 30px 20px 20px 20px;
    height: auto;
    text-align: center;
  }
  .layui-card-header {
    height: 42px;
    line-height: 42px;
    padding: 0 15px;
    border-bottom: 1px solid #f6f6f6;
    color: #333;
    border-radius: 2px 2px 0 0;
  }
  h2 {
    display: block;
    font-size: 15pt;
  }
  .layui-btn{
    margin-top: 20px;
  }
</style>
