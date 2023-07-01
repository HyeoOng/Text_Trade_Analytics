<template>
  <v-container>
    <v-card>
      <v-card-title>
        Daily Stock Prices
      </v-card-title>
      <v-card-text>
        <v-line-chart
            :datasets="chartData.datasets"
            :labels="chartData.labels"
        ></v-line-chart>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
export default {
  props: ['stockData'],
  computed: {
    chartData() {
      return {
        labels: this.stockData.map(data => data.date),
        datasets: [
          {
            label: 'Closing Price',
            data: this.stockData.map(data => data.close_price),
            fill: false,
            borderColor: 'blue',
            backgroundColor: 'blue',
            pointBorderColor: 'blue',
            pointBackgroundColor: 'blue',
          },
        ],
      };
    },
  },
};
</script>

<style scoped>
</style>
  