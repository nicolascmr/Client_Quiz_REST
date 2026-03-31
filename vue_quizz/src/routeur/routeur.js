import { createWebHistory, createRouter} from 'vue-router'
import App from '../App.vue'
import AdminView  from '../views/AdminView.vue'
import QuizDetailView from '../views/QuizDetailView.vue'
import QuizPlayListView from '../views/QuizPlayListView.vue'
import PlayView from '../views/PlayView.vue'

const routes = [
    {path: '/admin', name:'edition', component: AdminView},
    {path: '/admin/quiz/:id', name:'quiz-detail', component: QuizDetailView},
    {path: '/game', name:'game', component: QuizPlayListView},
    {path: '/game/quiz/:id', name:'quiz-game', component: PlayView},

]

const router = createRouter({
    history: createWebHistory(),
    routes, 
})
export default router