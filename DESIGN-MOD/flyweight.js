//TV
function TV(brand, size){
    this.brand = brand;
    this.size = size;
}

//TV工厂
var TVFactory = (function(){
    var createdTV = {};

    return {
        createTV: function(brand, size){
            var tv,
                key = brand + size;
            if(typeof createdTV[key] !== 'undefined'){
                return createdTV[key];
            }else{
                tv = new TV(brand, size);
                createdTV[key] = tv;
                return tv;
            }
        }
    }
})();

//TV管理器
function TVManager(){
    this.tvDatabase = {};
}
TVManager.prototype.addNewTV = function(owner, brand, size){
    tv = TVFactory.createTV(brand, size);
    this.tvDatabase[owner] = tv;
};
TVManager.prototype.showTV = function(){
    for(var item in this.tvDatabase){
        console.log(item + ': ' + this.tvDatabase[item].brand + ', ' + this.tvDatabase[item].size);
    }
};


var tvManager = new TVManager();
//同一品牌、同一尺寸的TV只会共享一个实例
tvManager.addNewTV('adult', 'TCL', 30);
tvManager.addNewTV('children', 'TCL', 30);

tvManager.showTV();

/*console out

adult: TCL, 30
children: TCL, 30
 */