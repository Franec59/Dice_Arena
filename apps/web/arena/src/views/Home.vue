<template>
  <div class="homepage">
    <div class="container-grid">
      <div class="bloc1"></div>
      <div class="bloc2">
        <div class="bienvenue">
          <h1 class="affichage">Bienvenue sur<br />Dice-Aréna</h1>
          <h2 class="affichage2">Une aide de jeux</h2>
          <h3 class="affichage2">Multijoueur & Thématique<br /> de lancé de dés !</h3>
        </div>
        <!--insertion du cube-->
        <Cube />
      </div>
      <div class="bloc3"></div>
      <div class="bloc4">
        <!-- logo de xavier -->
        <div class="logo">
          <!-- <img src="../assets/images/logo_da.png" alt="Logo_dice_arena" /> -->
        </div>
        
        <!-- btn enter -->
        <Btn_enter />
      </div>
      <div class="bloc5"></div>
      <div class="bloc6"></div>
      <div class="bloc7">
        <h2 class="affichage2">Les règles de l'arène</h2>
      </div>
    </div>
  </div>
</template>

<script>
// modele pour importer components
// import HelloWorld from '@/components/HelloWorld.vue'
import Btn_enter from "@/components/Btn_enter.vue";
import Cube from "@/components/Cube.vue";

export default {
  name: "Home",
  components: {
    // HelloWorld,
    Btn_enter,
    Cube,
  },
  
};
</script>

<style scoped>
.homepage {
  width: 65%;
  margin: auto;
  margin-top: 2rem;
}

.affichage {
  color: rgb(171, 219, 75);
  text-shadow: 2px 2px 4px black;
}

.affichage2 {
  color: white;
  text-shadow: 2px 2px 4px black;
}

.container-grid {
  width: 100%;
  height: 50rem;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
  grid-template-rows: 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr;
  grid-template-areas:
    "a a a a b b"
    "a a a a b b"
    "a a a a b b"
    "c c d d b b"
    "c c d d e e"
    "c c d d e e"
    "f f d d e e"
    "f f g g e e";
}

.bloc1 {
  background-image: url(../assets/images/WH_Mobile_Hero_Generic.jpg);
  background-position: center;
  background-size: cover;
  grid-area: a;
  border-radius: 20px 0px 0px 0px;
}
.bloc2 {
  grid-area: b;
  background-image: url(../assets/images/d-background1.jpg);
  background-size: cover;
  background-repeat: no-repeat;
  border-radius: 0px 20px 0px 0px;
  text-align: center;
}
.bloc3 {
  grid-area: c;
  background-image: url(../assets/images/d-fiche.jpg);
  background-position: center;
  background-size: cover;
}
.bloc4 {
  grid-area: d;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  background-color: black;
  color: antiquewhite;
}

.logo{
  margin-top: 2rem;
  width: 100%;
  height: 100rem;
  background-image: url(../assets/images/logo_da.png);
  background-position: center;
  background-size: contain;
  background-repeat: no-repeat;
}

.bloc5 {
  grid-area: e;
  background-image: url(../assets/images/d-bag.jpg);
  background-position: center;
  background-size: cover;
  border-radius: 0px 0px 20px 0px;
}
.bloc6 {
  grid-area: f;
  background-image: url(../assets/images/d-plateau.jpg);
  background-position: center;
  background-size: cover;
  border-radius: 0px 0px 0px 20px;
}

.bloc7 {
  grid-area: g;
  background-image: linear-gradient(
      45deg,
      rgb(73, 160, 30) 0%,
      rgb(73, 160, 30) 6%,
      rgb(88, 141, 55) 6%,
      rgb(88, 141, 55) 11%,
      rgb(103, 122, 81) 11%,
      rgb(103, 122, 81) 55%,
      rgb(118, 103, 106) 55%,
      rgb(118, 103, 106) 81%,
      rgb(132, 84, 131) 81%,
      rgb(132, 84, 131) 83%,
      rgb(147, 65, 156) 83%,
      rgb(147, 65, 156) 92%,
      rgb(162, 46, 182) 92%,
      rgb(162, 46, 182) 95%,
      rgb(177, 27, 207) 95%,
      rgb(177, 27, 207) 100%
    ),
    linear-gradient(
      112.5deg,
      rgb(73, 160, 30) 0%,
      rgb(73, 160, 30) 6%,
      rgb(88, 141, 55) 6%,
      rgb(88, 141, 55) 11%,
      rgb(103, 122, 81) 11%,
      rgb(103, 122, 81) 55%,
      rgb(118, 103, 106) 55%,
      rgb(118, 103, 106) 81%,
      rgb(132, 84, 131) 81%,
      rgb(132, 84, 131) 83%,
      rgb(147, 65, 156) 83%,
      rgb(147, 65, 156) 92%,
      rgb(162, 46, 182) 92%,
      rgb(162, 46, 182) 95%,
      rgb(177, 27, 207) 95%,
      rgb(177, 27, 207) 100%
    ),
    linear-gradient(
      67.5deg,
      rgb(73, 160, 30) 0%,
      rgb(73, 160, 30) 6%,
      rgb(88, 141, 55) 6%,
      rgb(88, 141, 55) 11%,
      rgb(103, 122, 81) 11%,
      rgb(103, 122, 81) 55%,
      rgb(118, 103, 106) 55%,
      rgb(118, 103, 106) 81%,
      rgb(132, 84, 131) 81%,
      rgb(132, 84, 131) 83%,
      rgb(147, 65, 156) 83%,
      rgb(147, 65, 156) 92%,
      rgb(162, 46, 182) 92%,
      rgb(162, 46, 182) 95%,
      rgb(177, 27, 207) 95%,
      rgb(177, 27, 207) 100%
    ),
    linear-gradient(90deg, rgb(24, 15, 143), rgb(170, 57, 157));
  background-blend-mode: overlay, overlay, overlay, normal;
  display: flex;
  align-items: center;
  justify-content: center;
}

/*Partie responsive ================================================= */

@media screen and (max-width: 900px) {
  
  h1 {
    font-size: 1.7rem;
  }
  h2 {
    font-size: 1.1rem;
  }
  h3 {
    font-size: 0.9rem;
  }

  .container-grid {
    width: 100%;
    height: 50rem;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
    grid-template-rows: 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr;
    grid-template-areas:
      "b b b b b b"
      "b b b b b b"
      "d d d d d d"
      "d d d d d d"
      "d d d d d d"
      "d d d d d d"
      "g g g e e e"
      "g g g e e e";
  }
  
  .bloc7 {
    border-radius: 0px 0px 0px 20px;
    text-align: center;
  }

  .bloc2 {
  border-radius: 20px 20px 0px 0px;
}

}
</style>
