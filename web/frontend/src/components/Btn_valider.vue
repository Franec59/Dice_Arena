<template>
    <button type="submit" class="button-53">Valider</button>
</template>
<script>
export default {
  name: 'Btn_valider',
  props: {
    msg: String
  },
  
}
</script>

<style scoped>
.button-53 {
    background-image: repeating-linear-gradient(0deg, rgba(232,224,224, 0.08) 0px, rgba(232,224,224, 0.08) 1px,transparent 1px, transparent 11px),repeating-linear-gradient(90deg, rgba(232,224,224, 0.08) 0px, rgba(232,224,224, 0.08) 1px,transparent 1px, transparent 11px),linear-gradient(90deg, rgb(20,20,20),rgb(20,20,20));
  border: 0 solid #E5E7EB;
  box-sizing: border-box;
  color: whitesmoke;
  display: flex;
  font-size: 1rem;
  font-weight: 700;
  justify-content: center;
  line-height: 1.75rem;
  padding: .75rem 1.65rem;
  position: relative;
  text-align: center;
  text-decoration: none #000000 solid;
  text-decoration-thickness: auto;
  width: 50%;
  max-width: 460px;
  position: relative;
  cursor: pointer;
  transform: rotate(-2deg);
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  margin-top: 2rem;
}

.button-53:focus {
  outline: 0;
}

.button-53:after {
  content: '';
  position: absolute;
  border: 3px solid whitesmoke;
  bottom: 10px;
  left: 15px;
  width: calc(100% - 10px);
  height: calc(100% - 10px);
}


.button-53:hover:after {
  bottom: 2px;
  left: 2px;
}

@media (min-width: 768px) {
  .button-53 {
    padding: .75rem 3rem;
    font-size: 1.25rem;
  }
}
</style>