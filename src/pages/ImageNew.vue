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
                        <h4 class=""><a class="text-secondary" href="">{{image.id}}</a></h4>
                        <p class="card-text">{{image.id}}</p>
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
        var p_string = "http://127.0.0.1:8000" + path
        console.log(p_string)
        var t_string = "@/../media/uploads/2023/07/11/img_2.png"
        console.log('---')
        return p_string
        
        }
      }


    }
  </script>
  
  <style scoped>
  
  </style>
  
  