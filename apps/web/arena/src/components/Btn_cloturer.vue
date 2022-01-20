<template>
    <div class="btn from-right" v-on:click.prevent="goToHome()">Cloturer la partie</div>
</template>

<script>
export default {
  name: 'Btn_cloturer',
  props: {
    msg: String
  },
  methods:{
    goToHome: function() {
      this.$router.push('/')
      // requête back pour effacer les données dans la BDD
    }
  }
}
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
    background-image: repeating-linear-gradient(0deg, rgba(232,224,224, 0.08) 0px, rgba(232,224,224, 0.08) 1px,transparent 1px, transparent 11px),repeating-linear-gradient(90deg, rgba(232,224,224, 0.08) 0px, rgba(232,224,224, 0.08) 1px,transparent 1px, transparent 11px),linear-gradient(90deg, rgb(20,20,20),rgb(20,20,20));
    border-radius: 10px 10px 10px 10px;
}

.btn:before, .btn:after {
	content: '';
	position: absolute;	
	transition: inherit;
}

.btn:hover {
	color: #96B7C4;
	transition-delay: .5s;
}

.btn:hover:before {
	transition-delay: 0s;
}

.btn:hover:after {
	background: whitesmoke;
	transition-delay: .35s;
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

a{
    text-decoration: none;
}

/* Partie responsive ================================================ */

@media only screen and (max-width: 900px) {

.btn{
	width: 85%;
}

}
</style>