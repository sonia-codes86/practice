const numbers=[1,2,3,4];
const dubale=numbers.map((n)=>n*n);

console.log(dubale);

const numbers_1=[10,15,20,25,30];
const max_eighteen=numbers_1.filter((n)=>n>18);

console.log(max_eighteen);

function captalize(word){
    const first=word[0].toUpperCase();
    const rest=word.slice(1);
    return first +rest;
}
const names=["sara","ali","reza"];
const upper_name=names.map((n)=>captalize(n));

console.log(upper_name);

const codes=["html","css","java","python"];
const found=codes.find((n)=>n.length>3);

console.log(found);

const furts=["apple","fig","banana","kiwi"];
const name_furt=furts.filter((n)=>n.length>=4);

console.log(name_furt);

const person=[{"name":"sara","age":20},{"name":"ali","age":17}];
const name_person=person.map((n)=>n["name"]);
console.log(name_person);

const person_age=person.filter((n)=>n["age"]>=18);
console.log(person_age);

const numbers_2=[1,2,3,4];
const redu=numbers_2.reduce((total,n)=>total+n,0);
console.log(redu);




// const max_names=products.filter((p)=>p.price>50).map((p)=>p.name);
// console.log(max_names);

// const total_product=products.reduce((total,p)=>total + p.price,0);
// console.log(total_product);

// const expensive=products.reduce((max,p)=>{
//     return p.price > max ? p.price:max;},0);
// console.log(expensive);

// const discount=products.map((p)=>{
//     return {name:p.name,price:p.price*0.9};
// });
// console.log(discount);

const products=[
    {name:"laptop",price:800},
    {name:"mouse",price:20},
    {name:"keyboard",price:50},
    {name:"monitor",price:200}
];
const products_List=document.getElementById("products_List");
function renderProducts(List){
    products_List.innerHTML="";
    List.forEach((p)=>{
        const li=document.createElement("li");
        li.textContent=`${p.name} - $${p.price}`;
        products_List.appendChild(li);
    });
}

document.getElementById("showAll").addEventListener("click",()=>{
    renderProducts(products);
});

document.getElementById("show").addEventListener("click",()=>{
    renderProducts(products.filter((p)=>p.price>50));
});

renderProducts(products);