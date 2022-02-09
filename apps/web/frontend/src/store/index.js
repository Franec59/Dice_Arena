import { createStore } from 'vuex'

export default createStore({
  state: {
    pseudoMaster : "Nom du joueur"

  },
  mutations: {
    SET_PSEUDOMASTER(state, pseudoRes){
      state.pseudoMaster = pseudoRes
    }
  },
  actions: {
  },
  modules: {
  }
})
