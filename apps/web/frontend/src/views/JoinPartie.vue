<template>
    <div class="page_choix">
        <!-- form-rejoinde une partie -->
        <div class="rejoindre">
            <div class="card">
                <div class="leftside">
                    <h1>Profil Joueur</h1>
                    <h3 class="left-name">{{ pseudoMaster }}</h3>
                    <!-- avatar du joueur -->
                    <img src="../assets/images/avatar_f.png" class="product" alt="avatar_fille" />
                    <Btn_supprimer />
                </div>
                <div class="rightside">
                    <form id="form_join_partie" v-on:submit.prevent="joinPartie()" method="get">
                        <h1>Rejoindre une partie</h1>
                        <p>Entrez le nom ou l'identifiant de la partie que vous souhaitez rejoindre !</p>
                        <input type="text" class="inputbox" name="name" placeholder="Nom ou identifiant de la partie" required v-model="idPartie" />
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
import { mapState } from 'vuex'
// import axios from 'axios';

export default {
  name: "JoinPartie",
  components: {
      Btn_valider,
      Btn_supprimer
  },
  data(){
      return {
          idPartie :"",
      }
  },
  methods:{
      joinPartie() {
        // const idJoinPartie = {
        //     idPartie : this.idPartie,
        // }
    // requete get by id partie ou by name partie pour récupérer idpartie + template
    //===============================================================================

      // axios.get('http://localhost:8000/partie, this.idPartie )
      //   .then(response => {
      //     console.log(response.data);
            // const idPartieRun = response.data._id
            // const templateRun = response.data.template

      // lien vers la partie en cour avec l'id et le template récupéré depuis le backend
        // if (this.idPartie == idPartieRun){
        //   this.$router.push({ name: templateRun, params: { id: idPartieRun }})
        // }else {
        //   alert("Le nom ou N° de partie ne correspond pas à une partie en cours !");
        // }

      //   })
      //   .catch(error => {
      //     console.log(error);
      //   })

    // lien vers la partie avec l'id en attendant le debug de get ( a supprimer ensuite )
    console.log("store :", this.$store.state.idPartie)
    console.log("id saisie :", this.idPartie)
      if (this.idPartie == this.$store.state.idPartie){
        this.$router.push({ name: this.$store.state.template, params: { id: this.$store.state.idPartie }})
      }else {
        this.$router.push('/error');
      }
      }
  },
computed:{
    ...mapState(['pseudoMaster', 'template']),
    
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