<!-- Plantilla lista compra -->
<template id='template-lista'>
    <div class="lista-vue">
        <input type='checkbox' v-bind:checked='checked' v-on:change="$emit('change','$event.target.checked')" >
         <span>
            {{id}} - {{texto}}
        </span>
    </div>
</template>

<script>
import ListaMaestraCompra from '@/components/ListaMaestraCompra.vue'
    
    export default {
        name: 'ListaCompra',
        props: {

        }
    }
</script>

<script>
    Vue.component('lista-vue', {

        template: '#template-lista',

        props: {
            id: {
                type: Number,
                default: 0
            },
            texto: {
                type: String,
                default: 'empty'
            },
            comprado: {
                type: Boolean,
                default: false
            },
            checked: Boolean
        },
        model: {
            prop: 'checked',
            event: 'change'
        },

        /*  methods: {
             update: function(item_comprado) { //hay que pasarle el id
                 item_comprado = !item_comprado
                     console.log("---------------------->  entra en update")
                      var check = document.getElementsByTagName("span")[id];
                      console.log("---------------------->  " + typeof check + "...." + check)
                      check.style.textDecoration = "line-through";
             }
         }*/
    });

    var app = new Vue({
        el: '#app',
        data: {
            items: [{
                id: 0,
                texto: 'Leche',
                comprado: false
            }],

        },
        computed: {},
        methods: {
            add: function() {
                this.items.push({
                    id: this.items.length,
                    texto: this.$refs.new_item.value,
                    comprado: false
                });
                this.$refs.new_item.value = "";
            }
        }
    });
</script>

<!-- ESTILOS -->
<style>
    template {
    /** Evitamos que se vean elementos 'templates' **/
        display: none;
    }
        
    .comprado {
        text-decoration: line-through;
    }
    </style>