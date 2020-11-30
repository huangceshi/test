import Vue from "vue";
import Vuex from "vuex";
import { get, post, del, put, patch } from "@/util/http";

Vue.use(Vuex);

const idToName = new Map();
const store = new Vuex.Store({
  state: {
    menu: [
      {
        id: 1,
        platformname: "基础业务线",
        lists: [
          {
            id: 16,
            platform: "基础业务线",
            moduless: "模块1",
            status: "1",
            createtime: "2020-11-10T16:39:00"
          },
          {
            id: 17,
            platform: "基础业务线",
            moduless: "模块2",
            status: "1",
            createtime: "2020-11-10T16:39:00"
          },
          {
            id: 18,
            platform: "基础业务线",
            moduless: "模块3",
            status: "1",
            createtime: "2020-11-10T16:39:00"
          },
          {
            id: 19,
            platform: "基础业务线",
            moduless: "模块4",
            status: "1",
            createtime: "2020-11-10T16:39:00"
          },
          {
            id: 22,
            platform: "基础业务线",
            moduless: "模块5",
            status: "1",
            createtime: "2020-11-10T16:39:00"
          },
          {
            id: 23,
            platform: "基础业务线",
            moduless: "模块6",
            status: "1",
            createtime: "2020-11-10T16:39:00"
          },
          {
            id: 24,
            platform: "基础业务线",
            moduless: "模块7",
            status: "1",
            createtime: "2020-11-10T16:39:00"
          },
          {
            id: 25,
            platform: "基础业务线",
            moduless: "模块8",
            status: "1",
            createtime: "2020-11-10T16:39:00"
          },
          {
            id: 26,
            platform: "基础业务线",
            moduless: "模块9",
            status: "1",
            createtime: "2020-11-10T16:39:00"
          },
          {
            id: 27,
            platform: "基础业务线",
            moduless: "模块10",
            status: "1",
            createtime: "2020-11-10T16:39:00"
          },
          {
            id: 30,
            platform: "基础业务线",
            moduless: "模块13",
            status: "1",
            createtime: "2020-11-10T16:39:00"
          },
          {
            id: 31,
            platform: "基础业务线",
            moduless: "模块14",
            status: "1",
            createtime: "2020-11-10T16:39:00"
          },
          {
            id: 32,
            platform: "基础业务线",
            moduless: "模块15",
            status: "1",
            createtime: "2020-11-10T16:39:00"
          },
          {
            id: 33,
            platform: "基础业务线",
            moduless: "模块16",
            status: "1",
            createtime: "2020-11-10T16:39:00"
          }
        ]
      },
      {
        id: 2,
        platformname: "外教业务线",
        lists: [
          {
            id: 28,
            platform: "外教业务线",
            moduless: "模块11",
            status: "1",
            createtime: "2020-11-10T16:39:00"
          }
        ]
      },
      {
        id: 3,
        platformname: "用户端业务线",
        lists: [
          {
            id: 29,
            platform: "用户端业务线",
            moduless: "模块12",
            status: "1",
            createtime: "2020-11-10T16:39:00"
          }
        ]
      },
      { id: 4, platformname: "教学业务线", lists: "" },
      { id: 5, platformname: "增长业务线", lists: "" },
      { id: 6, platformname: "活动课件", lists: "" },
      { id: 7, platformname: "课程顾问", lists: "" },
      { id: 8, platformname: "备用业务线1", lists: "" },
      { id: 9, platformname: "备用业务线2", lists: "" }
    ]
  },
  getters: {
    getDemoValue: state => state.demoValue
  },
  mutations: {
    increment(state) {
      state.count++;
    }
  },
  actions: {
    getModularById(state, id) {
      return Promise.resolve(idToName.get(Number(id)));
    },
    async fetchMenu() {
      const res = await get("/api/moduler/all/", this.dataForm);
      if (res.code !== 200) return;
      store.state.menu = res.data;
      res.data.forEach(item => {
        item.lists &&
          item.lists.forEach(value => {
            idToName.set(value.id, value);
          });
      });
    }
  }
});

export default store;
