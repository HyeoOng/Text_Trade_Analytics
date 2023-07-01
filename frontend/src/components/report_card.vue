<template>
  <v-card class="pa-3 ma-2 mr-0 ml-0">
    <v-row align="center" justify="space-between">
      <v-col align-self="center" cols="auto pa-3">
        <h3>최신 리포트 보기</h3>
      </v-col>
      <v-col cols="auto">
        <v-btn @click="goToHomeView">전체내용자세히보기</v-btn>
      </v-col>
    </v-row>
    <v-row class="pa-0 mt-0 mb-0" justify="center">
      <v-col cols="12">
        <v-chip-group
          v-model="selectedTags"
          active-class="primary--text"
          class="text-center"
          column
          multiple
          outlined
        >
          <v-chip v-for="tag in tags" :key="tag.name" :value="tag.filterValue" filter>
            {{ tag.name }}
          </v-chip>
        </v-chip-group>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-expansion-panels class="pa-3 pt-0">
          <v-expansion-panel v-for="(item, i) in filteredStockReports" :key="i">
            <v-expansion-panel-header @click="getStockReportContent(item.title)">
              {{ item.title }}
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <p class="smaller-text">
                증권사 {{ getItemValueWithoutName(item.stock_broker) }} | 종목 {{ item.company }} | 발행일 {{ item.wdate }}
              </p>
              <p>{{ item.pdf_sent_topic }}</p>
              <v-btn text @click="goToLink(item.report_link)">
                <v-icon left>mdi-format-align-justify</v-icon>
                Report보기
              </v-btn>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      tags: [
        { name: '신한투자증권', filterValue: '신한투자증권' },
        { name: '한국투자증권', filterValue: '한국투자증권' },
        { name: '한화투자증권', filterValue: '한화투자증권' },
        { name: 'KB증권', filterValue: 'KB증권' },
        { name: '유안타증권', filterValue: '유안타증권' },
        { name: '삼성증권', filterValue: '삼성증권' },
        { name: '키움증권', filterValue: '키움증권' },
        { name: '하나증권', filterValue: '하나증권' },
        { name: '나이스디앤비', filterValue: '나이스디앤비' },
        { name: 'NICE평가정보', filterValue: 'NICE평가정보' },
        { name: '이베스트증권', filterValue: '이베스트증권' },
        { name: '유진투자증권', filterValue: '유진투자증권' },
        { name: '미래에셋증권', filterValue: '미래에셋증권' },
        { name: 'DS투자증권', filterValue: 'DS투자증권' },
        { name: '한국IR협의회', filterValue: '한국IR협의회' },
        { name: 'SK증권', filterValue: 'SK증권' },
        { name: '교보증권', filterValue: '교보증권' },
        { name: '대신증권', filterValue: '대신증권' },
        { name: '하이투자증권', filterValue: '하이투자증권' },
      ],
      stockreports: [],
      selectedTags: [],
    };
  },
  methods: {
    goToHomeView() {
      this.$router.push({
        path: '/research/RecommendedStockbyCompany',
        query: { selectedTab: '종목분석 리포트' },
      });
    },
    getItemValueWithoutName(value) {
      if (typeof value === 'object' && value !== null && 'name' in value) {
        return value.name;
      }
      return value;
    },
    goToLink(link) {
      window.open(link);
    },
    getStockReport() {
      const url = 'http://localhost:8000/api/v1/stockreports';
      axios
        .get(url)
        .then((response) => {
          this.stockreports = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  computed: {
  filteredStockReports() {
    let filteredReports = [...this.stockreports];

    // 태그 선택 여부에 따라 필터링
    if (this.selectedTags.length > 0) {
      filteredReports = filteredReports.filter((item) =>
        this.selectedTags.includes(item.stock_broker.name)
      );
    }

    // 최신 리포트 순으로 정렬
    filteredReports.sort((a, b) => new Date(b.wdate) - new Date(a.wdate));

    // 최신 리포트 5개 반환
    return filteredReports.slice(0, 5);
  },
},
  created() {
    this.getStockReport()
  }
};
</script>

<style>
.text-center {
  display: flex;
  justify-content: center;
}
.my-chip-group {
  flex-wrap: wrap;
  justify-content: center;
}
.smaller-text {
  font-size: 12px;
}
</style>
