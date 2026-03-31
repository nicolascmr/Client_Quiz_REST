<script>
import QuizAPI from '../services/quizz_api';

export default {
    data() {
        return {
            quiz: null,
            api: new QuizAPI()
        }
    },
    methods: {
        getQuizDetail: async function() {
            const data = await this.api.getQuiz(this.$route.params.id);
            if (data) {
                this.quiz = data.questionnaire;
            }
        }
    },
    mounted: async function() {
        this.getQuizDetail();
    }
}
</script>

<template>
  <div>
    <div v-if="quiz">
      <h2>Détail du quiz : {{ quiz.nom }}</h2>
      
      <ul v-if="quiz.questions?.length">
        <li v-for="question in quiz.questions" :key="question.id">
          <strong>Question {{ question.numero }} : </strong> {{ question.enonce }}
          <br>
          <small>Type : {{ question.question_type }}</small>
        </li>
      </ul>
      <p v-else>Aucune question n'a été ajoutée à ce quiz pour le moment.</p>
    </div>
    
    <p v-else>Chargement du quiz en cours...</p>

    <br>
    <RouterLink to="/admin">Retour à l'édition</RouterLink>
  </div>
</template>

<style scoped>
</style>
