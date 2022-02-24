<template>
  <div class="lobby">
    <div class="template">
      <div class="template_title">
        <h1 class="yam">Craps</h1>
      </div>
      <div class="lancer" v-on:click.prevent="lancer()">
        <h3>Lancer les dés</h3>
      </div>
      <div class="template_rendu">
        <h3>Voici les règles de base du jeu de Craps selon le lancer de deux dés à 6 faces :</h3>
        <ul>
          <li>le joueur qui obtient 7 ou 11 remporte sa mise</li>
          <li>le joueur qui obtient 2, 3 ou 12 perd l’ensemble de sa mise. C’est ce qui s’appelle le « Craps ».</li>
          <li>le joueur qui obtient 4, 5, 6, 8, 9 ou 10 fait « le point ». Il doit alors relancer les dés jusqu’à ce que le point soit de nouveau obtenu. Si le point sort les mises sont gagnantes. Si un 7 est obtenu avant le point toutes les mises sont perdantes.</li>
        </ul>
        <h3>Pour jouer, appuyer sur le bouton lancer les dés</h3>
        <div class="affiche_resultat" v-show="craps">
          <h3>Sur ce lancé, vous obtenez : {{dice1}} et {{dice2}} pour un total de {{currentPoint}}</h3>
          <h4>{{resultat}}</h4>
        </div>
        <div class="affiche_resultat" v-show="lepoint">
          <h3 v-show="current">Sur ce lancé, vous obtenez : {{dice1}} et {{dice2}} pour un total de {{currentPoint}}</h3>
          <h3 v-show="newP">Sur ce lancé, vous obtenez : {{dice3}} et {{dice4}} pour un total de {{newPoint}}</h3>
          <h4>Vous devez faire le point à : {{currentPoint}}</h4>
          <div class="lancer" v-on:click.prevent="relancer()" v-show="bouton">
            <h3>Relancer</h3>
          </div>
          <h4 v-show="crapsEnd">{{resultat2}}</h4>
        </div>
      </div><!--fin de template_rendu-->
      </div><!--fin de template-->
      
    <Infos_partie />
    <!--fin de joueurs-->
  </div>
  <!--fin de lobby-->
</template>

<script>
import Infos_partie from "@/components/Infos_partie.vue";
import axios from "axios";

export default {
  name: "Craps",
  components: {
    Infos_partie
  },
  data() {
    return {
      profil: "",
      dice1: "",
      dice2:"",
      currentPoint:"",
      resultat:"",
      lepoint:false,
      craps:false,
      dice3:"",
      dice4:"",
      newPoint:"",
      resultat2:"",
      crapsEnd:false,
      current:true,
      newP:false,
      bouton:true
    
      };
  },
  props: ["id"],

  methods:{

    relancer(){
      axios
      .post("http://localhost:8020/relance")
      .then((response) => {
        console.log("relance :", response)
        this.dice3=response.data[1][0]
        this.dice4=response.data[1][1]
        this.newPoint=response.data[0]

        if(this.newPoint == this.currentPoint){
          this.resultat2="Gagné, toutes les mises sont gagnantes !"
          this.craps = false
          this.lepoint = true
          this.crapsEnd = true
          this.current = false
          this.newP = true
          this.bouton = false
        }
        else if(this.newPoint == 7){
          this.resultat="Perdu, toutes les mises sont perdantes !"
          this.craps = false
          this.lepoint = true
          this.crapsEnd = true
          this.current = false
          this.newP = true
          this.bouton = false
        }
        else {
          this.craps = false
          this.lepoint = true
          this.crapsEnd = false
          this.current = false
          this.newP = true
          this.bouton = true
        }
        
      })
      .catch(error => {
        console.log(error);
    })

    },

    lancer(){
    axios
      .post("http://localhost:8020/launch")
      .then((response) => {
        console.log("launch :", response)
        
      })
      .catch(error => {
        console.log(error);
    })
    axios
      .get("http://localhost:8020/check")
      .then((response) => {
        console.log("check :", response)
        this.dice1=response.data[2][0]
        this.dice2=response.data[2][1]
        this.currentPoint=response.data[1]

        let result=response.data[0]
        console.log(result)
        if(result == "v"){
          this.resultat="Gagné, vous remportez la mise !"
          this.craps = true
          this.lepoint = false
        }
        else if(result == "p"){
          this.resultat="Perdu, vous perdez votre mise !"
          this.craps = true
          this.lepoint = false
        }
        else if(result == "c"){
          this.lepoint = true
          this.craps = false
        }
      })
      .catch(error => {
        console.log(error);
    })
    }   // fin de la fonction lancer
  },   // fin de methods lancer

};
</script>

