<script setup lang="ts">

</script>



<template>
  <header>
    <!-- <h1 class="title">Thoughts Ravel</h1> -->
  </header>
  <main class="main">
    <RouterView :key="$route.fullPath" />
  </main>
  <footer></footer>
</template>
