<template>
  <div class="page_choix">
    <!-- form-création de la partie -->
    <div class="creation">
      <div class="card">
        <div class="leftside">
          <h1>Rejoindre une partie</h1>
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
            id="form_join_partie"
            v-on:submit.prevent="joinPartie()"
          >
            <h2 class="profil_joueur">Profil "joueur"</h2>
            <p>Entrer le N° de la partie.</p>
            <input
              type="text"
              class="inputbox"
              name="numPartie"
              placeholder="Numero de la partie"
              v-model="numPartie"
              required
            />
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
  name: "JoinPartie",
  components: {
    Btn_valider,
    Btn_annuler,
  },
  data() {
    return {
      numPartie: "",
    };
  },

  methods: {
    joinPartie() {
      const ipStatic = this.$store.state.ip_static
        // requete GET partie pour vérifier la partie en cours ====================================
        let verif = this.numPartie
      axios
        .get(`${ipStatic}` + ':80/mapartie/' + `${verif}`)
        .then((response) => {
          console.log("response.data :", response.data)
          console.log("envoi de l'id partie au store :", this.numPartie);

          // renseigner le N° de partie et le profil dans le store =============
        this.$store.commit("SET_IDPARTIE", this.numPartie);
        
        const profilRes = "joueur";
        this.$store.commit("SET_PROFIL", profilRes);
        
        // lien vers choix du pseudo =============
        this.$router.push("/pseudo");

        })
        .catch(error => {
          console.log(error);
          alert("Le N° : " + this.numPartie + " ne correspond à aucune partie en cours !")
        })
        
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

.profil_joueur {
  color:rgb(104, 197, 240);
  text-shadow: 2px 2px 4px black;
  margin-bottom: 2rem;
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
  margin-bottom: 3rem;
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