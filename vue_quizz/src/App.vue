<script setup>
</script>

<template>
  <nav>
    <RouterLink to="/admin" class="link" active-class="active">Page d'edition</RouterLink>
    <RouterLink to="/game" class="link" active-class="active">Page de jeu</RouterLink>
  </nav>  
  <RouterView />
</template>


<style scoped>
nav {
  display: flex;
  padding: 1rem;
  margin-bottom: 2rem;
}
.link {
  display: flex;
  padding: 1rem;
  text-decoration: none;
  color: black;
}
.active {
  color: blue;
  font-weight: bold;
}
</style>