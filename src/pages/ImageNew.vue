<template>
    <div class="image">
      <Navbar></Navbar> 
        <div class="album py-5 bg-light">
            <div class="container">
              <div class="row">
                <div v-for="image in APIData" :key="image.id" class="col-md-4">
                  <div class="card mb-4 box-shadow">
                    <!-- <img >{{image.image}} > -->
                    <!-- <html> $imagename = {{image.image}} </html> -->

                    <!-- <img src="@/../media/uploads/2023/07/11/img_2.png"/> -->
                    <!-- <img :src="getPhoto(image.document)"/> -->
                    <!-- "{{ (image.document) }}" -->

                    <!-- <img :src="require(image.document)"/> -->

                    <!-- <img :src="require(`${image.document}`)"/> -->
                    <!-- <img :src= "image.document" /> -->
                    <!-- <img :src=  "'@/..' + image.document"  /> -->
                    <!-- "require('@' + image.document)" -->
                    <!-- <img :src= "{/media/uploads/2023/07/11/img_2.png}" /> -->
                    
                    <!-- <img :src="require('@/..' + image.document)" /> -->


                    <!-- <img :src="require('@' + '/..' + `${image.document}`)"> -->
                    "{{ image.document }}"
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
  
  <script>
    import { getAPI } from '../axios-api'
    import Navbar from '../components/Navbar'
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
        // return require("@/../media/uploads/2023/07/11/img_2.png");
        console.log("@/../media/uploads/2023/07/11/img_2.png")
        console.log("@/.." + path);
        console.log(require("@/../media/uploads/2023/07/11/img_2.png"))
        // console.log(require(path));
        // return require.context("@/.." + path);
        // return require("@/../media/uploads/2023/07/11/img_2.png");
        var p_string = "/.." + path
        console.log(p_string)
        var t_string = "@/../media/uploads/2023/07/11/img_2.png"
        console.log(t_string)
        //var images = require.context('@/../', false, /\.png$/)
        console.log('---')
        return require("@/../media/uploads/2023/07/11/img_2.png")
        //return require(p_string)
        // return "@/.." + path
        
        }
      }


    }
  </script>
  
  <style scoped>
  
  </style>
  
  