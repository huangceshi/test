<template>
  <div>
    <div class="project-top">
      <el-button
        type="primary"
        @click="runAll"
        style="width: 20%;float: right;margin-left: 10px"
        >运行本模块
      </el-button>
      <el-button
        type="primary"
        @click="runPlatform"
        style="width: 20%; maigin-right: 40px;float: right;"
      >
        运行本平台
      </el-button>
      <el-button type="primary" @click="add" style="width: 20%;float: left;">
        新增用例
      </el-button>
    </div>
    <el-table :data="tableData" height="500px">
      <el-table-column label="序号" prop="id"></el-table-column>
      <el-table-column label="用例名称" prop="casename"></el-table-column>
      <el-table-column label="请求方式" prop="case_type"></el-table-column>
      <el-table-column label="检查点">
        <template slot-scope="scope">
          {{ scope.row.case_check.length > 0 ? "有" : "无" }}
        </template>
      </el-table-column>
      <el-table-column fixed="right" label="操作" width="150">
        <template slot-scope="scope">
          <el-button @click="editItem(scope.row)" type="text" size="small"
            >编辑</el-button
          >
          <el-button @click="deleteItem(scope.row)" type="text" size="small"
            >删除</el-button
          >
          <el-button @click="runOne(scope.row)" type="text" size="small"
            >运行</el-button
          >
        </template>
      </el-table-column>
    </el-table>
    <br />
    <el-pagination
      v-if="list.length > 0"
      background
      layout="prev, pager, next, sizes"
      :current-page="currentPage"
      :page-sizes="sizes"
      :page-size="pageSize"
      :total="list.length"
      style="float:right;"
      @current-change="change"
      @size-change="sizeChange"
    >
    </el-pagination>
  </div>
</template>

<script>
import dayjs from "dayjs";

export default {
  data() {
    return {
      id: this.$route.params.id,
      //如果值是从接口返回的，则为空即可
      tableData: [],
      list: [],
      sizes: [10, 15, 20, 50, 100],
      pageSize: 10,
      currentPage: 1,
      moduler: {
        id: 1,
        platform: "",
        moduless: "",
        status: ""
      }
    };
  },
  created() {
    this.loadData();
  },
  beforeRouteUpdate(to, from, next) {
    this.id = to.params.id;
    this.loadData();
    next();
  },
  computed: {},
  methods: {
    add() {
      this.$router.push(`/home/main/list/${this.id}/add`);
    },
    runAll() {
      this.$post(`/api/run/`, {
        createtime: dayjs().format(),
        run_url: "1",
        api_id: "null",
        modular: this.id,
        user: localStorage.getItem("uid")
      }).then(() => {
        this.$message({
          type: "success",
          message: "运行完成，请查看测试报告"
        });
      });
    },
    runPlatform() {
      console.log(this.moduler);
      this.$post(`/api/run/`, {
        createtime: dayjs().format(),
        run_url: "1",
        api_id: "null",
        modular: this.moduler.id,
        user: localStorage.getItem("uid")
      }).then(() => {
        this.$message({
          type: "success",
          message: "运行完成，请查看测试报告!"
        });
      });
    },
    runOne(item) {
      this.$post(`/api/run/`, {
        createtime: dayjs().format(),
        run_url: "1",
        api_id: item.id,
        modular: this.id,
        user: localStorage.getItem("uid")
      }).then(res => {
        const resStr = res.data[0].runsave[0].replace(/'/g, '"');
        this.$alert(JSON.stringify(JSON.parse(resStr), null, 2), "运行结果", {
          confirmButtonText: "确定"
        });
      });
    },
    sizeChange(size) {
      this.pageSize = size;
      this.change(this.currentPage);
    },
    change(currentPage) {
      this.currentPage = currentPage;
      this.tableData = this.list.slice(
        (currentPage - 1) * this.pageSize,
        currentPage * this.pageSize
      );
    },
    async loadData() {
      this.$post("/api/moduler/one/", {
        id: this.id
      }).then(response => {
        this.moduler = response.data;
      });
      this.$get(`/api/api/?modular=${this.id}`).then(res => {
        res.data.posts.forEach(data => {
          if (data.case_file_name === "null") data.case_file_name = "";
          if (data.case_replace === "null") data.case_replace = [];
          if (data.case_check === "null") data.case_check = [];
          if (data.case_save === "null") data.case_save = [];
          if (data.case_postpostposition === "null")
            data.case_postpostposition = [];

          data.case_replace = JSON.parse(data.case_replace);
          data.case_check = JSON.parse(data.case_check);
          data.case_save = JSON.parse(data.case_save);
          data.case_postpostposition = JSON.parse(data.case_postpostposition);
        });
        this.list = res.data.posts;
        this.change(1);
      });
      this.modular = await this.$store.dispatch("getModularById", this.id);
    },
    deleteItem(item) {
      this.$confirm("此操作将永久删除该数据, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      }).then(() => {
        this.$del(`/api/api/${item.id}/`).then(res => {
          let index = this.list.indexOf(item);
          this.list.splice(index, 1);
          this.change(this.currentPage);
          this.$message({
            type: "success",
            message: "删除成功!"
          });
        });
      });
    },
    editItem(item) {
      this.$router.push(`/home/main/list/${this.id}/edit/${item.id}`);
    }
  }
};
</script>

<style>
.project-top {
  margin-top: 30px;
}
</style>
