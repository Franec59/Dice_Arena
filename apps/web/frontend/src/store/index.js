import { createStore } from 'vuex'

export default createStore({
  state: {
    pseudoMaster : "Nom du joueur",
    idPseudo : "0000",
    nomPartie : "",
    idPartie : "",
    profile : ""
  },
  mutations: {
    SET_PSEUDO(state, pseudoRes){
      state.pseudoMaster = pseudoRes
    },
    SET_PSEUDOID(state, idPseudoRes){
      state.idPseudo = idPseudoRes
    },
    SET_NOMPARTIE(state, partieRes){
      state.nomPartie = partieRes
    },
    SET_IDPARTIE(state, idPartieRes){
      state.idPartie = idPartieRes
    },
    SET_PROFILE(state, profilRes){
      state.profile = profilRes
    }
  },
  actions: {
  },
  modules: {
  }
})
