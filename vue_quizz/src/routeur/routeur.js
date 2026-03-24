import { createWebHistory, createRouter} from 'vue-router'
import App from '../App.vue'
import AdminView  from '../views/AdminView.vue'

const routes = [
    {path: '/admin', name:'edition', component: AdminView},
]

const router = createRouter({
    history: createWebHistory(),
    routes, 
})
export default router