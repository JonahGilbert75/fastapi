<template>
  <div class="home">

    <div class="row row-sm mg-b-20 m-5">


 
<div class="col-lg-12">

  <div class="container py-1">
  
    <div class="col-12 shadow p-5" >

     <h1 class="new4">Post a job here</h1>
     <p class="new5">Run http://localhost:8080 </p>
      <p class="new5"> Here CRUD operation is done</p> 
      <p class="new5">Add data and Submit, Delete data by double click Delete button </p>

    <br><br><br>


     <form @submit.prevent="submitForm">
      

  <div class=row >

  <div class="form-group col-6">
    <label for="Company name">Company name</label>
    <input  class="form-control"  placeholder="Company name" v-model="job.Company_name">
    
  </div>


  <div class="form-group col-6">
    <label for="exampleInputPassword1">Title</label>
    <input class="form-control" placeholder="Enter Title" v-model="job.Title">
  </div>
  

   <div class="form-group col-6">
    <label for="exampleInputPassword1">Salary</label>
    <input class="form-control" placeholder="Enter Salary" v-model="job.Salary">
  </div>

   <div class="form-group col-6">
    <label for="exampleInputPassword1">No_of_post</label>
    <input class="form-control" placeholder="Enter No_of_post" v-model="job.No_of_post">
  </div> 
   
  <div class="form-group col-12">
    <label for="exampleInputPassword1">Job_Nature</label>
    <textarea type="text" class="form-control" placeholder="Enter Job_Nature" v-model="job.Job_nature"></textarea>
  </div>
     
  
<div class="col-4">
   <label for="exampleInputPassword1"></label><br>
   <button type="submit" class="btn btn-primary " >Submit</button>
  
</div>

  </div>

</form>



<br>


    <ul style="list-style: none;">
    <tr v-for="job in Job" :key="job.id" @click="$data.job=job"> 


 <div class="new">


      <li class="new1">Company Name : {{job.Company_name}}</li>
      <br><li class="new2">Job Title : {{job.Title}}</li>
     
      <li class="new3">SALARY : {{job.Salary}} <br>
      Vacancy : {{job.No_of_post}}</li> <br>

      <li class="new3">Job Nature : {{job.Job_nature}}</li>

<br>
      
      

      
     
      

 <td> <button class="btn btn-danger " @click="deleteJob(job.id)">Delete</button> </td>
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

        'Company_name':'',       
        'Title':'',
        'Job_nature':'',
        'Salary':'',
        'No_of_post':'',
        // 'Name':'',
      
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

    
    var response = await fetch('http://localhost:8000/register/');
    this.Job= await response.json();
  },

   

    async createJob(){
      
      await this.getJobs();

     
      await fetch(`http://localhost:8000/register/?Company_name=${this.job.Company_name}&Title=${this.job.Title}&Job_nature=${this.job.Job_nature}&Salary=${this.job.Salary}&No_of_post=${this.job.No_of_post}`,{
        method:'post',
        headers:{
          'Content-Type':'application/json'

        },

        body:JSON.stringify(this.job)
      });
     

      await this.getJobs();
      
      
    },

    
    

    

    async deleteJob(){ 
        
        await this.getJobs();
        
        
      await fetch(`http://localhost:8000/register/${this.job.id}`,{
        method:'delete', 
        headers:{
          'Content-Type':'application/json'

        },

        body: JSON.stringify(this.job)

      
      });
     
      
      await this.getJobs();
      
      
    },
    



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

p.new5{

  color: rgb(105, 94, 204);
  text-align: center;
  font-size: 100%;

}

</style>