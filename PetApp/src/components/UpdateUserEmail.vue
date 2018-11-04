<template>
<div class="zzc">
  <div class="tab-content">
    <form action="" >
      <div class="row alter-text">
        <div class="col-md-1"></div>
        <div class="col-md-9">绑定邮箱</div>
        <div class="col-md-2" @click="toUpdateEmail">
          <img src="../../assets/icons/X.svg">
        </div>
      </div>
      <div class="original-email">
        <span class="original-text">邮箱地址：</span>
        <input type="text" class="btn_tel" placeholder="请输入您的邮箱" v-model="uemail" @blur="showEmail">
        <p class="warn" v-if="isTipEmail">邮箱格式错误！</p>
      </div>
      <div class="container-fluid bg-input">
        <div class="row">
          <div class="col-md-6 bg-confirm">
            <input type="button" value="确认" class="confirm" @click="updateUserEmail">
          </div>
          <div class="col-md-6">
            <input type="button" value="取消" class="cancel" @click="toUpdateEmail">
          </div>
        </div>
      </div>

    </form>
  </div>
</div>
</template>

<script>
// import axios from 'axios'
import $ from 'jquery'
export default {
  name: 'UpdateUserEmail',
  data () {
    return {
      msg: '修改个人信息',
      url: 'http://localhost:8000/',
      uemail: '',
      isTipEmail: false
    }
  },
  created () {
    this.usertel = window.sessionStorage.getItem('usertel')
  },
  methods: {
    // 关闭模态框
    toUpdateEmail: function () {
      this.$emit('updateemclick')
    },
    // 修改用户密码
    updateUserEmail: function () {
      this.showEmail()
      if (this.isTipEmail === false) {
        let user = {
          'usertel': this.usertel,
          'email': this.uemail
        }
        let vm = this
        $.ajax({
          url: this.url + 'user/updateEmail/',
          type: 'POST',
          data: JSON.stringify(user),
          success: function (response, textStatus, request) {
            let res = response.res
            console.log(response.res)
            if (res === '') {
              vm.closeMyself()
              vm.$emit('updateUserEmailclick')
            }
          }
        })
      }
    },
    // 判断邮箱格式
    showEmail: function () {
      let EmRegex = /^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,4}$/
      if (EmRegex.test(this.uemail)) {
        this.isTipEmail = false
      } else {
        this.isTipEmail = true
      }
      return this.isTipEmail
    },
    closeMyself: function () {
      this.status = ''
      this.$emit('on-close')
    }
  }
}
</script>

<style scoped>
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
  .tab-content{
    width: 490px;
    height: 350px;
    background: white;
    position: absolute;
    left: 50%;
    transform: translate(-50%,50%);
    border-radius: 20px;
    border: solid 1px black;
  }
  .alter-text{
    margin-top: 20px;
    font-size: 1.4em;
    font-weight: bold;
  }
  .original-email{
    height: 60px;
    margin-top: 80px;
    margin-left: 60px;
  }
  .original-text{
    font-size: 1.3em;
  }
  .btn_tel{
    width: 250px;
    height: 40px;
    outline: none;
    border: solid 1px black;
    padding-left: 10px;
    border-radius: 3px;
  }
  .warn{
    margin-left: 100px;
    height: 30px;
    color: red;
  }
  .bg-input {
    margin-top: 80px;
    margin-bottom: 20px;
  }
  .bg-confirm {
    text-align: right;
  }
  .confirm {
    width: 60px;
    height: 35px;
    border-radius: 40px;
    text-align: center;
    line-height: 35px;
    background: #126693;
    color: white;
    opacity: 0.8;
    outline: none;
    border: none;
  }

  .cancel {
    width: 60px;
    height: 35px;
    border-radius: 40px;
    border: solid 1px black;
    text-align: center;
    line-height: 35px;
    outline: none;
    background: white;
  }

  .confirm:hover {
    opacity: 1;

  }
</style>
