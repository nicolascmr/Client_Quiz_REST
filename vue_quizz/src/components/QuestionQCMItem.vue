<template>
  <div class="form-text">
    <span>Énoncé: </span>
    <input type="text" v-model="local_name"/>
    <div v-for="(option, index) in local_options" :key="index">
      <span>Proposition {{ index+1 }}: </span>
        <input type="text" v-model="local_options[index]">
    </div>
    <span>Bonne proposition: </span>
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
    options: Array,
    answer: String,
    api: Object,
    creating: Boolean
  },
  data() {
    return {
      local_name: this.question_name,
      local_options: [...this.options],
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
      if (this.local_name == "" || this.local_answer == "" || any(this.local_options.forEach(element => {element == ""}))){
        alert("Vous ne pouvez pas laisser un champ vide")
        return;
      }
      await this.api.modifyQuestionQCM(idQuizz, numero, this.local_name, this.local_options, parseInt(this.local_answer));
      this.$parent.getQuizDetail();
      this.$parent.modifierQuestion(numero);
    },
    creerQuestion: async function(idQuizz) {
      if (this.local_name == "" || this.local_answer == "" || this.local_options.forEach(element => {element == ""})){
        annulerCreation()
      }
      await this.api.addQuestionQCM(idQuizz, this.local_name, this.local_options, parseInt(this.local_answer));
      this.$parent.getQuizDetail();
      this.$parent.isCreate = false;
    }
  }
}
</script>