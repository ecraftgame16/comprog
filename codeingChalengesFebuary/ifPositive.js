function positive (num) {
    if (num == 0){
        return 0
    }
    else if (num > 0){
        return "positive"
    }
    else if (num < 0){
        return "negative"
    }
}

const num = 10
console.log (positive(num))