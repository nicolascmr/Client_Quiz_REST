<template>
  <div class="form-text">
    <h3>{{ question_name }}</h3>
    <input class="input" type="text">
  </div>
</template>

<script>
export default {
  props: {
    question_name: String,
    input: String,
    answer: String
  },

  methods:{
    checkTruthiness : function() {
        this.$emit('isTrue',{answer: this.answer});
    }
  },
  emits : ['isTrue']
}
</script>