<template>
  <div class="form-text">
    <input :value="question_name"/>
    <input type="text" :value="answer">
    </div>
    <button>Enregistrer</button>
</template>

<script>
export default {
  props: {
    id: Number,
    question_name: String,
    answer: String
  },

  data() {
    return {
      selected: "",
    }
  },

  methods:{
  }
}
</script>