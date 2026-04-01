<script setup>
import QuizGameList from '../components/QuizGameList.vue';
import QuizList from '../components/QuizList.vue';

</script>

<template>
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    <h1>Edition de quizz</h1>
    <div id="list-quizz">
        <QuizList></QuizList>
    </div>
</template>