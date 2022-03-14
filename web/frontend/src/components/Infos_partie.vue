<template>
    <div class="joueurs">
      <div class="nom_partie">
        <h2>{{ nomPartie }}</h2>
        <h4 class="identifiant">N° : <span id="copyid">{{ numeroPartie }} </span> 
          <button id="btn_copy" v-on:click="copyToClickBoard()">
            <i class="fa-regular fa-copy"></i>
            </button></h4>
      </div>
      <div class="liste_joueurs">
        <h2 class="joueurs">Joueurs inscrits sur la partie</h2>
        <ol>
          <li v-for="joueur in joueurs" :key="joueur">
              <img
                src="../assets/images/avatar_g.png"
                class="avatar"
                alt="avatar_garçon"
              />
            {{ joueur.pseudo }} ( {{ joueur.profil }} )
          </li>
        </ol>
      </div>
      <Btn_cloturer v-if="profil==='master'" />
      <Btn_quitter v-else-if="profil==='joueur'" />
    </div>
    <!--fin de joueurs-->
</template>

<script>
import Btn_cloturer from "@/components/Btn_cloturer.vue";
import Btn_quitter from "@/components/Btn_quitter.vue";
import axios from 'axios';

export default {
  name: 'Infos_partie',
  props: {
    msg: String
  },
  components: {
    Btn_cloturer,
    Btn_quitter
  },
  data() {
    return {
      nomPartie : "",
      numeroPartie : "",
      profil : "",
      joueurs : ""
    }
  },
  mounted (){
    const idJoueur = this.$store.state.idPseudo
    this.idPartie = this.$store.state.idPartie
    console.log("idpartie from store :", this.idPartie)
    const ipStatic = this.$store.state.ip_static
     
    // requete GET partie en cours ====================================
      axios
        .get(`${ipStatic}` + ':8000/mapartie/' + `${this.idPartie}`)
        .then((response) => {
          // console.log("mapartie :", response)

          this.nomPartie = response.data.partie
          this.numeroPartie = response.data._id
          
        })
        .catch(error => {
          console.log(error);
        })

    // requete GET du joueur en cours ====================================
      axios
        .get(`${ipStatic}` + ':8000/joueur/' + `${idJoueur}`)
        .then((response) => {
          // console.log("joueur :", response)

          this.monPseudo = response.data.pseudo
          this.profil = response.data.profil
          
        })
        .catch(error => {
          console.log(error);
        })

    //requete GET pour récupérer la liste des joueurs ================================================
      axios
      .get(`${ipStatic}` + ':8000/liste/' + `${this.idPartie}`,
      )
      .then(response => {
          // console.log("liste des joueurs :", response);
          this.joueurs = response.data
          // console.log("tableau des joueurs :", response.data)
        })
      .catch(error => {
          console.log(error);
        })
      
  },
methods:{
  //fonction pour copier coller l'id de la partie dans le press papier
  copyToClickBoard : function (){
    var content = document.getElementById('copyid').innerText;
    navigator.clipboard.writeText(content)
        .then(() => {
        console.log("Text copied to clipboard :", content)
    })
        .catch(err => {
        console.log('Something went wrong', err);
    })
}
}
}//fin de export default
</script>


<style scoped>
.nom_partie{
    width: 110%;
    height: 5rem;
    border: 2px solid white;
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    padding-top:1rem;
    background-image: repeating-linear-gradient(0deg, rgba(232,224,224, 0.08) 0px, rgba(232,224,224, 0.08) 1px,transparent 1px, transparent 11px),repeating-linear-gradient(90deg, rgba(232,224,224, 0.08) 0px, rgba(232,224,224, 0.08) 1px,transparent 1px, transparent 11px),linear-gradient(90deg, rgb(20,20,20),rgb(20,20,20));
    border-radius: 10px 10px 10px 10px;
    margin-top : 2rem;
    margin-right:1rem;
}

.identifiant{
  color:rgb(168, 149, 149);
  position: relative;
  bottom: 2rem;
}

.nom_partie h2{
    color:whitesmoke;
    text-shadow: 2px 2px 4px black;
}

.liste_joueurs{
    width: 110%;
    min-height: 12rem;
    border: 2px solid white;
    display: flex;
    justify-content:flex-start;
    flex-direction: column;
    background-image: repeating-linear-gradient(0deg, rgba(232,224,224, 0.08) 0px, rgba(232,224,224, 0.08) 1px,transparent 1px, transparent 11px),repeating-linear-gradient(90deg, rgba(232,224,224, 0.08) 0px, rgba(232,224,224, 0.08) 1px,transparent 1px, transparent 11px),linear-gradient(90deg, rgb(20,20,20),rgb(20,20,20));
    border-radius: 10px 10px 10px 10px;
    margin-top : 2rem;
    margin-right:1rem;
}

li{
    color:whitesmoke;
    text-decoration: none;
}

.joueurs{
    color: whitesmoke;
    text-shadow: 2px 2px 4px black;
    padding-left: 1.5rem;
}

.avatar {
  object-fit: cover;
  width: 2em;
  height: 2em;
  border-radius: 100%;
  border: 1px solid whitesmoke;
  background-color: #030303;
  position: relative;
  top:0.7rem;
}

.fa-copy{
  margin-left: 2rem;
  color: whitesmoke;
  width: 1.5rem;
  height: 1.5rem;
}

.fa-copy:hover{
  transform: scale(1.4);
  cursor: pointer;
}

#btn_copy{
  background: transparent;
  border: none;
}

/* Partie responsive ================================================ */

@media only screen and (max-width: 900px) {

.nom_partie {
  width: 95%;
}

.liste_joueurs {
  width: 95%;
}

}
</style>
