<template>
  <div>
    <el-button type="text" @click="dialogFormVisible = true">打开嵌套表单的 Dialog</el-button>

      <el-dialog title="请输入配置信息" :visible.sync="dialogFormVisible">
        <el-form :model="form">
          <el-form-item label="配置名称" :label-width="formLabelWidth">
            <el-input v-model="form.key" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="配置值" :label-width="formLabelWidth">
            <el-input v-model="form.value" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
        </div>
      </el-dialog>
  </div>
</template>

<script>
    export default {
        name: "tests",
        data() {
    return {
      dialogTableVisible: false,
      dialogFormVisible: false,
      form: {
          name: '',
          value: '',
        },
        formLabelWidth: '120px'


    };
  },
    }
</script>

<style scoped>

</style>
