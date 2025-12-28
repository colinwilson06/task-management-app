<template>
  <transition name="toast-fade">
    <div
      v-if="visible"
      class="toast-container"
    >
      <span>{{ message }}</span>
    </div>
  </transition>
</template>

<script>
export default {
  name: "ToastMessage", // ← FIX: multi-word component name
  data() {
    return {
      visible: false,
      message: "",
      timeoutId: null,
    };
  },
  created() {
    // Listen global toast event
    window.addEventListener("toast", (e) => {
      this.showToast(e.detail);
    });
  },
  methods: {
    showToast(message) {
      this.message = message;
      this.visible = true;
      clearTimeout(this.timeoutId);
      this.timeoutId = setTimeout(() => {
        this.visible = false;
      }, 2500);
    }
  }
};
</script>

<style scoped>
.toast-container {
  position: fixed;
  top: 20px;
  right: 20px;
  background: white;
  padding: 12px 18px;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  font-weight: 600;
  animation: slide-in 0.4s ease;
  color: #333;
}
@keyframes slide-in {
  from { opacity: 0; transform: translateX(60px); }
  to { opacity: 1; transform: translateX(0); }
}
.toast-fade-enter-active, .toast-fade-leave-active {
  transition: opacity 0.3s;
}
.toast-fade-enter, .toast-fade-leave-to {
  opacity: 0;
}
</style>
