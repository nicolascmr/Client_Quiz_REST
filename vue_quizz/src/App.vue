<script setup>
</script>

<template>
  <nav>
    <RouterLink to="/admin">Page d'edition</RouterLink>
  </nav>  
  <RouterView />
</template>

<style scoped>
nav {
  display: flex;
  padding: 1rem;
  margin-bottom: 2rem;
}
</style>
