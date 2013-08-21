//心形原型
function HeartShape(color, size){
    this.color = color;
    this.size = size;
}

HeartShape.prototype.clone = function(){
   return new HeartShape(this.color, this.size);
};

//心形工厂
function HeartShapeFacotry(obj){
    this.obj = obj;
}
HeartShapeFacotry.prototype.getHeartShape = function(){
    return this.obj.clone();
}

var heartShapeFacotry = new HeartShapeFacotry(new HeartShape('red', 'big'));

//红色大心形，要多少有多少
var a = heartShapeFacotry.getHeartShape();
var b = heartShapeFacotry.getHeartShape();

console.log(a.color)
console.log(b.color)

console.log('--------------')

a.color = 'yellow';
console.log(a.color)
console.log(b.color)

/*print out

red
red
--------------
yellow
red
*/