<template>
  <div class="v-genres-create">
     <h2>Create new genres</h2>
      <br>
     <form class="form row">
        <div class="form-group col">
           <input type="text" class="form-control col-4" placeholder="Genre Name" v-model="form.name">
        </div>
        <div class="form-group col">
           <button class="btn btn-primary" type="button" :disabled="!canCreate" style="width: 203px" v-on:click="addAuthor">Create Genre</button>
        </div>
     </form>

      <br>

   <!-- <button class="btn btn-info" type="button" @click="$router.push('/genres')">View all genres</button> -->

  </div>
</template>

<script>
import axios from 'axios'


export default {
   name: 'v-genres-create',
   data() {
      return { 
         form: {
            name: '',
            id: 0,
         }
      }
   },
   components: {},
   props: {},
   computed: {
      canCreate(){
         return this.form.name.trim()
      }
   },
   methods: {
      addAuthor(){
         axios
         .post('http://127.0.0.1:8000/api/genres', this.form)
         .then(response => console.log(response))
         .catch(error => console.log(error))

         this.form.name = ''
      }
   },
   watch: {},
   mounted(){}
}
</script>

<style>

   .v-genres-create {
      display: inline-block;
      justify-content: center;
      align-items: center;
      max-width: 1200px;
      margin: 0 auto;
   }

</style>