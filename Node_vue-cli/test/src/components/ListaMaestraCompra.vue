<template id="template-lista-maestra">
      <div class="lista-maestra">
        <lista-vue  v-for='item in items' :key='item.id' v-bind:id='item.id' v-bind:texto='item.texto' v-bind:comprado='item.comprado' :class="{comprado:item.comprado}" v-model='item.comprado'></lista-vue>
      </div>
</template>

<script>
import ListaCompra from '@/components/ListaCompra.vue'

    export default {
        name: 'ListaMaestraCompra',
        props: {

        }
    }
</script>

<script>
    'use strict' // Aplica normas mas estrictas en el codigo

    Vue.component('lista-vue-maestra', {

        template: '#template-lista-maestra',

        props: {
            items: []
        },
    });

<script/>