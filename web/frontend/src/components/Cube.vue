<template>
  <!-- dé animé -->
  <div class="container">
    <div class="cube">
      <div class="face front"></div>
      <div class="face back"></div>
      <div class="face right"></div>
      <div class="face left"></div>
      <div class="face top"></div>
      <div class="face bottom"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Cube',
  props: {
    msg: String
  }
}
</script>


<style scoped>
.container{
    width: 5rem;
    height: 5rem;
    perspective: 1000px;
    margin: 4rem auto;
}

.cube{
    width: 100%;
    height: 100%;
    position: relative;
    transform-style: preserve-3d;
    animation : spin 8s infinite linear;
}

.face{
    position: absolute;
    width: 5rem;
    height: 5rem;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1rem;
    border-radius: 10px;
}

.top{
    background-color: wheat;
    transform: rotateX(90deg) translateZ(2.5rem);
    background-image:url(../assets/images/d6-1.jpg);
    background-size: cover;
    background-repeat:no-repeat;
}
.bottom{
    transform: rotateX(-90deg) translateZ(2.5rem);
    background-image:url(../assets/images/d6-2.jpg);
    background-size: cover;
}
.right{
    transform: rotateY(90deg) translateZ(2.5rem);
    background-image:url(../assets/images/d6-3.jpg);
    background-size: cover;
}
.left{
    transform: rotateY(-90deg) translateZ(2.5rem);
    background-image:url(../assets/images/d6-4.jpg);
    background-size: cover;
}
.front{
    transform: rotateX(0deg) translateZ(2.5rem);
    background-image:url(../assets/images/d6-5.jpg);
    background-size: cover;
}
.back{
    transform: rotateX(-180deg) translateZ(2.5em);
    background-image:url(../assets/images/d6-6.jpg);
    background-size: cover;
}


@keyframes spin {
    from {transform: rotateX(0deg) rotateY(0deg);
    }
    to {transform: rotateX(360deg) rotateY(360deg);
    }
}

/*Partie responsive ================================================= */

@media screen and (max-width: 900px) {
    .container{
        display:none;
    }
}
</style>