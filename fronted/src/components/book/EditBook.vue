<template>
  <div>
    <b-container>
      <b-row>
        <b-col class="text-left">
          <h2>Editar libro</h2>
        </b-col>
      </b-row>

      <b-row>
        <b-col>
          <b-card>
            <b-card-body>
              <b-form @submit="onSubmit">

                <b-form-group>
                <b-row>
                  <b-col cols="2">
                    <label for="title"> Título </label>
                  </b-col>
                  <b-col cols="10">
                   <input type="text" placeholder="Título" name="titulo" class="form-control"
                   v-model.trim="form.title">
                  </b-col>
                </b-row>
                </b-form-group>

                <b-form-group>
                <b-row>
                  <b-col cols="2">
                    <label for="descripcion"> Descripción </label>
                  </b-col>
                  <b-col cols="10">
                    <b-form-textarea  name="descriptions" placeholder="Descripción del libro" rows="3" v-model.trim="form.descriptions">
                    </b-form-textarea>
                  </b-col>
                </b-row>
                </b-form-group>

                <b-row>
                  <b-col class="text-left">
                    <b-button type="submit" variant="primary"> Editar </b-button>
                    <b-button variant="danger" :to="{name:'ListBook'}"> Cancelar </b-button>
                  </b-col>
                </b-row>
              </b-form>
            </b-card-body>
          </b-card>
        </b-col>
      </b-row>

    </b-container>
  </div>
</template>

<script>
// import axios
import axios from 'axios'
// import sweetalert
import swal from 'sweetalert'

export default {
  data () {
    return {
      bookId: this.$route.params.bookId,
      form: {
        title: '',
        descriptions: ''
      }
    }
  },
  methods: {
    onSubmit (event) {
      event.preventDefault()

      const path = `http://localhost:8000/api/book/${this.bookId}/`

      // Metodo Put
      axios.put(path, this.form).then((response) => {
        this.form.title = response.data.title
        this.form.descriptions = response.data.descriptions

        swal('Libro Actualizado exitosamente', '', 'success')
      }).catch((error) => {
        console.log('Este es el error', error)
      })
    },

    getBook () {
      const path = `http://localhost:8000/api/book/${this.bookId}/`
      // metodo Get
      axios.get(path).then((response) => {
        this.form.title = response.data.title
        this.form.descriptions = response.data.descriptions
      }).catch((error) => {
        console.log('Este es el error', error)
      })
    }
  },

  created () {
    this.getBook()
  }

}
</script>

<style scoped>

</style>
