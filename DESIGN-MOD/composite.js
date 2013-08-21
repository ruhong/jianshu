//物品
function Stuff(name, price){
    this.name = name;
    this.price = price;
}
Stuff.prototype.des = function(){
    console.log(this.name + ' : ' + this.price);
};

//购物单
function Order(){
    this.orderComponentList = []
}
//add方法可以添加物品、购物单哦
Order.prototype.add = function(obj){
    this.orderComponentList.push(obj);
};
Order.prototype.des = function(){
    for(var i in this.orderComponentList){
        this.orderComponentList[i].des();
    }
};

var girlOrder = new Order(),
    boyOrder = new Order(),
    bothOrder = new Order();

//美眉的购物单
girlOrder.add(new Stuff("shoe", 120));
girlOrder.add(new Stuff("handbag", 220));
girlOrder.add(new Stuff("dress", 320));

//我的的购物单
boyOrder.add(new Stuff("T shirt", 230));

//我俩的购物单，总之都是我付钱
bothOrder.add(girlOrder);
bothOrder.add(boyOrder);

bothOrder.des();

/*console out

shoe : 120
handbag : 220
dress : 320
T shirt : 230
*/