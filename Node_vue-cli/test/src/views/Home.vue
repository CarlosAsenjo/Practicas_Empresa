<template>
  <div class="home">
    <!-- EJEMPLO HelloWorld
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/> -->

  <!-- Lista de la compra -->
    <div class="listaCompra">
      <AddItems v-bind:items='items'></AddItems>
      <ListaCompra  v-for='item in items' :key='item.id' v-bind:id='item.id' v-bind:texto='item.texto' v-bind:comprado='item.comprado' :class="{comprado:item.comprado}" v-model='item.comprado'/>
    </div>
  </div>
</template>

<!-- Relojes -->

<script>
// @ is an alias to /src
//import HelloWorld from '@/components/HelloWorld.vue'
import ListaCompra from '@/components/ListaCompra.vue'
import AddItems from '@/components/AddItems.vue'

export default {
  name: 'Home',
  components: {
    //HelloWorld,
    ListaCompra,
    AddItems
  },
  data: function(){
    return {
    items:[]
    }
  }
}
</script>
