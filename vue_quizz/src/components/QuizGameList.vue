<script>
import QuizAPI from '../services/quizz_api.js';
import QuizItem from './QuizItem.vue';

export default{
    components: {
        QuizItem
    },
    data() {
        return {
            quizList: [],
            api: new QuizAPI()
        }
    },
    methods:{
        get: async function() {
        const json = await this.api.getQuizs();
            if (json){
                this.quizList = json.questionnaires;
            }
    },
    },
    
    mounted: async function() {
        this.get()
    }
}
</script>
<template>
    <div id="main">
        <div v-for="quiz in quizList">
            <h3>{{ quiz.nom }}</h3>
            <RouterLink :to="`/game/quiz/${quiz.id}`" class="btn">Jouer</RouterLink>
        </div>
    </div>
</template>

<style scoped>
</style>

