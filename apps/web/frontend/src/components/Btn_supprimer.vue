<template>
  <div class="btn from-right" v-on:click.prevent="deletePseudo()">Supprimer{{ idPseudo }}</div>
</template>

<script>
import axios from 'axios';
import { mapState } from 'vuex'

export default {
  name: "Btn_supprimer",
  props: {
    msg: String,
  },
  
  // created: function(){
  //       this.idC = this.$store.state.idPseudo
  //       console.log("this.idC =", this.idC)
  //     },

  methods: {
    deletePseudo: function () {
      // const id = this.$store.state.idPseudo
      // console.log("depuis store", id)
      axios
        .delete('http://localhost:8000/partie', { data: this.$store.state.idPseudo },
          {
            headers: {
            'Content-Type': 'application/json;charset=UTF-8',
            "Accept": "application/json",
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods' : "POST, GET, OPTIONS, DELETE, PUT",
            'Access-Control-Allow-Headers': "append,delete,entries,foreach,get,has,keys,set,values,Authorization"
          },
        }
        )
        .then((response) => {
          console.log(response)
        })
        .catch(error => {
          console.log(error);
        })

      this.$router.push("/pseudo");
    },
  },
  computed:{
    ...mapState(['idPseudo'])
    
  }
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