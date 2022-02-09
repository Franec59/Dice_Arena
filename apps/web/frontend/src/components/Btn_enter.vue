<template>
  <div class="btn-enter" v-on:click.prevent="goToPseudo()">
    <a href="" class="btn">
      <svg width="277" height="62">
        <defs>
          <linearGradient id="grad1">
            <stop offset="0%" stop-color="#FF8282" />
            <stop offset="100%" stop-color="#E178ED" />
          </linearGradient>
        </defs>
        <rect
          x="5"
          y="5"
          rx="25"
          fill="none"
          stroke="url(#grad1)"
          width="266"
          height="50"
        ></rect>
      </svg>
      <span>Entrez dans l'arène</span>
    </a>
  </div>
</template>

<script>
export default {
  name: 'Btn_enter',
  props: {
    msg: String
  },
  methods:{
    goToPseudo: function() {
      this.$router.push('/pseudo') 
    }
  }
}
</script>


<style scoped>
.btn-enter {
  height: 100%;
  position: relative;
  bottom: 0.5rem;
  margin-top: 3rem;
  margin-bottom: 1rem;
}

.btn {
  /* margin-top: calc(50% + 25px); */
  /* position: relative; */
  display: inline-block;
  width: 277px;
  height: 50px;
  font-size: 1em;
  font-weight: bold;
  line-height: 60px;
  text-align: center;
  cursor: pointer;
  text-decoration: none;
  letter-spacing: 0.045em;
  color: wheat;
}

.btn svg {
  position: absolute;
  top: 0;
  left: 0;
}

.btn svg rect {
  stroke: wheat;
  stroke-width: 4;
  stroke-dasharray: 353, 0;
  stroke-dashoffset: 0;
  -webkit-transition: all 600ms ease;
  transition: all 600ms ease;
}

/*fond derrière le texte*/
.btn span {
  background: transparent;
}

.btn:hover svg rect {
  stroke-width: 4;
  stroke-dasharray: 196, 543;
  stroke-dashoffset: 437;
}
</style>