<template>
  <v-card ref="kospi" class="pa-2" height="260">
    <v-card-subtitle class="pt-0 pb-0">
      <v-row align="center">
        <v-col>
          <h4 class="">KOSDAQ</h4>
        </v-col>
        <v-col class="text-right">
          <v-btn-toggle
              v-model="center"
              color="deep-purple accent-3"
              group
              tile
          >
            <v-btn @click="switchTo1Month()">1 month</v-btn>
            <v-btn @click="switchTo6Months()">6 month</v-btn>
          </v-btn-toggle>
        </v-col>
      </v-row>
    </v-card-subtitle>
    <v-card-title class="pa-1 ma-0">
      <v-row align="center" class="pl-4" justify="start">
        <v-col cols="auto">
          <h4><strong>{{ getPrprValue() }}</strong></h4>
        </v-col>
        <v-col cols="auto">
          <div class="icon-with-number">
            <div id="plma" :class="flucIconClass"></div>
            <h6 :style="getStyleObject">{{ getFLUC() }}%</h6>
          </div>
        </v-col>
      </v-row>

      <v-spacer></v-spacer>
    </v-card-title>

    <v-sheet color="transparent" height="200" width="100%">
      <component :is="lineChartComponent" :color="lineChartColor" height="150" width="100%"></component>
    </v-sheet>
  </v-card>
</template>

<script>
// import { Line } from 'vue-chartjs';
import Data from '@/data_json/kosdaq_data_1month.json';
import Data_6 from '@/data_json/kosdaq_data_6month.json';
import LineChart from '@/components/chart/kosdaq_chart.vue'
import LineChart_6 from '@/components/chart/kosdaq_chart_6.vue'

export default {
  // extends: Line,
  data() {
    return {
      data: Data,
      lineChartComponent: LineChart,
      currentDate: this.getCurrentDate(),
      lineChartColor: 'red', // 초기 값을 할당
      lineChartColor_Alpha: 'rgba(255, 0, 0, 0.1)', // 초기 값을 할당
    };
  },
  components: {
    LineChart: LineChart,
    LineChart_6: LineChart_6
  },
  computed: {
    flucIconClass() {
      const targetData = this.data.find((d) => d.Date === this.currentDate);
      if (targetData) {
        return targetData.FLUC < 0 ? 'inverse-triangle-icon' : 'triangle-icon';
      }
      return '';
    },
    getStyleObject() {
      const targetData = this.data.find((d) => d.Date === this.currentDate);
      if (targetData) {
        return {
          fontSize: '12px',
          color: targetData.FLUC < 0 ? '#4e02f2' : '#f20202',
        };
      }
      return {};
    },
  },
  methods: {
    getCurrentDate() {
      const date = new Date();
      const year = date.getFullYear();
      let month = date.getMonth() + 1;
      let day = date.getDate();

      // 월과 일이 한 자리 숫자인 경우 앞에 0을 붙여 두 자리로 만듦
      month = month < 10 ? `0${month}` : month;
      day = day < 10 ? `0${day}` : day;

      return `${year}${month}${day}`;
    },
    getPrprValue() {
      const targetData = this.data.find((d) => d.Date === this.currentDate);
      console.log(targetData)
      return targetData ? targetData.CLSPRC : '';
    },
    getFLUC() {
      const targetData = this.data.find((d) => d.Date === this.currentDate);
      console.log(targetData)
      return targetData ? targetData.FLUC : '';
    },
    switchTo1Month() {
      this.data = Data;
      this.lineChartComponent = LineChart;
    },
    switchTo6Months() {
      this.data = Data_6;
      this.lineChartComponent = LineChart_6;
    },
  },
};
</script>

<style>
.icon-with-number {
  display: flex;
  align-items: center;
  justify-content: center;
}

/* 삼각형 아이콘 */
.triangle-icon {
  width: 0;
  height: 0;
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-bottom: 10px solid #f20202;
}

/* 역삼각형 아이콘 */
.inverse-triangle-icon {
  width: 0;
  height: 0;
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-top: 10px solid #4e02f2;
}

</style>
