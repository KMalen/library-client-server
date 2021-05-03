<template>
  <div class="v-authors-create">
     <h2>Create new authors</h2>
      <br>
     <form class="form row">
        <div class="form-group col">
           <input type="text" class="form-control col-4" placeholder="First Name" v-model="form.first_name">
        </div>
        <div class="form-group col">
           <input type="text" class="form-control col-4" placeholder="Last Name" v-model="form.last_name">
        </div>
        <button class="btn btn-primary" type="button" :disabled="!canCreate" style="width: 203px" v-on:click="addAuthor">Create Author</button>
     </form>

      <br>

      <div class="row">
         <div class="col">
            <label for="">Date of birth</label>
         </div>
         <div class="form-group col">
           <input type="date" class="col" value="2018-07-22" style="width: 100%" v-model="form.date_of_birth">
        </div>
        <div class="col">
            <label for="">Date of death</label>
         </div>
         <div class="form-group col">
           <input type="date" class="col" value="2018-07-22" style="width: 100%" v-model="form.date_of_death">
        </div>
      </div>

   <br>

   <!-- <button class="btn btn-info" type="button" @click="$router.push('/authors')">View all authors</button> -->

  </div>
</template>

<script>
import axios from 'axios'


export default {
   name: 'v-authors-create',
   data() {
      return { 
         form: {
            first_name: '',
            last_name: '',
            date_of_birth: null,
            date_of_death: null,
            id: 0,
         }
      }
   },
   components: {},
   props: {},
   computed: {
      canCreate(){
         return this.form.first_name.trim() && this.form.last_name.trim() 
         && this.form.date_of_birth && this.form.date_of_death
      }
   },
   methods: {
      addAuthor(){
         axios
         .post('http://127.0.0.1:8000/api/authors', this.form)
         .then(response => console.log(response))
         .catch(error => console.log(error))

         this.form.first_name = this.form.last_name = ''
      }
   },
   watch: {},
   mounted(){}
}
</script>

<style>

   .v-authors-create {
      display: inline-block;
      justify-content: center;
      align-items: center;
      max-width: 1200px;
      margin: 0 auto;
   }

</style>