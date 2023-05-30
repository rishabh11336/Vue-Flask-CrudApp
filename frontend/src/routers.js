import { createRouter, createWebHistory } from "vue-router"
import HoMe from './components/HoMe'
import CreAte from './components/CreAte'
import ArticleDetails from './components/ArticleDetails'
import ArticleEdit from './components/ArticleEdit'

const routes = [
    {
        path:'/',
        name:'home',
        component:HoMe
    },
    {
        path:'/create',
        name:'create',
        component:CreAte
    },
    {
        path:'/details/:id',
        name:'details',
        component:ArticleDetails,
        props:true
    },
    {
        path:'/edit/:id',
        name:'articleedit',
        component:ArticleEdit,
        props:true
    }
]

const router = createRouter({
    history : createWebHistory(),
    routes,
})

export default router;