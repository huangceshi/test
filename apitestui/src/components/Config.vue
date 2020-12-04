<template>
  <div>
    <div>
      <el-row style="padding: 10px 0 0 10px;">
          <el-button  type="primary" @click="dialogFormVisible = true  ">新增环境配置</el-button>

          <el-dialog title="请输入配置信息" :visible.sync="dialogFormVisible">
            <el-form :model="form" ref="form" :rules="rules">
              <el-form-item label="配置名称" prop="key"  :label-width="formLabelWidth">
                <el-input v-model="form.key"  autocomplete="off"></el-input>
              </el-form-item>
              <el-form-item label="配置值" prop="value" :label-width="formLabelWidth">
                <el-input v-model="form.value"  autocomplete="off"></el-input>
              </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button @click="cancel">取 消</el-button>
              <el-button type="primary" @click="add('form')">确 定</el-button>
            </div>
          </el-dialog>
      </el-row>
    </div>


    <el-table :data="tableData" height="500px">
      <el-table-column label="序号" prop="id" width="50"></el-table-column>
      <el-table-column label="配置名称" prop="key"width="150"></el-table-column>
      <el-table-column label="配置项" prop="value" ></el-table-column>
      <el-table-column fixed="right" label="操作" width="150">
        <template fixed="right" slot-scope="scope">
          <el-button @click="editbuttun(scope.row)"  type="text" size="small"
            >编辑</el-button>
          <el-button @click="deleteItem(scope.$index,scope.row,tableData)" type="text" size="small"
            >删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <div>
      <el-dialog title="请修改配置信息" :visible.sync="dialogFormVisibleedit">
            <el-form :model="formedit" ref="formedit" :rules="rules">
              <el-form-item label="配置名称" prop="key"  :label-width="formLabelWidth">
                <el-input v-model="formedit.key"  autocomplete="off"></el-input>
              </el-form-item>
              <el-form-item label="配置值" prop="value" :label-width="formLabelWidth">
                <el-input v-model="formedit.value"  autocomplete="off"></el-input>
              </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button @click="canceledit">取 消</el-button>
              <el-button type="primary" @click="addedit(formedit)">确 定</el-button>
            </div>
          </el-dialog>
    </div>

  </div>
</template>

<script>
import dayjs from "dayjs";
import {put} from "../util/http";

export default {
  data() {
    return {
      //如果值是从接口返回的，则为空即可
      tableData: [],
      list: [],
      dialogFormVisible: false,
      dialogFormVisibleedit: false,
      form: {
          key: '',
          value: '',
        },
      formedit: {
        id:'',
        key: '',
        value: '',
      },
      formLabelWidth: '120px',
      rules: {
        key: [{ required: true, message: "不能为空", trigger: "blur" }],
        value: [{ required: true, message: "不能为空", trigger: "blur" }]
      }
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
    editbuttun(row){
      this.dialogFormVisibleedit = true;
      this.formedit = row
      alert(formedit.id)
    },
    canceledit(){
      this.dialogFormVisibleedit = false;
      this.formedit={brand_right:0}
    },
    addedit(item) {
      this.dialogFormVisibleedit = false;
      this.$refs["formedit"].validate(valid => {
        if (valid) {
          this.$put(`/api/config/${item.id}/`, this.formedit)
            .then(res => {
              if(res.status_code === 200){
                this.formedit={brand_right:0}
                this.$message({
                message: '修改成功',
                type: "success"
              });
              }
              this.$router.push("/home/config")
            })
            .catch(err => {
              this.$message({
                message: err,
                type: "error"
              });
            });
        }
      });
    },
    cancel(){
      this.dialogFormVisible = false;
      this.form={brand_right:0}
    },
    add(form) {
      this.dialogFormVisible = false;
      this.$refs["form"].validate(valid => {
        if (valid) {
          this.$post("/api/config/", this.form)
            .then(res => {
              if(res.status_code === 200){
                let newValue = res.data
                this.tableData.push(newValue);
                this.form={brand_right:0}
                // this.$router.go(0)
                this.$message({
                message: '创建成功',
                type: "success"
              });
              }
              this.$router.push("/home/config")
            })
            .catch(err => {
              this.$message({
                message: err,
                type: "error"
              });
            });
        }
      });
    },
  deleteItem(index,row,list) {
      this.$confirm('确定删除配置名称为【'+ row.key +'】的配置项吗？', "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      }).then(() => {
        this.$del(`/api/config/${row.id}/`).then(res => {
          list.splice(index, 1);
          this.$message({
            type: "success",
            message: "删除成功!"
          });
        });
      });
    },
}
};
</script>

<style>
  .msgBox {
  max-height: 550px;
  overflow-y: auto;

  width: 60%;
  height: 60%;
}
  .project-top {
    margin-top: 30px;
  }
</style>
