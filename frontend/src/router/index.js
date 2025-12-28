import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/Home.vue";
import DashboardView from "../views/Dashboard.vue";

const routes = [
  { path: "/", name: "HomeView", component: HomeView },
  { path: "/dashboard", name: "DashboardView", component: DashboardView }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
