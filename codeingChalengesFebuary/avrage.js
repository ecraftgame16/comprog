function avrage(arr){
    let total = 0
    for (let i = 0; i < arr.length; i++){
        total += arr[i]
    }
    return total / arr.length
}

arr = [1, 5, 150, 20, 7, 5]
console.log(avrage(arr))