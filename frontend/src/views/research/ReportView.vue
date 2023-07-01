<template>
<v-card>
    <!-- 선택한 추가 메뉴 정보 -->
    <div class="contents">
    <div class="g-selectBox">
        <v-select v-model="selectedSubmenu" :items="submenuOptions" label="" @change="selectSubmenu"
                :append-outer-icon="selectedSubmenu === submenuOptions[0] ? 'mdi-chevron-up' : ''"></v-select>
    </div>
    <v-data-table :headers="headers" :items="polishedData()" :search="searchKeyword" :custom-filter="customSearch"/>
    </div>
</v-card>
</template>

<script>
import axios from 'axios';

export default {
data() {
    const submenuOptions = [
    '전체',
    '신한투자증권',
    '한국투자증권',
    '한화투자증권',
    'KB증권',
    '유안타증권',
    '삼성증권',
    '키움증권',
    '하나증권',
    '나이스디앤비',
    'NICE평가정보',
    '이베스트증권',
    '유진투자증권',
    '미래에셋증권',
    'DS투자증권',
    '한국IR협의회',
    'SK증권',
    '교보증권',
    '대신증권',
    '하이투자증권',
    '대신증권',
    ];
    const searchKeywordBySelectedSubmenu = {
    '전체': '',
    '신한투자증권': '신한투자증권',
    '한국투자증권': '한국투자증권',
    '한화투자증권': '한화투자증권',
    'KB증권': 'KB',
    '유안타증권': '유안타증권',
    '삼성증권': '삼성',
    '키움증권': '키움증권',
    '하나증권': '하나증권',
    '나이스디앤비': '나이스디앤비',
    '이베스트증권':'이베스트증권',
    'NICE평가정보':'NICE평가정보',
    '유진투자증권':'유진투자증권',
    '미래에셋증권':'미래에셋증권',
    'DS투자증권':'DS투자증권',
    '한국IR협의회': '한국IR협의회',
    'SK증권': 'SK증권',
    '교보증권': '교보증권',
    '하이투자증권': '하이투자증권',
    '대신증권':'대신증권',
    };
    return {
    headers: [
        { text: '증권사', value: 'stock_broker' },
        { text: '종목명', value: 'company' },
        { text: '감성지수', value: 'pdf_sent_score' },
        { text: '목표가(₩)', value: 'target_price' },
        { text: '추천일', value: 'wdate' },
        { text: '의견', value: 'target_opinion' },

    ],
    submenuOptions: submenuOptions,
    stockreports: null,
    selectedSubmenu: submenuOptions[0],
    searchKeyword: '',
    searchKeywordBySelectedSubmenu: searchKeywordBySelectedSubmenu,
    loading: false,
    };
},
created() {
    this.getStockReport();
},
methods: {
    selectSubmenu(submenu) {
    console.log(submenu);
    this.selectedSubmenu = submenu;
    this.searchKeyword = this.searchKeywordBySelectedSubmenu[submenu];
    },
    customSearch(value, search, item) {
    return value != null && search != null && item.stock_broker === search;
    },
    polishedData() {
  // stockreports 데이터를 복제하여 정렬
    const sortedData = [...this.stockreports];
    
    // 감성지수를 기준으로 내림차순 정렬
    sortedData.sort((a, b) => b.pdf_sent_score - a.pdf_sent_score);
    
    // stock_broker 값을 변환하여 반환
    return sortedData.map((stockreports) => {
        return {
        ...stockreports,
        stock_broker: stockreports.stock_broker.name,
        target_price: stockreports.target_price === -9999 ? "없음" : stockreports.target_price,
        target_opinion: stockreports.target_opinion === "no_opinion" ? "의견 없음" : stockreports.target_opinion === "Buy" ? "매수" : stockreports.target_opinion,
        };
    });
    },
    toPriceString(price) {
    return price.toLocaleString('ko-KR', { style: 'currency', currency: 'KRW' });
    },
    getStockReport() {
    this.loading = true;
    const url = "http://localhost:8000/api/v1/stockreports";
    axios
        .get(url)
        .then((result) => {
        this.stockreports = result.data;
        this.loading = false;
        })
        .catch((error) => {
        console.log(error);
        this.loading = false;
        });
    },
},
};
</script>

<style scoped>
.g-selectBox {
position: relative;
width: 20%;
margin-left: 15px;
}

.contents {
padding: 40px;
}
</style>
