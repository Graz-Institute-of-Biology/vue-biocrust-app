<template>
    <div class="image">
      <Navbar></Navbar> 
        <div class="album py-5 bg-light">
            <div class="container">
              <div class="row">
                <div v-for="image in APIData" :key="image.id" class="col-md-4">
                  <div class="card mb-4 box-shadow">
                    <img :src= getPhoto(image.document) alt="Image">
                    <!-- <img src = "http://127.0.0.1:8000/media/uploads/images/img_2.png" > -->
                    <div class="card-body">
                        <!-- <h4 class=""><a class="text-secondary" href="">{{image.id}}</a></h4> -->
                        <p class="text-secondary">{{getFilename(image.document)}}</p>
                        <div class="d-flex justify-content-between align-items-center">
                        <div class="btn-group">
                        
                        <button class="btn btn-sm btn-outline-primary" @click="downloadImage(getPhoto(image.document))">Download</button> 
                        <!-- <button @click=getPhoto(image.document) >View</button>  -->
                        <a :href=getPhoto(image.document)  class="btn btn-sm btn-outline-primary" role="button" aria-pressed="true">View</a>
                        <!-- <a :href=downloadImage(getPhoto(image.document)) download="image.jpg" class="btn btn-sm btn-outline-primary" role="button">Download</a> -->
                        <!-- <a class="btn btn-sm btn-outline-secondary" :on-click=downloadImage(getPhoto(image.document)) role="button" aria-pressed="true">Download</a> -->
                        <button class="btn btn-sm btn-outline-primary" @click="deleteImage(getPhoto(image.document))">Delete</button> 
                        </div>
                        <!-- <small class="text-muted">9 mins</small> -->
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
        </div>
    </div>
  </template>
  
  <script>
    import { getAPI } from '../axios-api'
    import Navbar from '../components/Navbar'
    import axios from 'axios'
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
    axios.defaults.xsrfCookieName = "csrftoken"
    export default {
      name: 'ImageNew',
      data () {
        return {
            APIData: []
          }
      },
      components: {
        Navbar
      },
      created () {
          getAPI.get('/image/',)
            .then(response => {
              console.log('Post API has recieved data')
              this.APIData = response.data

            })
            .catch(err => {
              console.log(err)
            })
      },
      methods: {
        getPhoto(path) {
        var p_string = "http://127.0.0.1:8000" + path
        console.log(p_string)
        var t_string = "@/../media/uploads/2023/07/11/img_2.png"
        console.log('---')
        return p_string        
        },
        getFilename(path) {
        var filename = path.replace(/^.*[\\\/]/, '')
        return filename
        },
        downloadImage(url) {
        fetch(url)
          .then(response => response.blob())
          .then(blob => {
            const objectURL = URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = objectURL;
            link.download = this.getFilename(url);
            link.target = '_blank';
            link.rel = 'noopener noreferrer';
            link.click();
          })
        },
        deleteImage(url) {

        axios
          .delete(url, {
            headers: {
             'X-CSRFTOKEN': "csrftoken" }}
          )
          .then(response => {
            console.log('Image deleted successfully!');
          })
          .catch(error => {
            console.error('Error deleting image:', error);
          });
        }
      }


    }
  </script>
  
  <style scoped>
  
  </style>
  
  