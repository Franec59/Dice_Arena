<template>
  <div class="lobby">
    <div class="template">
      <div class="template_title">
        <h1>Nom du template</h1>
      </div>
      <div class="lancer">
        <h3>Lancer les dés</h3>
      </div>
      <div class="template_rendu">
        <h3>Résultats ou scores attendus en fonction des templates de jeu</h3>
      </div>
    </div>
    <!--fin de template-->
    <div class="joueurs">
      <div class="nom_partie">
        <h2>Nom de la partie</h2>
      </div>
      <div class="liste_joueurs">
        <h2 class="joueurs">Joueurs inscrits sur la partie</h2>
        <ol>
          <li>nom joueur 1</li>
          <li>nom joueur 2</li>
          <li>nom joueur 3</li>
        </ol>
      </div>
      <Btn_cloturer />
    </div>
    <!--fin de joueurs-->
  </div>
  <!--fin de lobby-->
</template>

<script>
import Btn_cloturer from "@/components/Btn_cloturer.vue";

export default {
  name: "Neutre",
  components: {
    Btn_cloturer,
  },
  
};
</script>

<style scoped>
    .lobby{
    margin:auto;
    margin-top: 4rem;
    margin-bottom: 2rem;
    width: 90%;
    border: 1px solid white;
    min-height: 100vh;
    border-radius: 20px 20px 20px 20px;
    background-image: url(../assets/images/d-background1.jpg);
    background-size: cover;
    background-repeat: no-repeat;
    display: flex;
    justify-content: space-around;
}

.template{
    display: flex;
    justify-content: flex-start;
    flex-direction: column;
    align-items: center;
}

.template_title{
    width: 25rem;
    height: 5rem;
    border: 2px solid wheat;
    display: flex;
    justify-content: center;
    background-image: radial-gradient(circle at top center, rgb(255, 255, 34),rgb(8, 130, 133));
    border-radius: 10px 10px 10px 10px;
    margin-top : 2rem;
    margin-left:1rem;
}

.template_title h1{
    color:whitesmoke;
    text-shadow: 2px 2px 4px black;
}

.lancer{
    display: flex;
    justify-content: center;
    align-items: center;
    width: 10rem;
    height: 10rem;
    border-radius: 50%;
    margin-top: 5rem;
    border: 2px solid wheat;
    background-image: radial-gradient(circle at top center, rgb(145, 186, 14),rgb(9, 119, 83));
}

.lancer h3{
    padding:auto;
    color:whitesmoke;
    font-size: 1.3rem;
    text-shadow: 2px 2px 4px black;
}

.lancer:hover{
    cursor: pointer;
    transform: scale(1.3);
}

.template_rendu{
    width: 40rem;
    min-height: 20rem;
    border: 2px solid wheat;
    margin-top: 3rem;
    margin-bottom: 2rem;
    background-image: radial-gradient(circle at center center, rgb(86, 197, 113),rgb(77, 181, 95),rgb(67, 165, 77),rgb(58, 149, 59),rgb(48, 133, 41));
    padding-left: 1rem;
}

.nom_partie{
    width: 25rem;
    height: 5rem;
    border: 2px solid white;
    display: flex;
    justify-content: center;
    background-image: repeating-linear-gradient(0deg, rgba(232,224,224, 0.08) 0px, rgba(232,224,224, 0.08) 1px,transparent 1px, transparent 11px),repeating-linear-gradient(90deg, rgba(232,224,224, 0.08) 0px, rgba(232,224,224, 0.08) 1px,transparent 1px, transparent 11px),linear-gradient(90deg, rgb(20,20,20),rgb(20,20,20));
    border-radius: 10px 10px 10px 10px;
    margin-top : 2rem;
    margin-right:1rem;
}

.nom_partie h2{
    color:whitesmoke;
    text-shadow: 2px 2px 4px black;
}

.liste_joueurs{
    width: 25rem;
    min-height: 12rem;
    border: 2px solid white;
    display: flex;
    justify-content:flex-start;
    flex-direction: column;
    background-image: repeating-linear-gradient(0deg, rgba(232,224,224, 0.08) 0px, rgba(232,224,224, 0.08) 1px,transparent 1px, transparent 11px),repeating-linear-gradient(90deg, rgba(232,224,224, 0.08) 0px, rgba(232,224,224, 0.08) 1px,transparent 1px, transparent 11px),linear-gradient(90deg, rgb(20,20,20),rgb(20,20,20));
    border-radius: 10px 10px 10px 10px;
    margin-top : 2rem;
    margin-right:1rem;
}

li{
    color:whitesmoke;
    text-decoration: none;
}

.joueurs{
    color: whitesmoke;
    text-shadow: 2px 2px 4px black;
    padding-left: 1.5rem;
}
</style>