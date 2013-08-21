//装饰者
function Decorator(){

}
Decorator.prototype.getPrice = function(){
    if(typeof this.obj !== 'undefined'){
        return this.obj.getPrice() + ', ' + this.name + ': ' + this.price;
    }else{
        return this.name + ': ' + this.price;
    }
};
Decorator.prototype.getCost = function(){
    if(typeof this.obj !== 'undefined'){
        return parseFloat(this.obj.getCost()) + parseFloat(this.price);
    }else{
        return parseFloat(this.price);
    }
};

//新发型
function NewHair(obj){
    this.name = "new hair style";
    this.price = "20";
    this.obj = obj;
}
NewHair.prototype = Decorator.prototype;

//新衣服
function NewCloth(obj){
    this.name = "new cloth";
    this.price = "200";
    this.obj = obj;
}
NewCloth.prototype = Decorator.prototype;

//新鞋子
function NewShoes(obj){
    this.name = "new shoes";
    this.price = "130";
    this.obj = obj;
}
NewShoes.prototype = Decorator.prototype;

//我的所有装备
var equipment = new NewHair();
equipment = new NewCloth(equipment);
equipment = new NewShoes(equipment);

console.log(equipment.getPrice());
console.log('total cost：' + equipment.getCost());

/*console out

new hair style: 20, new cloth: 200, new shoes: 130
total：350
*/
