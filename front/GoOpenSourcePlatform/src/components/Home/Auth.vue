<template>
    <div>
      <!-- Show login button if not logged in -->
      <!-- Google Login Button -->
    <button v-if="!isLoggedIn" @click="login" class="google-login-btn">
      <img src="../../assets/images/Google__G__logo.png" alt="Google logo" class="google-logo"> Login with Google
    </button>
      
      <!-- Logout Button -->
      <button v-else @click="logout" class="logout-btn">Logout</button>
    </div>
  </template>
  
  <script>
  import Cookies from 'js-cookie';
  
  export default {
    name: 'AuthButtons',
    data() {
      return {
        // Initial state of login based on the token's presence
        isLoggedIn: false,
      };
    },
    methods: {
      login() {
        // Implement your login logic here
        // For demonstration, we'll just set a cookie
        Cookies.set('token', 'yourAuthToken', { expires: 7 }); // Expires in 7 days
        this.checkLoginState();
      },
      logout() {
        // Implement your logout logic here
        // For demonstration, we'll remove the cookie
        Cookies.remove('token');
        this.checkLoginState();
      },
      checkLoginState() {
        // Check if the cookie named 'token' exists
        this.isLoggedIn = !!Cookies.get('token');
      }
    },
    mounted() {
      // Check login state when the component mounts
      this.checkLoginState();
    }
  };
  </script>
  
<style scoped>
.google-login-btn {
  background-color: #4285F4;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 2px;
  font-weight: bold;
  display: inline-flex;
  align-items: center;
  cursor: pointer;
}

.google-login-btn:hover {
  background-color: #357ae8;
}

.google-logo {
  margin-right: 10px;
  width: 20px;
  height: 20px;
}

.logout-btn {
  background-color: #db4437;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 2px;
  font-weight: bold;
  cursor: pointer;
}

.logout-btn:hover {
  background-color: #c1351d;
}
</style>
