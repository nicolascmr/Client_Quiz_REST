<template>
  <main class="app-container">
    <div v-if="activeQuestion">
      <div class="score">
      </div>
      <h1>Question n°{{ activeQuestion.id }}</h1>

      <QuestionsFormText
        v-if="activeQuestion.type === 'text'"
        :question_name="activeQuestion.question_name"
        :answer="activeQuestion.answer"
        @isTrue="checkTruthiness"
      />

      <QuestionsFormQCM
        v-else-if="activeQuestion.type === 'qcm'"
        :question_name="activeQuestion.question_name"
        :options="activeQuestion.options"
        :answer="activeQuestion.answer"
        @isTrue="checkTruthiness"
      />
    </div>

    <div v-else>
      <label for="score">Score : {{ score }} / {{ scoreMax }}</label>
      <p>Vous avez fini le questionnaire!</p>
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

    <div id="progress">
      <ProgressBar
      :valeurActuelle="progressValue"
      :objectif="scoreMax" 
      />
    </div>
  </main>
</template>

<script>
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
      correctAnswers: {}, // On remplace "score: 0" par un objet qui garde l'état de chaque question
      scoreMax: 0,
      questions: [
        {
          id: 1,
          type: 'text',
          question_name: 'Quelle est la capitale de la France ?',
          answer: 'Paris'
        },
        {
          id: 2,
          type: 'qcm',
          question_name: 'Combien font 2 + 2 ?',
          options: ['3', '4', '5'],
          answer: '4'
        }
      ]
    };
  },
  computed: {
    score() {
      // Calcule le score en comptant les questions où la réponse enregistrée est `true`
      return Object.values(this.correctAnswers).filter(isCorrect => isCorrect === true).length;
    },
    activeQuestion() {
      return this.questions[this.currentQuestion] ?? null;
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
      this.scoreMax = this.questions.length;
    },
    checkTruthiness(payload) {
      // payload contient {answer: true/false} pour QCM ou {bool: true/false} pour Text
      const isCorrect = payload.answer !== undefined ? payload.answer : payload.bool;
      
      // On associe directement vrai ou faux selon l'index de la question actuelle
      this.correctAnswers[this.currentQuestion] = isCorrect;
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
    }
    
  },
  beforeMount() {
    this.setScoreMax();
  }
};
</script>