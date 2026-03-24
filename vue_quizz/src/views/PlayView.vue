<script setup>
import QuestionsFormQCM from '../components/QuestionsFormQCM.vue';
import QuestionsFormText from '../components/QuestionsFormText.vue';
</script>
<template>
  <main class="app-container">
    <div v-if="activeQuestion">
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

    <div class="valider">
      <button @click="nextQuestion" class="valide_button">✅ Valider</button>
    </div>
  </main>
</template>

<script>
import QuestionsFormQCM from '../components/QuestionsFormQCM.vue';
import QuestionsFormText from '../components/QuestionsFormText.vue';

export default {
  // ... tes imports et components ...
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
      return this.questions[this.currentQuestion];
    }
  },
  methods: {
    setScoreMax(){

    },
    incrementScore(){

    },
    nextQuestion(){
      this.currentQuestion++
    },
    checkTruthiness($event){
        return this.input == $event.answer;
    }
  }
}
</script>