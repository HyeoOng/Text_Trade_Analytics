<template>
    <v-card>
        <!-- 메뉴 -->
        <v-row no-gutters>
            <v-col v-for="(menu, index) in menus" :key="index" cols="6">
                <v-card @click="selectMenu(index)">
                    <v-card-text>{{ menu.name }}</v-card-text>
                </v-card>
            </v-col>
        </v-row>

        <!-- 선택한 메뉴 정보 -->
        <v-card v-if="selectedMenu">
            <v-card-title>{{ selectedMenu.name }}</v-card-title>
            <v-card-text>{{ selectedMenu.description }}</v-card-text>
        </v-card>

        <!-- 메뉴 1에 대한 추가 선택 메뉴 -->
        <v-card v-if="selectedMenu && selectedMenu.name === '증권사별 추천종목'">
            <ReportView />
        </v-card>
        <v-card v-if="selectedMenu && selectedMenu.name === '종목분석 리포트'">
            <RecommendedStockByCompany />
        </v-card>
    </v-card>
</template>
<script>
import RecommendedStockByCompany from './RecommendedStockByCompany.vue';
import ReportView from './ReportView.vue';

export default {
    data() {
        return {
            menus: [
                { name: "증권사별 추천종목", description: "" },
                { name: "종목분석 리포트", description: "" },
            ],
            selectedMenu: null,
            selectedTab:''
        };
    },
    methods: {
        selectMenu(index) {
            this.selectedMenu = this.menus[index];
        },
    },
    components: { RecommendedStockByCompany, ReportView }
};
</script>
<style scoped>
</style>
