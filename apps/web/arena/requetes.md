# Requetes pour le front

## front : utilisation d'axios pour les requêtes
https://fr.vuejs.org/v2/cookbook/using-axios-to-consume-apis.html
> mounted () {
    axios
      .get('https://api.coindesk.com/v1/bpi/currentprice.json')
      .then(response => (this.info = response))
  }

## besoins pour le backend

### Pseudo
page : views/pseudo.vue
POST => bdd : envoi au back le pseudo et le profil du joueur
.   pseudo du joueur
.   profil : master ou joueur
>createPseudo() {
      const newPseudo = {
        pseudo : this.pseudo,
        profil : this.profilChoice
      }
      axios.post('http://...., newPseudo )

le back renvoi l'id du pseudo (idPseudo)

### createPartie
page : views/createPartie

1) get => bdd pour pouvoir afficher le pseudo du joueur (master) sur la page
>created(){
    axios.get('http://..../idPseudo )
    .then(response => { pseudo +idPseudo
  },

le back renvoi le pseudo du joueur + idPseudo

2) POST => bdd : pour la création de la partie
. nom de la partie
. idPseudo ( pour associer la partie au pseudo qui la créé)

>createPartie() {
        const newPartie = {
            partie : this.partie,
            idPseudo : this.idPseudo
        }
      axios.post('http://...., newPartie )
         .then(response => {
          console.log(response);
         response : ok + id de la partie
        this.$router.push("/en fonction du template/ { id de la partie }");
        })
        .catch(error => {
          console.log(error);
       })

le back renvoi l'id de la partie

### joinPartie
page : views/joinPartie

1) get => bdd pour pouvoir afficher le pseudo du joueur (joueur) sur la page
>created(){
    axios.get('http://..../idPseudo )
    .then(response => { pseudo +idPseudo
  },

le back renvoi le pseudo du joueur + idPseudo

2) POST => bdd : pour rejoindre une partie, le joueur entre l'id de la partie
.   id de la partie
.   id du pseudo qui rejoint la partie ( idPseudo)

>joinPartie() {
        const joinPartie = {
            idPartie : this.idPartie,
            idPseudo : this.idPseudo
        }
    // requete Get by id ou by name avec Axios pour le back
    //=====================================================
      // axios.post('http://...., idPartie )
      //   .then(response => {
       //     response => ok 
      //     this.$router.push("/en fonction du template/ { id de la partie }");
      //   })
      //   .catch(error => {
      //     console.log(error);
      //   })


### pour chaque template
page : views/"nom template"
get => bdd pour obtenir les informations de la partie :
.   nom de la partie
.   id de la partie
.   pseudo du joueur (master)
.   pseudo du joueur '1'
.   pseudo du joueur 'n'

>templatePartie() {
    // requete avec Axios pour le back
    //===============================================
      // axios.get('http://...., idPartie)
      //   .then(response => {
      //     console.log(response);
      //    response : idPartie + nom de la partie + pseudos des joueurs
      //   })
      //   .catch(error => {
      //     console.log(error);
      //   })
      }

### Bouton cloturer la partie
page : component/Btn_cloturer.vue

delete => bdd : en cloturant la partie le master efface les données ( partie + tous les pseudos)

>methods:{
    cloture: function() {
      this.$router.push('/')
      // requête back pour effacer les données dans la BDD
	  // axios.delete(http://......./idPartie)
    }
  }

### Bouton quitter la partie
page : component/Btn_quitter.vue

delete => bdd : en quittant la partie le joueur efface les données concernant son pseudo 

>methods:{
    quit: function() {
      this.$router.push('/')
      // requête back pour effacer les données dans la BDD
	  // axios.delete(http://......./idPseudo)
    }
  }



