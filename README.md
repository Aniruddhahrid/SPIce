const api_url_11P = "http://localhost:5000/phy11chapters";
const api_url_11C = "http://localhost:5000/chem11chapters";
const api_url_11M = "http://localhost:5000/math11chapters";
const api_url_12P = "http://localhost:5000/phy12chapters";
const api_url_12C = "http://localhost:5000/chem12chapters";
const api_url_12M = "http://localhost:5000/math12chapters";

let C12Content;
let P11Content;
let C11Content;
let M11Content;
let P12Content;
let M12Content;

fetch(api_url_11P)
.then((response) => {
return response.json();
})
.then((data) => {
P11Content = data;
console.log(P11Content);
})


fetch(api_url_11C)
.then((response) => {
  return response.json();
})
.then((data) => {
  C11Content = data;
  console.log(C11Content);
})


fetch(api_url_11M)
.then((response) => {
  return response.json();
})
.then((data) => {
  M11Content = data;
  console.log(M11Content);
})


fetch(api_url_12P)
.then((response) => {
  return response.json();
})
.then((data) => {
  P12Content = data;
  console.log(P12Content);
})


fetch(api_url_12C)
.then((response) => {
  return response.json();
})
.then((data) => {
  C12Content = data;
  console.log(C12Content);
  console.log(C12Content.jsonStrChapters.length);
})

fetch(api_url_12M)
.then((response) => {
  return response.json();
})
.then((data) => {
  M12Content = data;
  console.log(M12Content);
})


disableSubmit = function() {
  // submit.disabled = this.checked
  if((document.getElementById("std").value == "nothing") || (document.getElementById("sub").value == "nothing")){
    document.getElementById("genbutton").disabled = true;
  }
  else{
    document.getElementById("genbutton").disabled = false;
  }
};

// document.getElementById("genbutton").disabled = true;
document.getElementById("sub").addEventListener('change', disableSubmit);
document.getElementById("std").addEventListener('change', disableSubmit);


function GenerateTable() {
  //Build an array containing Customer records.
  myFunction();
  var customers = new Array();
  customers.push(["Chapter", "Date", "Day"]);
  // for(var i=0;i<C12Content.jsonStrChapters.length;i++){
  //   customers.push([C12Content.jsonStrChapters[i],C12Content.jsonStrDates[i].slice(0,10),C12Content.jsonStrDates[i].slice(10,)])
  // }
  if(document.getElementById("std").value=="eleven" && document.getElementById("sub").value=="che"){
for(var i=0;i<C11Content.jsonStrChapters.length;i++){
    customers.push([C11Content.jsonStrChapters[i],C11Content.jsonStrDates[i].slice(0,10),C11Content.jsonStrDates[i].slice(10,)])
  }
  }
  if(document.getElementById("std").value=="eleven" && document.getElementById("sub").value=="phy"){
for(var i=0;i<P11Content.jsonStrChapters.length;i++){
    customers.push([P11Content.jsonStrChapters[i],P11Content.jsonStrDates[i].slice(0,10),P11Content.jsonStrDates[i].slice(10,)])
  }
  }
  if(document.getElementById("std").value=="eleven" && document.getElementById("sub").value=="mat"){
for(var i=0;i<M11Content.jsonStrChapters.length;i++){
    customers.push([M11Content.jsonStrChapters[i],M11Content.jsonStrDates[i].slice(0,10),M11Content.jsonStrDates[i].slice(10,)])
  }
  }
  if(document.getElementById("std").value=="twelve" && document.getElementById("sub").value=="che"){
    for(var i=0;i<C12Content.jsonStrChapters.length;i++){
    customers.push([C12Content.jsonStrChapters[i],C12Content.jsonStrDates[i].slice(0,10),C12Content.jsonStrDates[i].slice(10,)])
  }
  }
  if(document.getElementById("std").value=="twelve" && document.getElementById("sub").value=="phy"){
    for(var i=0;i<P12Content.jsonStrChapters.length;i++){
    customers.push([P12Content.jsonStrChapters[i],P12Content.jsonStrDates[i].slice(0,10),P12Content.jsonStrDates[i].slice(10,)])
  }
  } 
  if(document.getElementById("std").value=="twelve" && document.getElementById("sub").value=="mat"){
    for(var i=0;i<M12Content.jsonStrChapters.length;i++){
    customers.push([M12Content.jsonStrChapters[i],M12Content.jsonStrDates[i].slice(0,10),M12Content.jsonStrDates[i].slice(10,)])
  }
  }

//   // Data Picker Initialization
// $('.datepicker').datepicker();

// Date picker input

function myFunction() {
  var x = document.getElementById("myText").value;
  document.getElementById("demo").innerHTML = x;
}

  //Create a HTML Table element.
  var table = document.createElement("TABLE");
  table.border = "10";

  //Get the count of columns.
  var columnCount = customers[0].length;

  //Add the header row.
  var row = table.insertRow(0);
  for (var i = 0; i < columnCount; i++) {
      var headerCell = document.createElement("TH");
      headerCell.innerHTML = customers[0][i];
      row.appendChild(headerCell);
  }

  //Add the data rows.
  for (var i = 1; i < customers.length; i++) {
      row = table.insertRow(-1);
      for (var j = 0; j < columnCount; j++) {
          var cell = row.insertCell(-1);
          cell.innerHTML = customers[i][j];
      }
  }

  var dvTable = document.getElementById("dvTable");
  dvTable.innerHTML = "";
  dvTable.appendChild(table);
}
