<template>
  <div class="page_pseudo">
    <!-- form-pseudo -->
    <div class="mainscreen">
      <div class="card">
        <div class="leftside">
          <h1>Créer ou rejoindre <br>une partie !</h1>
          <!-- logo de xavier -->
          <img
            src="../assets/images/logo_da.png"
            class="product"
            alt="Logo Dice_arena"
          />
        </div>
        <div class="rightside">
          <form id="form" v-on:submit.prevent="monChoix()">
            <div class="check">
                <h2 class="definir">A peine entré dans l'arène, vous devez déjà choisir votre destin :</h2>
                    <p class="master">"Profil Master"</p>
                    <h3 class="profil">Je souhaite créer une partie !
                        <input type="radio" class="box" name="choix" value="master" v-model="monProfil" required/>
                    </h3>
                    <p class="joueur">"Profil Joueur"</p>
                    <h3 class="profil">Je souhaite rejoindre une partie !
                        <input type="radio" class="box" name="choix" value="joueur" v-model="monProfil" required />
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

export default {
  name: "Choix",
  components: {
    Btn_valider,
  },
  data(){
    return{
      monProfil: ""
  
    }
      
  },
  methods:{
    //fonction choix : créer une partie ou rejoindre une partie ============================
    monChoix() {
    // redirection en fonction de monProfil =============================
    if ( this.monProfil == "master"){
      this.$router.push("/creerPartie")
    } else if ( this.monProfil == "joueur"){
      this.$router.push("/joinPartie");
    } else {
        this.$router.push('/error');
    }
    }//fin de monChoix
  
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
  object-fit: contain;
  width: 20em;
  height: 20em;
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

h1 {
  color: rgb(171, 219, 75);
  text-shadow: 2px 2px 4px grey;
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
    margin-bottom: 1.5rem;
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
    margin-top: 1.5rem;
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