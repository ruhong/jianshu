    //KFC store
    function KFCStore(){

    }
    KFCStore.prototype.getChickenWing = function(){
        return "KFC chicken wing.";
    };

    //MCD store
    function MCDStore(){

    }
    MCDStore.prototype.getChickenWing = function(){
            return "MCD chicken wing.";
    };

    //ChickenWing Factory
    function ChickenWingFactory(){

    }
    ChickenWingFactory.prototype.createChickenWing = function(obj){
        return obj.getChickenWing()
    };


    var chickenWingFactory = new ChickenWingFactory();

    console.log(chickenWingFactory.createChickenWing(new KFCStore()));
    console.log(chickenWingFactory.createChickenWing(new MCDStore()));

    /*console out

    KFC chicken wing.
    MCD chicken wing.
     */