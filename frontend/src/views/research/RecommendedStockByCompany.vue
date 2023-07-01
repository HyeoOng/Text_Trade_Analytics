<template>
  <v-data-table :headers="headers" :items="sortedItems" :items-per-page="All" class="elevation-1">
    <template slot="item.title" slot-scope="{ item }">
      <span class="custom-link" @click="goToReport(item)">
        {{ item.title }}
      </span>
    </template>
    <template slot="item.report_link" slot-scope="{ item }">
    <a :href="item.report_link" target="_blank">
        <v-icon>mdi-file-document-arrow-right-outline</v-icon>
    </a>
    </template>
    <template slot="item.stock_broker" slot-scope="{ item }">
    {{ item.stock_broker.name }}
    </template>
</v-data-table>
</template>

<script>
import axios from 'axios';

export default{
    data(){
        return{
            headers: [
                { text: '종목명', value: 'company', align: 'start', sortable: false},
                { text: '제목', value: 'title' },
                { text: '증권사', value: 'stock_broker' },
                { text: '작성일', value: 'wdate' },
                { text: '리포트', value: 'report_link' },
            ],
            items: []
        };
    },
    created() {
    this.getStockReport();
},
methods: {
    getStockReport() {
    const url = "http://localhost:8000/api/v1/stockreports";
    axios
        .get(url)
        .then((response) => {
        // API 데이터를 받아온 후 정렬하여 items 배열에 할당
        this.items = response.data.sort((a, b) => new Date(b.wdate) - new Date(a.wdate));
        this.report_link = this.items[0].report_link;
        })
        .catch((error) => {
        console.log(error);
        });
    },
    goToReport(item) {
    this.$router.push({
      path: '/ReportContent',
      query: {
        company: item.company,
        stock_broker: item.stock_broker,
        wdate: item.wdate,
        content: item.content,
        title: item.title,
        report_link: item.report_link,
        pdf_sent_score: item.pdf_sent_score,
        pdf_sent_topic: item.pdf_sent_topic,
        pdf_summerize: item.pdf_summerize
      }
    });
  },
},
computed: {
    sortedItems() {
    // items 배열을 반환
    return this.items;
    },
},
};
</script>

<style>
.custom-link {
  color: darkolivegreen;
  text-decoration: none;
  cursor: pointer;
}
</style>