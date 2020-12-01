<template>
  <el-form
    :model="form"
    :rules="rules"
    ref="form"
    label-width="100px"
  >
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>请求参数</span>
        <el-button type="primary" @click="back"
          >返回</el-button>
      </div>
      <el-form-item label="接口名称" prop="casename">
        <el-input v-model="form.casename"></el-input>
      </el-form-item>
      <el-form-item label="接口地址" prop="case_url">
        <el-input v-model="form.case_url"></el-input>
      </el-form-item>
      <el-form-item label="请求类型" prop="case_type">
        <el-select v-model="form.case_type" placeholder="请选择请求类型">
          <el-option label="post" value="post"></el-option>
          <el-option label="get" value="get"></el-option>
          <el-option label="delete" value="delete"></el-option>
          <el-option label="put" value="put"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="请求参数" prop="case_data">
        <el-input type="textarea" v-model="form.case_data" @blur='handleInput'></el-input>
        <el-row :gutter="20">
          <el-col :span="8">
            <div>替换参数</div>
          </el-col>
          <el-col :span="8">
            <div>替换值</div>
          </el-col>
          <el-col :span="8">
            <el-button @click='addCaseReplace'>添加</el-button>
          </el-col>
        </el-row>
        <el-row :gutter="20" v-for="(replace,index) in form.case_replace">
            <el-col :span="8" >
              <el-input placeholder="" v-model="replace.key"></el-input>
            </el-col>
            <el-col :span="8">
              <el-input v-model="replace.value"></el-input>
            </el-col>
            <el-col :span="8">
              <el-button @click="deleteCaseReplace(index)">删除</el-button>
            </el-col>
          </el-row>
      </el-form-item>
      <el-form-item label="文件名称" prop="case_file_name">
        <el-input v-model="form.case_file_name"></el-input>
      </el-form-item>
      <el-form-item label="校验参数" prop="name">
        <el-row></el-row>
        <el-row :gutter="20">
          <el-col :span="6" >
            <div>参数路径</div>
          </el-col>
          <el-col :span="6">
             <div>校验方式</div>
          </el-col>
          <el-col :span="6" >
            <div>期望值</div>
          </el-col>
          <el-col :span="6">
            <el-button @click="addCheck">添加</el-button></el-button>
          </el-col>
        </el-row>

        <el-row :gutter="20" v-for="(check, index) in form.case_check">
          <el-col :span="6" >
            <el-input placeholder="" v-model="check.key"></el-input>
          </el-col>
          <el-col :span="6">
            <el-select v-model="check.type" placeholder="请选择校验方式">
              <el-option label="等于" value="check1"></el-option>
              <el-option label="小于" value="check2"></el-option>
              <el-option label="包含" value="check3"></el-option>
              <el-option label="字段长度" value="check4"></el-option>
            </el-select>
          </el-col>
          <el-col :span="6" >
            <el-input placeholder="" v-model="check.value"></el-input>
          </el-col>
          <el-col :span="6">
            <el-button @click="deleteCheck">删除</el-button></el-button>
          </el-col>
        </el-row>
      </el-form-item>
      <el-form-item label="保存参数" prop="name">
        <el-row></el-row>
        <el-row :gutter="20">
          <el-col :span="12" >
            <div>参数名</div>
          </el-col>
          <el-col :span="6" >
            <el-button @click="addSave">添加</el-button>
          </el-col>
        </el-row>
        <el-row :gutter="20" v-for="(save, index) in form.case_save">
          <el-col :span="12" >
            <el-input placeholder="" v-model="save.key"></el-input>
          </el-col>
          <el-col :span="6">
            <el-button @click="deleteSave(index)">删除</el-button></el-button>
          </el-col>
        </el-row>
      </el-form-item>
      <el-form-item label="后置处理" prop="name">
        <el-row></el-row>
        <el-row :gutter="20">
          <el-col :span="8">
            <div>数据库名</div>
          </el-col>
          <el-col :span="8">
            <div>执行语句</div>
          </el-col>
          <el-col :span="8">
            <el-button @click='addPosition'>添加</el-button>
          </el-col>
        </el-row>
        <el-row :gutter="20" v-for="(replace,index) in form.case_postpostposition">
            <el-col :span="8" >
              <el-input placeholder="" v-model="replace.key"></el-input>
            </el-col>
            <el-col :span="8">
              <el-input v-model="replace.value"></el-input>
            </el-col>
            <el-col :span="8">
              <el-button @click="deletePosition(index)">删除</el-button>
            </el-col>
          </el-row>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm"
          >立即创建</el-button
        >
      </el-form-item>
    </el-card>
  </el-form>
