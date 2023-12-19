class Vehicle {
    constructor(make, model, year){
        this.make = make
        this.model = model
        this.year = year
    }
    honk(){
        return 'Beep'
    }
    toString(){
        return `the vehicle is a ${this.make} ${this.model} from ${this.year}`
    }

}

class Car extends Vehicle{
    constructor(make, model, year){
        super(make, model, year)
        this.numWheels = 4
    }
     

}

class Motorcycle extends Vehicle{
    constructor(make, model, year){
        super(make, model, year)
        this.numWheels = 2
    }
    revEngine(){
        return 'VROOM'
    }
}

class Garage {
    constructor(capacity){
        this.vehicles = []
        this.capacity = capacity
    }
    add(newVehicle){
        if(!(newVehicle instanceof Vehicle)){
            return 'Only vehicles are allowed in here'
        }
        if(this.vehicles.length >= this.capacity){
            return 'Sorry we are full'
        }
        this.vehicles.push(newVehicle)
        return 'Vehicle has been added'
    }
      
    

}




let myFirstVehicle = new Vehicle('honda', 'monster truck', 1999)
let myFirstCar = new Car('honda', 'monster truck', 1999)
let myFirstMotorcycle = new Motorcycle('honda', 'nighthawk', 2000)
let garage = new Garage(2);










