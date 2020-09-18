<template>
  <b-container>
      <b-row>
          <b-col>
            <h2>¿Esta seguro que desea eliminar este libro?</h2>
            <p>Título: {{ this.element.title }}</p>
            <p>Descripción: {{ this.element.descriptions }}</p>
          </b-col>
      </b-row>

      <b-row>
        <b-col class="text-center">
          <b-button variant="danger" v-on:click="deleteBook"> Eliminar </b-button>
          <b-button variant="primary" :to="{name:'ListBook'}"> Cancelar </b-button>
        </b-col>
      </b-row>
  </b-container>
</template>

<script>
// import axios
import axios from 'axios'
// import sweetalert
import swal from 'sweetalert'

export default {
  name: 'DeleteBook',
  data () {
    return {
      bookId: this.$route.params.bookId,
      element: {
        title: '',
        descriptions: ''
      }
    }
  },
  methods: {
    getBook () {
      const path = `http://localhost:8000/api/book/${this.bookId}/`
      // metodo Get
      axios.get(path).then((response) => {
        this.element.title = response.data.title
        this.element.descriptions = response.data.descriptions
      }).catch((error) => {
        console.log('Este es el error', error)
      })
    },
    // Método Delete (si estas usando mixin que no se te olvide importar el mixin en llos viewsets)
    deleteBook () {
      const path = `http://localhost:8000/api/book/${this.bookId}/`
      axios.delete(path).then((response) => {
        /* location.href = '/books' */
        this.$router.push('/books') // sirve para no recargar una pagina al tener una redirección
      }).catch((error) => {
        swal('No es posible eliminar este elemento', '', 'error')
        console.log('Este es el error', error.response)
      })
    }
  },
  created () {
    this.getBook()
  }

}
</script>

<style scope>

</style>
