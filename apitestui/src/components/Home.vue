<template>
  <div class="main">
    <el-container>
      <el-header height="65px">
        <a href="/" style="width:300px;">自动化测试平台</a>

        <div class="header_name">
          <span style="float: right">管理员: {{ username }}</span>
          <el-dropdown
            style="float: right;margin-right: 15px"
            @command="loginOut"
          >
            <i class="el-icon-setting"></i>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item command="a">退出</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </div>
      </el-header>
      <div class="content">
        <el-aside class="menu" width="200px">
          <el-menu
            router
            :default-active="$route.path"
            class="el-menu-vertical-demo"
            background-color="#ECF5FF"
            text-color="#6E6E6E"
            active-text-color="#409EFF"
            style="border-right: none"
            :default-openeds="['1']"
          >
            <el-submenu index="1">
              <template slot="title">
                <i class="iconfont icon-accountbook"></i>
                <span>接口测试</span>
              </template>
              <el-menu-item-group>
                <el-menu-item index="/home/main">链路化接口测试</el-menu-item>
              </el-menu-item-group>
            </el-submenu>

            <el-submenu index="2">
              <template slot="title">
                <i class="iconfont icon-user"></i>
                <span>环境配置</span>
              </template>
              <el-menu-item-group>
                <el-menu-item index="/home/config">环境设置</el-menu-item>
                <el-menu-item index="/home/tests">环境设置</el-menu-item>
              </el-menu-item-group>
            </el-submenu>

            <el-submenu index="3">
              <template slot="title">
                <i class="iconfont icon-accountbook"></i>
                <span>报告管理</span>
              </template>
              <el-menu-item-group>
                <el-menu-item index="">接口报告</el-menu-item>
              </el-menu-item-group>
            </el-submenu>
            <el-submenu index="4">
              <template slot="title">
                <i class="iconfont icon-accountbook"></i>
                <span>定时任务</span>
              </template>
              <el-menu-item-group>
                <el-menu-item index="">定时任务</el-menu-item>
              </el-menu-item-group>
            </el-submenu>
          </el-menu>
        </el-aside>
        <el-main>
          <router-view
            style="height: 100%;max-height: 100%;overflow: hidden;"
          ></router-view>
        </el-main>
      </div>
    </el-container>
  </div>
</template>

<script>
import "../assets/icon/iconfont.css";
// import {delCookie} from "../util/util";
export default {
  data() {
    const username = window.localStorage.getItem("name") || "";
    return {
      username,
      isRouterAlive: true
    };
  },
  methods: {
    loginOut() {
      window.localStorage.removeItem("uid");
      window.localStorage.removeItem("name");
      this.$router.push("/login");
    }
  }
};
</script>

<style>
.main,
.el-container {
  font-weight: bold;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
}

.el-header {
  display: block;
  background-color: #409eff;
  font-size: 18px;
  line-height: 60px;
  color: #ecf5ff;
}

.content {
  display: flex;
  flex: 1;
  overflow: hidden;
}

.el-aside {
  background-color: #ecf5ff;
}

.el-main {
  overflow: hidden;
  margin: 0;
  padding: 0;
  height: 100%;
}

.header_name {
  position: relative;
  top: -60px;
}

.menu {
  height: 100%;
}

a {
  color: #ffffff;
}

a:hover {
  color: #eeeeee;
}

a {
  text-decoration: none;
}

body {
  margin: 0px;
  height: 100%;
}
</style>
