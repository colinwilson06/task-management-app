<template>
  <div class="modal-backdrop" v-if="show">
    <div :class="['modal-box', darkTheme?'dark':'light']">
      <h3>Confirm Delete</h3>
      <p>{{ message }}</p>
      <div class="modal-actions">
        <button class="btn btn-cancel" @click="$emit('cancel')">Cancel</button>
        <button class="btn btn-delete" @click="$emit('confirm')">Yes, Delete</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name:"ConfirmModal",
  props:["show","message","darkTheme"]
}
</script>

<style scoped>
.modal-backdrop {position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.4);display:flex;align-items:center;justify-content:center;}
.modal-box{background:white;padding:18px;border-radius:14px;width:300px;box-shadow:0 4px 16px rgba(0,0,0,0.2);color:#222;}
.modal-box.dark{background:#2b2b2b;color:#eee;}
.modal-actions{display:flex;gap:8px;justify-content:flex-end;margin-top:10px;}
.btn{padding:6px 10px;border:none;border-radius:6px;cursor:pointer;}
.btn-cancel{background:#ddd;color:#222;}
.btn-delete{background:#ff4d4d;color:white;}
</style>
