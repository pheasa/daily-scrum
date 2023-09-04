<template>
  <div class="card w-100 mb-3">
    <div class="card-body">
      <div class="row">
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
    closeCard() {
      this.$emit('handle-closeCard', this.cardObject)
    }
  }
}
</script>
