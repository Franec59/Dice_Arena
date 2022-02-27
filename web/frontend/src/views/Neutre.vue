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
    <Infos_partie />
    </div>
  <!--fin de lobby-->
</template>

<script>
import Infos_partie from "@/components/Infos_partie.vue";

// import axios from 'axios';

export default {
  name: "Neutre",
  components: {
    Infos_partie
    
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
  background-image: url(../assets/images/d-background1.jpg);
  background-size: cover;
  background-repeat: no-repeat;
  display: flex;
  justify-content: space-around;
}

.template {
  display: flex;
  justify-content: flex-start;
  flex-direction: column;
  align-items: center;
}

.template_title {
  width: 100%;
  min-height: 5rem;
  border: 2px solid wheat;
  display: flex;
  justify-content: center;
  background-image: radial-gradient(
    circle at top center,
    rgb(255, 255, 34),
    rgb(8, 130, 133)
  );
  border-radius: 10px 10px 10px 10px;
  margin-top: 2rem;
  margin-left: 1rem;
}

.template_title h1 {
  color: whitesmoke;
  text-shadow: 2px 2px 4px black;
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
    circle at top center,
    rgb(145, 186, 14),
    rgb(9, 119, 83)
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
  margin-bottom: 2rem;
  background-image: radial-gradient(
    circle at center center,
    rgb(86, 197, 113),
    rgb(77, 181, 95),
    rgb(67, 165, 77),
    rgb(58, 149, 59),
    rgb(48, 133, 41)
  );
  padding-left: 1rem;
}



/* Partie responsive ================================================ */

@media only screen and (max-width: 900px) {
  .lobby {
    flex-direction: column;
  }
  .template_title {
    width: 80%;
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