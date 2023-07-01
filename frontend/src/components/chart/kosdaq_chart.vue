<div>
<canvas ref="lineChart"></canvas>
</div>


<script>
import {Line} from 'vue-chartjs';
import Data from '@/data_json/kosdaq_data_1month.json';

export default {
  extends: Line,
  data() {
    return {
      data: Data,
      currentDate: this.getCurrentDate(),
    };
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
  },
  computed: {
    lineChartColor() {
      const targetData = this.data.find((d) => d.Date === this.currentDate);
      if (targetData) {
        return targetData.FLUC < 0 ? 'blue' : 'red';
      }
      return 'blue';
    },
    lineChartColor_Alpha() {
      const targetData = this.data.find((d) => d.Date === this.currentDate);
      if (targetData) {
        return targetData.FLUC < 0 ? 'rgba(0, 0, 255, 0.1)' : 'rgba(255, 0, 0, 0.1)';
      }
      return 'blue';
    },
  },
  mounted() {
    this.renderChart(
        {
          labels: this.data.map((d) => d.Date),
          datasets: [
            {
              label: 'CLSPRC',
              backgroundColor: this.lineChartColor_Alpha,
              borderColor: this.lineChartColor,
              data: this.data.map((d) => d.CLSPRC),
              // pointRadius: 2, // 포인트 크기 설정
            },
          ],
        },
        {
          responsive: true,
          maintainAspectRatio: false,
          legend: {
            display: false,
          },
          scales: {
            yAxes: [
              {
                display: false, // y축 숨김
                gridLines: {
                  display: false,
                  drawBorder: false,
                },
              },
            ],
            xAxes: [
              {
                display: false, // x축 숨김
                gridLines: {
                  display: false,
                  drawBorder: false,
                },
              },
            ],
          },
        }
    );
  },
};
</script>
