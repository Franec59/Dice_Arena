import { createStore } from 'vuex'
import createPersistedState from "vuex-persistedstate";

export default createStore({
  state: {
    idPartie : null,
    profil : null,
    idPseudo : null
    
  },
  mutations: {
    SET_IDPARTIE(state, idPartieRes){
      state.idPartie = idPartieRes
    },
    SET_PROFIL(state, profilRes){
      state.profil = profilRes
    },
    SET_IDPSEUDO(state, idPseudoRes){
      state.idPseudo = idPseudoRes
    },
  },
  actions: {
  },
  modules: {
  },
  plugins: [createPersistedState()]
})
