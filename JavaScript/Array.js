// //! Array :
// //1.Array Literal
// // syntax : var/let/const arr_name = [val1,val2...............]
// let arr = [10,20,30,40,70,50];
// console.log(arr)

// let arr1 = [10,'Yatheesh',9.0,'Reddy'];
// console.log(arr1)

// //2.Array Constructer
// let arr2 = new Array(10,20,30,40,70,50)
// console.log(arr)

// let arr3 = new Array(2)
// arr2[0]=20;
// arr2[1]=21;
// arr2[2]=22

// console.log(arr3)

// // !
// let nums = [10,20,30,40,50,60]
// console.log(nums);

// // 1 access
// console.log(nums[4])

// // 2 add
// nums[6]=70
// console.log(nums)

// // 3 delete
// delete nums[3];
// console.log(nums)

// // 4 update
// nums[2]=211
// console.log(nums)


// ! Array Methods
let flipkart = ['watch','kurtha','mobile','hair_dryer']
// console.log(flipkart);

// // ! Push() : add multiple elements at the end of the array
// flipkart.push('laptop','books','calculator','phone')
// console.log('After push');
// console.log(flipkart);

// // ! unshift() : add multiple elements from the starting of the array
// flipkart.unshift('shirt','shoes');
// console.log('After Unshift');
// console.log(flipkart);

// // ! pop() : delete the last element
// flipkart.pop()
// console.log('After POP');
// console.log(flipkart);

// // ! shit() : delete the first element
// flipkart.shift()
// flipkart.shift()
// console.log("After Shift");
//console.log(flipkart);

// ! splice(start_index,delete_count,replacement elements) : add and delete middle elements elements from the array
// [ "watch", "kurtha", "mobile", "hair_dryer" ]

flipkart.splice(1,2,'dress','smart watch','stove','perfume')
flipkart.splice(1,0,'book','cover','tv')
flipkart.splice(2,1)
console.log(flipkart);

// !slice(start_index,end_index) : extarct the part of the array

let slicedArr = flipkart.slice(0,3)
console.log(slicedArr);
console.log(flipkart);