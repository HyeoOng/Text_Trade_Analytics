<template>
  <v-container fluid>
    <v-row>
      <v-col cols="12">
        <v-card elevation="10">
          <v-card-title>
            <v-text-field
              v-model="searchQuery"
              label="종목 이름"
              color="black"
              @keydown.enter="performSearch"
            ></v-text-field>
            <v-spacer></v-spacer>
            <v-select
              v-model="selectedInterval"
              :items="intervals"
              label="기간"
              style="width: 10%"
              color="black"
            ></v-select>
            <v-btn color="gray" @click="performSearch">검색</v-btn>
          </v-card-title>
        </v-card>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="7">
        <v-card elevation="10">
          <div style="width: 100%; height: 500px;">
            <canvas ref="stockChartCanvas"></canvas>
          </div>
          <v-overlay :value="showOverlay" opacity="0.5" color="black" style="position: absolute; display: flex; align-items: center; justify-content: center;">
            <div class="text-h4 font-weight-thin" style="font-size: 40px; color: white;">
              종목 이름이나 코드를 입력해주세요
            </div>
          </v-overlay>
        </v-card>
      </v-col>
      <v-col cols="5">
        <v-card class="mb-4" elevation="10">
          <v-card-text class="text-left" style="background-color: #FFFFFF; height: 110px;">
            <div class="text-h4 font-weight-thin" style="font-size: 15px !important;">
              현재가
              <v-divider></v-divider>
              <span style="font-size: 25px; font-weight: bold;">{{ currentPrice }}</span>
            </div>
          </v-card-text>
        </v-card>

        <v-card class="mb-4" elevation="10">
          <v-card-text class="text-left" style="background-color: #FFFFFF;height: 110px; overflow: hidden;">
            <div class="text-h4 font-weight-thin" style="font-size: 15px !important;">
              종목상태구분
              <v-divider></v-divider>
              <span style="font-size: 25px; font-weight: bold;">{{ getStatusLabel(status) }}</span>
            </div>
          </v-card-text>
        </v-card>
        

        <v-card class="mb-4" elevation="10">
          <v-card-text class="mx-auto" style="background-color: #FFFFFF; height: 125px;">
            <div class="text-h4 font-weight-thin" style="font-size: 15px !important; margin-top: -10px;">
              퀀트데이터
              <v-divider></v-divider>
              <div class="quant-data">
                <div style="font-size: 20px; font-weight: bold;">
                  PER: {{ quantData.PER }}
                </div>
                <div style="font-size: 20px; font-weight: bold;">
                  PBR: {{ quantData.PBR }}
                </div>
                <div style="font-size: 20px; font-weight: bold;">
                  EPS: {{ quantData.EPS }}
                </div>
                <div style="font-size: 20px; font-weight: bold;">
                  BPS: {{ quantData.BPS }}
                </div>
              </div>
            </div>
          </v-card-text>
        </v-card>

        <v-card elevation="10">
  <v-card-text class="text-left" style="background-color: #FFFFFF;height: 110px;">
    <div class="text-h4 font-weight-thin" style="font-size: 15px !important;">
      시장경고
      <v-divider></v-divider>
      <span style="font-size: 25px; font-weight: bold;">{{ getMarketAlertLabel(marketAlert) }}</span>
    </div>
  </v-card-text>
</v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Chart from 'chart.js';
import axios from 'axios';

