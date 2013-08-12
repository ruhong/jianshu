function A(){
    this.name = "A";
}

function B(){
    this.age = 24;

}

B.prototype = new A();
B.prototype.constructor = B;

var b = new B();
console.log(b.constructor);