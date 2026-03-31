<template>
  <div class="form-text">
    <input type="text" v-model="local_name"/>
    <input type="text" v-model="local_answer"/>
  </div>
  <div v-if="!creating">
    <button @click="retourQuestion(id)">Retour</button>
    <button @click="enregistrerQuestion($route.params.id, id)">Enregistrer</button>
  </div>
  <div v-else>
    <button @click="annulerCreation()">Annuler</button>
    <button @click="creerQuestion($route.params.id)">Enregistrer</button>
  </div>
</template>

<script>
export default {
  props: {
    id: Number,
    question_name: String,
    answer: String,
    api: Object,
    creating: Boolean
  },
  data() {
    return {
      local_name: this.question_name,
      local_answer: this.answer
    }
  },
  methods:{
    retourQuestion: function(numero) {
      this.$parent.modifierQuestion(numero)
    },
    annulerCreation: function() {
      this.$parent.isCreate = false;
    },
    enregistrerQuestion: async function(idQuizz, numero) {
      await this.api.modifyQuestionOuverte(idQuizz, numero, this.local_name, this.local_answer);
      this.$parent.getQuizDetail();
      this.retourQuestion(numero);
    },
    creerQuestion: async function(idQuizz) {
      await this.api.addQuestionOuverte(idQuizz, this.local_name, this.local_answer);
      this.$parent.getQuizDetail();
      this.$parent.isCreate = false;
    }
  }
}
</script>