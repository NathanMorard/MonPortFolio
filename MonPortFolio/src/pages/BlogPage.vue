<template>
  <div class="Content">
    <h1>Qui suis-je ?</h1>
    <p>
      Qui cum venisset ob haec festinatis itineribus Antiochiam, praestrictis
      palatii ianuis, contempto Caesare, quem videri decuerat, ad praetorium cum
      pompa sollemni perrexit morbosque diu causatus nec regiam introiit nec
      processit in publicum, sed abditus multa in eius moliebatur exitium addens
      quaedam relationibus supervacua, quas subinde dimittebat ad principem.
    </p>
    <h2>Mon parcours</h2>
    <div class="timeline">
      <div class="container left">
        <img src="../assets/img/amazon.png" alt="Amazon" />
        <div class="content">
          <h2>Amazon Inc.</h2>
          <small>2019 - 2020</small>
          <p>
            The success of every websites depends on search engine optimisation
            and digital marketing strategy. If you are on first page of all
            major search...
          </p>
          <span class="left-container-arrow"></span>
        </div>
      </div>
      <div class="container right">
        <img src="../assets/img/tesla.png" alt="Tesla" />
        <div class="content">
          <h2>Tesla Inc.</h2>
          <small>2020 - 2021</small>
          <p>
            The success of every websites depends on search engine optimisation
            and digital marketing strategy. If you are on first page of all
            major search...
          </p>
          <span class="right-container-arrow"></span>
        </div>
      </div>
      <div class="container left">
        <img src="../assets/img/flipkart.png" alt="Flipkart" />
        <div class="content">
          <h2>Flipkart</h2>
          <small>2021 - 2022</small>
          <p>
            The success of every websites depends on search engine optimisation
            and digital marketing strategy. If you are on first page of all
            major search...
          </p>
          <span class="left-container-arrow"></span>
        </div>
      </div>
      <div class="container right">
        <img src="../assets/img/toyota.png" alt="Toyota" />
        <div class="content">
          <h2>Toyota</h2>
          <small>2021 - 2022</small>
          <p>
            The success of every websites depends on search engine optimisation
            and digital marketing strategy. If you are on first page of all
            major search...
          </p>
          <span class="right-container-arrow"></span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup></script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Poppins', sans-serif;
}

body {
  background-color: #2e364a;
}

.timeline {
  position: relative;
  max-width: 1200px;
  margin: 100px auto;
}

.container {
  padding: 10px 50px;
  position: relative;
  width: 50%;
  animation: movedawn 1s linear forwards;
  opacity: 0;
}

@keyframes movedawn {
  0% {
    opacity: 1;
    transform: translateY(-30px);
  }
  100% {
    opacity: 1;
    transform: translateY(0px);
  }
}

.container:nth-child(1) {
  animation-delay: 0s;
}
.container:nth-child(2) {
  animation-delay: 1s;
}

.container:nth-child(3) {
  animation-delay: 2s;
}
.container:nth-child(4) {
  animation-delay: 3s;
}

.container.left {
  left: 50%;
}

.container.right {
  right: 0;
}

.content {
  padding: 20px 30px;
  background-color: #fff;
  position: relative;
  border-radius: 6px;
  font-size: 15px;
}

.container img {
  position: absolute;
  width: 40px;
  border-radius: 50%;
  top: 32px;
  z-index: 10;
}

.container.right img {
  right: -20px;
}

.container.left img {
  left: -20px;
}

.timeline::after {
  content: '';
  position: absolute;
  width: 6px;
  height: 100%;
  background-color: #fff;
  top: 0;
  left: 50%;
  margin-left: -3px;
  z-index: -1;
  animation: moveline 6s linear forwards;
}
@keyframes moveline {
  0% {
    height: 0;
  }
  100% {
    height: 100%;
  }
}

.content h2 {
  font-weight: 600;
}

.content small {
  display: inline-block;
  margin-bottom: 15px;
}

.left::before {
  content: '';
  height: 0;
  width: 0;
  position: absolute;
  top: 28px;
  z-index: 1;
  border-top: 15px solid transparent;
  border-bottom: 15px solid transparent;
  border-left: 15px solid #fff;
  right: -15px;
}

.right::before {
  content: '';
  height: 0;
  width: 0;
  position: absolute;
  top: 28px;
  z-index: 1;
  border-top: 15px solid transparent;
  border-bottom: 15px solid transparent;
  border-right: 15px solid #fff;
  left: -15px;
}

.left-container-arrow {
  height: 0;
  width: 0;
  position: absolute;
  top: 28px;
  z-index: 1;
  border-top: 15px solid transparent;
  border-bottom: 15px solid transparent;
  border-right: 15px solid #fff;
  left: -15px;
}

.right-container-arrow {
  height: 0;
  width: 0;
  position: absolute;
  top: 28px;
  z-index: 1;
  border-top: 15px solid transparent;
  border-bottom: 15px solid transparent;
  border-left: 15px solid #fff;
  right: -15px;
}

/* @media screen and (max-width: 800px) {
.timeline {
margin: 50px auto;
}
.timeline::after {
right: 31px;
}
.container {
width: 100%;
padding-left: 80px;
padding-right: 25px;
}
.text-box {
font-size: 13px;
}
.text-box small {
margin-bottom: 10px;
}

.container.right{
left: 0;
}

.container.left img, .container.right img{
left: 10px
}

.left-container-arrow, .right-container-arrow{
border-right: 15px solid #fff;
border-left: 0;
left: -15px;
}
} */
</style>
