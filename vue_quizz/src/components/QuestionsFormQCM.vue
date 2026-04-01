<template>
  <div class="form-text">
    <h3>{{ question_name }}</h3>
    <div v-for="option in options">
      <input type="radio" :name="option" :id="option" :value="option" v-model="selected" @change="checkTruthiness">
      <label :for="option" >{{ option }}</label>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    question_name: String,
    options: Array,
    answer: String,
    previous_answer: String
  },

  data() {
    return {
      selected: this.previous_answer || "",
    }
  },

  methods:{
    checkTruthiness : function() {
        this.$emit('isTrue',{answer: this.answer == this.selected, userAnswer: this.selected});
    }
  },
  emits : ['isTrue']
}
</script>