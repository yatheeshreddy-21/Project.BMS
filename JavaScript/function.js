// //fun_name(argument1,argument2)

// function add(num1,num2){
//     let res = num1+num2
//     //console.log(res)
//     return res
// }

// console.log(add(3,4))

//? Generator function --used to generatemultiple values - yield--return
function* generate(){
    yield "ram";
    yield 56
    yield 3444.65
    yield true
}

// let res = generate()
// console.log(res.next().value);
// console.log(res.next().value);
// console.log(res.next().value);
// console.log(res.next().value)

console.log(generate().next().value);
