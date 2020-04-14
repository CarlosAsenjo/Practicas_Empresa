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
    export default {
        name: 'ListaCompra',
        
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

        methods:{
            add: function(){
              this.items.push({
                  id:this.items.length +1, texto:this.$refs.new_item.value,comprado:false
              });
              this.$refs.new_item.value="";
            }
        }
    }
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