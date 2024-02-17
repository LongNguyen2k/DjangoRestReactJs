// let firstName = "Thanh"
// let lastName = "Duong"

// let hello = `Hello ${firstName} ${lastName}`
// console.info(hello)


// function add(a, b){
//     return a + b
// }

// let add = (a, b) => {
//     a *= 2;
//     b *= 2;
//     return a + b;
// }

// console.info(add(2, 5))

// let a = [5, 4, 2, 7, -7, 4, "2", 4, "8"]

// console.info(a.filter(v => typeof(v) == 'number' && v % 2 ==0))
// console.info(a.map(v => v + 1))
// a.sort((v1, v2) => -(v1 - v2))
// console.info(a)

// function execute(callback) {
//     let a = 100;
//     let b = 99;
//     return callback(a, b)
// }

// console.info(execute((a, b) => a + b))
// console.info(execute((a, b) => a * b))

// var student = {
// 	fn: "LE",
// 	ln: "Duong", 
// 	fullName: function() {
// 		return `${this.fn} ${this.ln}`;
// 	}
// }

// let stu = student

// console.info(stu.fullName())

function User(fn, ln) {
    this.firstName = fn;
    this.lastName = ln;

    this.hello = function() {
        return `Hello ${this.firstName} ${this.lastName}`
    }
}

User.prototype.test = function() {
    return this.firstName.toUpperCase();
}

let u = new User("Thanh", "Duong")
console.info(u.hello())
console.info(u.test())

Array.prototype.isDigitArray = function() {
    var isDigit = true; 
    for(var i = 0; i < this.length && isDigit; i++){
        if(typeof this[i] != "number")
            isDigit = false;    
    }

    return isDigit;
}

let a = [3,"4",  4, 2]
console.info(a.isDigitArray())