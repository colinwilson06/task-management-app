<template>
  <div :class="['app-container']" :style="backgroundStyle">
    <header class="app-header">
      <h1>Task Management</h1>
    </header>

    <main class="app-main">
      <router-view />
    </main>

    <ToastMessage />
  </div>
</template>

<script>
import ToastMessage from "./components/ToastMessage.vue";

export default {
  name: "App",
  components: { ToastMessage },
  data() {
    return {
      wallpaperUrl: require('./assets/flat-lay-workstation-with-copy-space-laptop.jpg')
    };
  },
  computed: {
    backgroundStyle() {
      return {
        backgroundImage: `url(${this.wallpaperUrl})`,
        backgroundSize: "cover",
        backgroundPosition: "center",
        minHeight: "100vh",
        transition: "background-color 0.3s ease"
      };
    }
  }
};
</script>

<style>
.app-container {
  font-family: Arial, sans-serif;
  padding: 0 16px;
  transition: color 0.3s ease, background-color 0.3s ease;
}

.app-header {
  display: flex;
  justify-content: center; 
  align-items: center;
  margin-bottom: 20px;
  padding: 10px 0;
  color: white; 
}

.app-main {
  max-width: 950px;
  margin: 0 auto;
  padding-bottom: 40px;
}
</style>
