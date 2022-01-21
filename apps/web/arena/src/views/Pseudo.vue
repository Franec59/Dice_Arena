<template>
  <div class="page_pseudo">
    <!-- form-pseudo -->
    <div class="mainscreen">
      <div class="card">
        <div class="leftside">
          <!-- logo de xavier -->
          <h2>logo de xavier</h2>
          <img
            src="../assets/images/samurai-logo.jpg"
            class="product"
            alt="Samurai-mask"
          />
        </div>
        <div class="rightside">
          <form id="form" v-on:submit.prevent="createPseudo()" method="post">
            <h2>Qui ose entrer dans l'arène ?</h2>
            <p>Par quel nom te fais tu connaitre ?</p>
            <input
              type="text"
              class="inputbox"
              name="pseudo"
              placeholder="Entrez votre pseudo"
              required
              v-model="pseudo"
            />
            <div class="avartar_container">
              <img
                src="../assets/images/avatar_g.png"
                class="avatar"
                alt="avatar_garçon"
              />
              <p>Quel avartar te définit le mieux ? (optionnel)</p>
            </div>
            <input type="file" class="inputbox" name="avatar" id="avatar" />
            <div class="check">
                <h2 class="definir">Définit ton profil :</h2>
                    <p class="master">"Master"</p>
                    <h3 class="profil">Je souhaite créer une partie !
                        <input type="radio" class="box" name="choix" value="master" v-model="profilChoice" required/>
                    </h3>
                    <p class="joueur">"Joueur"</p>
                    <h3 class="profil">Je souhaite rejoindre une partie !
                        <input type="radio" class="box" name="choix" value="joueur" v-model="profilChoice" required />
                    </h3>
            </div>
            <Btn_valider />
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Btn_valider from "@/components/Btn_valider.vue";
// importer axios pour les requêtes vers le back
// import axios from 'axios';

export default {
  name: "Pseudo",
  components: {
    Btn_valider,
  },
  data(){
    return{
      errors: [],
      pseudo: null,
      profilChoice: ""
  
    }
      
  },
  methods:{

    createPseudo() {
      const newPseudo = {
        pseudo : this.pseudo,
        profil : this.profilChoice
      }
    // requete POST avec Axios pour le back
    //===============================================
      // axios.post('http://...., newPseudo )
      //   .then(response => {
      //     console.log(response);
      //     this.$router.push("/createPartie");
      //   })
      //   .catch(error => {
      //     console.log(error);
      //   })

    // test ====================================================
    console.log(newPseudo)
    console.log(this.profilChoice)
    
    // lien vers les pages en attendant la connexion avec le back => a supprimer ensuite ========
    if ( this.profilChoice == "master"){
      this.$router.push("/createPartie")
    } else if ( this.profilChoice == "joueur"){
      this.$router.push("/joinPartie");
    } else {
        this.$router.push('/error');
    }
    },
  

  }//fin de methods
  
};
</script>

<style scoped>
.page_pseudo {
  width: 90%;
  margin: auto;
  margin-top: 2rem;
  margin-bottom: 2rem;
  display: flex;
  justify-content: center;
  flex-direction: column;
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

.product {
  object-fit: cover;
  width: 15em;
  height: 15em;
  border-radius: 100%;
}

.avatar {
  object-fit: cover;
  width: 2em;
  height: 2em;
  border-radius: 100%;
  border: 1px solid whitesmoke;
  background-color: #030303;
}

.avartar_container {
  display: flex;
  justify-content: left;
  margin-top: 1rem;
}

.avartar_container p {
  position: relative;
  bottom: 0.5rem;
  margin-left: 0.2rem;
}

.rightside {
  background-image: url(../assets/images/d-background2.png);
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
  background: rgb(0, 0, 0, 0.1);
}

h2 {
  color: whitesmoke;
  text-shadow: 4px 4px 8px black;
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

.check{
    display: flex;
    flex-direction: column;

}

.profil{
    background: whitesmoke;
    border-radius: 10px 10px 10px 10px;
    color: #000000;
    height: 2rem;
    padding-top: 0.8rem;
    padding-left: 0.8rem;
    padding-right: 0.8rem;
    display: flex;
    justify-content: space-between;
    margin-top:-0.8rem;
    
}

.definir{
    margin-bottom: -0.2rem;
    color: whitesmoke;
    text-shadow: 4px 4px 4px black;
}

.box{
    position: relative;
    height: 1.5rem;
    width: 1.5rem;
    bottom: 0.2rem;
}

.master{
    color:rgb(11, 226, 11);
}
.joueur{
    color:rgb(104, 197, 240);
}

/* partie responsive ================================================== */
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

  h3{
      font-size: 1rem;
  }
}
</style>