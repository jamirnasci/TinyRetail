import {createRouter, createWebHistory} from 'vue-router'
import Index from '../pages/index.vue'
import LoginPage from '../pages/LoginPage.vue'
import SalesPage from '../pages/sales/SalesPage.vue'
import CreateUserPage from '../pages/CreateUserPage.vue'
import ProductsPage from '../pages/products/ProductsPage.vue'
import SupplierPage from '../pages/supplier/SupplierPage.vue'
import PointSalePage from '../pages/sales/PointSalePage.vue'
import SaleDetailPage from '../pages/sales/SaleDetailPage.vue'

const routes = createRouter({
    history: createWebHistory(),
    routes:[
        {
            name: 'index',
            path: '/',
            component: Index
        },
        {
            name: 'login',
            path: '/login',
            component: LoginPage
        },
        {
            name: 'sales',
            path: '/sales',
            component: SalesPage
        },
        {
            name: 'saleDetails',
            path: '/sales/details/:id',
            component: SaleDetailPage
        },
        {
            name:'pointOfSale',
            path: '/point-of-sale',
            component: PointSalePage
        },
        {
            name: 'user',
            path:'/user',
            component: CreateUserPage
        },
        {
            name: 'products',
            path:'/products',
            component: ProductsPage
        },
        {
            name: 'supplier',
            path: '/supplier',
            component: SupplierPage
        }
    ]
})

const authRoute = [
    '/sales',
    '/products',
    '/profile'
]

routes.beforeEach((to, from)=>{
    const token: string | null = localStorage.getItem('token')
    if(!token){
        return false
    }
})

export default routes