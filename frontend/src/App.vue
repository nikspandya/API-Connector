<template>
  <div id="app">
    <UserData />
  </div>
</template>

<script>
import UserData from "./components/UserData.vue";

export default {
  name: "App",
  components: {
    UserData,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
