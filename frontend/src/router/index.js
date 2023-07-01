import Vue from 'vue'
import VueRouter from 'vue-router'
import stockChart from '@/views/stockChart.vue'
import HomeView from "@/views/HomeView.vue";
import ResearchPage from '@/views/research/ResearchPage.vue';
import ReportView from '@/views/research/ReportView.vue';
import RecommendedStockByCompany from '@/views/research/RecommendedStockByCompany.vue';
import ReportContent from '@/components/ReportContent.vue';

Vue.use(VueRouter)

const routes = [
{
    path: '/',
    name: 'HomeView',
    component: HomeView,
    meta: { title: 'Trade Text Analytics' } // 제목 설정
},
{
    path: '/stock-chart',
    name: 'stockChart',
    component: stockChart,
    meta: { title: 'Chart' } // 제목 설정
},
{
    path: '/research',
    name: 'ResearchPage',
    component: ResearchPage,
    meta: { title: 'Research' } // 제목 설정
},
{
    path: '/research/ReportView',
    name: 'ReportView',
    component: ReportView,
    meta: { title: '리포트 보기' } // 제목 설정
},
{
    path: '/research/RecommendedStockByCompany',
    name: 'RecommendedStockByCompany',
    component: RecommendedStockByCompany,
    meta: { title: '증권사별 추천 종목' } // 제목 설정
},
{
    path: '/ReportContent',
    name: 'ReportContent',
    component: ReportContent,
    meta: { title: '리포트 내용' } // 제목 설정
},
]

const router = new VueRouter({
mode: 'history',
routes
})

router.beforeEach((to, from, next) => {
document.title = to.meta.title || '기본 제목'; // 라우트별 제목 설정
next();
})

export default router
