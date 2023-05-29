import { createRouter, createWebHistory } from "vue-router"
import HoMe from './components/HoMe'
import CreAte from './components/CreAte'

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
    }
]

const router = createRouter({
    history : createWebHistory(),
    routes,
})

export default router;