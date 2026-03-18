<template>
  <div class="form-text">
    <h3>{{ question_name }}</h3>
    <input class="input" type="text">
  </div>
</template>

<script>
export default {
  question_name: '',
  props: {
    input: '',
    answer: ''
  },

  methods:{
    checkTruthiness : function() {
        this.$emit('isTrue',{answer: this.answer});
    }
  },
  emits : ['isTrue']
}
</script>