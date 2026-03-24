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

      <div v-else>
        <label for="score">Score : {{ score }} / {{ scoreMax }}</label>
        <p>Vous avez fini le questionnaire!</p>
      </div>
    </div>

    <div class="valider">
      <button @click="nextQuestion" class="valide_button">✅ Valider</button>
    </div>

    <div id="progress">
      <ProgressBar
      :valeurActuelle="currentQuestion"
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
      score: 0,
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
    activeQuestion() {
      return this.questions[this.currentQuestion] ?? null;
    }
  },
  methods: {
    setScoreMax() {
      this.scoreMax = this.questions.length;
    },
    incrementScore() {
      this.score++;
    },
    nextQuestion() {
      if (this.currentQuestion < this.questions.length - 1) {
        this.currentQuestion++;
      }
    },
    checkTruthiness(isTrue) {
      if (isTrue) {
        this.incrementScore();
      }
      return isTrue;
    },
    
  },
  beforeMount() {
    this.setScoreMax();
  }
};
</script>