<style scoped>
.lobby {
  margin: auto;
  margin-top: 4rem;
  margin-bottom: 2rem;
  width: 90%;
  border: 1px solid white;
  min-height: 100vh;
  border-radius: 20px 20px 20px 20px;
  background-image: url(../assets/images/craps.png);
  background-size: cover;
  background-repeat: no-repeat;
  display: flex;
  justify-content: space-around;
  padding-bottom: 2rem;
}

.template {
  display: flex;
  justify-content: flex-start;
  flex-direction: column;
  align-items: center;
}

.template_title {
  background-image: url(../assets/images/craps_logo.png);
  background-size: cover;
  background-repeat: no-repeat;
  margin-top: 2rem;
  margin-bottom: 4rem;
  width: 20rem;
  height: 10rem;
}

.yam {
  color: whitesmoke;
  text-shadow: 4px 4px 6px black;
  font-size: 3rem;
}

.lancer {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 10rem;
  height: 10rem;
  border-radius: 50%;
  border: 2px solid wheat;
  background-image: radial-gradient(
    circle at center center,
    rgb(86, 197, 113),
    rgb(77, 181, 95),
    rgb(67, 165, 77),
    rgb(58, 149, 59),
    rgb(48, 133, 41)
  );
}

.lancer h3 {
  padding: auto;
  color: whitesmoke;
  font-size: 1.3rem;
  text-shadow: 2px 2px 4px black;
}

.lancer:hover {
  cursor: pointer;
  transform: scale(1.1);
}

.template_rendu {
  width: 90%;
  min-height: 20rem;
  border: 2px solid wheat;
  margin-top: 3rem;
  background-image: linear-gradient(
      127deg,
      rgba(153, 255, 88, 0.46) 0%,
      rgba(153, 255, 88, 0.46) 14.286%,
      rgba(134, 245, 84, 0.46) 14.286%,
      rgba(134, 245, 84, 0.46) 28.572%,
      rgba(114, 236, 80, 0.46) 28.572%,
      rgba(114, 236, 80, 0.46) 42.858%,
      rgba(95, 226, 76, 0.46) 42.858%,
      rgba(95, 226, 76, 0.46) 57.144%,
      rgba(76, 216, 72, 0.46) 57.144%,
      rgba(76, 216, 72, 0.46) 71.43%,
      rgba(56, 207, 68, 0.46) 71.43%,
      rgba(56, 207, 68, 0.46) 85.716%,
      rgba(37, 197, 64, 0.46) 85.716%,
      rgba(37, 197, 64, 0.46) 100.002%
    ),
    linear-gradient(
      285deg,
      rgb(116, 183, 117) 0%,
      rgb(116, 183, 117) 14.286%,
      rgb(113, 173, 114) 14.286%,
      rgb(113, 173, 114) 28.572%,
      rgb(110, 163, 110) 28.572%,
      rgb(110, 163, 110) 42.858%,
      rgb(107, 154, 107) 42.858%,
      rgb(107, 154, 107) 57.144%,
      rgb(104, 144, 103) 57.144%,
      rgb(104, 144, 103) 71.43%,
      rgb(101, 134, 100) 71.43%,
      rgb(101, 134, 100) 85.716%,
      rgb(98, 124, 96) 85.716%,
      rgb(98, 124, 96) 100.002%
    );
  padding-left: 1rem;
  color: whitesmoke;
}

.affiche_resultat{
  background-color: rgb(101, 134, 100, 0.4);
  padding-left:0.5rem;
  padding-top: 0.5rem;
  padding-bottom: 1.5rem;
  margin-right: 1rem;
  margin-bottom: 1rem;
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
}

/* Partie responsive ================================================ */

@media only screen and (max-width: 900px) {
  .lobby {
    flex-direction: column;
  }

}
</style>