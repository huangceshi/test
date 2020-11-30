<template>
  <div>
    <div class="project-top">
      <el-form inline label-position="right" label-width="80px" class="query-form">
        <el-form-item label="项目名称" prop="name">
          <el-input></el-input>
        </el-form-item>
      </el-form>
    </div>
    <el-table :data="tableData" :row-class-name="rowClassName">
      <el-table-column label="序号" prop="tid"></el-table-column>
      <el-table-column label="项目名称" prop="name">
        <template slot-scope="scope">
          <el-input v-if="scope.row.isSelected" v-model="scope.row.name"
                     @focus="focusEvent(scope.row)"
                     @blur="blurEvent(scope.row)"></el-input>
          <p v-else @click="cellClick(scope.row)">{{scope.row.name}}</p>
        </template>

      </el-table-column>
      <el-table-column label="负责人" prop="principal">
        <template slot-scope="scope">
          <el-input v-if="scope.row.isSelected" v-model="scope.row.principal"
                     @focus="focusEvent(scope.row)"
                     @blur="blurEvent(scope.row)"></el-input>
          <p v-else @click="cellClick(scope.row)">{{scope.row.principal}}</p>
        </template>

      </el-table-column>
      <el-table-column label="当前环境" prop="environment">
        <template slot-scope="scope">
          <el-select v-model="scope.row.environment.name">
            <el-option
              v-for="item in runenvironment"
              :key="item.name"
              :label="item.name"
              :value="item.name">
            </el-option>
          </el-select>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button type="primary"
                     v-if="scope.$index === tableData.length-1"
                     @click="addLine" class="el-icon-document-add">添加</el-button>
          <el-button type="danger"
                     v-if="tableData.length>1"
                     @click="handleDelete(scope.$index,scope.row)" class="el-icon-delete">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

  </div>
</template>

<script>
export default {
  data(){
   return{
      tableData:[],
      runenvironment:[
        {
          name:'测试环境',
          value:'http://127.0.0.1:8000/api'
        },
        {
          name:'运行环境',
          value:'http://huice.huicewang.com'
        }
      ]
   }
  },
  mounted() {
    this.loadData();
  },
  methods:{
    handleDelete(index,row){
      this.tableData.splice(index,1);
      // 判断数据是否为新添加的数据
      if(typeof(row.id) ==='undefined'){

      }
    },
    addLine(){
      let newValue={
        name:'慧测',
        environment:{
          name:'测试环境',
          value:'http://127.0.0.1:8000/api/'
        },
        principal:'田老师',
        isSelected:true
      };
      this.tableData.push(newValue);
    },
    cellClick(row){
      row.isSelected = !row.isSelected;
    },
    blurEvent(row){
      row.isSelected = !row.isSelected;
      //逻辑判断
      //修改数据
      //添加数据
    },
    focusEvent(row){
      row.oldName = row.name;
      row.oldPrincipal = row.principal;
      row.oldEnvironment = row.environment;
    },
    rowClassName({row,rowindex}){
      row.tid = rowindex + 1;
    },
    loadData(){
      this.$get('project/')
      .then(res=>{
        this.tableData = res.data.map(item=>{
          return{ ...item,isSelected:false}
        });
      });
    }
  }
}

</script>

<style>
  .project-top {
    margin-top: 30px;
  }
</style>
