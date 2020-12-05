<template>
  <el-row>
    <el-col style="height: 100%;overflow-y: hidden;" :span="6">
      <el-menu class="modular_menu" @select="selectMenu">
        <el-row style="padding: 10px 0 0 10px;">
          <el-button type="primary" @click="runAll" style="width: 45%"
            >全部运行</el-button
          >
        </el-row>

        <el-submenu
          v-for="item in data"
          :key="item.id"
          :index="String(item.id)"
        >
          <template slot="title">
            <i class="el-icon-location"></i>
            <span>{{ item.platformname }}</span>
            <i class="el-icon-plus" @click.stop="addItem(item)" style="padding: 12px 0px 12px 0px;"></i>
          </template>
          <el-menu-item-group>
            <el-menu-item
              v-for="subItem in item.lists"
              :key="subItem.id"
              :index="String(subItem.id)">
<!--              -->
              <el-row>
                <el-col :span="12" >{{ subItem.moduless }}</el-col>
                <el-col :span="12">
                  <i class="el-icon-edit" @click.stop="editItem(subItem)" style="padding: 12px 0px 12px 0px;margin-left: 70px;"></i>
                  <i
                    class="el-icon-delete"
                    style="color:red;"
                    @click.stop="deleteItem(subItem.id)"
                  ></i>
                </el-col>
              </el-row>
            </el-menu-item>
          </el-menu-item-group>
        </el-submenu>
      </el-menu>
    </el-col>
    <el-col :span="18" style="height:100%;overflow-y:auto;padding:10px;">
      <router-view />
    </el-col>
  </el-row>
</template>

<script>
import "../assets/icon/iconfont.css";
import dayjs from "dayjs";

export default {
  data() {
    return {
      isRouterAlive: true
    };
  },
  computed: {
    data() {
      return this.$store.state.menu;
    }
  },
  created() {
    this.updateMenu();
  },
  methods: {
    updateMenu() {
      this.$store.dispatch("fetchMenu");
    },
    addItem(item) {
      this.$prompt("请输入模块名称", `${item.platformname} 添加模块`, {
        confirmButtonText: "确定",
        cancelButtonText: "取消"
      }).then(({ value }) => {
        this.$post(`/api/moduler/`, {
          platform: item.platformname,
          moduless: value,
          createtime: dayjs().format()
        }).then(() => {
          this.updateMenu();
          this.$message({
            type: "success",
            message: "添加成功!"
          });
        });
      });
    },
    editItem(item) {
      this.$prompt("请输入新名称", `修改名称`, {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        inputValue: item.name
      }).then(({ value }) => {
        this.$put(`/api/moduler/${item.id}/`, {
          moduless: value,
          createtime: dayjs().format()
        }).then(() => {
          item.moduless = value;
          this.$message({
            type: "success",
            message: "修改成功!"
          });
        });
      });
    },
    deleteItem(id) {
      this.$confirm("此操作将永久删除该项目, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      }).then(async () => {
        this.$del(`/api/moduler/${id}`).then(() => {
          this.updateMenu();
          this.$message({
            type: "success",
            message: "删除成功!"
          });
        });
      });
    },
    runAll() {
      this.$post(`/api/run/`, {
        createtime: dayjs().format(),
        run_url: "1",
        api_id: "null",
        modular: 15,
        user: localStorage.getItem("uid")
      }).then(() => {
        this.$message({
          type: "success",
          message: "运行成功!"
        });
      });
    },
    selectMenu(id) {
      this.$router.push(`/home/main/list/${id}`);
    }
  }
};
</script>

<style>
.modular_menu {
  height: 100%;
  overflow-y: auto;
}
.form-p {
  position: absolute;
  left: 40px;
  bottom: 25px;
}
</style>
