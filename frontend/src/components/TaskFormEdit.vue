<template>
  <div :class="['task-form-edit', darkTheme ? 'dark' : 'light']">
    <form @submit.prevent="updateTask" class="edit-form">
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

      <div class="btn-group">
        <button type="submit" class="save-btn">Save</button>
        <button type="button" class="cancel-btn" @click="$emit('cancel')">Cancel</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "TaskFormEdit",
  props: ["task", "darkTheme"],
  data() {
    return {
      title: this.task[1],
      description: this.task[2],
      status: this.task[3],
      titleError: "",
      descriptionError: "",
      statusError: ""
    };
  },
  emits: ["task-updated", "cancel"],
  methods: {
    async updateTask() {
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
        const token = localStorage.getItem("token");
        await axios.put(
          `http://127.0.0.1:5000/api/tasks/${this.task[0]}`,
          { title: this.title, description: this.description, status: this.status },
          { headers: { Authorization: `Bearer ${token}` } }
        );
        this.$emit("task-updated");
      } catch (error) {
        console.error(error.response || error);
      }
    }
  }
};
</script>

<style scoped>
.task-form-edit {
  margin-top: 12px;
  padding: 18px;
  background: white;
  border-radius: 12px;
  box-shadow: 0px 3px 8px rgba(0,0,0,0.1);
  transition: background 0.3s, color 0.3s;
}

.task-form-edit.dark {
  background: #2c2c2c;
  color: #eee;
}

.edit-form {
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
  margin-bottom: 4px;
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

.task-form-edit.dark input,
.task-form-edit.dark textarea,
.task-form-edit.dark select {
  background: #3a3a3a;
  color: #eee;
  border: 1px solid #555;
}

.input-error {
  border-color: #e63946 !important;
}

.error-msg {
  font-size: 0.8rem;
  color: #e63946;
  margin-top: 3px;
}

.btn-group {
  display: flex;
  gap: 10px;
}

.save-btn {
  background: #0077b6;
  color: white;
  padding: 8px 12px;
  border-radius: 6px;
  border: none;
  font-weight: bold;
  cursor: pointer;
}

.cancel-btn {
  background: #888;
  color: white;
  padding: 8px 12px;
  border-radius: 6px;
  border: none;
  cursor: pointer;
}
</style>
