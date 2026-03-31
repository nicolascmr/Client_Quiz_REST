<template>
  <div class="form-text">
    <input :value="question_name"/>
    <div v-for="option in options">
        <input type="text" :value="option" v-model="option">
    </div>
    <input type="text" :value="answer">
    </div>
</template>

<script>
export default {
  props: {
    id: Number,
    question_name: String,
    options: Array,
    answer: String
  },

  methods:{
  }
}
</script>