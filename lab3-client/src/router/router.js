import VueRouter from "vue-router";

import vMainWrapper from '../components/v-main-wrapper'
import vAuthors from '../components/v-authors'
import vGenres from '../components/v-genres'
import vBooks from '../components/v-books'
import vLanguages from '../components/v-languages'

export default new VueRouter({
   mode: 'history',
   routes: [
      {
         path: '/',
         component: vMainWrapper
      },
      {
         path: '/authors',
         component: vAuthors
      },
      {
         path: '/genres',
         component: vGenres
      },
      {
         path: '/books',
         component: vBooks
      },
      {
         path: '/languages',
         component: vLanguages
      }
   ]
})