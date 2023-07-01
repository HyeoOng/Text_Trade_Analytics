<template>
  <v-app>
    <v-app-bar
        app
        color="grey darken-4"
        dark
    >
      <v-app-bar-nav-icon @click="drawer = !drawer"/>

      <div class="d-flex align-center">
        <v-img
            alt="TTA Logo"
            src="@/assets/tta1.png"
            width="120"
        />
      </div>

    </v-app-bar>
    <v-navigation-drawer
        v-model="drawer"
        app
        color="grey darken-4"
        dark
    >
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="text-h6">
            <v-btn
                text
                @click="$router.push('/')"
            >
              Text Trade Analytics
            </v-btn>
          </v-list-item-title>
          <v-list-item-subtitle
              style="text-align: center;">
            증권사
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
      <!-- Navigation Items -->
      <v-list dense nav>
        <v-list-item
            v-for="item in items"
            :key="item.title"
            :to="item.to"
            link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-main>
      <v-container fluid>
        <router-view/>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',

  components: {},

  data: () => ({
    drawer: true,/* false로 설정하면 처음 들어갔을 때 펼쳐지지 않은 상태로 되어 있음 */
    items: [
      {title: 'Home', icon: 'mdi-home', to: '/'},
      {title: 'Research', icon: 'mdi-table-of-contents', to: '/research' },
      {title: 'StockChart', icon: 'mdi-chart-line', to: '/stock-chart'}
    ],
    right: null,
  }),
};
</script>
