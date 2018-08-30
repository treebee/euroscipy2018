<template>
<v-app id="inspire">
    <v-content class="content">
      <v-container fluid>
        <v-layout>
          <v-flex xs6>
            <v-form>
              <v-menu full-width offset-y :close-on-content-click="false" v-model="dateMenu" bottom>
                <v-text-field slot="activator" :label="dateLabel"></v-text-field>
                <v-card>
                  <v-card-text>
                    <v-daterange :options="dateRangeOptions" @input="onDateRangeChange" />
                  </v-card-text>
                </v-card>
              </v-menu>
              <v-autocomplete
                v-model="selectedStore"
                :items="stores"
                item-text="store_name"
                item-value="store_id"
                label="Store"
                persistent-hint
              >
              </v-autocomplete>
              <v-autocomplete
                v-model="selectedProduct"
                :items="products"
                item-text="product_name"
                item-value="product_id"
                label="Product"
                persistent-hint
              >
              </v-autocomplete>
              <v-btn color="primary" :disabled="!isValid" @click="plotData">Render Plot</v-btn>
            </v-form>
          </v-flex>  
        </v-layout>
      </v-container>
     <div ref="vis"></div>
    </v-content>
  </v-app>
</template>

<script>
import axios from "axios";
import { format, subDays } from "date-fns";
import vegaEmbed from "vega-embed";

const START_DATES = [
  format(subDays(new Date(), 7), "YYYY-MM-DD"),
  format(new Date(), "YYYY-MM-DD")
];

export default {
  name: "app",
  data: function() {
    return {
      stores: [],
      selectedStore: null,
      products: [],
      selectedProduct: null,
      dateMenu: false,
      range: [START_DATES[0], START_DATES[1]],
      dateRangeOptions: {
        startDate: START_DATES[0],
        endDate: START_DATES[1],
        format: "YYYY-MM-DD",
        presets: [
          {
            label: "Today",
            range: [
              format(new Date(), "YYYY-MM-DD"),
              format(new Date(), "YYYY-MM-DD")
            ]
          },
          {
            label: "Yesterday",
            range: [
              format(subDays(new Date(), 1), "YYYY-MM-DD"),
              format(subDays(new Date(), 1), "YYYY-MM-DD")
            ]
          },
          {
            label: "Last 30 Days",
            range: [
              format(subDays(new Date(), 30), "YYYY-MM-DD"),
              format(subDays(new Date(), 1), "YYYY-MM-DD")
            ]
          }
        ]
      },
      items: []
    };
  },
  computed: {
    dateLabel() {
      return this.range[0] + " - " + this.range[1];
    },
    isValid() {
      return (
        this.range[0] != null &&
        this.range[1] != null &&
        this.selectedStore != null &&
        this.selectedProduct != null
      );
    }
  },
  created() {
    this.fetchStores();
    this.fetchProducts();
  },
  methods: {
    onDateRangeChange(input) {
      this.range = input;
    },
    fetchStores() {
      axios.get("http://localhost:5000/api/stores").then(response => {
        this.stores = response.data;
      });
    },
    fetchProducts() {
      axios.get("http://localhost:5000/api/products").then(response => {
        this.products = response.data;
      });
    },
    plotData() {
      const params = {
        from: this.range[0],
        to: this.range[1],
        store: this.selectedStore,
        product: this.selectedProduct
      };
      const embedOptions = {
        mode: "vega-lite",
        actions: false,
        renderer: "svg",
        width: "800"
      };
      console.log(params);
      axios.get("http://localhost:5000/api/plot", { params }).then(response => {
        vegaEmbed(this.$refs.vis, response.data, embedOptions);
      });
    }
  }
};
</script>
