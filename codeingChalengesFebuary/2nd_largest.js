let num = [1, 2 ,3 , 4, 5];

function selarg(objectsArray) {
    num.sort();
    return objectsArray[objectsArray.length - 2];
}

console.log(selarg(num))