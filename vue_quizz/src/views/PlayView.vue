<template>
  <main v-if="quiz" class="app-container">
    <div v-if="activeQuestion">
      <div class="score">
      </div>
      <h1>Question n°{{ activeQuestion.numero }}</h1>

      <QuestionsFormText
        v-if="activeQuestion.question_type === 'questionOuverte'"
        :question_name="activeQuestion.enonce"
        :answer="activeQuestion.reponse"
        @isTrue="checkTruthiness"
        :key="'text-' + activeQuestion.numero"
      />

      <QuestionsFormQCM
        v-else-if="activeQuestion.question_type === 'questionChoixMultiple'"
        :question_name="activeQuestion.enonce"
        :options="[activeQuestion.proposition1, activeQuestion.proposition2]"
        :answer="activeQuestion.bonne_reponse === 1 ? activeQuestion.proposition1 : activeQuestion.proposition2"
        @isTrue="checkTruthiness"
        :key="'qcm-' + activeQuestion.numero"
      />

      <div v-else>
        <h3>{{ activeQuestion.enonce }}</h3>
        <p>Question sans réponse, passez à la suite.</p>
      </div>
    </div>

    <div v-else>
      <h2>Score : {{ score }} / {{ scoreMax }}</h2>
      <p>Vous avez fini le questionnaire !</p>

      <div>
        <div v-for="(question, index) in quiz.questions" :key="index" style="margin-bottom: 1.5rem; padding: 1rem; border: 1px solid lightgray; border-radius: 8px;">
          <h3 style="margin-top: 0;">Question n°{{ question.numero }} : {{ question.enonce }}</h3>
          <p>
            Votre réponse : 
            <span :style="{ color: correctAnswers[index] ? 'green' : 'red', fontWeight: 'bold' }">
              {{ userAnswers[index] || '(Aucune réponse)' }}
            </span>
          </p>
          <p v-if="!correctAnswers[index]" style="color: #666;">
            La bonne réponse était : <strong>{{ getCorrectAnswer(question) }}</strong>
          </p>
        </div>
      </div>
      
      <div style="margin-top: 2rem;">
        <RouterLink to="/game" class="btn">Retour à la liste des quiz</RouterLink>
      </div>
    </div>

    <div v-if="canGoNext" class="">
      <div class="retour">
        <button @click="previousQuestion" :disabled="!canGoPrevious">Retour à la question d'avant</button>
      </div>
      <div v-if="canGoNext" class="valider">
        <button @click="nextQuestion" class="valide_button">➡️ Prochaine Question</button>
      </div>
      <div v-else>
        <button disabled>❗ Fin du quiz</button>
      </div>
    </div>

    <div id="progress" v-if="canGoNext">
      <ProgressBar
      :valeurActuelle="progressValue"
      :objectif="scoreMax" 
      />
    </div>
  </main>
</template>

<script>
import API from '../services/api';
import QuestionsFormQCM from '../components/QuestionsFormQCM.vue';
import QuestionsFormText from '../components/QuestionsFormText.vue';
import ProgressBar from '../components/ProgressBar.vue';

export default {
  components: {
    QuestionsFormQCM,
    QuestionsFormText,
    ProgressBar
    
  },
  data() {
    return {
      currentQuestion: 0,
      dailyGoal: 8,
      correctAnswers: {},
      userAnswers: {},
      scoreMax: 0,
      quiz: null,
      api: new API()
    };
  },
  computed: {
    score() {
      return Object.values(this.correctAnswers).filter(isCorrect => isCorrect === true).length;
    },
    activeQuestion() {
      return this.quiz.questions[this.currentQuestion] ?? null;
    },
    canGoPrevious() {
      return this.currentQuestion > 0;
    },
    canGoNext() {
      return this.currentQuestion < this.scoreMax;
    },
    progressValue() {
      if (this.scoreMax === 0) return 0;
      return Math.min(this.currentQuestion + 1, this.scoreMax);
    }
  },
  methods: {
    setScoreMax() {
      this.scoreMax = this.quiz.questions.length;
    },
    checkTruthiness(payload) {
      // payload contient {answer: true/false} pour QCM ou {bool: true/false} pour Text
      const isCorrect = payload.answer !== undefined ? payload.answer : payload.bool;
      
      // On associe directement vrai ou faux selon l'index de la question actuelle
      this.correctAnswers[this.currentQuestion] = isCorrect;
      this.userAnswers[this.currentQuestion] = payload.userAnswer;
    },
    getCorrectAnswer(question) {
      if (question.question_type === 'questionOuverte') {
        return question.reponse;
      } else if (question.question_type === 'questionChoixMultiple') {
        return question.bonne_reponse === 1 ? question.proposition1 : question.proposition2;
      }
      return '';
    },
    previousQuestion() {
      if (this.currentQuestion > 0) {
        this.currentQuestion--;
      }
    },
    nextQuestion() {
      if (this.currentQuestion < this.scoreMax) {
        this.currentQuestion++;
      }
    },
    getQuizDetail: async function() {
        const data = await this.api.getQuiz(this.$route.params.id);
        if (data) {
            this.quiz = data.questionnaire;
            this.setScoreMax();
        }
    },
    
  },
  mounted: async function() {
      this.getQuizDetail();
  }
};
</script>