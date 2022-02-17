<template>
  <div class="about">
    <h1>page de test</h1>
    <button v-on:click.prevent="modifier()">modifier</button>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: "About",
computed:{
    ...mapState(['idPartie', 'profil']),
    
  },
mounted (){
  console.log("id de la partie :", this.$store.state.idPartie)
  console.log("profil du joueur :", this.$store.state.profil)
  console.log("id du pseudo :" , this.$store.state.idPseudo)

},
methods:{
  modifier: function(){
    this.$store.commit("SET_IDPARTIE", null);
    this.$store.commit("SET_PROFIL", "doudou");
  }
}

  
}//fin de about

// {
//     headers: {
//         'Content-Type': 'application/json;charset=UTF-8',
//         'Access-Control-Allow-Origin': '*',
//         "Accept": "application/json",
//         'Access-Control-Allow-Methods' : "POST, GET, OPTIONS, DELETE, PUT",
//         'Access-Control-Allow-Headers': "append,delete,entries,foreach,get,has,keys,set,values,Authorization"
//     },


// liens vers les pages en attendant la connexion avec le back => a supprimer ensuite ========
    //dataIdPartie => id de la partie venant du backend ( bdd )
    // const dataIdPartieNeutre = "n214"
    // const dataIdPartieWh = "wh18"
    // const dataIdPartieDd = "add12"
    
    // if ( this.idPartie == dataIdPartieNeutre ){
    //   this.$router.push({ name: 'Neutre', params: { id: dataIdPartieNeutre }})
    // }
    // else if ( this.idPartie == dataIdPartieWh){
    //   this.$router.push({ name: 'Warhammer', params: { id: dataIdPartieWh }})
    // } 
    // else if ( this.idPartie == dataIdPartieDd){
    //   this.$router.push({ name: 'Donjon', params: { id: dataIdPartieDd }})
    // } else {
    //     this.$router.push('/error');
    // }

// lien vers le template choisi + id de la partie
          // if (idPartieRes && templateRes) {
          //   this.$router.push({
          //     name: templateRes,
          //     params: { id: idPartieRes },
          //   });
          // } else {
          //   this.$router.push("/error");
          // }



</script>



<style scoped>
h1{
  color:white;
}
</style>