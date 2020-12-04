<template>
  <div>
    <div>
      <el-row style="padding: 10px 0 0 10px;">
          <el-button type="primary" @click="add" style="width: 10%"
            >新增环境配置</el-button
          >
      </el-row>
    </div>


    <el-table :data="tableData" height="500px">
      <el-table-column label="序号" prop="id" width="50"></el-table-column>
      <el-table-column label="配置名称" prop="key"width="150"></el-table-column>
      <el-table-column label="配置项" prop="value" ></el-table-column>
      <el-table-column fixed="right" label="操作" width="150">
        <template slot-scope="scope">
          <el-button @click="editItem(scope.row)" type="text" size="small"
            >编辑</el-button
          >
          <el-button @click="deleteItem(scope.row)" type="text" size="small"
            >删除</el-button
          >
        </template>
      </el-table-column>
    </el-table>

  </div>
</template>

<script>
import dayjs from "dayjs";

export default {
  data() {
    return {
      //如果值是从接口返回的，则为空即可
      tableData: []

    };
  },
  created() {
    this.loadData();
  },

  methods: {

    loadData() {
      this.$get("/api/config/")
        .then(res=>{
          this.tableData = res.data.posts
        })
    },
    add(item){
      this.$prompt("请输入模块名称", `添加模块`, {
        confirmButtonText: "确定",
        cancelButtonText: "取消"
      }).then(({ value }) => {
        this.$post(`/api/moduler/`, {
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
  }
};
</script>

<style>
.project-top {
  margin-top: 30px;
}
</style>
