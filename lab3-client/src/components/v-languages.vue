<template>
  <div class="v-languages">
     <p>Work with languages</p>

   <div class="container">
     <button class="btn btn-dark" type="button" @click="$router.push('/')">Back</button>
   </div>
     <br>

      <ul v-if="languages.length" class="list-group" style="width: 500px">
         <li class="list-group-item" v-for="language in languages" :key="language.name">
            Language Name - {{language.name}}
            <button class="btn btn-danger" @click="removeLanguage(language.id)">Delete</button>
            <button class="btn btn-primary" @click="showModal(language.name, language.id)">Edit</button>
         </li> 
      </ul>

      <p v-else>No Languages</p>

      <div v-if="modal">
         <transition name="modal">
            <div class="modal-mask">
               <div class="modal-wrapper">
                  <div class="modal-dialog">
                     <div class="modal-content">
                        <div class="modal-header">
                           <h4 class="modal-title">Edit Language</h4>
                           <button type="button" @click="modal=false" class="btn-danger">
                              <span aria-hidden="true">&times;</span>
                           </button>
                        </div>
                        <div class="modal-body">
                           <div class="form-group">
                              <label>Name</label>
                              <input type="text" class="form-control" v-model="name.name">
                           </div>
                           <br>
                           <div align="center">
                              <input type="button" class="btn btn-success btn-xs" @click="updateData" value="Update Genre">
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
   name: 'v-genres',
   data() {
      return { 
         languages: [],
         modal: false,
         name: {
            name: ''
         },
         idToUpdate : 0
      }
   },
   components: {},
   props: {},
   computed: {},
   methods: {
      async removeLanguage(id) {
         console.log(id)

         axios
         .delete('http://127.0.0.1:8000/api/language/' + id)
         .then(response => {
            console.log(response)
         })
      },

      showModal(name, id) {
         this.modal = true

         console.log(name)

         this.name.name = name
         this.idToUpdate = id
      },

      async updateData(){
         
         axios
         .put('http://127.0.0.1:8000/api/language/' + this.idToUpdate, this.name)
         .then(response => {

            console.log(response)

            axios
            .get('http://localhost:8000/api/languages', {
            })
            .then(response => {
               console.log(response)

               this.languages = response.data
               this.languages.sort(function(a, b){
                  return b.id - a.id
            })
            
            })
            .catch(error => console.log(error))
         })
         .catch(error => console.log(error))

         this.modal = false

         this.name.name = ''
         this.idToUpdate = 0
      }
   },
   watch: {},
   async mounted(){
      setInterval(() => (
      axios
         .get('http://localhost:8000/api/languages', {
         })
         .then(response => {
            this.languages = response.data
            this.languages.sort(function(a, b){
               return b.id - a.id
            })
         })
      ),1000)
   }
}
</script>

<style>

   .v-languages {
      display: inline-block;
      justify-content: center;
      align-items: center;
      max-width: 1200px;
      margin: 0 auto;
   }

   li {
      display: flex !important ;
      justify-content: space-evenly !important ;
      align-items: center !important ;
   }

   .modal-mask {
      position: fixed;
      z-index: 9998;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: rgba(0, 0, 0, 0.5);
      display: table;
      transition: opacity .3s ease;
   }

   .modal-wrapper {
      display: table-cell;
      vertical-align: middle;
   }

</style>