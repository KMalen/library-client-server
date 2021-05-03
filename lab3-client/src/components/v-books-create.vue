<template>
  <div class="v-books-create">
     <h2>Create new books</h2>
      <br>
     <form class="form row">
        <div class="form-group col">
           <input type="text" class="form-control col-4" placeholder="Title" v-model="form.title">
        </div>
        <div class="form-group col">
           <input type="text" class="form-control col-4" placeholder="Summary" v-model="form.summary">
        </div>
        <button class="btn btn-primary" type="button" :disabled="!canCreate" style="width: 203px" @click="addBook">Create Book</button>
     </form>

      <br>

      <div class="row">
         <div class="form-group col">
           <input type="text" class="form-control col-4" placeholder="ISBN" v-model="form.isbn">
        </div>
      </div>

   <br>

   <div class="row">
      <label class="col">Choose</label>
      <div class="col">
         <select class="custom-select" v-model="form.author">
            <option v-for="author in authors" v-bind:value="author.id" :key="author.id">
               {{author.first_name}}
            </option>
         </select>
      </div>
      <label class="col">Choose</label>
      <div class="form-group col">
         <select v-model="form.language">
            <option v-for="language in languages" v-bind:value="language.id" :key="language.id">
               {{language.name}}
            </option>
         </select>
      </div>
      <div class="form-group col">
         <select v-model="form.genre" multiple>
            <option v-for="genre in genres" v-bind:value="genre.id" :key="genre.id">
               {{genre.name}}
            </option>
         </select>
      </div>
   </div>

   <br>

   <!-- <button class="btn btn-info" type="button" @click="$router.push('/books')">View all books</button> -->

  </div>
</template>

<script>
import axios from 'axios'


export default {
   name: 'v-books-create',
   data() {
      return { 
         form: {
            title: '',
            summary: '',
            isbn: '',
            author: 0,
            language: 0,
            genre: []
         },

         authors: [],
         languages: [],
         genres: []
      }
   },
   components: {},
   props: {},
   computed: {
      canCreate(){
         return this.form.title.trim() && this.form.summary.trim() && ( this.form.isbn.length === 13)
         && this.form.author && this.form.language && (this.form.genre.length >= 1)
      }
   },
   methods: {
      addBook(){
         axios
         .post('http://127.0.0.1:8000/api/books', this.form)
         .then(response => console.log(response))
         .catch(error => console.log(error))

         this.form.title = this.form.summary = this.form.isbn = ''
      }
   },
   watch: {},
   async mounted(){
      axios
         .get('http://localhost:8000/api/authors', {
         })
         .then(response => {
            console.log(response);
            this.authors = response.data
         })
         .catch(error => {
            console.log(error)
         })

      axios
         .get('http://localhost:8000/api/languages', {
         })
         .then(response => {
            console.log(response);
            this.languages = response.data
         })
         .catch(error => {
            console.log(error)
         })

      axios
         .get('http://localhost:8000/api/genres', {
         })
         .then(response => {
            console.log(response);
            this.genres = response.data
         })
         .catch(error => {
            console.log(error)
         })
         
   }
}
</script>

<style>

   .v-books-create {
      display: inline-block;
      justify-content: center;
      align-items: center;
      max-width: 1200px;
      margin: 0 auto;
   }

</style>