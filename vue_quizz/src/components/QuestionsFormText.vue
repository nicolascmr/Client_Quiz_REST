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
    answer: String
  },

  data() {
    return {
      input: ""
    }
  },

  methods:{
    checkTruthiness : function() {
        this.$emit('isTrue',{bool: this.answer == this.input});
    }
  },
  emits : ['isTrue']
}
</script>