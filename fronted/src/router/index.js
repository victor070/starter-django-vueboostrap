import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import ListBook from '@/components/book/ListBook.vue'
import EditBook from '@/components/book/EditBook.vue'
import DeleteBook from '@/components/book/DeleteBook.vue'
import CreateBook from '@/components/book/CreateBook.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/books',
      name: 'ListBook',
      component: ListBook
    },
    {
      path: '/books/:bookId/edit',
      name: 'EditBook',
      component: EditBook
    },
    {
      path: '/books/:bookId/delete',
      name: 'DeleteBook',
      component: DeleteBook
    },
    {
      path: '/books/create',
      name: 'CreateBook',
      component: CreateBook
    }
  ],
  mode: 'history'
})
