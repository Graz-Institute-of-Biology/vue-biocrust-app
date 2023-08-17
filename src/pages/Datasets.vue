<template>
    <div class="image">
      <Navbar></Navbar> 
        <div class="album py-5 bg-light">
            <div class = "d-flex flex-column justify-content-center align-items-center"> 
                <h2>Upload Dataset</h2>
                <form @submit.prevent="uploadDataset">
                <div class = "form-grid"> 
                <label class="text-secondary" for="dataset_name">Dataset Name:&nbsp</label>
                <input class="btn btn-sm btn-outline-primary" v-model="dataset_name" id="dataset_name" required />
                <br />
                </div>
                <div class = "form-grid"> 
                <label class="text-secondary" for="description">Description:&nbsp</label>
                <input class="btn btn-sm btn-outline-primary" v-model="description" id="description" required />
                <br />
                </div>
                <div class = "form-grid"> 
                <label class="text-secondary" for="coordinates">Coordinates:&nbsp</label>
                <input class="btn btn-sm btn-outline-primary" v-model="coordinates" id="coordinates" required />
                <br />
                </div>

                <button class="btn btn-primary btn-lg" type="submit">Upload</button>
                </form>
                <div v-if="responseMessage">
                    <div class="alert alert-success" v-if="success == true">
                    <button type="button" aria-hidden="true" class="close">×</button>
                    <span>
                    <b> It Worked! - </b> {{ responseMessage }} </span
                    >
                    </div>
                    <div class="alert alert-warning" v-if="success == false">
                    <button type="button" aria-hidden="true" class="close">×</button>
                    <span>
                    <b> Warning - </b> {{ responseMessage }} </span
                    >
                    </div>
                </div>  
                <h2>Uploaded Datasets</h2>
                <ul>
                <li class ="col-12" v-for="(dataset, index) in APIData" :key="index">
                    <!-- "{{ dataset.dataset_name }}" -->
                    <strong>{{ dataset.dataset_name }}</strong><br />
                    Description: {{ dataset.description }}<br />
                    Coordinates: {{ dataset.coordinates }}
                </li>
                </ul>
            </div>

        </div>
    </div>
</template>

<script src="https://unpkg.com/vue@3"></script>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script>
    import { getAPI } from '../axios-api'
    import Navbar from '../components/Navbar'
    import axios from 'axios'
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
    axios.defaults.xsrfCookieName = "csrftoken"
        
    export default {
    name: 'Datasets',
    data() {
        return {
        dataset_name: "",
        description: "",
        coordinates: "",
        datasets: [],
        APIData: [],
        responseMessage: '',
        success: 0
        };
    },
    mounted() {
        // Fetch the list of datasets when the component is mounted
        this.fetchDatasets()
    },
    components: {
        Navbar
    },
    methods: {
        uploadDataset() {
        // Send dataset details to backend (Django) using Axios
        const newDataset = {
            dataset_name: this.dataset_name,
            description: this.description,
            coordinates: this.coordinates
        }

        return getAPI
            .post("/uploaddataset/", newDataset, {
                        headers: {"Content-Type": "multipart/form-data",
                            //"X-CSRFToken": "csrf_token"
                            //xsrfCookieName: 'csrftoken',
                            //xsrfHeaderName: 'X-CSRFTOKEN',
                        }
                    })
            .then(response => {
            // Add the new dataset to the list on the frontend
            this.datasets.push(newDataset);
            this.responseMessage = 'Upload Successful'
            this.success = true

            // Clear the input fields after successful upload
            this.dataset_name = "";
            this.description = "";
            this.coordinates = "";
            })
            .catch(error => {
            console.error(error);
            this.responseMessage = error.response.data.message;
            this.success = false
            });
        },
        fetchDatasets() {
        // Fetch the list of datasets from backend (Django) using Axios
        return getAPI.get("/datasets/")
            .then(response => {
            this.APIData = response.data;
            })
            .catch(error => {
            console.error(error);
            });
        }
    
    }
    };
</script>
  
  <style scoped>
  
  </style>
  
  