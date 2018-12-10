const ajoutPret = Vue.component('ajoutPret', {
    data : function(){
        return{
            membersearch:"",
            memberListe:[],
            deb:""
            
        }    
    },
    created:function(){
        this.deb = _.debounce(this.fun,1500)
    }, 
    methods:{
        fun(){
            if(this.membersearch.length > 0){
                var url = 'http://localhost:8000/bibliotheque/searchmember?member='+this.membersearch
                var that = this
                this.memberListe=[]
                function fun (){
                    fetch(url)
                    .then(data=>{return data.json()})
                    .then(res=>{that.meberliste = res})
                }
            }
        }
    },
    watch:{
        membersearch:function(){
            this.deb()
        }
    },    
    template : '<div>Ajouter un pret\
                <form>\
        <div class="form-group" id = "ajoutPret">\
        <label>Document</label>\
        <input class="form-control">\
        </div>\
        <div class="form-group">\
        <label>Membre Search</label>\
        <input type = "text" id="member" v-model="membersearch" class="form-control">\
        </div>\
        <div>\
        <label>Date de début</label>\
        <input class="form-control">\
        </div>\
        </form>\
</div>\
        '
})