<template lang="pug">
.page-loader-wrapper
    .page-loader
</template>

<style>
.page-loader-wrapper {
  background-color: rgba(15, 15, 15, 0.5);
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1000;
}
.page-loader {
  display: block;
  position: relative;
  left: 50%;
  top: 50%;
  width: 150px;
  height: 150px;
  margin: -75px 0 0 -75px;

  border: 3px solid #3498db;
  z-index: 1500;
}

.page-loader:before {
  content: "";
  position: absolute;
  top: 5px;
  left: 5px;
  right: 5px;
  bottom: 5px;
  border: 3px solid #e74c3c;
}
.page-loader:after {
  content: "";
  position: absolute;
  top: 15px;
  left: 15px;
  right: 15px;
  bottom: 15px;
  border: 3px solid #f9c922;
}

/* change border to transparent and set only border-top to a solid color */
.page-loader {
  border: 3px solid transparent;
  border-top-color: #3498db;
}
.page-loader:before {
  border: 3px solid transparent;
  border-top-color: #e74c3c;
}
.page-loader:after {
  border: 3px solid transparent;
  border-top-color: #f9c922;
}

.page-loader {
  border-radius: 50%;
}
.page-loader:before {
  border-radius: 50%;
}
.page-loader:after {
  border-radius: 50%;
}

/* .page-loader, .page-loader:before, .page-loader:after */

/* include this only once */
@-webkit-keyframes spin {
  0%   {
      -webkit-transform: rotate(0deg);  /* Chrome, Opera 15+, Safari 3.1+ */
      -ms-transform: rotate(0deg);  /* IE 9 */
      transform: rotate(0deg);  /* Firefox 16+, IE 10+, Opera */
  }
  100% {
      -webkit-transform: rotate(360deg);  /* Chrome, Opera 15+, Safari 3.1+ */
      -ms-transform: rotate(360deg);  /* IE 9 */
      transform: rotate(360deg);  /* Firefox 16+, IE 10+, Opera */
  }
}
@keyframes spin {
  0%   {
      -webkit-transform: rotate(0deg);  /* Chrome, Opera 15+, Safari 3.1+ */
      -ms-transform: rotate(0deg);  /* IE 9 */
      transform: rotate(0deg);  /* Firefox 16+, IE 10+, Opera */
  }
  100% {
      -webkit-transform: rotate(360deg);  /* Chrome, Opera 15+, Safari 3.1+ */
      -ms-transform: rotate(360deg);  /* IE 9 */
      transform: rotate(360deg);  /* Firefox 16+, IE 10+, Opera */
  }
}

.page-loader {
  -webkit-animation: spin 2s linear infinite;
  animation: spin 2s linear infinite;
}
.page-loader:before {
  -webkit-animation: spin 3s linear infinite;
  animation: spin 3s linear infinite;
}
</style>
