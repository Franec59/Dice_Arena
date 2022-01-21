<template>
  <div class="lobby">
    <div class="template">
      <div class="template_title">
        <h1 class="yam">Yam's</h1>
      </div>
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
        <h4 class="identifiant">{{ id }}</h4>
      </div>
      <div class="liste_joueurs">
        <h2 class="joueurs">Joueurs inscrits sur la partie</h2>
        <ol>
          <li>nom joueur 1</li>
          <li>nom joueur 2</li>
          <li>nom joueur 3</li>
        </ol>
      </div>
      <Btn_cloturer v-if="profil === 'master'" />
      <Btn_quitter v-else-if="profil === 'joueur'" />
    </div>
    <!--fin de joueurs-->
  </div>
  <!--fin de lobby-->
</template>

<script>
import Btn_cloturer from "@/components/Btn_cloturer.vue";
import Btn_quitter from "@/components/Btn_quitter.vue";

export default {
  name: "Yam",
  components: {
    Btn_cloturer,
    Btn_quitter,
  },
  data() {
    return {
      profil: "",
    };
  },
  props: ["id"],
  created() {
    console.log(this.id);
  },
methods: {
    templatePartie() {
      // requete avec Axios pour le back
      //===============================================
      // axios.get('http://...., idPartie)
      //   .then(response => {
      //     console.log(response);
      //    response : idPartie + nom de la partie + liste des joueurs ( pseudos) + profil master et joueur
      //     this.$router.push("/en fonction du template");
      //   })
      //   .catch(error => {
      //     console.log(error);
      //   })
    },
  },
  mounted() {
    // pour tester les bouton cloturer ou quitter en attendant le retour du back
    // this.profil = "master"
    this.profil = "joueur";
  },
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
  background-image: url(../assets/images/b_yam.jpg);
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

.lancer {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 10rem;
  height: 10rem;
  border-radius: 50%;
  margin-top: 5rem;
  border: 2px solid wheat;
  background-image: radial-gradient(
    circle at center center,
    rgb(86, 197, 113),
    rgb(77, 181, 95),
    rgb(67, 165, 77),
    rgb(58, 149, 59),
    rgb(48, 133, 41)
  );
}

.lancer h3 {
  padding: auto;
  color: whitesmoke;
  font-size: 1.3rem;
  text-shadow: 2px 2px 4px black;
}

.lancer:hover {
  cursor: pointer;
  transform: scale(1.3);
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

.nom_partie {
  width: 110%;
  height: 5rem;
  border: 2px solid white;
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  padding-top: 1rem;
  background-image: repeating-linear-gradient(
      0deg,
      rgba(232, 224, 224, 0.08) 0px,
      rgba(232, 224, 224, 0.08) 1px,
      transparent 1px,
      transparent 11px
    ),
    repeating-linear-gradient(
      90deg,
      rgba(232, 224, 224, 0.08) 0px,
      rgba(232, 224, 224, 0.08) 1px,
      transparent 1px,
      transparent 11px
    ),
    linear-gradient(90deg, rgb(20, 20, 20), rgb(20, 20, 20));
  border-radius: 10px 10px 10px 10px;
  margin-top: 2rem;
  margin-right: 1rem;
}

.identifiant {
  color: rgb(168, 149, 149);
  position: relative;
  bottom: 2rem;
}

.nom_partie h2 {
  color: whitesmoke;
  text-shadow: 2px 2px 4px black;
}

.liste_joueurs {
  width: 110%;
  min-height: 12rem;
  border: 2px solid white;
  display: flex;
  justify-content: flex-start;
  flex-direction: column;
  background-image: repeating-linear-gradient(
      0deg,
      rgba(232, 224, 224, 0.08) 0px,
      rgba(232, 224, 224, 0.08) 1px,
      transparent 1px,
      transparent 11px
    ),
    repeating-linear-gradient(
      90deg,
      rgba(232, 224, 224, 0.08) 0px,
      rgba(232, 224, 224, 0.08) 1px,
      transparent 1px,
      transparent 11px
    ),
    linear-gradient(90deg, rgb(20, 20, 20), rgb(20, 20, 20));
  border-radius: 10px 10px 10px 10px;
  margin-top: 2rem;
  margin-right: 1rem;
}

li {
  color: whitesmoke;
  text-decoration: none;
}

.joueurs {
  color: whitesmoke;
  text-shadow: 2px 2px 4px black;
  padding-left: 1.5rem;
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

  .nom_partie {
    width: 95%;
  }

  .liste_joueurs {
    width: 95%;
  }
}
</style>