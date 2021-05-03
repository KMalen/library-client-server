<template>
  <div class="v-main-wrapper">
     <vAuthorsCreate/>
     <br>
     <vAuthors/>
     <br>
     <v-genres-create/>
     <br>
     <vGenres/>
     <br>
     <v-books-create/>
     <br>
     <vBooks/>
     <br>
     <v-languages-create/>
     <br>
     <vLanguages/>
  </div>
</template>

<script>
import vAuthors from './v-authors'
import vAuthorsCreate from './v-authors-create'
import vGenresCreate from './v-genres-create.vue'
import vBooksCreate from './v-books-create'
import VBooksCreate from './v-books-create.vue'
import vLanguagesCreate from './v-languages-create'
import VLanguagesCreate from './v-languages-create.vue'
import VBooks from './v-books.vue'
import vGenres from './v-genres'
import VLanguages from './v-languages.vue'


export default {
   name: 'v-main-wrapper',
   components: {
      vAuthorsCreate,
      vGenresCreate,
      vBooksCreate,
      VBooksCreate,
      vLanguagesCreate,
      VLanguagesCreate,
      vAuthors,
      VBooks,
      vGenres,
      VLanguages
   },
   props: {},
   computed: {},
   methods: {},
   watch: {},
   mounted(){}
}
</script>

<style>

   .v-main-wrapper {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      max-width: 1200px;
      margin: 0 auto;
   }

</style>