<template>
  <div :class="['dashboard-container', darkTheme ? 'dark' : 'light']">
    <div class="header">
      <h2 class="dashboard-title">Task Management</h2>
      <div class="header-actions">
        <input type="text" v-model="searchQuery" placeholder="Search tasks..." class="search-input" />
        <select v-model="filterStatus" class="filter-select">
          <option value="">All Status</option>
          <option>To Do</option>
          <option>In Progress</option>
          <option>Done</option>
        </select>
        <select v-model="sortBy" class="sort-select">
          <option value="">Sort By</option>
          <option value="title">Title (A-Z)</option>
          <option value="status">Status</option>
        </select>
        <select v-model="pageSize" class="page-size-select">
          <option :value="6">6 per page</option>
          <option :value="12">12 per page</option>
          <option :value="24">24 per page</option>
        </select>
        <button @click="toggleTheme" class="theme-btn">{{ darkTheme ? '🌞 Light Mode' : '🌙 Dark Mode' }}</button>
        <button @click="logout" class="logout-btn">Logout</button>
      </div>
    </div>

    <transition name="toast-fade">
      <div v-if="toastMessage" class="toast">{{ toastMessage }}</div>
    </transition>

    <TaskFormComponent @task-created="fetchTasks" :darkTheme="darkTheme" />

    <div class="task-list" @dragover.prevent @drop="onDrop($event, null)">
      <template v-if="paginatedTasks.length === 0">
        <div class="empty-state">No tasks found.</div>
      </template>
      <div
        v-for="(task, index) in paginatedTasks"
        :key="task[0]"
        class="task-card"
        :class="{ 'drag-over': dragOverIndex === index }"
        draggable="true"
        @dragstart="onDragStart($event, index)"
        @dragover.prevent="dragOverIndex = index"
        @drop="onDrop($event, index)"
      >
        <template v-if="editingId !== task[0]">
          <div class="task-content">
            <strong>{{ task[1] }}</strong> - 
            <span class="task-desc">{{ task[2] }}</span>
            <span :class="statusClass(task[3])">&nbsp;({{ task[3] }})</span>
            <div class="task-timestamp">Last Updated: {{ formatDate(task[4]) }}</div>
          </div>
          <div class="task-actions">
            <button class="edit-btn" @click="startEdit(task[0])">Edit</button>
            <button class="delete-btn" @click="openDelete(task[0])">Delete</button>
          </div>
        </template>

        <TaskFormEdit
          v-else
          :task="task"
          :darkTheme="darkTheme"
          @task-updated="finishEdit"
          @cancel="cancelEdit"
        />
      </div>
    </div>

    <div class="pagination" v-if="totalPages > 1">
      <button @click="prevPage" :disabled="currentPage === 1">Prev</button>
      <button
        v-for="page in totalPages"
        :key="page"
        @click="goToPage(page)"
        :class="{ active: page === currentPage }"
      >
        {{ page }}
      </button>
      <button @click="nextPage" :disabled="currentPage === totalPages">Next</button>
    </div>

    <ConfirmModal
      :show="confirmVisible"
      :darkTheme="darkTheme"
      message="Are you sure you want to delete this task?"
      @cancel="cancelDelete"
      @confirm="deleteNow"
    />
  </div>
</template>

<script>
import TaskFormComponent from "../components/TaskForm.vue";
import TaskFormEdit from "../components/TaskFormEdit.vue";
import ConfirmModal from "../components/ConfirmModal.vue";
import axios from "axios";

