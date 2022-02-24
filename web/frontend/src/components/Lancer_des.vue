<template>
    <h1>lancer 3D</h1>
    <div id="info_div" style="display: none">
      <div class="center_field">
        <span id="label"></span>
      </div>
      <div class="center_field">
        <div class="bottom_field">
          <span id="labelhelp">click to continue or tap and drag again</span>
        </div>
      </div>
    </div>
    <div id="selector_div" style="display: none">
      <div class="center_field">
        <div id="sethelp">
          choose your dice set by clicking the dices or by direct input of
          notation,<br />
          tap and drag on free space of screen or hit throw button to roll
        </div>
      </div>
      <div class="center_field">
        <input type="text" id="set" value="4d6" />
        <button id="clear">clear</button>
        <button style="margin-left: 0.6em" id="throw">throw</button>
      </div>
    </div>
    <div id="canvas"></div>
</template>

<script>
import { loadScript } from "vue-plugin-load-script";

export default {
  name: 'Lancer_des',
  props: {
    msg: String,
    
  },

mounted(){
  loadScript("/libs/three.min.js")
      .then(() => {
        console.log("threejs ok");
      })
      .catch(() => {
        console.log("threejs not ok")
      });

  loadScript("/libs/cannon.min.js")
      .then(() => {
        console.log("cannon ok");
      })
      .catch(() => {
        console.log("cannon not ok")
      });

  loadScript("/teal.js")
      .then(() => {
        console.log("teal ok");
      })
      .catch(() => {
        console.log("teal not ok")
      });

  loadScript("/dice.js")
      .then(() => {
        console.log("dice ok");
      })
      .catch(() => {
        console.log("dice not ok")
      });

  loadScript("/main.js")
      .then(() => {
        console.log("main ok");
      })
      .catch(() => {
        console.log("main not ok")
      });

    let initialize = document.createElement('script');
      initialize.setAttribute('type', 'text/javascript')
      initialize.setAttribute('defer', 'defer', );
      initialize.innerText = 'dice_initialize(document.body)'
      document.body.appendChild(initialize)
},

  

}//fin de export default

</script>


<style scoped>

/* #svg *, .svg * {
    -moz-user-select: none;
    -webkit-user-select: none;
    -khtml-user-select: none;
    -o-user-select: none;
    user-select: none;
} */

#waitform {
    position: absolute;
    width: 100%;
    height: 100%;
    z-index: 10000;
    cursor: wait;
}

a {
    color: gray;
}

em {
    border: 1px rgba(0, 0, 0, 0.2) solid;
    font-style: normal;
    padding: 0px 3px;
    background-color: rgba(0, 0, 0, 0.08);
    border-radius: 3px;
}

body {
    font-family: Georgia;
}

h6 {
    font-size: 100%;
    font-weight: normal;
    margin: 0px;
}

p {
    font-size: 80%;
    margin-top: 5px;
    margin-bottom: 0px;
}

.control_panel {
    padding: 15px;
    padding-bottom: 0px;
    position: absolute;
    z-index: 10;
}

.center_field {
    position: absolute;
    text-align: center;
    height: 100%;
    width: 100%;
}

.center_field * {
    position: relative;
    font-family: Trebuchet MS;
    background-color: rgba(255, 255, 255, 0.6);
    padding: 5px 15px;
}

.center_field br {
    background-color: rgba(0, 0, 0, 0);
}

.bottom_field {
    position: absolute;
    text-align: center;
    bottom: 5px;
    width: inherit;
    padding: 0px;
}

#label {
    font-size: 32pt;
    word-spacing: 0.5em;
    padding: 5px 15px;
    color: rgba(21, 26, 26, 0.6);
    top: 45%;
}

#labelhelp {
    font-size: 12pt;
    padding: 5px 15px;
    color: rgba(21, 26, 26, 0.5);
    bottom: 50px;
}

#set {
    text-align: center;
    font-size: 26pt;
    border: none;
    color: rgba(0, 0, 0, 0.8);
    background-color: rgba(255, 255, 255, 0);
    top: 60%;
}

#sethelp {
    font-size: 12pt;
    color: rgba(21, 26, 26, 0.5);
    background: none;
    top: 25%;
}

#selector_div button {
    font-size: 20pt;
    color: rgb(255, 255, 255);
    background-color: rgba(0, 0, 0, 0.6);
    cursor: pointer;
    border: none;
    width: 5em;
    top: 62%;
}

.dice_place {
    position: absolute;
    border: solid black 1px;
}
</style>
