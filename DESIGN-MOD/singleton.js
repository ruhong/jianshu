//这就是我，世界上独一无二
function Me(){
    if(typeof Me.instance === "object"){
        return Me.instance;
    }

    this.__name = 'Mr.Zhou',
    this.__height = '120cm',
    this.__gender = 'man';

    Me.instance = this;
}

Me.prototype = {
    getName: function(){
        return this.__name;
    },
    getHeight: function(){
        return this.__height;
    },
    getGender: function(){
        return this.__gender;
    },
    getIntroduction: function(){
        return 'Hi, I am ' + this.__name + ', ' + this.__height + ', and a ' + this.__gender + '.';
    }
};


var m1 = new Me();
var m2 = new Me();

console.log(m1===m2);
console.log(m1.getIntroduction());

/*console out

true
Hi, I am Mr.Zhou, 120cm, and a man.
*/