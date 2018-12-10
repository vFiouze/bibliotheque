//Vuex configuration//
const store = new Vuex.Store({
    state : {
        name : "",
        actif : false,
        res : [],
        page : 0
    },
    mutations : {
        save(state,obj){
            state.name = obj.name
            state.actif = obj.actif
            state.page=obj.page
        },
        result(state,res){
            state.res = res
        },
    }
})
//Vuex configuration//

//Vue router configuration//
const routes = [{ path : '/prets', component : templatePret },
               { path : '/personnes', component : templatePersonne },
               { path : '/membres', component :templateMembre },
               { path : '/typeDoc', component : templateTypeDocument },
               { path : '/auteurs', component : templateAuteur },
               { path : '/docs', component : templateDocument },
               ]

const router = new VueRouter({
    routes
})
//Vue router configuration//

var app = new Vue({
    router, 
    el : "#app",
    delimiters: ["<<",">>"]
})