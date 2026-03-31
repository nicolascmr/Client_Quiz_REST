<script>
import QuizAPI from '../services/quizz_api';
import QuestionAPI from '../services/question_api';
import QuestionTextItem from '../components/QuestionTextItem.vue';
import QuestionsQCMItem from '../components/QuestionQCMItem.vue';

export default {
    data() {
        return {
            quiz: null,
            quizzApi: new QuizAPI(),
            questionApi: new QuestionAPI(),
            idModif: [],
            isCreate: false,
            typeCreate: null,
        }
    },

    components: {
      QuestionTextItem,
      QuestionsQCMItem
    },
    methods: {
        getQuizDetail: async function() {
            const data = await this.quizzApi.getQuiz(this.$route.params.id);
            if (data) {
                this.quiz = data.questionnaire;
            }
        },
        modifierQuestion: function(numero) {
          const index = this.idModif.indexOf(numero);
          if (index > -1) {
            // Si la question est déjà en mode édition, on la retire (retour)
            this.idModif.splice(index, 1);
          } else {
            // Sinon, on l'ajoute au mode édition
            this.idModif.push(numero);
          }
        },
        supprimerQuestion: async function(idQuizz, numero){
          const confirmer = confirm("Êtes-vous sûr de vouloir supprimer cette question?");
          if (confirmer) {
            await this.questionApi.deleteQuestion(idQuizz, numero);
            await this.getQuizDetail(); // Recharger la liste après suppression
          }
        },
        ajouterQuestion: async function(){
          const confirmer = confirm("Voulez vous créer une question ouverte? (sinon ce sera un QCM)")
          this.isCreate = true;
          if(confirmer){
            this.typeCreate = "Ouverte"
          }
          else {
            this.typeCreate = "QCM"
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
        <li v-for="question in quiz.questions" :key="question.numero">
          <div>
            <div v-if="question.question_type == 'questionOuverte' && idModif.includes(question.numero)">
              <QuestionTextItem :id="question.numero" :question_name="question.enonce" :answer="question.reponse" :api="questionApi" :creating="false"/>
            </div>
            <div v-else-if="idModif.includes(question.numero)">
              <QuestionsQCMItem :id="question.numero" :question_name="question.enonce" :options="[question.proposition1, question.proposition2]" :answer="String(question.bonne_reponse)" :api="questionApi" :creating="false"/>
            </div>
            <div v-else>
              <strong>Question {{ question.numero }} : </strong> {{ question.enonce }}
              <br>
              <small>Type : {{ question.question_type }}</small>
              <br>
              <button @click="modifierQuestion(question.numero)">Modifier</button>
              <button @click="supprimerQuestion($route.params.id, question.numero)">Supprimer</button>
            </div>
          </div>
        </li>
        <button @click="ajouterQuestion()">Ajouter</button>
        <div v-if="isCreate && typeCreate == 'Ouverte'">
          <QuestionTextItem :id="0" question_name="" answer="" :api="questionApi" :creating="true"/>
        </div>

        <div v-else-if="isCreate && typeCreate == 'QCM'">
          <QuestionsQCMItem :id="0" question_name="" :options="['', '']" answer="1" :api="questionApi" :creating="true"/>
        </div>
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
