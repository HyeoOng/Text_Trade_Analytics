<template>
<v-card> 
    <v-toolbar flat>
    <v-toolbar-title>종목분석 리포트</v-toolbar-title>
    <v-spacer></v-spacer>
    <div>
        <v-btn text color="primary" @click="gotolist()">
        목록
        </v-btn>
    </div>
    </v-toolbar>
    <v-divider />
    <v-card>
    <div class="pa-5 pl-8">
        <v-row>
        <v-col cols="10">
            <v-row class="report_title"> 
            <h2> [ {{ company }} ]  </h2>
            </v-row>
            <v-row class="align-end">
            <p> {{getItemValueWithoutName(stockBroker)}}  |  {{wdate}}  </p>
            </v-row>
        </v-col>
        <v-col cols="2" class="text-center">
            <div class="icon-container">
            <a :href="report_link" target="_blank">
            <v-icon
                style="font-size: 40px;" v-on:mouseover="changeIconColor(true)" v-on:mouseout="changeIconColor(false)" :color="iconColor">
                mdi-file-document-outline
                </v-icon></a>
            <p>리포트 보기</p>
            </div>
        </v-col>
        </v-row>
    </div>
    </v-card>
    <v-card>
    <v-card-text>
        <h3 class="mb-10"> {{ title }} </h3>
        
        {{ content }}
        <div class="mt-5 mb-5">
                {{ pdf_summerize }}
        </div>
        <h5 class="mt-20"><strong> {{pdf_sent_topic}} | {{ pdf_sent_score }}</strong></h5>
    </v-card-text>

    </v-card>
</v-card>
</template>

<script>
export default {
data() {
    return {
    company: '',
    stockBroker: '',
    wdate: '',
    content: '',
    pdf_sent_topic: '',
    pdf_sent_score: '',
    pdf_summerize: '',
    title: '',
    report_link: '',
    //gridsystem에서 데이터 제목이랑 증권사만 가지고 와서 db에서 두개가 같은 데이터로 가지고 올 수 있으면 좋겠다. 뭔 느낌인지 알죠
    v0: true,
    iconColor: "black",
    };
    
},
mounted() {
    this.company = this.$route.query.company;
    this.stockBroker = this.$route.query.stock_broker;
    this.wdate = this.$route.query.wdate;
    this.content = this.$route.query.content;
    this.pdf_sent_topic = this.$route.query.pdf_sent_topic;
    this.pdf_sent_score = this.$route.query.pdf_sent_score;
    this.pdf_summerize = this.$route.query.pdf_summerize;
    this.title = this.$route.query.title;
    this.report_link = this.$route.query.report_link;
},
methods:{
    gotolist(){
    this.$router.push('research/RecommendedStockByCompany') //목록의 경로
    },
    changeIconColor(isHovered) {
    this.iconColor = isHovered ? "primary" : "black";
    },
    getItemValueWithoutName(value) {
        if (typeof value === "object" && value !== null && "name" in value) {
        return value.name;
        }
        return value;
    },
},
};
</script>

<style>
.report_title{
    height:85px;
    align-items: center;
}
.align-end {
align-items: end;
}
.text-center {
text-align: center;
align-items: start;
}
.icon-container {
display: flex;
flex-direction: column;
align-items: center;
}
.icon-container p {
margin-top: 4px;
margin-bottom: 0px;
}
</style>
