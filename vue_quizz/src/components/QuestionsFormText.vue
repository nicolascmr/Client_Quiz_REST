<template>
  <div class="form-text">
    <h3>{{ question_name }}</h3>
    <input class="input" type="text" v-model="input" @input="checkTruthiness">
  </div>
</template>

<script>
export default {
  props: {
    question_name: String,
    answer: String,
    previous_answer: String
  },

  data() {
    return {
      input: this.previous_answer || ""
    }
  },

  methods:{
    checkTruthiness : function() {
        this.$emit('isTrue',{bool: this.answer == this.input, userAnswer: this.input});
    }
  },
  emits : ['isTrue']
}
</script>