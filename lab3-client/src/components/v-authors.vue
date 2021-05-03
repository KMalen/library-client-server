<template>
  <div class="v-authors">
     <p>Work with authors</p>

   <div class="container">
     <button class="btn btn-dark" type="button" @click="$router.push('/')">Back</button>
   </div>
     <br>

      <ul v-if="authors.length" class="list-group" style="width: 500px">
         <li class="list-group-item" v-for="author in authors" :key="author.first_name">
            First Name - {{author.first_name}}
            <br>
            Last Name - {{author.last_name}}
            <br>
            Date of birth - {{author.date_of_birth}}
            <br>
            Date of death - {{author.date_of_death}}
            <br>
            <button class="btn btn-danger" @click="removeContact(author.id)" >Delete</button>
            <br>
            <button class="btn btn-primary" @click="showModal(author.first_name, author.last_name,
                                                author.date_of_birth, author.date_of_death, author.id)">Edit</button>
         </li> 
      </ul>

      <p v-else>No Authors</p>

      <div v-if="modal">
         <transition name="modal">
            <div class="modal-mask">
               <div class="modal-wrapper">
                  <div class="modal-dialog">
                     <div class="modal-content">
                        <div class="modal-header">
                           <h4 class="modal-title">Edit Author</h4>
                           <button type="button" @click="modal=false" class="btn-danger">
                              <span aria-hidden="true">&times;</span>
                           </button>
                        </div>
                        <div class="modal-body">
                           <div class="form-group">
                              <label>First Name</label>
                              <input type="text" class="form-control" v-model="dataForUpdate.first_name">
                           </div>
                           <div class="form-group">
                              <label>Last Name</label>
                              <input type="text" class="form-control" v-model="dataForUpdate.last_name">
                           </div>
                           <div class="form-group">
                              <label>Date of birth</label>
                              <input type="date" class="col" style="width: 100%" v-model="dataForUpdate.date_of_birth">
                           </div>
                           <div class="form-group">
                              <label>Date of death</label>
                              <input type="date" class="col" style="width: 100%" v-model="dataForUpdate.date_of_death">
                           </div>
                           <br>
                           <div align="center">
                              <input type="button" class="btn btn-success btn-xs" @click="updateData" value="Update Author">
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
   name: 'v-authors',
   data() {
      return { 
         authors: [],
         modal: false,
         dataForUpdate: {
            first_name: '',
            last_name: '',
            date_of_birth: null,
            date_of_death: null,
            id: 0
         }
      }
   },
   components: {},
   props: {},
   computed: {},
   methods: {
      removeContact(id){
         console.log(id)

         axios
         .delete('http://127.0.0.1:8000/api/author/' + id)
         .then(response => {
            console.log(response)
         })
      },

      showModal(first_name, last_name, date_of_birth, date_of_death, id){

         this.modal = true

         this.dataForUpdate.first_name = first_name
         this.dataForUpdate.last_name = last_name
         this.dataForUpdate.date_of_birth = date_of_birth
         this.dataForUpdate.date_of_death = date_of_death
         this.dataForUpdate.id = id
      },

      async updateData(){

         axios
         .put('http://127.0.0.1:8000/api/author/' + this.dataForUpdate.id, this.dataForUpdate)
         .then(response => {
            console.log(response)

            axios
            .get('http://localhost:8000/api/authors', {
            })
            .then(response => {
               console.log(response)
               this.authors = response.data
               this.authors.sort(function(a, b){
                  return b.id - a.id
               })
            })
            .catch(error => console.log(error))
         })
         .catch(error => console.log(error))

         this.modal = false

      }
   },
   watch: {},
   async mounted(){
      setInterval( () => (
      axios
         .get('http://localhost:8000/api/authors', {
         })
         .then(response => {
            console.log(response);
            this.authors = response.data
            this.authors.sort(function(a, b){
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