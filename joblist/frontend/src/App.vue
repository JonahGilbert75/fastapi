<template>


<nav class="navbar navbar-expand-lg navbar-dark bg-primary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Job</a>
    
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="/Search">Search Job</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" href="/home">Post Job</a>
        </li>

         <li class="nav-item">
          <a class="nav-link active" href="/about">About us</a>
        </li>
    
      </ul>
     
    </div>
  </div>
</nav>

  <router-view/>

</template>
