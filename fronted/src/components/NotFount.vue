<template>
  <b-container>
      <b-row>
          <b-col class="text-left mt-5" cols="12" align-h="center">
              <h2> 404 not found </h2>
          </b-col>
      </b-row>
      <br>
      <b-row>
          <b-col class="text-left">
              <img src="@/assets/Astronaut.gif" alt="astronauta" height="350px">
          </b-col>
          <b-col  class="text-left">
              <b-row cols="1" cols-sm="1" cols-md="1" cols-lg="1">
                  <b-col class="mt-5">
                      <b-card>
                          <b-card-title>
                            <h2 id="Titulo"> Malas noticias <br> para ti</h2>
                          </b-card-title>
                          <b-card-body>
                            <p>La pagina esta bloqueada para ti <br> o no esta disponible en estos momentos</p>
                            <b-row>
                                <b-col class="text-left">
                                    <b-button variant="dark" :to="{name:'HelloWorld'}"> Regresar </b-button>
                                </b-col>
                            </b-row>
                          </b-card-body>
                      </b-card>
                  </b-col>
              </b-row>
          </b-col>
      </b-row>
  </b-container>
</template>

<script>
export default {
  name: 'NotFount'
}
</script>
<style scope>
#Titulo{
    font-weight: 700;
    font-size: 4rem;
    }
</style>
