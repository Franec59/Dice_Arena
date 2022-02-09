<template>
  <div class="notfound">
    <h1 class="error">Erreur 404</h1>
    <h2 class="notexist">Cette page n'existe pas ...</h2>
    <h3 class="notexist"><em>... ou alors elle s'est perdue dans les méandres du cosmos !</em></h3>
  </div>
</template>

<script>
export default {
  name: "Notfound",
};
</script>

<style scoped>
.notfound {
  margin: auto;
  margin-top: 2rem;
  width: 90%;
  height: 80vh;
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
}

.error {
  color: rgb(171, 219, 75);
  text-shadow: 2px 2px 4px black;
  font-size: 4rem;
}

.notexist {
  color: whitesmoke;
  text-shadow: 2px 2px 4px black;
  
}
</style>