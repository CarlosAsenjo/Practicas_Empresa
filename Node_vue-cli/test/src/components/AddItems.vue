<!-- DIV LISTA COMPRA-->  
<template>
    <div class="listaCompra">
      <h2>Lista de la compra</h2>
        <input type="text" ref="new_item" />
        <button @click="add">Añadir</button>
    </div>
</template>


<script>
export default {
 name:'AddItems',
    props:{
        items:[]
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

