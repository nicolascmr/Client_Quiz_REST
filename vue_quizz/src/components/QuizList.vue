<script>
import QuizAPI from '../services/quizz_api';
import QuizItem from './QuizItem.vue';

export default{
    components: {
        QuizItem
    },
    data() {
        return {
            quizList: [],
            newQuizNom: '',
            errorMessage: '',
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
        removeItem: function(quiz) {
            this.api.deleteQuiz(quiz.id)
            this.quizList.splice(quiz, 1)
            this.get()

      },
      modifyItem: async function(quiz) {
          try {
              this.errorMessage = '';
              await this.api.modifyQuiz(quiz.id, quiz.nom)
              this.get()
          } catch (error) {
              this.errorMessage = error.message;
              this.get()
          }
      },
      addItem: async function() {
          try {
              this.errorMessage = '';
              await this.api.addQuiz(this.newQuizNom);
              this.newQuizNom = '';
              this.get();
          } catch (error) {
              this.errorMessage = error.message;
          }
      }
    },
    
    mounted: async function() {
        this.get()
    }
}
</script>
<template>
    <div id="main">
        <div v-if="errorMessage" class="alert alert-danger" style="color: red; margin-bottom: 10px;">
            {{ errorMessage }}
        </div>
        <form @submit.prevent="addItem">
            <label>Nom : </label>
            <input type="text" name="name" v-model="newQuizNom" required />
            <input type="submit" value="Créer le quiz">
        </form>
        <div v-for="(quiz, index) in quizList" :key="quiz.id">
            <QuizItem :quiz="quiz" :index="index" @remove="removeItem(quiz)" @modify="modifyItem(quiz)"></QuizItem>
        </div>
    </div>
</template>

<style scoped>
</style>

