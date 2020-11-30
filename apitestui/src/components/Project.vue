<template>
  <div>
    <div class="project-top">
      <el-form
        inline
        label-position="right"
        label-width="80px"
        class="query-form"
      >
        <el-form-item label="项目名称" prop="name">
          <el-input></el-input>
        </el-form-item>
      </el-form>
    </div>
    <el-table :data="dableData">
      <el-table-column label="序号" prop="id"></el-table-column>
      <el-table-column label="项目名称" prop="name"></el-table-column>
      <el-table-column label="负责人" prop="principal"></el-table-column>
      <el-table-column label="当前环境" prop="environment"></el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      //如果值是从接口返回的，则为空即可
      dableData: [
        {
          id: 1,
          name: "慧测",
          environment: "测试环境",
          principal: "崔创"
        }
      ]
    };
  },
  // mounted(){
  //   this.loadData();
  // },
  methods: {
    loadData() {
      this.$get("project/").then(res => {
        this.tableData = res.data;
      });
    }
  }
};
</script>

<style>
.project-top {
  margin-top: 30px;
}
</style>
