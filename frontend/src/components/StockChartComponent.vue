<template>
  <div>
    <h1>주식 차트</h1>
    <StockChart/>
  </div>
</template>

<script>
import StockChart from './components/StockChart.vue';

export default {
  name: 'App',
  components: {
    StockChart
  }
};
</script>

<style>
/* 필요한 스타
