<template>
  <div class="card w-100 mb-3">
    <div class="card-body">
      <div class="row">
        <div class="col-md-10">
          <h5 class="card-title">{{ cardObject.title }}</h5>
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
    }
  }
}
</script>
