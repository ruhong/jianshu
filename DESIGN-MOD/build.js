//套餐A
function MealA(){
    
}
MealA.prototype = {
    mainFood: function(){
        console.log("main food is ready.");
    },
    sideFood: function(){
        console.log("side food is ready.");
    },
    drink: function(){
        console.log("drink food is ready.");
    }
}

//套餐B
function MealB(){
    
}
MealB.prototype = {
    mainFood: function(){
        console.log("main food is ready.");
    },
    sideFood: function(){
        console.log("side food is ready.");
    },
    drink: function(){
        console.log("drink food is ready.");
    }
}

//服务生
function Waiter(){

}
Waiter.prototype.deliver = function(meal){
    meal.mainFood();
    meal.sideFood();
    meal.drink();
};

waiter = new Waiter();
waiter.deliver(new MealA());

/*console out

main food is ready.
side food is ready.
drink food is ready.
*/