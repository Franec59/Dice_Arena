<template>
  <div class="btn from-right" v-on:click.prevent="deletePseudo()">Supprimer mon pseudo</div>
</template>

<script>
import axios from 'axios';

export default {
  name: "Btn_supprimer",
  props: {
    msg: String,
  },
  
  methods: {
    deletePseudo: function () {
      const idDeleted = this.$store.state.idPseudo
      console.log("store : ", this.$store.state.idPseudo)
      const ipStatic = this.$store.state.ip_static

      axios.defaults.baseURL = 'http://' + `${ipStatic}` + ':8000/partie';
      axios.defaults.headers.post['Content-Type'] ='application/json;charset=utf-8';
      axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
      axios
        .delete('http://' + `${ipStatic}` + ':8000/partie/' + `${idDeleted}`)
        // .delete('http://localhost:8000/partie/' + `${idDeleted}`)
        .then((response) => {
          console.log(response)
          this.$router.push("/pseudo");
        })
        .catch(error => {
          console.log(error);
        })
    },
  },
  
};
</script>

<style scoped>
.btn {
  position: relative;
  padding: 0.5rem 1rem;
  font-size: 1.4rem;
  color: whitesmoke;
  transition: all 500ms cubic-bezier(0.77, 0, 0.175, 1);
  cursor: pointer;
  user-select: none;
  margin-top: 1.5rem;
  margin-bottom: 0.5rem;
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
</style>