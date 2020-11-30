import Vue from "vue";
import Router from "vue-router";
import Login1 from "../components/Login1";
import Regediter from "../components/Regediter";
import Home from "../components/Home";
import Main from "../components/Main";
import Project from "../components/Project";
import List from "../components/list";
import Add from "../components/add";
import Edit from "../components/edit";

Vue.use(Router);

const router = new Router({
  routes: [
    {
      path: "/",
      name: "Login1",
      component: Login1
    },
    {
      path: "/login",
      name: "Login1",
      component: Login1
    },
    {
      path: "/regediter",
      name: "Regediter",
      component: Regediter
    },
    {
      path: "/home",
      name: "Home",
      component: Home,
      children: [
        {
          path: "project",
          name: "Project",
          component: Project
        },
        {
          path: "main",
          name: "Main",
          component: Main,
          children: [
            {
              path: "list/:modular/add",
              name: "Project",
              component: Add
            },
            {
              path: "list/:modular/edit/:id",
              name: "Project",
              component: Edit
            },
            {
              path: "list/:id",
              name: "Project",
              component: List
            }
          ]
        }
      ]
    }
  ]
});

router.beforeEach((to, from, next) => {
  const id = window.localStorage.getItem("uid");
  const name = window.localStorage.getItem("name");
  const passList = ["/", "/login", "/regediter"];
  if (passList.indexOf(to.fullPath) === -1 && (!id || !name)) {
    next("/login");
  } else {
    next();
  }
});

export default router;
