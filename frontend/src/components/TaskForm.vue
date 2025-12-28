<template>
  <div :class="['task-form-wrapper', darkTheme ? 'dark' : 'light']">
    <h3 class="form-title">Create Task</h3>

    <form @submit.prevent="createTask" class="task-form">
      <div class="form-group">
        <label>Title</label>
        <input
          v-model="title"
          :class="{ 'input-error': titleError }"
          placeholder="Enter task title"
        />
        <small v-if="titleError" class="error-msg">{{ titleError }}</small>
      </div>

      <div class="form-group">
        <label>Description</label>
        <textarea
          v-model="description"
          :class="{ 'input-error': descriptionError }"
          placeholder="Enter task description"
        ></textarea>
        <small v-if="descriptionError" class="error-msg">{{ descriptionError }}</small>
      </div>

      <div class="form-group">
        <label>Status</label>
        <select v-model="status" :class="{ 'input-error': statusError }">
          <option value="">-- Select Status --</option>
          <option>To Do</option>
          <option>In Progress</option>
          <option>Done</option>
        </select>
        <small v-if="statusError" class="error-msg">{{ statusError }}</small>
      </div>

      <button type="submit" class="create-btn" :disabled="loading">
        {{ loading ? "Saving..." : "Create Task" }}
      </button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "TaskFormComponent",
  props: ["darkTheme"],
  data() {
    return {
      title: "",
      description: "",
      status: "",
      titleError: "",
      descriptionError: "",
      statusError: "",
      loading: false,
    };
  },
  emits: ["task-created"],
  methods: {
    async createTask() {
      this.titleError = "";
      this.descriptionError = "";
      this.statusError = "";

      if (!this.title || this.title.length < 3) {
        this.titleError = "Title wajib diisi (minimal 3 karakter)";
        return;
      }
      if (!this.description || this.description.length < 5) {
        this.descriptionError = "Description wajib diisi (minimal 5 karakter)";
        return;
      }
      if (!this.status) {
        this.statusError = "Status wajib dipilih";
        return;
      }

      try {
        this.loading = true;
        const token = localStorage.getItem("token");
        await axios.post(
          "http://127.0.0.1:5000/api/tasks",
          { title: this.title, description: this.description, status: this.status },
          { headers: { Authorization: `Bearer ${token}` } }
        );
        this.$emit("task-created");
        this.title = "";
        this.description = "";
        this.status = "";
      } catch (error) {
        console.error(error.response || error);
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
.task-form-wrapper {
  background: #ffffff;
  padding: 18px 22px;
  border-radius: 12px;
  box-shadow: 0px 3px 10px rgba(0,0,0,0.1);
  margin-top: 15px;
  transition: background 0.3s, color 0.3s;
}

.task-form-wrapper.dark {
  background: #2c2c2c;
  color: #eee;
}

.form-title {
  font-size: 1.2rem;
  margin-bottom: 12px;
  font-weight: bold;
}

.task-form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.form-group {
  display: flex;
  flex-direction: column;
}

label {
  font-weight: 600;
  margin-bottom: 5px;
}

input,
textarea,
select {
  width: 100%;
  padding: 10px 14px;
  border-radius: 8px;
  border: 1px solid #ccc;
  background: #fff;
  color: #000;
}

.task-form-wrapper.dark input,
.task-form-wrapper.dark textarea,
.task-form-wrapper.dark select {
  background: #3a3a3a;
  color: #eee;
  border: 1px solid #555;
}

input:focus,
textarea:focus,
select:focus {
  outline: none;
  border-color: #0077b6;
}

.input-error {
  border-color: #e63946 !important;
}

.error-msg {
  font-size: 0.8rem;
  color: #e63946;
  margin-top: 4px;
}

.create-btn {
  background: #0077b6;
  color: white;
  padding: 10px 14px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: bold;
}

.create-btn:hover {
  background: #005a8c;
}

.create-btn:disabled {
  background: gray;
  cursor: not-allowed;
}
</style>
