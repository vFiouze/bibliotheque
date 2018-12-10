const templatePret = Vue.component('templatePret', {
    data : function(){
        return{
            name : "",
            actif : false,
            res : [],
            page : 1,
            showComponent: false
        }
    },
    watch : {
        memberSearch: function(){
            var texte = this.memberSearch
            if (texte.length >=2){
                url = 'http://localhost:8000/bibliotheque/searchmembre?member='+texte
                fetch(url)
                .then(data=>{
                    return data.json()})
                .then(res=>{var a =1
                            a=a+1
                })
            }
        },
    },
    methods : {
        filter(p){
            //on sauvegarde l'etat dans le store
            var name = this.name
            var actif = this.actif
            if (p==null){
                var page = 1
            }else{
                var page = p+1
            }
            store.commit('save',this)
            //construction de la requête
            var that = this
            var nameadd = 0
            var actifadd= 0
            var url = "http://localhost:8000/bibliotheque/liste?"
            if (name != ""){
                url = url + "name="+name
                nameadd = 1
            }
            if (actif == true){
                if (nameadd ==1){
                    url = url + "&"
                }
                url = url + "actif=1"
                actifadd = 1
            }
            if (nameadd==1 || actifadd==1){
                url = url + "&"
                }
            url = url+"page="+page.toString()
            fetch(url)
            .then(data=>{
                    return data.json()})
            .then(res=>{for(var i in res.data){
                        var dtEnd = res.data[i].LOAN_END_EFFECTIVE_DATE
                        var dtStart = res.data[i].LOAN_START_DATE
                        var dtEndF = moment(dtEnd).format("DD/MM/YYYY")
                        var dtStartF = moment(dtStart).format("DD/MM/YYYY")
                        res.data[i].LOAN_END_EFFECTIVE_DATE = dtEndF
                        res.data[i].LOAN_START_DATE = dtStartF
                        }
                        that.res = res
                        store.commit('result',res)
                        try{
                            var v = document.getElementsByClassName("active")[0]
                            if (v){
                                v.classList.remove("active")
                            }   
                        }catch(err){
                            console.log(err)
                        }
                        var x = document.getElementById(p.toString()).parentNode.classList.add("active")
                       })
        },
        ajoutpret(){
            this.showComponent==true ? this.showComponent=false : this.showComponent=true
            }
    },
    mounted:function(){
        //On restaure l'état à l'affichage du composant
        this.name = store.state.name
    },
    template :  '<div id="content"> \
                <h1>Pret</h1> \
                    <p>Consulter les prêts en cours ou <a href="#" v-on:click="ajoutpret" data-toggle="modal" data-target="#modalAjout">ajoutez en un</a></p>\
                    <ajoutPret v-if="showComponent"></ajoutPret>\
                    <div class="container"> \
                        <form> \
                            <div class ="row align-items-center"> \
                                        <div class="col-1"> \
                                            <label>Membre </label>\
                                        </div>\
                                        <div class="col-5"> \
                                            <input v-model="name" type="text" class="form-control" id="membreName">\
                                        </div>\
                                        <div class="col-4"> \
                                            <input type="checkbox" class="form-check-input" id="actif" v-model="actif"> Uniquement les prêts en cours\
                                        </div>\
                                        <div class="col"> \
                                            <button type="submit" class="btn btn-primary" v-on:click="filter(0)"> Afficher</button>\
                                        </div>\
                            </div> \
                        </form> \
                        <div class="row">\
                            <table class="table table-striped table-hover">\
                                <thead>\
                                    <tr>\
                                        <th>Membre</th>\
                                        <th>Document</th>\
                                        <th>Date du prêt</th>\
                                        <th>Identifiant du prêt</th>\
                                    </tr>\
                                </thead>\
                                <tbody>\
                                    <tr v-for="donnee in res.data">\
                                        <td id="memberId">{{donnee.LOAN_MEMBER_ID_id}}</td>\
                                        <td id="documentId">{{donnee.LOAN_DOCUMENT_ID_id}}</td>\
                                        <td id="startDate">{{donnee.LOAN_START_DATE}}</td>\
                                        <td id="LoanId">{{donnee.LOAN_ID}}</td>\
                                    </tr>\
                                </tbody>\
                            </table>\
                        </div>\
                        <div class="row">\
                            <div class="col">\
                                <nav aria-label="Page navigation">\
                                    <ul class = "pagination justify-content-center">\
                                        <li class="page-item" v-for="(page,index) in res.range">\
                                            <a :id="index" class="page-link" v-on:click="filter(index)">{{page}}</a>\
                                        </li>\
                                    </ul>\
                                </nav>\
                            </div>\
                        </div>\
                    </div> \
                 </div> \
                '
})

