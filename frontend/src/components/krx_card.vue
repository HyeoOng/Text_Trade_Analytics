<template>
  <div fluid height="300" width="100%">
    <v-row class="custom-margin-bottom" height="13">
      <v-col align-self="center" cols="6" sm="8">
        <div class="text-subtitle-1 auto pa-2"><h3>업종별 주가 시세</h3></div>
      </v-col>
    </v-row>
    <v-row>
      <v-carousel
          :continuous="true"
          :show-arrows="true"
          cycle
          delimiter-icon="mdi-minus"
          delimiter-icon-color="grey"
          height="400"
          hide-delimiter-background
          show-arrows-on-hover
      >
        <v-carousel-item v-for="(slide, index) in slides" :key="index">
          <v-row align="center" justify="center">
            <v-col v-for="item in slide" :key="item.IDX_NM" class="d-flex justify-center">
              <v-card elevation="5" height="180" width="170">
                <v-card-title class="text-center">
                  <v-row align="center" justify="center">
                    <v-col>
                      <h5 style="font-size: 14px;"><strong>{{ item.IDX_NM }}</strong></h5>
                    </v-col>
                  </v-row>
                </v-card-title>
                <v-card-text class="text-center">
                  <v-row align="center" justify="center">
                    <v-col>
                      <h2>{{ item.CLSPRC_IDX }}</h2>
                    </v-col>
                  </v-row>
                </v-card-text>
                <v-card-subtitle class="text-center">
                  <v-row align="center" justify="center">
                    <v-col cols="auto">
                      <p>
                        <span v-if="item.CMPPREVDD_IDX < 0" style="color: blue">{{
                            item.CMPPREVDD_IDX
                          }} ({{ item.FLUC_RT }}%)</span>
                        <span v-else style="color: red">{{ item.CMPPREVDD_IDX }} ({{ item.FLUC_RT }}%)</span>
                      </p>
                    </v-col>
                  </v-row>
                </v-card-subtitle>
              </v-card>
            </v-col>
          </v-row>
        </v-carousel-item>
      </v-carousel>
    </v-row>
  </div>
</template>

<script>
import KRX1 from "@/data_json/krx_data/krx_data1.json";
import KRX2 from "@/data_json/krx_data/krx_data2.json";
import KRX3 from "@/data_json/krx_data/krx_data3.json";
import KRX4 from "@/data_json/krx_data/krx_data4.json";

export default {
  data() {
    return {
      totalCards: 28,
      cardsPerSlide: 14,
      KRX: [KRX1, KRX2, KRX3, KRX4]
    };
  },
  computed: {
    slides() {
      const slides = [];
      let currentSlide = [];
      let cardCount = 0;

      this.KRX.forEach((sector) => {
        sector.forEach((item) => {
          currentSlide.push(item);
          cardCount++;

          if (cardCount % this.cardsPerSlide === 0) {
            slides.push(currentSlide);
            currentSlide = [];
          }
        });
      });

      if (currentSlide.length > 0) {
        slides.push(currentSlide);
      }

      return slides;
    },
  },
};
</script>

<style>

</style>