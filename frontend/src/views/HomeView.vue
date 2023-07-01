<template>
  <v-container :md="!$vuetify.breakpoint.xs" fluid>
    <v-row align="center" width="100%">
      <v-col cols="6" md="6" sm="12">
        <line_kospi></line_kospi>
      </v-col>

      <v-col cols="6" md="6" sm="12">
        <line_kosdaq></line_kosdaq>
      </v-col>
    </v-row>

    <krx_card></krx_card>

    <v-spacer></v-spacer>

    <report_card></report_card>

  </v-container>
</template>


<script>
import report_card from "@/components/report_card.vue";
import kospi_gVue from '@/components/kospi_card.vue';
import kosdaq_gVue from '@/components/kosdaq_card.vue';
import krx_card from '@/components/krx_card.vue';
import axios from 'axios'; // axios import 추가

export default {
  components: {
    line_kospi: kospi_gVue,
    line_kosdaq: kosdaq_gVue,
    report_card: report_card,
    krx_card: krx_card
  },
  created() {
    this.getStockReport();
  },
  methods: {
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
    }
  }
};
</script>

<style>

</style>