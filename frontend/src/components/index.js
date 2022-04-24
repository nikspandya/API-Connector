import Vue from 'vue'
import UserData from "./components/UserData.vue";

const commons = {
    UserData
};

Object.keys(commons).forEach(name=>{
    Vue.component(name,commons[name]);
});

export default commons;
