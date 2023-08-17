<template class="section" id="app">
    <div class="container">
        <h1 class="title mb-6">Uploader</h1>
        <div class="file">
            <label class="file-label">
                <form @submit.prevent="selectFile">
                    <select v-model="DatasetName" required>
                        <option v-for="(item, index) in APIData" :key="index" :value="item.dataset_name">{{ item.dataset_name }} </option>
                    </select>
                    <input type="file" ref="file" class="file-input"  multiple required>
                    <span class="file-cta">
                        <span class="file-label">Choose a file...</span>
                    </span>
                    <!-- <button class="button is-primary mt-2" v-if="documents.length" @click="upload">Upload</button> -->
                    <button class="btn btn-primary btn-lg" type="submit">Upload</button>
                </form>

            </label>
        </div>
        <!-- <button class="button is-primary mt-2" v-if="documents.length" @click="upload">Upload</button> -->
        
        <div 
            class="notification mt-6"
            v-if="documents.length"
        >
            <p v-for="document in documents">
                {{  document.name }} {{ document.status }}
            </p>
            <!-- <img v-for="p in context" :src="p.url" :alt="dere" /> -->
        </div>
    </div>
</template>

<script src="https://unpkg.com/vue@3"></script>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script>
import axios from 'axios'
import { getAPI } from '../axios-api'
axios.defaults.xsrfCookieName = 'csrf_token';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
export default {
    name: 'Upload',
        data() {
            return {
                documents: [],
                DatasetName: null,
                APIData: [],
                allNames: [] 
            }
        },
        mounted() {
            // When the component is mounted, call a method to extract the names
            this.fetchDatasets();
        },
        delimiters: ['[[', ']]'],
        methods: {
            selectFile() {
                Array.from(this.$refs.file.files).forEach(file => {
                    this.upload(file, this.DatasetName)

                    this.documents.push({
                        'name': file.name,
                        'status': 'is uploading'
                    })
                })
            },
            upload(file, DatasetName) {
                this.progress = 0

                this.performUpload(file, this.DatasetName)
                .then(response => {
                    this.documents.forEach(document => {
                        if (document.name === file.name) {
                            document['status'] = 'is uploaded'
                        }
                    })
                })
                .catch(error => {
                    this.documents.forEach(document => {
                        if (document.name === file.name) {
                            document['status'] = 'failed'
                        }
                    })
                })
            },
            performUpload(file, DatasetName) {
                let formData = new FormData()
                formData.append('document', file)
                formData.append('name', DatasetName)
                console.log(DatasetName)
                console.log(formData)

                return getAPI
                    .post('/upload/', formData, {
                        headers: {"Content-Type": "multipart/form-data",
                            //"X-CSRFToken": "csrf_token"
                            //xsrfCookieName: 'csrftoken',
                            //xsrfHeaderName: 'X-CSRFTOKEN',
                        }
                    })
                
                /*getAPI.post('/upload/',formData, {
                        headers: {
                            "Content-Type": "multipart/form-data",
                            "X-CSRFToken": "{{ csrf_token }}"
                        }
                    })*/
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
            },
        }
    }
    
</script>