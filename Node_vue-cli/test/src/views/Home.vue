<!-- EJEMPLO HelloWorld
<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
<template/> -->


<!-- Lista de la compra -->
<template>    
  <div class="listaCompra">
      <ListaCompra  v-for='item in items' :key='item.id' v-bind:id='item.id' v-bind:texto='item.texto' v-bind:comprado='item.comprado' :class="{comprado:item.comprado}" v-model='item.comprado'/>
  </div>
</template>

<!-- PLANTILLA Relojes -->

<script>
// @ is an alias to /src
//import HelloWorld from '@/components/HelloWorld.vue'
import ListaCompra from '@/components/ListaCompra.vue'

export default {
  name: 'Home',
  components: {
    //HelloWorld,
    ListaCompra,
  }
}
</script>
