<template>
  <div class="lobby">
    <div class="template">
      <div class="template_title">
        <h1 class="yam">Wargame : Démo.</h1>
      </div>
      <div class="template_rendu">
        <h2 class="mode">attaque</h2>
        <h3>Joueur en attaque</h3>
        <h3>Nombre de figurines</h3>
        <h3>Nombre d'attaques</h3>
        <h3>Bonus</h3>
        <h3>Malus</h3>
        <h3>Score limite à atteindre :</h3>
        <button type="button">Lancer</button>
        <h3>Résultats bruts :</h3>
        <h3>Réussites :</h3>
        <h3>Total :</h3>
        <hr/>
        <h2 class="mode">défense</h2>
        <h3>Joueur en défense :</h3>
        <h3>Nombre de sauvegarde à réaliser :</h3>
        <h3>Bonus</h3>
        <h3>Malus</h3>
        <h3>Score limite à atteindre :</h3>
        <button type="button">Lancer</button>
        <h3>Résultats bruts :</h3>
        <h3>Réussites :</h3>
        <h3>Total :</h3>
        <hr/>
        <h2 class="mode">Comparatif</h2>
        <h3>Score attaque</h3>
        <h3>Score défense</h3>
        <h3>Balance :</h3>

      </div>
    </div>
    <!--fin de template-->
    <Infos_partie />
    <!--fin de joueurs-->
  </div>
  <!--fin de lobby-->
</template>

<script>
import Infos_partie from "@/components/Infos_partie.vue";

export default {
  name: "Wargame",
  components: {
    Infos_partie
  },
  data() {
    return {
      profil: "",
    };
  },
  props: ["id"],
};
</script>

<style scoped>
.lobby {
  margin: auto;
  margin-top: 4rem;
  margin-bottom: 2rem;
  width: 90%;
  border: 1px solid white;
  min-height: 100vh;
  border-radius: 20px 20px 20px 20px;
  background-image: url(../assets/images/wargame.jpg);
  background-size: cover;
  background-repeat: no-repeat;
  display: flex;
  justify-content: space-around;
  padding-bottom: 2rem;
}

.template {
  display: flex;
  justify-content: flex-start;
  flex-direction: column;
  align-items: center;
}

.template_title {
  width: 16rem;
  height: 13rem;
  background-image: url(../assets/images/yam.png);
  background-size: cover;
  background-repeat: no-repeat;
  margin-top: 2rem;
  margin-left: 1rem;
}

.yam {
  color: whitesmoke;
  text-shadow: 4px 4px 6px black;
  font-size: 3rem;
}

.template_rendu {
  width: 90%;
  min-height: 20rem;
  border: 2px solid wheat;
  margin-top: 3rem;
  background-image: linear-gradient(
      127deg,
      rgba(153, 255, 88, 0.46) 0%,
      rgba(153, 255, 88, 0.46) 14.286%,
      rgba(134, 245, 84, 0.46) 14.286%,
      rgba(134, 245, 84, 0.46) 28.572%,
      rgba(114, 236, 80, 0.46) 28.572%,
      rgba(114, 236, 80, 0.46) 42.858%,
      rgba(95, 226, 76, 0.46) 42.858%,
      rgba(95, 226, 76, 0.46) 57.144%,
      rgba(76, 216, 72, 0.46) 57.144%,
      rgba(76, 216, 72, 0.46) 71.43%,
      rgba(56, 207, 68, 0.46) 71.43%,
      rgba(56, 207, 68, 0.46) 85.716%,
      rgba(37, 197, 64, 0.46) 85.716%,
      rgba(37, 197, 64, 0.46) 100.002%
    ),
    linear-gradient(
      285deg,
      rgb(116, 183, 117) 0%,
      rgb(116, 183, 117) 14.286%,
      rgb(113, 173, 114) 14.286%,
      rgb(113, 173, 114) 28.572%,
      rgb(110, 163, 110) 28.572%,
      rgb(110, 163, 110) 42.858%,
      rgb(107, 154, 107) 42.858%,
      rgb(107, 154, 107) 57.144%,
      rgb(104, 144, 103) 57.144%,
      rgb(104, 144, 103) 71.43%,
      rgb(101, 134, 100) 71.43%,
      rgb(101, 134, 100) 85.716%,
      rgb(98, 124, 96) 85.716%,
      rgb(98, 124, 96) 100.002%
    );
  padding-left: 1rem;
  color: whitesmoke;
}

/* Partie responsive ================================================ */

@media only screen and (max-width: 900px) {
  .lobby {
    flex-direction: column;
  }

  .template_title {
    width: 60%;
    min-height: 5rem;
  }

}
</style>