<script setup>
import DataTable from 'datatables.net-vue3'
import DataTablesCore from 'datatables.net'
// import CardPreviousDay from '../components/CardPreviousDay.compo.vue'
// import CardToday from '../components/CardTday.comp.vue'
import CardOfDay from '../components/CardOfDay.copn.vue'
import CardEmpty from '../components/cardEmpty.compo.vue'
import CreateTask from '../components/createTask.compo.vue'

DataTable.use(DataTablesCore)
</script>
<template>
  <main>
    <div class="container">
      <div class="container-fluid text-center">
        <h2>My daily scrum</h2>
      </div>
      <div class="container-fluid float-end">
        <button type="button" class="float-end btn btn-primary" @click="showAddTaskModal">
          Add Task
        </button>
      </div>
      <div id="day-compare" class="container-fluid">
        <div class="row text-center title p-2">
          <div class="col-md-6">
            <h4>PREVIOUS DAY</h4>
            <p>02/09/2023</p>
          </div>
          <div class="col-md-6">
            <h4>TODAY</h4>
            <p>02/09/2023</p>
          </div>
        </div>
        <div class="row" id="listing-compare">
          <div class="col-md-6">
            <div class="card main-cards-list">
              <CardEmpty v-if="card_empty.prevoius_day"></CardEmpty>
              <transition
                name="fade"
                mode="out-in"
                v-for="object in task_previous_day"
                :cardObject="object"
                :key="object"
                @handle-transfer="addCardToToday"
                @handle-closeCard="closeCard"
              >
                <CardOfDay v-show="object.visible"></CardOfDay>
              </transition>
            </div>
          </div>
          <div class="col-md-6">
            <div class="card main-cards-list">
              <CardEmpty v-if="card_empty.today"></CardEmpty>
              <transition
                name="fade"
                mode="in-out"
                v-for="object in task_today"
                :cardObject="object"
                :key="object"
                @handle-closeCard="closeCard"
              >
                <CardOfDay v-show="object.visible"></CardOfDay>
              </transition>
            </div>
          </div>
        </div>
        <div id="daily-record">
          <div class="row p-3">
            <div class="col-md-11 text-center">
              <h2>Daily record</h2>
            </div>
            <div class="col-md-1" style="display: inline;">
              <button type="button" class="btn btn-success m-1" @click="saveForPreviousday">
                Send PD  <i class="bi bi-chevron-double-down"></i>
              </button>
              <button type="button" class="btn btn-success m-1" @click="saveForToday">
                send TD <i class="bi bi-chevron-double-down"></i>
              </button>
            </div>
          </div>
          <div class="row">
            <div class="col-md-12">
              <DataTable
                :data="[
                  [1, 2],
                  [3, 4]
                ]"
                class="display"
              >
                <thead>
                  <tr>
                    <th>A</th>
                    <th>B</th>
                  </tr>
                </thead>
              </DataTable>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
  <CreateTask @handle-new-task="newTask" ref="popupModal" :transferObject="transfterCard" ></CreateTask>
</template>
<script>
export default {
  // components: {
  //   CardPreviousDay
  // },
  data() {
    return {
      transfterCard : null,
      card_empty: {
        prevoius_day: false,
        today: false
      },
      task_previous_day: [
        {
          id: 1,
          title: 'Mobile app',
          description: 'create login',
          challenge: '',
          is_previous: true,
          btn_transfer:true,
          is_old: true,
          visible: true
        },
        {
          id: 2,
          title: 'Teting',
          description: 'This is testing',
          challenge: '',
          is_previous: true,
          btn_transfer:true,
          is_old: true,
          visible: true
        }
      ],
      task_today: [
        {
          id: 2,
          title: 'fa and si form',
          description: 'testing',
          challenge: '',
          is_previous: true,
          is_old: false,
          visible: true
        }
      ],
      
    }
  },
  mounted() {

  },
  methods: {
    removeTask(id){
      let index = -1,
      in_today = false;
      // check in today object
      index = this.task_today.findIndex((x) => x.id === id)
      if(index != -1){
        in_today = true;
        this.task_today.splice(
          index,
            1
        );
      }
      
      // check in prevoius day
      index = this.task_previous_day.findIndex((x) => x.id === id)
      if(index != -1 && in_today){
        this.task_previous_day.forEach(taskObj => {
          if(taskObj.id == id){
            taskObj.btn_transfer = true;
          }
        });
      }else if(index != -1 && !in_today){
        this.task_previous_day.splice(
          index,
          1
        );
      }
    },
    showAddTaskModal() {
      this.$refs.popupModal.showModal()
    },
    addCardToToday(cardObject) {
      this.transfterCard = cardObject;
      this.$refs.popupModal.showModal();

      cardObject.btn_transfer = false;
      let transferCard = Object.assign({}, cardObject) ;
      transferCard.visible = true;
      transferCard.is_previous = true
      transferCard.is_old = false
      console.log(transferCard);
      this.task_today.push(transferCard);
      this.checkCaredEmpty()
    },
    closeCard(cardObject) {
      cardObject.visible = false
      setTimeout(() => {
        this.removeTask(cardObject.id);
        this.checkCaredEmpty()
      }, 500)
    },
    checkCaredEmpty() {
      this.card_empty.today = !this.task_today.length ? true : false
      this.card_empty.prevoius_day = !this.task_previous_day.length ? true : false
    },
    newTask(newTaskObject) {
      console.log(newTaskObject);
      if(newTaskObject.is_previous){ //// insert to previous day
        this.task_previous_day.push(newTaskObject)
      }else{ //// is today
        this.task_today.push(newTaskObject)
      }
      newTaskObject.visible = true;
    },
    saveForToday() {
      alert('send today to backend.')
    },
    saveForPreviousday() {
      alert('send previous day to backend.')

    }
  }
}
</script>
