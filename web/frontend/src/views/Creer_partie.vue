<template>
  <div class="page_choix">
    <!-- form-création de la partie -->
    <div class="creation">
      <div class="card">
        <div class="leftside">
          <h1>Créer votre partie</h1>
          <!-- logo de xavier -->
          <img
            src="../assets/images/logo_da.png"
            class="product"
            alt="Logo Dice_arena"
          />
          <Btn_annuler />
        </div>
        <div class="rightside1">
          <form
            id="form_create_partie"
            v-on:submit.prevent="createPartie()"
            method="post"
          >
            <h2>Profil "master"</h2>
            <p>Nommer votre partie !</p>
            <input
              type="text"
              class="inputbox"
              name="partie"
              placeholder="Nom de la partie"
              v-model="nomPartie"
              required
            />
            <p>Choix du thème</p>
            <select
              class="inputbox"
              name="template"
              id="template"
              required
              v-model="choixTemplate"
            >
              <option value="">-- Choississez un thème de jeu --</option>
              <option value="Neutre">Neutre</option>
              <option value="Donjon">Donjon & Dragon</option>
              <option value="Warhammer">Warhammer 40k</option>
              <option value="Craps">Partie de craps</option>
              <option value="Yam">Partie de Yam's</option>
              <option value="Cyperpunk">Cyberpunk (jdr)</option>
            </select>
            <Btn_valider />
          </form>
        </div>
      </div>
    </div>
    <!-- fin création de la partie -->
  </div>
</template>

<script>
import Btn_valider from "@/components/Btn_valider.vue";
import Btn_annuler from "@/components/Btn_annuler.vue";
import axios from "axios";

export default {
  name: "Creer_partie",
  components: {
    Btn_valider,
    Btn_annuler,
  },
  data() {
    return {
      nomPartie: "",
      choixTemplate: "",
    };
  },

  methods: {
    async createPartie() {
      const newPartie = {
        partie: this.nomPartie,
        template: this.choixTemplate,
      };
      // console.log(newPartie);
      const ipStatic = this.$store.state.ip_static
      // requete avec Axios pour le back ====================================
      await axios
        .post('http://' + `${ipStatic}` + ':8000/partie', newPartie)
        .then((response) => {
          // console.log(response);
          console.log("retour db :", response.data._id);

        // renseigner le N° de partie et le profil dans le store =============
          const idPartieRes = response.data._id;
          this.$store.commit("SET_IDPARTIE", idPartieRes);

          const profilRes = "master";
          this.$store.commit("SET_PROFIL", profilRes);

          //alert pour communiquer l'id de la partie
          alert("Le n° de votre partie, à communiquer aux autres joueurs, est : " + idPartieRes + "  ( bouton copier/coller en page suivante )")

          // lien vers choix du pseudo =============
          this.$router.push("/pseudo");
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
.page_choix {
  width: 90%;
  margin: auto;
  margin-top: 2rem;
  display: flex;
  justify-content: center;
  flex-direction: column;
  margin-bottom: 2rem;
}

.card {
  width: 60rem;
  margin: auto;
  background: white;
  position: center;
  align-self: center;
  top: 50rem;
  border-radius: 1.5rem;
  box-shadow: 4px 3px 20px #3535358c;
  display: flex;
  flex-direction: row;
}

.leftside {
  background: #030303;
  width: 25rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border-top-left-radius: 1.5rem;
  border-bottom-left-radius: 1.5rem;
}

.left-name {
  color: whitesmoke;
  margin-top: 0.5rem;
}

.product {
  object-fit: contain;
  width: 20em;
  height: 20em;
}

.rightside1 {
  background-image: url(../assets/images/d-background1.jpg);
  background-size: cover;
  background-repeat: no-repeat;
  width: 35rem;
  border-bottom-right-radius: 1.5rem;
  border-top-right-radius: 1.5rem;
  padding: 1rem 2rem 3rem 3rem;
}

p {
  display: block;
  font-size: 1.3rem;
  font-weight: 400;
  margin: 0.8rem 0;
  color: white;
  text-shadow: 2px 2px 2px black;
}

h1 {
  color: rgb(171, 219, 75);
  text-shadow: 2px 2px 4px grey;
}

h2 {
  color: rgb(171, 219, 75);
  text-shadow: 2px 2px 4px black;
}

.inputbox {
  color: #030303;
  width: 100%;
  padding: 0.5rem;
  border: none;
  border-bottom: 1.5px solid #ccc;
  margin-bottom: 1rem;
  border-radius: 0.3rem;
  color: #615a5a;
  font-size: 1.1rem;
  font-weight: 500;
  outline: none;
  background: whitesmoke;
}

/* Partie responsive ======================================*/

@media only screen and (max-width: 900px) {
  .card {
    flex-direction: column;
    width: auto;
  }

  .leftside {
    width: 100%;
    border-radius: 1.5rem 1.5rem 0rem 0rem;
  }

  .rightside1 {
    width: auto;
    padding: 0.5rem 3rem 3rem 2rem;
    border-radius: 0rem 0rem 1.5rem 1.5rem;
  }
}

.rejoindre {
  margin-top: 3rem;
}
</style>