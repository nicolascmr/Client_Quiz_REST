<script>
import API from '../services/api';
import QuizItem from './QuizItem.vue';

export default{
    components: {
        QuizItem
    },
    data() {
        return {
            quizList: [],
            api: new API()
        }
    },
    methods:{
        get: async function() {
        const json = await this.api.getQuizs();
            if (json){
                this.quizList = json.questionnaires;
            }
    },
        removeItem: function(quiz) {
            this.api.deleteQuiz(quiz.id)
            this.quizList.splice(quiz, 1)
            this.get()

      },
      modifyItem: async function(quiz) {
            await this.api.modifyQuiz(quiz.id, quiz.nom)
            this.get()
      },
    },
    
    mounted: async function() {
        this.get()
    }
}
</script>
<template>
    <ul>
        <li v-for="(quiz, index) in quizList" :key="quiz.id">
            <QuizItem :quiz="quiz" :index="index" @remove="removeItem(quiz)" @modify="modifyItem(quiz)"></QuizItem>
        </li>
    </ul>
</template>