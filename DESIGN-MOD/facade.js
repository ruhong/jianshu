//支付系统
function PaySystem(){

}
PaySystem.prototype.pay = function(){
    console.log('Payments completed.');
};

//卖家系统
function SellerSystem(){

}
SellerSystem.prototype.sendOut = function(){
    console.log('Seller sended out.');
};

//快递系统
function ExpressSystem(){

}
ExpressSystem.prototype.express = function(){
    console.log('Expressors delivered.');
}

//高层接口，简单易用，只能支付一次哦
function Facade(){
    if(typeof Facade.instance == 'object'){
        return Facade.instance; 
    }

    var paySys,
        sellerSys,
        expSys;
    paySys = new PaySystem();
    paySys.pay();

    sellerSys = new SellerSystem();
    sellerSys.sendOut();

    expSys = new ExpressSystem();
    expSys.express();

    Facade.instance = this;
}

var facade = new Facade();

/*console out

Payments completed.
Seller sended out.
Expressors delivered.
 */
