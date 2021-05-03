<template>
  <div class="v-authors">
     <p>Work with Books</p>

   <div class="container">
     <button class="btn btn-dark" type="button" @click="$router.push('/')">Back</button>
   </div>
     <br>

      <ul v-if="books.length" class="list-group" style="width: 500px">
         <li class="list-group-item" v-for="book in books" :key="book.id">
            Title - {{book.title}}
            <br>
            Summary - {{book.summary}}
            <br>
            ISBN - {{book.isbn}}
            <br>
            Author ID - {{book.author}}
            <br>
            Language ID - {{book.language}}
            <br>
            Genres ID's - {{book.genre}}
            <br>
            <button class="btn btn-danger" @click="removeBook(book.id)">Delete</button>
            <br>
            <button class="btn btn-primary" @click="showModal(book.title, book.summary,
                                                book.isbn, book.author, book.language, book.genre, book.id)">Edit</button>
         </li> 
      </ul>

      <p v-else>No Books</p>

      <div v-if="modal">
         <transition name="modal">
            <div class="modal-mask">
               <div class="modal-wrapper">
                  <div class="modal-dialog">
                     <div class="modal-content">
                        <div class="modal-header">
                           <h4 class="modal-title">Edit Book</h4>
                           <button type="button" @click="modal=false" class="btn-danger">
                              <span aria-hidden="true">&times;</span>
                           </button>
                        </div>
                        <div class="modal-body">
                           <div class="form-group">
                              <label>Title</label>
                              <input type="text" class="form-control" v-model="dataForUpdate.title">
                           </div>
                           <div class="form-group">
                              <label>Summary</label>
                              <input type="text" class="form-control" v-model="dataForUpdate.summary">
                           </div>
                           <div class="form-group">
                              <label>ISBN</label>
                              <input type="text" class="col" style="width: 100%" v-model="dataForUpdate.isbn">
                           </div>
                           <div class="form-group">
                              <label>Author</label>
                                 <select class="custom-select" v-model="dataForUpdate.author">
                                    <option v-for="author in authors" v-bind:value="author.id" :key="author.id">
                                       {{author.first_name}}
                                    </option>
                                 </select>
                           </div>
                           <div class="form-group col">
                              <label>Language</label>
                                 <select v-model="dataForUpdate.language">
                                    <option v-for="language in languages" v-bind:value="language.id" :key="language.id">
                                       {{language.name}}
                                    </option>
                                 </select>
                           </div>
                           <div class="form-group col">
                              <label>Language</label>
                                 <select v-model="dataForUpdate.genre" multiple>
                                    <option v-for="genre in genres" v-bind:value="genre.id" :key="genre.id">
                                       {{genre.name}}
                                    </option>
                                 </select>
                           </div>
                           <br>
                           <div align="center">
                              <input type="button" class="btn btn-success btn-xs" @click="updateData" value="Update Book">
                           </div>
                        </div>
                     </div>
                  </div>
               </div>
            </div>
         </transition>
      </div>

  </div>
</template>

<script>
import axios from 'axios'

export default {
   name: 'v-books',
   data() {
      return { 
         books: [],
         modal: false,
         dataForUpdate: {
            title: '',
            summary: '',
            isbn: '',
            author: 0,
            language: 0,
            genre: [],
            id: 0
         },

         authors: [],
         languages: [],
         genres: []
      }
   },
   components: {},
   props: {},
   computed: {},
   methods: {
      removeBook(id){
         console.log(id)

         axios
         .delete('http://127.0.0.1:8000/api/book/' + id)
         .then(response => {
            console.log(response)
         })

      },

      showModal(title, summary, isbn, author, language, genre, id){

         this.modal = true

         this.dataForUpdate.title = title
         this.dataForUpdate.summary = summary
         this.dataForUpdate.isbn = isbn
         this.dataForUpdate.author = author
         this.dataForUpdate.language = language
         this.dataForUpdate.genre = genre
         this.dataForUpdate.id = id

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
      },

      async updateData(){

         axios
         .put('http://127.0.0.1:8000/api/book/' + this.dataForUpdate.id, this.dataForUpdate)
         .then(response => {
            console.log(response)

            axios
            .get('http://localhost:8000/api/books', {
            })
            .then(response => {
               console.log(response)
               this.books = response.data
            })
            .catch(error => console.log(error))
         })
         .catch(error => console.log(error))

         this.modal = false

      }
   },
   watch: {},
   async mounted(){
      setInterval(() => (
      axios
         .get('http://localhost:8000/api/books', {
         })
         .then(response => {
            console.log(response);
            this.books = response.data
            this.books.sort(function(a, b){
               return b.id - a.id
            })
         })
      ), 1000)
   }
}
</script>

<style>

   .v-authors {
      display: inline-block;
      justify-content: center;
      align-items: center;
      max-width: 1200px;
      margin: 0 auto;
   }

</style>