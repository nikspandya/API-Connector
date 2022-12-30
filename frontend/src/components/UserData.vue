<template>
  <div id="app">
    <v-app>
      <!-- v-data-table to show list of users data -->
      <v-data-table
        :headers="headers"
        :items="users"
        item-key="name"
        class="elevation-1 pa-6"
      >
        <template v-slot:top>
          <!-- v-container, v-col and v-row are just for decoration purposes. -->
          <v-container fluid>
            <v-row>
              <v-col cols="4">
                <v-row class="pa-6">
                  <!-- Filter for user name-->
                  <v-text-field
                    v-model="nameFilterValue"
                    type="text"
                    label="User Name"
                  ></v-text-field>
                </v-row>
              </v-col>

              <v-col cols="4">
                <v-row class="pa-6">
                  <!-- Filter for countries -->
                  <v-select
                    :items="countryList"
                    v-model="countryFilterValue"
                    label="Country"
                  ></v-select>
                </v-row>
              </v-col>
              <v-col cols="4">
                <v-row class="pa-6">
                  <v-btn depressed color="green" @click="reloadData()">
                    Reaload Data
                  </v-btn>
                </v-row>
              </v-col>
            </v-row>
          </v-container>
        </template>
      </v-data-table>
    </v-app>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      // Available countries in randomuser api
      countryList: [
        { text: "All", value: null },
        { text: "Australia", value: "Australia" },
        { text: "Brazil", value: "Brazil" },
        { text: "Canada", value: "Canada" },
        { text: "Denmark", value: "Denmark" },
        { text: "Finland", value: "Finland" },
        { text: "France", value: "France" },
        { text: "Germany", value: "Germany" },
        { text: "Iran", value: "Iran" },
        { text: "Ireland", value: "Ireland" },
        { text: "Netherlands", value: "Netherlands" },
        { text: "New Zealand	", value: "New Zealand	" },
        { text: "Norway", value: "Norway" },
        { text: "Spain", value: "Spain" },
        { text: "Switzerland", value: "Switzerland" },
        { text: "Turkey", value: "Turkey" },
        { text: "United Kingdom	", value: "United Kingdom" },
        { text: "United States", value: "United States" },
      ],
      countryFilterValue: "",
      // Filter models.
      nameFilterValue: "",
      users: [],
    };
  },
  computed: {
    headers() {
      return [
        {
          text: "User Name",
          align: "left",
          sortable: false,
          value: "name",
          filter: this.nameFilter,
        },
        { text: "Gender", value: "gender" },
        {
          text: "Country",
          value: "country",
          filter: this.countryFilter,
        },
        { text: "Email", value: "email" },
      ];
    },
  },
  methods: {
    getData() {
      // Get user data from flask controller using axious
      axios
        .get("http://localhost:8601/users")
        .then((res) => {
          this.users = res.data.users;
        })
        .catch((error) => {
          console.error(error);
        });
    },

    reloadData() {
      this.getData();
    },

    nameFilter(value) {
      // If this filter has no value we just skip the entire filter.
      if (!this.nameFilterValue) {
        return true;
      }
      // Check if the current loop value (The user name)
      // partially contains the searched word.
      return value.toLowerCase().includes(this.nameFilterValue.toLowerCase());
    },

    countryFilter(value) {
      // If this filter has no value we just skip the entire filter.
      if (!this.countryFilterValue) {
        return true;
      }
      // Check if the current loop value (The countirs value)
      // equals to the selected value at the <v-select>.
      return value === this.countryFilterValue;
    },
  },
  created() {
    this.getData();
  },
};
</script>
