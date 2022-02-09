<template>
    <div class="page_choix">
        <!-- form-création de la partie -->
        <div class="creation">
            <div class="card">
                <div class="leftside">
                    <h1>Profil Master</h1>
                    <h2 class="left-name">"{{ pseudoMaster }}"</h2>
                    <!-- avatar du joueur -->
                    <img src="../assets/images/avatar_g.png" class="product" alt="avatar_garçon" />
                    <Btn_supprimer />
                </div>
                <div class="rightside1">
                    <form id="form_create_partie" v-on:submit.prevent="createPartie()" method="post">
                        <h1>Créer une partie</h1>
                        <p>Nommez votre partie !</p>
                        <input type="text" class="inputbox" name="partie" placeholder="Nom de la partie" v-model="partie" required />
                        <p>Choix du thème</p>
                        <select class="inputbox" name="template" id="template" required v-model="templateChoice">
                            <option value="">-- Matrice de jeu --</option>
                            <option value="neutre">Neutre</option>
                            <option value="donjon">Donjon & Dragon</option>
                            <option value="warhammer">Warhammer 40k</option>
                            <option value="yams">Partie de Yam's</option>
                            <option value="cyperpunk">Cyberpunk (jdr)</option>
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
import Btn_supprimer from "@/components/Btn_supprimer.vue";
// import axios from 'axios';
import { mapState } from 'vuex'

export default {
  name: "CreatePartie",
  components: {
      Btn_valider,
      Btn_supprimer
  },
  data(){
      return {
          partie :"",
          templateChoice : "",
          
      }
  },
  
  methods:{
      createPartie() {
        const newPartie = {
            partie : this.partie,
        }
    // requete avec Axios pour le back
    //===============================================
      // axios.post('http://...., newPartie )
      //   .then(response => {
      //     console.log(response);
      //    response : idPartie + nom de la partie + Pseudo + profil master
      //     this.$router.push("/en fonction du template");
      //   })
      //   .catch(error => {
      //     console.log(error);
      //   })

    // test ====================================================
    console.log(newPartie)
    console.log(this.templateChoice)

    // liens vers les pages en attendant la connexion avec le back => a supprimer ensuite ========
    
    if ( this.templateChoice == "neutre"){
      this.$router.push({ name: 'Neutre', params: { id: this.partie }})
    } else if ( this.templateChoice == "donjon"){
      this.$router.push({ name: 'Donjon', params: { id: this.partie }})
    } else if ( this.templateChoice == "warhammer"){
      this.$router.push({ name: 'Warhammer', params: { id: this.partie }})
    } else if ( this.templateChoice == "yams"){
      this.$router.push({ name: 'Yam', params: { id: this.partie }})
    } else {
        this.$router.push('/error');
    }


      }
  },
  computed:{
    ...mapState(['pseudoMaster'])
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