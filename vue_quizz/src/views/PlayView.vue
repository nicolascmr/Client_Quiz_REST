<template>
  <main class="app-container">
    <h1>Question n°1</h1>
    
    <QuestionsFormText
      @isTrue="checkTruthiness"
    />

  <div class="valider">
    <button @click="nextQuestion" v-if="isTrue" class="valide_button">✅ valider</button>
  </div>
  </main>
</template>

<script>
import QuestionsFormQCM from '../components/QuestionsFormQCM.vue';
import QuestionsFormText from '../components/QuestionsFormText.vue';

export default {
  name: 'PlayerView',
  components: {
    QuestionsFormQCM,
    QuestionsFormText
  },
  data() {
    return {
      glasses: 0,
      dailyGoal: 8,
      questions: [],
      score: 0,
      scoreMax: 0
    };
  },
  methods: {
    setScoreMax(){

    },
    incrementScore(){

    },
    nextQuestion(){

    },
    checkTruthiness($event){
        return this.input == $event.answer;
    }
  }
}
</script>