//充电器--Iphone专用
function Charger(){

}
Charger.prototype.charge = function(){
    console.log("A charger for Iphone.");
};

//万能充
function ChargerAdapter(){
    Charger.apply(this);
}
ChargerAdapter.prototype.charge = function(){
    console.log("A charger for phones.");
};

var iphoneCharger = new Charger();
var phoneCharger = new ChargerAdapter();

iphoneCharger.charge();
phoneCharger.charge();

/*cosole out

A charger for Iphone.
A charger for phones.
 */
