<template>
  <div>
    <div class="project-top">
      <el-form inline :model="query" label-position="right" label-width="80px" class="query-form">
        <el-form-item label="项目名称" prop="name">
          <el-input v-model="query.name" placeholder="请输入要查询的项目名称"
                    @input="search" style="width: 400px"></el-input>
        </el-form-item>
      </el-form>
    </div>

      <el-table :data="tableData" highlight-current-row class="table" stripe border
                :row-class-name="rowClassName">
        <el-table-column prop="tid" label="序号" width="130"></el-table-column>
        <el-table-column prop="name" label="项目名称">
          <template slot-scope="scope">
             <el-input v-if="scope.row.isSelected" v-model="scope.row.name"
                        @focus="focusEvent(scope.row)"
                        @blur="blurEvent(scope.row)" placeholder="请输入项目名称" ></el-input>
              <p v-else @click="cellClick(scope.row)" >{{scope.row.name}}</p>
          </template>

        </el-table-column>

        <el-table-column prop="principal" label="负责人" width="200">
           <template slot-scope="scope">
            <el-input v-if="scope.row.isSelected" v-model="scope.row.principal"
                      @focus="focusEvent(scope.row)"
                      @blur="blurEvent(scope.row)" placeholder="请输入负责人" ></el-input>
            <p v-else @click="cellClick(scope.row)" >{{scope.row.principal}}</p>
          </template>

        </el-table-column>

        <el-table-column prop="environment" label="当前环境" width="350">
          <template slot-scope="scope">
          <el-select v-model="scope.row.environment"
                     @change="selectItem(scope.row)" placeholder="请选择">
              <el-option
                v-for="item in runenvironment"
                :key="item.name"
                :label="item.name"
                :value="item">
              </el-option>
            </el-select>
          </template>
        </el-table-column>

        <el-table-column label="操作" align="center" width="300">
           <template slot-scope="scope">
             <el-button
               @click="addLine"
               type="primary"
               v-if="scope.$index === tableData.length - 1" class="el-icon-document-add"
             >添加</el-button>

             <el-button
               type="danger"
               v-if="tableData.length > 1"
               @click="handleDelete(scope.$index,scope.row)"
               class="el-icon-delete"
             >删除</el-button>
           </template>
         </el-table-column>
      </el-table>
  </div>
</template>

<script>
  export default {
    data(){
      return {
        tableData: [],
        query:{
          name:''
        },
        runenvironment: [{
          name:'测试环境',
          value:'http://127.0.0.1:8000/api'
        },{
          name:'线上环境',
          value:'http://www.huicewang.com'
        }]
      }
    },
    mounted() {
      this.loadData();
    },
    directives: {
        focus: {
          inserted: function (el) {
            el.querySelector('input').focus()
          }
        }
      },
    methods: {
      loadData(){
        let name = '';
        if(this.query.name !==''){
          name = '?name=' + this.query.name
        }
        this.$get('project/'+name)
        .then(res=>{
          this.tableData = res.data.map(item=>{
            return {...item, isSelected:false}
          });
        })
      },

      addData(row){
        var self = this;
        self.$post('project/',row)
          .then(res=>{
            if(res.code === 201){
                self.$message({
                message: '数据添加成功',
                type: 'success',
                duration: 1000
              });
              self.loadData();
            }
          })
          .catch(error=> {
            self.$message({
              message: '数据添加失败，请检查项目名称是否重复',
              type: 'error'
            });
            console.log(error);
          });
      },
      deleteData(row){
        var self = this;
        self.$del('project/'+row.id + '/')
          .then(res=>{
            if(res.status === 204){
                self.$message({
                message: '数据删除成功',
                type: 'success',
                duration: 1000
              });
            }
          })
          .catch(function (error) {
            self.$message({
              message: '数据已取消删除',
              type: 'error'
            });
            console.log(error);
          });
      },
      updateData(row){
        var self = this;
        self.$put('project/'+row.id + '/',row)
          .then(res=>{
            if(res.code === 200){
                self.$message({
                message: '数据修改成功',
                type: 'success',
                duration: 1000
              });
              this.loadData();
            }
          })
          .catch(function (error) {
            self.$message({
              message: '项目名称不能重复',
              type: 'error'
            });
            row.name = row.oldName;
            console.log(error);
          });
      },
      // ------------------以下为界面事件处理------------------
      search(){
        this.loadData();
      },
      // 更新项目环境信息
      selectItem(row){
        if(typeof(row.id) == 'undefined'){
          this.addData(row);
        }else{
          this.updateData(row);
        }
      },
      cellClick (row) {
        row.isSelected = !row.isSelected
      },
      focusEvent (row) {
        row.oldName = row.name
        row.oldPrincipal = row.principal
        row.oldEnvironment = row.environment
      },
      // 更新项目名称或负责人
      blurEvent (row) {
        row.isSelected = !row.isSelected

        if(row.name.length === 0){
          this.$message({
            message: '项目名称不能为空',
            type: 'error',
            duration: 1000
          })
          row.isSelected = true;
          row.name = row.oldName;
          return;
        }
        if(row.principal.length === 0){
          this.$message({
            message: '负责人不能为空',
            type: 'error',
            duration: 1000
          })
          row.isSelected = true;
          row.principal = row.oldPrincipal;
          return;
        }

          // 添加数据
        if(typeof(row.id) == 'undefined'){
          this.addData(row);
        }else{
            // 修改数据
           if (row.name !== row.oldName || row.principal !== row.oldPrincipal) {
            this.updateData(row);
          }
        }
      },

      // 设置序号列
      rowClassName({row, rowIndex}) {
          //把每一行的索引放进row.tid
          row.tid = rowIndex+1;
        },

      addLine() {
        //添加行数
        let newValue = {
          name: "慧测"+Date.parse(new Date()),
          environment: {
            name:"测试环境",
            value:'http://127.0.0.1:8000/api'
          },
          principal: "田老师",
          isSelected: true
        };
        //添加新的行数
        this.tableData.push(newValue);
    },
      /** 删除按钮操作 */
    handleDelete(index,row) {
      // 未保存数据处理
      if(typeof(row.id) == 'undefined'){
        this.tableData.splice(index,1);
        return;
      }
      this.$confirm(
        '确定删除项目名称为【'+ row.name +'】的项目吗？',
        "警告",
        {
          confirmButtonText: "确定",
          cancelButtonText: "取消",
          type: "warning"
          }
        )
        .then(()=> {
          this.deleteData(row);
        })
        .then(() => {
          this.tableData.splice(index,1);
        })
    },
    }
  }
</script>

<style>
  .project-top {
    margin-top: 15px;
  }
</style>
