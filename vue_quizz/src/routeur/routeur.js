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

let isAuthenticated = false;
const password_saved = 'admin'; 

router.beforeEach((to, from, next) => {
    if (to.path.startsWith('/admin')) {
        if (!isAuthenticated) {
            const password = window.prompt("Veuillez entrer le mot de passe :");
            
            if (password_saved == password) {
                isAuthenticated = true; 
                next();
            } else {
                window.alert('Mot de passe incorrect ! Access refusé.');
                if (!from.path === '/') {
                    next(false);
                }
            }
        } else {
            next();
        }
    } else {
        next();
    }
})

export default router