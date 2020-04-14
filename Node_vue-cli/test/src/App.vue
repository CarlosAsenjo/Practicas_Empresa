<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view/>
     <!-- DIV LISTA COMPRA-->  
    <div id="lista">
        <!-- Crea un compoenente lista-vue se le pasan las propiedades id, texto y comprado -->
        <lista-vue-maestra v-bind:items='items'></lista-vue-maestra>
        <input type="text" ref="new_item" />
        <button @click="add">Añadir</button>
    </div>
  </div>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