</template>

<script>

function isJSON(str) {
    if (typeof str == 'string') {
        try {
            var obj=JSON.parse(str);
            if(typeof obj == 'object' && obj ){
                return true;
            }else{
                return false;
            }

        } catch(e) {
            console.log('error：'+str+'!!!'+e);
            return false;
        }
    }
    return false;
}
import dayjs from "dayjs";

export default {
  name: 'add',
  data() {
    return {
      modular: this.$route.params.modular,
      form: {
        casename: "",
        case_type: "POST",
        case_url: "",
        case_data: "",
        case_replace: [],
        case_file_name: "",
        case_check: [],
        case_save: [],
        case_postpostposition: []
      },
      rules: {
        casename: [
          { required: true, message: "请输入接口名称", trigger: "blur" }
        ],
        case_url: [
          { required: true, message: "请输入接口地址", trigger: "blur" }
        ],
        case_type: [
          { required: true, message: "请选择请求类型", trigger: "change" }
        ],
        case_data: [
          { required: true, message: "请求参数不能为空", trigger: "change" }
        ],
      }
    };
  },
  beforeRouteUpdate(to, from, next) {
    this.modular = to.params.modular;
    next();
  },
  methods: {
    back() {
      this.$router.back();
    },
    saveData() {
    },
    submitForm() {
      this.$refs['form'].validate(valid => {
        if (valid) {
          const {
            casename,
            case_type,
            case_url,
            case_data,
            case_replace,
            case_file_name,
            case_check,
            case_save,
            case_postpostposition
          } = this.form;
          const modular = this.modular;
          this.$post(`/api/api/`, {
            casename,
            case_type,
            case_url,
            case_data,
            case_replace: JSON.stringify(case_replace),
            case_file_name: case_file_name?case_file_name: 'null',
            case_check: JSON.stringify(case_check),
            case_save: JSON.stringify(case_save),
            case_postpostposition: JSON.stringify(case_postpostposition),
            case_createtime: dayjs().format(),
            modular
          }).then(res => {
            this.$router.push(`/home/main/list/${this.modular}`)
          });
        } else {
          return false;
        }
      });
    },
    submitUpload() {
      this.$refs.upload.submit();
    },
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    handlePreview(file) {
      console.log(file);
    },
    handleInput() {
      if(isJSON(this.case_data)) {
        console.log('json 格式');
      }
    },
    addCaseUrl() {
      this.form.case_replace.push({key: 'key', value: ''});
    },
    addSave(){
      this.form.case_save.push({key:''});
    },
    deleteSave(index){
      this.form.case_save.splice(index, 1)
    },
    addCheck(){
      this.form.case_check.push({key:'', type:'check1', value: ''});
    },
    deleteCheck(index){
      this.form.case_check.splice(index, 1)
    },
    addCaseReplace(){
      this.form.case_replace.push({key:'', value:''});
    },
    deleteCaseReplace(index){
      this.form.case_replace.splice(index, 1)
    },
    addPosition(){
      this.form.case_postpostposition.push({key:'', value:''});
    },
    deletePosition(index) {
      this.form.case_postpostposition.splice(index, 1)
    }
  }
};
</script>
