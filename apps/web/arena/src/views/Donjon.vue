<template>
  <div class="lobby">
    <div class="template">
      <div class="template_title"></div>
      <div class="lancer">
        <h3>Lancer les dés</h3>
      </div>
      <div class="template_rendu">
        <h3>Résultats ou scores attendus en fonction des templates de jeu</h3>
        <h4>attaque</h4>
        <h4>défense</h4>
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
    margin-top: 2rem;
    margin-bottom: 2rem;
    width: 90%;
    border: 1px solid white;
    min-height: 100vh;
    border-radius: 20px 20px 20px 20px;
    background-image: url(../assets/images/back_dd.jpg);
    background-size: cover;
    background-repeat: no-repeat;
    display: flex;
    justify-content: space-around;
    padding-bottom: 2rem;
}

.template{
    display: flex;
    justify-content: flex-start;
    flex-direction: column;
    align-items: center;
}

.template_title{
    width: 100%;
    min-height: 15rem;
    background-image: url(../assets/images/title_dd2.png);
    background-size: contain;
    background-repeat: no-repeat;
    margin-top : 2rem;
    margin-left:1rem;
    /* background-color: rgb(0,0,0, 0.3); */
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
    background-image: radial-gradient(circle at center center, rgb(71, 71, 71),rgb(8, 8, 8));
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
    width: 90%;
    min-height: 20rem;
    border: 2px solid wheat;
    margin-top: 3rem;
    background-image: linear-gradient(216deg, rgba(77, 77, 77,0.05) 0%, rgba(77, 77, 77,0.05) 25%,rgba(42, 42, 42,0.05) 25%, rgba(42, 42, 42,0.05) 38%,rgba(223, 223, 223,0.05) 38%, rgba(223, 223, 223,0.05) 75%,rgba(36, 36, 36,0.05) 75%, rgba(36, 36, 36,0.05) 100%),linear-gradient(44deg, rgba(128, 128, 128,0.05) 0%, rgba(128, 128, 128,0.05) 34%,rgba(212, 212, 212,0.05) 34%, rgba(212, 212, 212,0.05) 57%,rgba(25, 25, 25,0.05) 57%, rgba(25, 25, 25,0.05) 89%,rgba(135, 135, 135,0.05) 89%, rgba(135, 135, 135,0.05) 100%),linear-gradient(241deg, rgba(55, 55, 55,0.05) 0%, rgba(55, 55, 55,0.05) 14%,rgba(209, 209, 209,0.05) 14%, rgba(209, 209, 209,0.05) 60%,rgba(245, 245, 245,0.05) 60%, rgba(245, 245, 245,0.05) 69%,rgba(164, 164, 164,0.05) 69%, rgba(164, 164, 164,0.05) 100%),linear-gradient(249deg, rgba(248, 248, 248,0.05) 0%, rgba(248, 248, 248,0.05) 32%,rgba(148, 148, 148,0.05) 32%, rgba(148, 148, 148,0.05) 35%,rgba(202, 202, 202,0.05) 35%, rgba(202, 202, 202,0.05) 51%,rgba(181, 181, 181,0.05) 51%, rgba(181, 181, 181,0.05) 100%),linear-gradient(92deg, hsl(214,0%,11%),hsl(214,0%,11%));
    padding-left: 1rem;
    color:whitesmoke;
}

.nom_partie{
    width: 110%;
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
    width: 110%;
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

/* Partie responsive ================================================ */

@media only screen and (max-width: 900px) {
.lobby{
  flex-direction: column;
}

.template_title{
    width: 80%;
    min-height: 10rem;
}

.nom_partie {
  width: 95%;
}

.liste_joueurs {
  width: 95%;
}

}
</style>