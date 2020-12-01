<template>
  <div class="finish-wrap">
    <div class="login_box">
      <div class="login_l_img"><img src="../assets/login-img.png" /></div>
      <div class="login">
        <div class="login_logo">
          <a href="#"><img src="../assets/login_logo.png"/></a>
        </div>
        <div class="login_name">
          <p>自动化测试平台</p>
        </div>
        <el-form :model="dataForm" :rules="rules" ref="dataForm">
          <el-form-item prop="email" class="form-item">
            <el-input
              v-model="dataForm.email"
              placeholder="邮箱账号"
            ></el-input>
          </el-form-item>
          <el-form-item prop="password" class="form-item">
            <el-input
              v-model="dataForm.password"
              type="password"
              placeholder="密码"
            ></el-input>
          </el-form-item>
          <el-button type="primary" @click="submitForm" style="width: 60%"
            >登录</el-button
          >
          <el-button type="primary" @click="submitForm1" style="width: 35%"
            >注册</el-button
          >
        </el-form>
      </div>
      <div class="copyright">比邻教育</div>
    </div>
  </div>
</template>

<script>
// import {setCookie} from "../util/util"
export default {
  name: "Login",
  data() {
    return {
      dataForm: {
        email: "",
        password: ""
      },
      rules: {
        email: [{ required: true, message: "邮箱不能为空", trigger: "blur" }],
        password: [
          { required: true, message: "用户名不能为空", trigger: "blur" }
        ]
      }
    };
  },
  methods: {
    submitForm1() {
      this.$router.push("/regediter");
    },
    submitForm() {
      this.$refs["dataForm"].validate(valid => {
        if (valid) {
          this.$get("/api/user/", this.dataForm)
            .then(res => {
              if (res.data.posts.length > 0) {
                const { id, username } = res.data.posts[0];
                window.localStorage.setItem("uid", id);
                window.localStorage.setItem("name", username);
                this.$router.push("/home/main");
              } else {
                this.$message({
                  message: "登录失败",
                  type: "error"
                });
              }
            })
            .catch(err => {
              this.$message({
                message: err,
                type: "error"
              });
            });
        }
      });
    }
  }
};
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/* CSS Document */

* {
  font: 13px/1.5 "微软雅黑";
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  -box-sizing: border-box;
  /*padding: 0;*/
  margin: 0;
  list-style: none;
  box-sizing: border-box;
}

/*body, html {*/
/*height: 100%;*/
/*overflow: hidden;*/
/*}*/

.finish-wrap {
  background-color: #93defe;
  /*background-color: #0091e6;*/
  height: 100%;
  position: fixed;
  overflow: hidden;
  width: 100%;
}

a {
  color: #27a9e3;
  text-decoration: none;
  cursor: pointer;
}

img {
  border: none;
}

.login_box {
  width: 1100px;
  margin: 120px auto 0;
}

.login_box .login_l_img {
  float: left;
  width: 432px;
  height: 440px;
  margin-left: 50px;
}

.login_box .login_l_img img {
  width: 500px;
  height: 440px;
}

.login {
  height: 360px;
  width: 400px;
  padding: 50px;
  background-color: #ffffff;
  border-radius: 6px;
  box-sizing: border-box;
  float: right;
  margin-right: 50px;
  position: relative;
  margin-top: 50px;
}

.login_logo {
  width: 120px;
  height: 120px;
  border: 5px solid #93defe;
  border-radius: 100px;
  background: #fff;
  text-align: center;
  line-height: 110px;
  position: absolute;
  top: -60px;
  right: 140px;
}

.login_name {
  width: 100%;
  float: left;
  text-align: center;
  margin-top: 20px;
}

.login_name p {
  width: 100%;
  text-align: center;
  font-size: 18px;
  color: #444;
  padding: 10px 0 20px;
}

.login_logo img {
  width: 60px;
  height: 60px;
  display: inline-block;
  vertical-align: middle;
}

input[type="text"],
input[type="file"],
input[type="password"],
input[type="email"],
select {
  border: 1px solid #dcdee0;
  vertical-align: middle;
  border-radius: 3px;
  height: 50px;
  padding: 0px 16px;
  font-size: 14px;
  color: #555555;
  outline: none;
  width: 100%;
  margin-bottom: 15px;
  line-height: 50px;
  color: #888;
}

input[type="text"]:focus,
input[type="file"]:focus,
input[type="password"]:focus,
input[type="email"]:focus,
select:focus {
  border: 1px solid #27a9e3;
}

input[type="submit"],
input[type="button"] {
  display: inline-block;
  vertical-align: middle;
  padding: 12px 24px;
  margin: 0px;
  font-size: 16px;
  line-height: 24px;
  text-align: center;
  white-space: nowrap;
  vertical-align: middle;
  cursor: pointer;
  color: #ffffff;
  background-color: #27a9e3;
  border-radius: 3px;
  border: none;
  -webkit-appearance: none;
  outline: none;
  width: 100%;
}
.form-item {
  margin-bottom: 25px;
}
.copyright {
  font-size: 14px;
  color: #fff;
  display: block;
  width: 100%;
  float: left;
  text-align: center;
  margin-top: 60px;
}

#password_text {
  border: 1px solid #dcdee0;
  vertical-align: middle;
  border-radius: 3px;
  height: 50px;
  padding: 0px 16px;
  font-size: 14px;
  color: #888;
  outline: none;
  width: 100%;
  margin-bottom: 15px;
  display: block;
  line-height: 50px;
}
</style>
