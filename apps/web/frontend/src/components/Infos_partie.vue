<template>
    <div class="joueurs">
      <div class="nom_partie">
        <h2>{{ nomPartie }}</h2>
        <h4 class="identifiant">{{ idPartie }}</h4>
      </div>
      <div class="liste_joueurs">
        <h2 class="joueurs">Joueurs inscrits sur la partie</h2>
        <ol>
          <li>nom joueur 1</li>
          <li>nom joueur 2</li>
          <li>nom joueur 3</li>
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
import { mapState } from 'vuex'

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
      profil:""
    }
  },
  mounted (){

    this.profil = this.$store.state.profile
    console.log(this.profil)
     
    //requete GET pour récupérer la liste des joueurs ================================================
      axios.defaults.baseURL = 'http://localhost:8000/partie';
      axios.defaults.headers.post['Content-Type'] ='application/json;charset=utf-8';
      axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
      
      axios
      .get('http://localhost:8000/partie',
      {
    headers: {
        'Content-Type': 'application/json;charset=UTF-8',
        'Access-Control-Allow-Origin': '*',
        "Accept": "application/json",
        'Access-Control-Allow-Methods' : "POST, GET, OPTIONS, DELETE, PUT",
        'Access-Control-Allow-Headers': "append,delete,entries,foreach,get,has,keys,set,values,Authorization"
    },
      }
      )
      .then(response => {
          console.log(response);
        })
      .catch(error => {
          console.log(error);
        })
      
  },

computed:{
    ...mapState(['nomPartie', 'idPartie'])
    
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
