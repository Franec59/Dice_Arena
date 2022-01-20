<template>
    <div class="page_choix">
        <!-- form-rejoinde une partie -->
        <div class="rejoindre">
            <div class="card">
                <div class="leftside">
                    <h1>Profil Joueur</h1>
                    <h3 class="left-name">Nom du joueur</h3>
                    <!-- avatar du joueur -->
                    <img src="../assets/images/avatar_f.png" class="product" alt="avatar_fille" />
                    <Btn_supprimer />
                </div>
                <div class="rightside">
                    <form id="form_join_partie" v-on:submit.prevent="joinPartie()" method="get">
                        <h1>Rejoindre une partie</h1>
                        <p>Entrez le nom ou l'identifiant de la partie que vous souhaitez rejoindre !</p>
                        <input type="text" class="inputbox" name="name" placeholder="Nom ou identifiant de la partie" required v-model="IdPartie" />
                        <Btn_valider />
                    </form>
                </div>
            </div>
        </div>
        <!-- fin rejoindre une partie -->
    </div><!--fin page choix-->
</template>

<script>
import Btn_valider from "@/components/Btn_valider.vue";
import Btn_supprimer from "@/components/Btn_supprimer.vue";
// importer axios pour les requêtes vers le back
// import axios from 'axios';

export default {
  name: "JoinPartie",
  components: {
      Btn_valider,
      Btn_supprimer
  },
  data(){
      return {
          IdPartie :"",
      }
  },
  methods:{
      joinPartie() {
        const IdPartie = {
            IdPartie : this.IdPartie,
        }
    // requete Get by id ou by name avec Axios pour le back
    //=====================================================
      // axios.get('http://...., idPartie )
      //   .then(response => {
      //     this.IdPartie = response.data
      //     console.log(response.data);
      //     this.$router.push("/en fonction du template");
      //   })
      //   .catch(error => {
      //     console.log(error);
      //   })

    // test ====================================================
    console.log(IdPartie)
    
    // liens vers les pages en attendant la connexion avec le back => a supprimer ensuite ========
    if ( this.IdPartie == "wh18"){
      this.$router.push("/warhammer")
    } else {
        this.$router.push('/error');
    }
      }
  }
    
};
</script>

<style scoped>
.page_choix {
  width: 90%;
  margin: auto;
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
  margin-top: 2rem;
}

.product {
  object-fit: cover;
  width: 10rem;
  height: 10rem;
  border: 1px solid whitesmoke;
  border-radius: 100%;
  margin-top: 1rem;
}

.rightside {
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

  .rightside {
    width: auto;
    padding: 0.5rem 3rem 3rem 2rem;
    border-radius: 0rem 0rem 1.5rem 1.5rem;
  }
}

.rejoindre {
  margin-top: 3rem;
}
</style>