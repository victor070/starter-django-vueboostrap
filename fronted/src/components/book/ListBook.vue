<template>
  <b-container>
    <b-row>
      <b-col class="text-left">
        <div>
          <b-row>
            <b-col>
            <h2>Listado de libros</h2>
            </b-col>
            <b-col>
              <b-button size="lg" variant="primary" class="mb-2" :to="{name:'CreateBook'}">
                <b-icon icon="question-circle-fill" aria-label="Help"></b-icon>
              </b-button>
            </b-col>
          </b-row>

          </div>
        <b-col class="md-12">
          <b-table
            :items="books"
            :fields="fields"
            hover>
            <!-- se le obtine el id de la url   -->
            <template v-slot:cell(action)=data>
              <b-button
                size="sm"
                variant="primary" :to="{name:'EditBook', params: {bookId: data.item.id}}">Editar </b-button>
              <b-button
                size="sm"
                variant="danger" :to="{name:'DeleteBook', params: {bookId: data.item.id}}">Eliminar</b-button>
            </template>
          </b-table>
        </b-col>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
// import axios
import axios from 'axios'

export default {
  data () {
    return {
      fields: [
        {key: 'title', label: 'Titulo'},
        {key: 'descriptions', label: 'Descripcion'},
        {key: 'action', label: 'Acción'}

      ],
      books: []

    }
  },
  // ejecutados el metodo
  created () {
    this.getBooks()
  },
  methods: {
    // Metodo Get
    getBooks () {
      // colocamos el end-point
      const path = 'http://localhost:8000/api/book/'
      // usamos axios para hacer la llamada al servidor
      axios.get(path).then((response) => {
        this.books = response.data
      }).catch((error) => {
        console.log('hubo un error', error)
      })
    }
  }
}
</script>

<style lang="css" scoped>

</style>>
