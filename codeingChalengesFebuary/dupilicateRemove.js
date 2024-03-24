function removeDuplicates(originalArray) {
    let newArray = [];
    for (let i = 0; i < originalArray.length; i++) {
        if (!newArray.includes(originalArray[i])) {
            newArray.push(originalArray[i]);
        }
    }
    return newArray;
}

const originalArray = ["a", "b", "a", "c", "b", "d", "a", "b", "c"];

console.log(removeDuplicates(originalArray));
