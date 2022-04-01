



function validate(event) {
  var format = /[ `!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~1234567890]/;
  var invalid_stock = false;
var i;
const errorElement = document.getElementById('error');
const num_portfolios = document.getElementsByName('num_portfolios'); 
const stock1 = document.getElementById('stock1');
const stock2 = document.getElementById('stock2');
const stock3 = document.getElementById('stock3');
const stock4 = document.getElementById('stock4');
const stock5 = document.getElementById('stock5');
const stock6 = document.getElementById('stock6');
const stock7 = document.getElementById('stock7');
const stock8 = document.getElementById('stock8');
const stock9 = document.getElementById('stock9');
const stock10 = document.getElementById('stock10');

var stock_array = [stock1,stock2,stock3,stock4,stock5,stock6,stock7,stock8,stock9,stock10];

    var messages = [];
    for(i =1;i<11;i++){
      
     if(!stock_array[i-1].value == ""){
    if( (format.test(stock_array[i-1].value)) == true){
      invalid_stock = true;
      
      messages.push("Stock " + (i+1) + " Contains an illegal character");  
    }
    if(stock_array[i-1].value.length>8){
        invalid_stock = true;

       messages.push("Stock " + (i+1) + " Contains too many characters");
      
      }
     if(num_portfolios[0].value < 4){
       messages.push("Number of simulations should be larger than 3");  
      invalid_stock = true;
     }
  }
  if(invalid_stock){
  
       event.preventDefault();
       
       //title.append(messages.join('\n '));
       
      //errorElement.innerText = messages.join('\n ');
  }
 

}
if(invalid_stock){
  var title = document.getElementById("errorMessages");
  title.style.color="red";
title.innerHTML = "Illegal value entered";
}
}
var today = new Date();
var dd = String(today.getDate()).padStart(2, '0');
var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
var yyyy = today.getFullYear();
var todayStr = yyyy + '-' + mm + '-' + dd;
var yesterday = today.setDate(today.getDate()-5);
var dd1= String(today.getDate()).padStart(2, '0');
var mm1= String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
var yyyy1 = today.getFullYear();
var yesterDay1 = yyyy1 + '-' + mm1 + '-' + dd1;
var startDate = document.getElementById("start");
startDate.setAttribute("max",yesterDay1);
var endDate = document.getElementById("end");
endDate.setAttribute("max",todayStr);
endDate.setAttribute("value",todayStr);
let form = document.getElementById("form");
form.addEventListener('submit', validate);
