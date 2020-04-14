<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    
    <ListaCompra/>
    <ListaMaestraCompra/>
  </div>
</template>

<!-- PLANTILLA Relojes -->

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import ListaCompra from '@/components/ListaCompra.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld,
    ListaCompra,
    ListaMaestraCompra
  }
}
</script>
