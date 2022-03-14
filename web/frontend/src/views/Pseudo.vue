<template>
  <div class="page_pseudo">
    <!-- form-pseudo -->
    <div class="mainscreen">
      <div class="card">
        <div class="leftside">
          <h1>Créer votre pseudo</h1>
          <!-- logo de xavier -->
          <img
            src="../assets/images/logo_da.png"
            class="product"
            alt="Logo Dice_arena"
          />
        </div>
        <div class="rightside">
          <form id="form" v-on:submit.prevent="createPseudo()" method="post">
            <p>Qui ose entrer dans l'arène ?</p>
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
            <Btn_valider />
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Btn_valider from "@/components/Btn_valider.vue";
import axios from 'axios';

export default {
  name: "Pseudo",
  components: {
    Btn_valider,
  },
  data(){
    return{
      pseudo: null
    }
      
  },
  methods:{

    createPseudo() {
      const newPseudo = {
        pseudo : this.pseudo,
        profil : this.$store.state.profil,
        numero_partie : this.$store.state.idPartie
      };
      console.log("verif newpseudo : ", newPseudo)
      const ipStatic = this.$store.state.ip_static
      //requete axios vers le backend ===============================================
      axios.defaults.baseURL = `${ipStatic}` + ':8000/partie';
      axios.defaults.headers.post['Content-Type'] ='application/json;charset=utf-8';
      axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';

      axios
        .post(`${ipStatic}` + ':8000/partie', newPseudo )
        .then((response) => {
          console.log(response)

          // information pour le store =============
          const idPseudoRes = response.data._id;
          this.$store.commit("SET_IDPSEUDO", idPseudoRes);

          this.$router.push("/commencer")
        })
        .catch(error => {
          console.log(error);
          this.$router.push('/error');
        })
    }//fin de createpseudo
  
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

.box{
    position: relative;
    height: 1.5rem;
    width: 1.5rem;
    bottom: 0.2rem;
}

/* .master{
    color:rgb(11, 226, 11);
}
.joueur{
    color:rgb(104, 197, 240);
} */

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