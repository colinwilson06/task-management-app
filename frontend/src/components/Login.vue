<template>
  <div class="login-container">
    <h2>Login</h2>
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <label>Username</label>
        <input v-model="username" :class="{ 'input-error': usernameError }" required />
        <small v-if="usernameError" class="error-msg">{{ usernameError }}</small>
      </div>
      <div class="form-group">
        <label>Password</label>
        <input type="password" v-model="password" :class="{ 'input-error': passwordError }" required />
        <small v-if="passwordError" class="error-msg">{{ passwordError }}</small>
      </div>
      <button type="submit">Login</button>
      <p v-if="errorMessage" class="error-msg">{{ errorMessage }}</p>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name:"LoginComponent",
  data(){ return { username:"", password:"", errorMessage:"", usernameError:"", passwordError:"" }; },
  methods:{
    async handleLogin(){
      this.usernameError=""; this.passwordError=""; this.errorMessage="";
      if(!this.username){ this.usernameError="Username wajib diisi"; return; }
      if(!this.password){ this.passwordError="Password wajib diisi"; return; }
      if(this.password.length<6){ this.passwordError="Password minimal 6 karakter"; return; }
      try{
        const res = await axios.post("http://127.0.0.1:5000/api/login",{username:this.username,password:this.password});
        localStorage.setItem("token",res.data.token);
        this.$router.push({name:"DashboardView"});
      }catch(err){ this.errorMessage="Login failed: Invalid username atau password"; console.error(err.response||err); }
    }
  }
}
</script>

<style scoped>
.login-container{max-width:400px;margin:50px auto;padding:20px;border:1px solid #ccc;border-radius:8px;background:#f9f9f9;}
.form-group{margin-bottom:15px;}
input{width:100%;padding:8px;margin-top:5px;border:1px solid #ccc;border-radius:4px;box-sizing:border-box;}
input.input-error{border-color:red;}
button{padding:10px 15px;cursor:pointer;}
.error-msg{color:red;font-size:0.9em;margin-top:3px;display:block;}
</style>
