<template>
  <div class="task-list-container">
    <h3 class="title">📝 Task List</h3>

    <ul class="task-ul">
      <li v-for="task in tasks" :key="task[0]" class="task-item">
        <div v-if="editingId !== task[0]" class="task-row">
          <div>
            <strong class="task-title">{{ task[1] }}</strong>
            <span class="task-desc"> - {{ task[2] }} </span>
            <span class="task-status"> ({{ task[3] }})</span>
          </div>

          <div class="btn-actions">
            <button class="btn-edit" @click="startEdit(task[0])">Edit</button>
            <button class="btn-del" @click="askDelete(task[0])">Delete</button>
          </div>
        </div>

        <!-- Edit Form -->
        <TaskFormEdit
          v-else
          :task="task"
          @task-updated="finishEdit"
          @cancel="cancelEdit"
        />
      </li>
    </ul>
  </div>
</template>

<script>
import TaskFormEdit from "./TaskFormEdit.vue";

export default {
  name: "TaskList",
  props: ["tasks"],
  components: { TaskFormEdit },
  data() {
    return {
      editingId: null
    };
  },
  emits: ["ask-delete", "refresh"],
  methods: {
    startEdit(id) {
      this.editingId = id;
    },
    cancelEdit() {
      this.editingId = null;
    },
    finishEdit() {
      this.editingId = null;

      // Show toast popup
      window.dispatchEvent(new CustomEvent("toast", { detail: "Task updated!" }));

      // Refresh task from parent
      this.$emit("refresh");
    },
    askDelete(id) {
      // Emit ke Dashboard → akan muncul popup confirm
      this.$emit("ask-delete", id);
    }
  }
};
</script>

<style scoped>
.task-list-container {
  margin-top: 10px;
}

.title {
  margin: 0 0 8px;
  font-size: 18px;
  font-weight: 600;
}

.task-ul {
  list-style: none;
  padding: 0;
}

.task-item {
  background: #ffffff;
  padding: 10px;
  border-radius: 6px;
  margin-bottom: 8px;
  border: 1px solid #dcdcdc;
  display: flex;
  flex-direction: column;
}

.task-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.task-title {
  font-size: 16px;
  font-weight: 600;
}
.task-desc {
  margin-left: 4px;
}
.task-status {
  opacity: 0.7;
  margin-left: 4px;
}

.btn-actions {
  display: flex;
  gap: 6px;
}

.btn-edit,
.btn-del {
  padding: 4px 8px;
  border-radius: 4px;
  border: none;
  cursor: pointer;
}

.btn-edit {
  background: #0074ff;
  color: white;
}

.btn-del {
  background: #d90000;
  color: white;
}
</style>
