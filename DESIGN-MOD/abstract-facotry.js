//汉堡抽象工厂
function HamburgerFactory(){

}

//汉堡里加辣椒的工厂
function HamburgerWithPepperFacotry(){

}
HamburgerWithPepperFacotry.prototype = new HamburgerFactory();
HamburgerWithPepperFacotry.prototype.constructor = HamburgerWithPepperFacotry;

HamburgerWithPepperFacotry.prototype.createHamburger = function(){
    console.log("A hamburder with pepper is ready.");
}


//汉堡里加火腿的工厂
function HamburgerWithHamFacotry(){

}
HamburgerWithHamFacotry.prototype = new HamburgerFactory();
HamburgerWithHamFacotry.prototype.constructor = HamburgerWithHamFacotry;

HamburgerWithPepperFacotry.prototype.createHamburger = function(){
    console.log("A hamburder with ham is ready.");
}

//美眉A 喜欢吃辣椒
function MeiMeiA(){

}
MeiMeiA.prototype.getHamburger = function(){
    console.log("I want to a hanburger with pepper.");
    hamburgerFactory = new HamburgerWithPepperFacotry();
    hamburgerFactory.createHamburger();
}

//美眉B 喜欢吃火腿
function MeiMeiB(){

}
MeiMeiB.prototype.getHamburger = function(){
    console.log("I want to a hanburger with ham.");
    hamburgerFactory = new HamburgerWithHamFacotry();
    hamburgerFactory.createHamburger();
}

var mA = new MeiMeiA();
mA.getHamburger();

/*console out

I want to a hanburger with pepper.
A hamburder with ham is ready.
*/