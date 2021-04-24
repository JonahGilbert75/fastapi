<template>



  <div class="Search">
    <div class="row row-sm mg-b-20 m-5">

 
<div class="col-lg-12">

  <div class="container py-1">
  
    <div class="col-12 shadow p-5">
    <h1 class="new4">Here You can Search job</h1>
    

    <br><br><br>

   

        <ul style="list-style: none;">
    <tr v-for="job in Job" :key="job.id" @dblclick="$data.job=job">

 <div class="new">
 

      <li class="new1">Company Name : {{job.Company_name}}</li>
      <li class="new2">Job Title : {{job.Title}}</li><br>
      
      <li class="new3">SALARY : {{job.Salary}} <br>
      Vacancy : {{job.No_of_post}}</li> <br>

      <li class="new3">Job Nature : {{job.Job_nature}}</li>

<br>
      
      <button type="button" class="btn btn-primary" autocomplete="off">Apply</button>

      
      <br>
      <p>You can apply this job if you are intrested, The recuter may call you when they see...</p>
      


 </div>

          </tr>
      
</ul>

      
      
      
       </div>
  </div>
</div>
     </div>
  
  </div>
  
</template>



<script>







export default {
  name: 'App',

  data(){

    return{
      job:{},

        // 'id':'',

        // 'Company_name':'',       
        // 'Title':'',
        // 'Job_Nature':'',
        // 'Salary':'',
        // 'No_of_post':'',
      
      Job:[]
    }
  },

  async created(){
    

    await this.getJobs();

  },

  methods:{


    submitForm(){
      if(this.job.id === undefined)
      {
        this.createJob();
        
      }else {
        this.editJob();
      }
    },


  async getJobs(){
    
    
    var response = await fetch('http://127.0.0.1:8000/register/');
    this.Job= await response.json();
  },

    async createJob(){
      await this.getJobs();
      
      await fetch('http://127.0.0.1:8000/register/',{
        method:'axios.post',
        headers:{
          'Content-Type':'application/json'

        },

        body:JSON.stringify(this.job)
      });
      

      await this.getJobs();
    },


      async editJob(){
        await this.getJobs();

        // 

      await fetch(`http://127.0.0.1:8000/register/${this.job.id}/`,{
        method:'axios.post',
        headers:{
          'Content-Type':'application/json'

        },

        body:JSON.stringify(this.job)
      });
     
      await this.getJobs();
      this.job = {};
    },
    
      async deleteJob(){ 
        
        await this.getJobs();
     
      await fetch(`http://127.0.0.1:8000/register/${this.job.id}/`,{
        method:'delete', 
        headers:{
          'Content-Type':'application/json'

        },

        body: JSON.stringify(this.job)
      });
     

      await this.getJobs();
    }  


    }

}
</script>

<style>
div.new{
  background-color: rgb(240, 232, 232);
  width: 100%;
  border: 5px solid rgb(49, 131, 238);
  padding: 50px;
  margin: 5px;
}



li.new1{

  color: rgb(3, 150, 248);
  text-align-last: center;
  font-size: 200%;
  
  
}


li.new2{

  color: rgb(3, 150, 248);
  text-align-last: center;
  font-size: 150%;

}


li.new3{

  color: rgb(0, 0, 0);
  text-align: left;
  font-size: 100%;

}

h1.new4{

  color: rgb(105, 94, 204);
  text-align: center;
  font-size: 400%;

}

</style>