export default {
  name: "DashboardView",
  components: { TaskFormComponent, TaskFormEdit, ConfirmModal },
  data() {
    return {
      tasks: [],
      editingId: null,
      confirmVisible: false,
      selectedDeleteId: null,
      darkTheme: localStorage.getItem("darkTheme") === "true",
      searchQuery: "",
      filterStatus: "",
      currentPage: 1,
      pageSize: 6,
      sortBy: "",
      dragIndex: null,
      dragOverIndex: null,
      toastMessage: "",
    };
  },
  computed: {
    filteredTasks() {
      let filtered = this.tasks;
      if (this.searchQuery) {
        const q = this.searchQuery.toLowerCase();
        filtered = filtered.filter(t => t[1].toLowerCase().includes(q) || t[2].toLowerCase().includes(q));
      }
      if (this.filterStatus) filtered = filtered.filter(t => t[3] === this.filterStatus);
      if (this.sortBy === "title") filtered.sort((a,b) => a[1].localeCompare(b[1]));
      else if (this.sortBy === "status") {
        const order = ["To Do","In Progress","Done"];
        filtered.sort((a,b)=> order.indexOf(a[3])-order.indexOf(b[3]));
      }
      return filtered;
    },
    totalPages() { return Math.ceil(this.filteredTasks.length / this.pageSize); },
    paginatedTasks() {
      const start = (this.currentPage-1)*this.pageSize;
      return this.filteredTasks.slice(start,start+this.pageSize);
    }
  },
  watch: { darkTheme(val){ localStorage.setItem("darkTheme",val); } },
  created() { this.ensureLogin(); this.fetchTasks(); },
  methods: {
    ensureLogin() { if(!localStorage.getItem("token")) this.$router.push({name:"HomeView"}); },
    async fetchTasks() {
      try {
        const token = localStorage.getItem("token");
        const response = await axios.get("http://127.0.0.1:5000/api/tasks",{headers:{Authorization:`Bearer ${token}`}});
        this.tasks = response.data;
        localStorage.setItem("taskBackup", JSON.stringify(this.tasks));
      } catch(err){ console.error(err); const backup = localStorage.getItem("taskBackup"); if(backup) this.tasks = JSON.parse(backup); }
    },
    startEdit(id){ this.editingId=id; },
    cancelEdit(){ this.editingId=null; },
    finishEdit(){ this.editingId=null; this.fetchTasks(); },
    openDelete(id){ this.selectedDeleteId=id; this.confirmVisible=true; },
    cancelDelete(){ this.confirmVisible=false; },
    async deleteNow() {
      try {
        const token = localStorage.getItem("token");
        await axios.delete(`http://127.0.0.1:5000/api/tasks/${this.selectedDeleteId}`,{headers:{Authorization:`Bearer ${token}`}});
        this.fetchTasks(); this.showToast("Task deleted!");
      } catch(err){ console.error(err); this.showToast("Delete failed!"); } finally { this.confirmVisible=false; }
    },
    statusClass(status){ return {"To Do":"status-todo","In Progress":"status-progress","Done":"status-done"}[status]||""; },
    logout(){ localStorage.removeItem("token"); this.$router.push({name:"HomeView"}); },
    toggleTheme(){ this.darkTheme=!this.darkTheme; },
    showToast(msg){ this.toastMessage=msg; setTimeout(()=>this.toastMessage="",2500); },
    nextPage(){ if(this.currentPage<this.totalPages) this.currentPage++; },
    prevPage(){ if(this.currentPage>1) this.currentPage--; },
    goToPage(page){ this.currentPage=page; },
    onDragStart(e,i){ this.dragIndex=i; },
    onDrop(e,i){
      if(this.dragIndex===null) return;
      const moved=this.tasks.splice(this.dragIndex,1)[0];
      if(i===null||i===this.tasks.length) this.tasks.push(moved);
      else this.tasks.splice(i,0,moved);
      this.dragIndex=null; this.dragOverIndex=null;
      localStorage.setItem("taskBackup",JSON.stringify(this.tasks));
      this.showToast("Task reordered!");
    },
    formatDate(str){ const d=new Date(str); return isNaN(d)?"N/A":d.toLocaleString(); }
  }
};
</script>

<style scoped>
.dashboard-container {max-width:1000px;margin:20px auto;padding:24px;border-radius:12px;background:#fafafa;color:#222;transition:background 0.3s,color 0.3s;}
.dark {background:#2b2b2b;color:#eee;}
.dashboard-title{margin-bottom:10px;}
.header{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;margin-bottom:20px;gap:10px;}
.header-actions{display:flex;flex-wrap:wrap;gap:10px;}
.search-input,.filter-select,.sort-select,.page-size-select{padding:6px 10px;border-radius:6px;border:1px solid #ccc;background:#fff;color:#222;}
.dark .search-input,.dark .filter-select,.dark .sort-select,.dark .page-size-select{background:#444;color:#eee;border:1px solid #666;}
.logout-btn,.theme-btn,.edit-btn,.delete-btn{padding:6px 12px;border:none;border-radius:6px;cursor:pointer;}
.logout-btn{background:#e63946;color:white;} .theme-btn{background:#555;color:white;} .edit-btn{background:#0077b6;color:white;} .delete-btn{background:#d90429;color:white;}
.task-list{display:flex;flex-direction:column;gap:12px;margin-top:20px;}
.task-card{padding:14px;background:#fff;border-radius:10px;box-shadow:0 2px 6px rgba(0,0,0,0.1);cursor:grab;display:flex;flex-direction:column;justify-content:space-between;transition:transform 0.2s,background 0.2s;}
.task-card.drag-over{transform:scale(1.02);background-color:#ffd;}
.dark .task-card{background:#3b3b3b;color:#eee;}
.task-content{margin-bottom:10px;}
.task-desc{margin-right:6px;}
.status-todo{color:orange;font-weight:600;}
.status-progress{color:royalblue;font-weight:600;}
.status-done{color:green;font-weight:600;}
.task-actions{display:flex;gap:8px;}
.task-timestamp{font-size:0.7rem;color:#555;margin-top:6px;}
.empty-state{padding:20px;text-align:center;color:#888;font-style:italic;}
.pagination{margin-top:20px;display:flex;justify-content:center;gap:5px;flex-wrap:wrap;}
.pagination button{padding:6px 10px;border-radius:6px;border:none;cursor:pointer;}
.pagination button.active{background:#0077b6;color:white;}
.pagination button:disabled{opacity:0.5;cursor:not-allowed;}
.toast{position:fixed;bottom:20px;right:20px;background:#0077b6;color:white;padding:10px 14px;border-radius:8px;z-index:1000;box-shadow:0 2px 6px rgba(0,0,0,0.2);}
.toast-fade-enter-active,.toast-fade-leave-active{transition:opacity 0.3s;}
.toast-fade-enter-from,.toast-fade-leave-to{opacity:0;}
@media(max-width:768px){.task-list{flex-direction:column;}}
</style>
