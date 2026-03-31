import { createWebHistory, createRouter} from 'vue-router'
import App from '../App.vue'
import AdminView  from '../views/AdminView.vue'
import QuizDetailView from '../views/QuizDetailView.vue'

const routes = [
    {path: '/admin', name:'edition', component: AdminView},
    {path: '/admin/quiz/:id', name:'quiz-detail', component: QuizDetailView},
]

const router = createRouter({
    history: createWebHistory(),
    routes, 
})
export default router