export default {
  data() {
    return {
      showOverlay: true, // 초기에는 표시됨
      searchQuery: '',
      selectedInterval: 'Daily',
      intervals: ['Daily', 'Weekly', 'Monthly', 'Quarterly', 'Yearly'],
      stockChart: null,
      currentPrice: "",
      status: "",
      quantData: {
        PER: "",
        PBR: "",
        EPS: "",
        BPS: "",
      },
      marketAlert: "",
      searchInput: "",
      data: null,
      marketAlertLabels: {
        "00": "없음",
        "01": "투자주의",
        "02": "투자경고",
        "03": "투자위험"
      },
      statusLabels: {
        "00": "그외",
        "51": "관리종목",
        "52": "투자의견",
        "53": "투자경고",
        "54": "투자주의",
        "55": "신용가능",
        "57": "증거금 100%",
        "58": "거래정지",
        "59": "단기과열"
      },
    };
  },
  mounted() {
    this.loadData();
  },
  methods: {
    hideOverlay() {
      this.showOverlay = false; // overlay를 숨기는 메소드
    },
    performSearch() {
      if (this.searchQuery !== '') {
        this.fetchStockData();
        this.searchItem();
        this.hideOverlay();
      }
    },
    fetchStockData() {
      if (this.searchQuery !== '') {
        const encodedStockName = encodeURIComponent(this.searchQuery);
        const interval = this.selectedInterval.toLowerCase();
        axios
          .get(`http://localhost:5000/${interval}_stock_data?stock_name=${encodedStockName}`)
          .then(response => {
            const data = JSON.parse(response.data);
            this.clearStockChart();
            if (data.length > 0) {
              this.createStockChart(data);
            }
          })
          .catch(error => {
            console.error(error);
          });
      }
    },
    clearStockChart() {
      if (this.stockChart) {
        this.stockChart.destroy();
      }
    },
    createStockChart(data) {
      const validData = data.filter(item => item['Close'] !== null && item['Close'] !== undefined);
      const displayedData = validData.slice(-20);

      const dates = displayedData.map(item => item['Date']);
      const closePrices = displayedData.map(item => item['Close']);

      const canvas = this.$refs.stockChartCanvas;
      const context = canvas.getContext('2d');
      context.clearRect(0, 0, canvas.width, canvas.height);

      const lastPrice = closePrices[closePrices.length - 1];
      const isLastPriceRising = lastPrice > closePrices[closePrices.length - 2];

      this.stockChart = new Chart(context, {
        type: 'line',
        data: {
          labels: dates,
          datasets: [
            {
              label: '주식 가격',
              data: closePrices,
              borderColor: isLastPriceRising ? 'red' : 'blue',
              borderWidth: 5,
              backgroundColor: isLastPriceRising ? 'rgba(255, 0, 0, 0.1)' : 'rgba(0, 0, 255, 0.1)'
            },
          ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            x: {
              display: true,
              title: {
                display: true,
                text: 'Date',
              },
            },
            y: {
              display: true,
              title: {
                display: true,
                text: 'Close',
              },
            },
          },
        },
      });
    },
    loadData() {
      axios
        .get('/extracted_data_kospi2.json')
        .then(response => {
          this.data = response.data;
          this.fetchStockData(); // Initial stock data fetch
          this.searchItem(); // Initial search
        })
        .catch(error => {
          console.error('Error loading data:', error);
        });
    },
    searchItem() {
      const input = this.searchQuery.trim().toLowerCase();
      let item;

      if (input) {
        // Search by code
        item = this.data[input];

        // If not found, search by name
        if (!item) {
          item = Object.values(this.data).find(
            entry => entry.Name.toLowerCase() === input
          );
        }
      }

      if (item) {
        this.currentPrice = item.Current;
        this.status = item.Status;
        this.quantData.PER = item.PER;
        this.quantData.PBR = item.PBR;
        this.quantData.EPS = item.EPS;
        this.quantData.BPS = item.BPS;
        this.marketAlert = item.Mkt;
      } else {
        console.error('Item not found with Code or Name: "' + this.searchQuery + '"');
      }
    },
    getMarketAlertLabel(code) {
      return this.marketAlertLabels[code] || "";
    },
    getStatusLabel(code) {
      return this.statusLabels[code] || "";
    },
  },
};
</script>

<style>
.quant-data {
  display: flex;
  flex-wrap: wrap;
}

.quant-data div {
  width: 50%;
}

</style>