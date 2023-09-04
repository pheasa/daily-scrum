<script setup>
import DataTable from 'datatables.net-vue3'
import DataTablesCore from 'datatables.net'
import CardPreviousDay from '../components/CardPreviousDay.compo.vue'
import CardToday from '../components/CardTday.comp.vue'
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
        <button
          type="button"
          class="float-end btn btn-primary"
          @click="showAddTaskModal"
        >
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
              <transition name="fade" mode="out-in" v-for="object in task_previous_day"  :cardObject="object"
                :key="object" @handle-transfer="transferCard">
                <CardPreviousDay  v-if="visible[object.id]"></CardPreviousDay>
              </transition>
            </div>
          </div>
          <div class="col-md-6">
            <div class="card main-cards-list">
              <CardEmpty v-if="card_empty.today" ></CardEmpty>
              <transition name="fade" mode="in-out" v-for="object in task_today"
                :cardObject="object"
                :key="object"
                @handle-closeCard="closeCard"
              >
              <CardToday v-if="visible[object.id]"></CardToday>
            </transition>
            </div>
          </div>
        </div>
        <div id="daily-record">
          <div class="row p-3">
            <div class="col-md-11 text-center">
              <h2>Daily record</h2>
            </div>
            <div class="col-md-1">
              <button type="button" class="btn btn-success" @click="saveForToday">
                send <i class="bi bi-chevron-double-down"></i>
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
  <CreateTask @handle-new-task="newTask" ref="popupModal"></CreateTask>
</template>
<script>
export default {
  components: {
    CardPreviousDay,
  },
  data() {
    return {
        visible: {},
      card_empty: {
        prevoius_day: false,
        today: false
      },
      task_previous_day: [
        {
          id: 1,
          title: 'Mobile app',
          description: 'create login',
          is_previous: true
        }
      ],
      task_today: [
        {
          id: 2,
          title: 'fa and si form',
          description: 'testing',
          is_previous: false
        }
      ]
    }
  },
  mounted() {
    const merge_obj = this.task_today.concat(this.task_previous_day);
    merge_obj.forEach(task_obj => {
        this.visible[task_obj.id] = true;
    });
  },
  methods: {
    showAddTaskModal(){
      this.$refs.popupModal.showModal();
    },
    transferCard(cardObject) {
      this.visible[cardObject.id] = false;
      setTimeout(() => {
        this.task_today.push(cardObject);
        this.task_previous_day.splice(this.task_previous_day.findIndex(x => x.id === cardObject.id), 1);
        this.checkCaredEmpty();
        this.visible[cardObject.id] = true;
      }, 500);
      
    },
    closeCard(cardObject) {
        this.visible[cardObject.id] = false;
      setTimeout(() => {
        if (cardObject.is_previous) {
            this.task_previous_day.push(cardObject)
        }
        this.task_today.splice(this.task_today.findIndex(x => x.id === cardObject.id), 1);
        this.checkCaredEmpty()
        this.visible[cardObject.id] = true;
      }, 500);
    },
    checkCaredEmpty() {
      this.card_empty.today = !this.task_today.length ? true : false
      this.card_empty.prevoius_day = !this.task_previous_day.length ? true : false
    },
    newTask(newTaskObject){
        this.visible[newTaskObject.id] = false;
      setTimeout(() => {
        this.task_today.push({
          id: newTaskObject.id,
          title: newTaskObject.title,
          description: newTaskObject.description,
          is_previous: false
        });
      this.checkCaredEmpty()
        this.visible[newTaskObject.id] = true;
      }, 500);
    },
    saveForToday(){
      
    }
  }
}
</script>
