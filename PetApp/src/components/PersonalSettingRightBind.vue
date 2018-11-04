<template>
  <div class="content">
    <!--账号绑定-->
    <div class="con-bind">
      <div class="u-title">
        账号绑定
      </div>
      <div class="u-email">
        <span class="e-img"></span>
        <span class="tip">邮箱未绑定</span>
        <button @click="updateUserEmail">绑定</button>
      </div>
      <div class="u-phone">
        <span class="p-img"></span>
        <span class="tip">手机
          <span class="u-tel">147*****075</span>
          已绑定
        </span>
        <button>更改</button>
      </div>
      <div class="u-pwd">
        <span class="pwd-img"></span>
        <span class="tip">密码已设置</span>
        <button @click="updateUserPwd">修改</button>
      </div>
    </div>
    <UpdateUserPassword v-if="showUpdateUserPwd" @updatepwdclick="updateUserPwd"
                        @updateUserPwdclick="updatePwdSuccess"
    ></UpdateUserPassword>
    <UpdateUserEmail v-if="showUpdateUserEmail" @updateemclick="updateUserEmail"
                     @updateUserEmailclick="updateEmailSuccess"
    ></UpdateUserEmail>
  </div>
</template>

<script>
import axios from 'axios'
import UpdateUserPassword from './UpdateUserPassword'
import UpdateUserEmail from './UpdateUserEmail'
export default {
  name: 'PersonalSettingRightBind',
  data () {
    return {
      url: 'http://localhost:8000/',
      msg: '右侧账号绑定',
      usertel: '',
      user: {},
      // 修改用户信息
      showUpdateUserPwd: false,
      updatedPwd: false,
      hackResetPwd: true,
      // 绑定邮箱
      showUpdateUserEmail: false,
      updatedEmail: false,
      hackResetEmail: true
    }
  },
  created: function () {
    this.usertel = window.sessionStorage.getItem('usertel')
  },
  mounted: function () {
    let vm = this
    axios.get(this.url + 'user/getUser/' + this.usertel + '/')
      .then(function (response) {
        vm.user = response.data.user[0]
        console.log(vm.user)
      })
      .catch(function (error) {
        console.log(error)
      })
  },
  components: {
    UpdateUserPassword,
    UpdateUserEmail
  },
  methods: {
    // 弹出修改用户密码
    toUserPassword: function () {
      this.$emit('upwdclick')
    },
    // 显示修改用户信息组建
    updateUserPwd: function () {
      this.showUpdateUserPwd = !this.showUpdateUserPwd
    },
    // 修改个人信息成功、刷新
    updatePwdSuccess: function () {
      this.updateUserPwd()
      this.updatedPwd = true
      // 强制刷新子组件
      this.hackResetPwd = false
      this.$nextTick(() => {
        this.hackResetPwd = true
      })
    },
    // 显示绑定用户邮箱组建
    updateUserEmail: function () {
      this.showUpdateUserEmail = !this.showUpdateUserEmail
    },
    // 修改个人信息成功、刷新
    updateEmailSuccess: function () {
      this.updateUserEmail()
      this.updatedEmail = true
      // 强制刷新子组件
      this.hackResetEmail = false
      this.$nextTick(() => {
        this.hackResetEmail = true
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .content {
    padding: 10px 30px;
  }
  .u-title {
    font-size: 1.5em;
    font-weight: bold;
    color: black;
    padding-bottom: 10px;
    border-bottom: 1px solid gray;
  }
  /*账户绑定*/
  .u-email span, .u-phone span, .u-pwd span {
    display: inline-block;
    height: 80px;
  }

  .u-email, .u-phone, .u-pwd {
    position: relative;
    border-bottom: 1px solid gray;
  }

  .u-email .e-img {
    position: absolute;
    width: 80px;
    background: url("../../assets/icons/email.svg") no-repeat 23px 24px;
  }

  .u-pwd .pwd-img {
    position: absolute;
    width: 80px;
    background: url("../../assets/icons/pwd.svg") no-repeat 23px 24px;
  }

  .u-phone .p-img {
    position: absolute;
    width: 80px;
    background: url("../../assets/icons/phone.svg") no-repeat 23px 24px;
  }

  .u-phone .u-tel {
    color: red;
    height: 80px;
    line-height: 80px;
    font-weight: normal;
  }

  .u-email .tip, .u-phone .tip, .u-pwd .tip {
    font-size: 1.2em;
    font-weight: bold;
    line-height: 80px;
    margin-left: 80px;
  }

  .u-email button, .u-phone button, .u-pwd button {
    width: 70px;
    height: 40px;
    outline: none;
    font-size: 1.1em;
    border: 1px solid gray;
    border-radius: 40px;
    position: absolute;
    right: 20px;
    top: 20px;
    background: white;
  }
</style>
