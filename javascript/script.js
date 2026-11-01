const number=document.getElementById("number");
const plus=document.getElementById("plus");
const minus=document.getElementById("minus");
const reset=document.getElementById("reset");
let count=0;
function updateDiplay(){
    number.textContent=count;
    if (count>10){
        number.style.color="blue";
    }
    else if(count<0){
        number.style.color="red";
    }else{
        
        number.style.color="black";
    }
}
plus.addEventListener("click",()=>{
    count++;
    updateDiplay();
});
minus.addEventListener("click",()=>{
    count--;
    updateDiplay();
});
reset.addEventListener("click",()=>{
    count=0;
    updateDiplay();
})