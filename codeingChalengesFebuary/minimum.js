function smallestNumber (arr) {
    let smallest = Infinity
    for (let i = 0; i < arr.length; i++){
        if (arr[i] < smallest){
            smallest = arr[i]
        }
    }
    return smallest
}

arr = [1, 5, -20, 5, 250, 90, 56]

console.log(smallestNumber(arr))