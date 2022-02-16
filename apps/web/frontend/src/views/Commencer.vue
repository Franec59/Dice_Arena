<template>
    <div class="page_choix">
        <!-- form-création de la partie -->
        <div class="creation">
            <div class="card">
                <div class="leftside">
                    <h1>Bienvenue</h1>
                    <h2 class="left-name">" {{ monPseudo }} "</h2>
                    <!-- avatar du joueur -->
                    <img src="../assets/images/avatar_g.png" class="product" alt="avatar_joueur" />
                    <Btn_supprimer />
                </div>
                <div class="rightside1">
                    <form id="form_create_partie" v-on:submit.prevent="goToPartie()">
                        <h1>Prêt à entrer dans la partie suivante ?</h1>
                        <p>Nom de la partie :</p>
                        <input type="text" class="inputbox" name="partie" v-bind:value="nomPartie" />
                        <p>N° de la partie :<i class="fa-solid fa-copy"></i></p>
                        <input type="text" class="inputbox" name="numero" v-bind:value="numero" />
                        <p>Thème choisi :</p>
                        <input type="text" class="inputbox" name="theme" v-bind:value="theme" />
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
import Btn_supprimer from "@/components/Btn_supprimer.vue";
import axios from 'axios';

export default {
  name: "Commencer",
  components: {
      Btn_valider,
      Btn_supprimer
  },
  data() {
    return {
      monPseudo: "",
      nomPartie : "",
      numero : "",
      theme : ""
    };
  },
  
  mounted (){
      const idJoueur = this.$store.state.idPseudo
      const idPartie = this.$store.state.idPartie
    // requete GET pseudo du joueur ====================================
      axios
        .get('http://localhost:8000/joueur/' + `${idJoueur}`)
        .then((response) => {
          console.log("joueur :", response)

          this.monPseudo = response.data.pseudo
          
        })
        .catch(error => {
          console.log(error);
        })

    // requete GET partie en cours ====================================
      axios
        .get('http://localhost:8000/mapartie/' + `${idPartie}`)
        .then((response) => {
          console.log("mapartie :", response)

          this.nomPartie = response.data.partie
          this.numero = response.data._id
          this.theme = response.data.template
          
        })
        .catch(error => {
          console.log(error);
        })

  },
methods:{
    goToPartie : function (){
        //lien vers le template choisi + id de la partie
          if (this.numero && this.theme) {
            this.$router.push({
              name: this.theme,
              params: { id: this.numero },
            });
          } else {
            this.$router.push("/error");
          }
    }
}
  
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
  object-fit: cover;
  width: 10rem;
  height: 10rem;
  border: 1px solid whitesmoke;
  border-radius: 100%;
  margin-top: 2rem;
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
  outline:none;
  background: whitesmoke;
}

.fa-copy{
  margin-left: 1.5rem;
  color: whitesmoke;
  text-shadow: 2px 2px 4px black;
  width: 1.5rem;
  height: 1.5rem;
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