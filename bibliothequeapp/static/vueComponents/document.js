const templateDocument = Vue.component('templateDocument', { 
    data: function(){
            return {
                text : "Hello"
            }
        },
    methods: {
        myMethod(){
            alert('method triggered'),
            this.text = "text changed"
        }
    },
    template : '<div> {{text}} \
                <input type = "button" v-on:click="myMethod">\
                </div>'
})