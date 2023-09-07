<template>
    <div class="card w-100 mb-3">
      <div class="card-body">
        <div class="row" v-if="cardObject.is_previous && cardObject.is_old">
          <div class="col-md-10">
            <h5 class="card-title">{{ cardObject.title }}</h5>
            <p class="card-text">{{ cardObject.description }}</p>
          </div>
          <div class="col-md-2" v-if="cardObject.btn_transfer">
            <button type="button" class="btn btn-primary float-end" @click="moveCard">
              <i class="bi bi-caret-right-fill"></i>
              <i class="bi bi-caret-right-fill"></i>
            </button>
          </div>
        </div>
        <div class="row" v-else-if="!cardObject.is_old">
            <div class="col-md-11">
            <h5 class="card-title">{{ cardObject.title }}</h5>
            </div>
            <div class="col-md-1 text-end">
            <button class="close-card" @click="closeCard"><i class="bi bi-x-circle-fill"></i></button>
            </div>
            <div class="col-md-12">
            <p class="card-text">{{ cardObject.description }}</p>
            </div>
        </div>
      </div>
    </div>
  </template>
  <script>
  export default {
    props: ['cardObject'],
    methods: {
      moveCard() {
        this.$emit('handle-transfer', this.cardObject)
      },
      closeCard() {
      this.$emit('handle-closeCard', this.cardObject)
    }
    }
  }
  </script>
  