<template>
  <div class="btn from-right" v-on:click.prevent="quitter()">
    Quitter la partie
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "Btn_quitter",
  props: {
    msg: String,
  },
  methods: {
    quitter: function () {
      const ipStatic = this.$store.state.ip_static
      let text = "Voulez vous quitter définitivement cette partie ?";
      if(confirm(text) == true){
      //requête back pour effacer ce joueur dans la BDD ==================
      const idDeleted = this.$store.state.idPseudo
      console.log("store : ", this.$store.state.idPseudo)

      axios
        .delete('http://' + `${ipStatic}` + ':8000/partie/' + `${idDeleted}`)
        // .delete('http://localhost:8000/partie/' + `${idDeleted}`)
        .then((response) => {
          console.log(response)
          this.$router.push("/");
        })
        .catch(error => {
          console.log(error);
          this.$router.push("/");
        })
      } else {
        console.log("Quitter la partie annulée")
      }
    },
  },
};
</script>

<style scoped>
.btn {
  position: relative;
  width: 100%;
  padding: 0.5rem 1rem;
  display: flex;
  justify-content: center;
  font-size: 1.4rem;
  color: red;
  transition: all 500ms cubic-bezier(0.77, 0, 0.175, 1);
  cursor: pointer;
  user-select: none;
  margin-top: 3rem;
  margin-bottom: 0.5rem;
  background-image: repeating-linear-gradient(
      0deg,
      rgba(232, 224, 224, 0.08) 0px,
      rgba(232, 224, 224, 0.08) 1px,
      transparent 1px,
      transparent 11px
    ),
    repeating-linear-gradient(
      90deg,
      rgba(232, 224, 224, 0.08) 0px,
      rgba(232, 224, 224, 0.08) 1px,
      transparent 1px,
      transparent 11px
    ),
    linear-gradient(90deg, rgb(20, 20, 20), rgb(20, 20, 20));
  border-radius: 10px 10px 10px 10px;
}

.btn:before,
.btn:after {
  content: "";
  position: absolute;
  transition: inherit;
}

.btn:hover {
  color: #96b7c4;
  transition-delay: 0.5s;
}

.btn:hover:before {
  transition-delay: 0s;
}

.btn:hover:after {
  background: whitesmoke;
  transition-delay: 0.35s;
}

/* From Right */

.from-right:before,
.from-right:after {
  top: 0;
  width: 0;
  height: 100%;
}

.from-right:before {
  left: 0;
  border: 1px solid whitesmoke;
  border-left: 0;
  border-right: 0;
}

.from-right:after {
  right: 0;
}

.from-right:hover:before,
.from-right:hover:after {
  width: 100%;
}

a {
  text-decoration: none;
}

/* Partie responsive ================================================ */

@media only screen and (max-width: 900px) {
  .btn {
    width: 85%;
  }
}
</style>