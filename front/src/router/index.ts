import {createRouter, createWebHistory} from 'vue-router'
import Index from '../pages/index.vue'
import LoginPage from '../pages/LoginPage.vue'

const routes = createRouter({
    history: createWebHistory(),
    routes:[
        {
            name: 'index',
            path: '/',
            component: Index
        },
        {
            name: 'login',
            path: '/login',
            component: LoginPage
        }
    ]
})

export default routes