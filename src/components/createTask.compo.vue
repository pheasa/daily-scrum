<template>
  <!-- Modal -->
  <div
    class="modal fade"
    id="createTaskModal"
    tabindex="-1"
    aria-labelledby="createTaskModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="createTaskModalLabel">New task for today!</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <label for="task-title">Title</label>
          <div class="form-floating mb-3">
            <input type="text" class="form-control" id="task-title" v-model="title" />
            <label for="task-title">Here is your task title.</label>
          </div>
          <label for="description">Description</label>
          <div class="form-floating">
            <textarea
              class="form-control"
              placeholder="Leave a description here"
              id="description"
              rows="4"
              maxlength="500"
              v-model="description"
            ></textarea>
            <label for="description">Here is you description.</label>
          </div>
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-primary"
            :disabled="disabled"
            @click="saveTask"
            v-html="btnLabel"
          ></button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import * as bootstrap from 'bootstrap';
import axios from 'axios';

export default {
  data() {
    return {
      title: '',
      description: '',
      btnLabel: 'Save',
      dis_btn: false,
      disabled: false,
      myModal: null
    }
  },
  mounted() {
    this.myModal = new bootstrap.Modal(document.getElementById('createTaskModal'), {})
  },
  methods: {
    showModal() {
      this.myModal.show()
    },
    async saveTask() {
      this.disabled = true
      this.btnLabel ='<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>Loading...'
      let eThis = this;
      if (this.title && this.description) {
        await axios.get(eThis.$apiURL).then(response => {
          // do something with response.data
          eThis.$emit('handle-new-task', {
            id: response.data.id,
            title: response.data.title,
            description: response.data.description
          })
          eThis.title = '';
          eThis.description = '';
        }).catch(error => {
          // handle error
        });
      }
      this.myModal.hide()
      // document.getElementsByClassName('modal-backdrop')[0].remove();
      this.disabled = false
      this.btnLabel = 'Save'
    }
  },
  computed: {}
}
</script>
