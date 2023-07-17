<template class="section" id="app">
    <div class="container">
        <h1 class="title mb-6">Uploader</h1>
        <div class="file">
            <label class="file-label">
                <input type="file" ref="file" class="file-input" @change="selectFile" multiple>

                <span class="file-cta">
                    <span class="file-label">Choose a file...</span>
                </span>
            </label>
        </div>
        <button class="button is-primary mt-2" v-if="documents.length" @click="upload">Upload</button>
        
        <div 
            class="notification mt-6"
            v-if="documents.length"
        >
            <p v-for="document in documents">
                {{  document.name }} {{ document.status }}
            </p>
            <!-- <img v-for="p in context" :src="p.url" :alt="dere" /> -->
        </div>
        <div class="album py-5 bg-light">
            <div class="container">
              <div class="row">
                <div v-for="image in APIData" :key="image.id" class="col-md-4">
                  "{{ image.document }}"
                  <div class="card mb-4 box-shadow">
                    <div class="card-body">
                        <h4 class=""><a class="text-secondary" href="">{{image.document}}</a></h4>
                        <p class="card-text">{{image.document}}</p>
                        <div class="d-flex justify-content-between align-items-center">
                        <div class="btn-group">
                        <a href="" class="btn btn-sm btn-outline-primary" role="button" aria-pressed="true">View</a>
                        <a href="" class="btn btn-sm btn-outline-secondary" role="button" aria-pressed="true">Edit</a>
                        </div>
                        <small class="text-muted">9 mins</small>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
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
    name: 'UploadModel',
        data() {
            return {
                documents: [],
                APIData: []
            }
        },
        created () {
          getAPI.get('/getmodels/',)
            .then(response => {
              console.log('Post API has recieved data')
              this.APIData = response.data

            })
            .catch(err => {
              console.log(err)
            })
      },
        delimiters: ['[[', ']]'],
        methods: {
            selectFile() {
                Array.from(this.$refs.file.files).forEach(file => {
                    this.upload(file)

                    this.documents.push({
                        'name': file.name,
                        'status': 'is uploading'
                    })
                })
            },
            upload(file) {
                this.progress = 0

                this.performUpload(file)
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
            performUpload(file) {
                let formData = new FormData()
                formData.append('document', file)

                return getAPI
                    .post('/uploadmodel/', formData, {
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
            }
        }
    }
    
</script>