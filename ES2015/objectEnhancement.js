// function createInstructor(firstName, lastName){
//     return {
//       firstName: firstName,
//       lastName: lastName
//     }
//   }

function createInstructor(firstName, lastName){
    return {
        firstName,
        lastName
    }
}

// var favoriteNumber = 42;

// var instructor = {
//   firstName: "Colt"
// }

// instructor[favoriteNumber] = "That is my favorite!"

const instructor = {
    firstName: 'colt',
    [favoriteNumber]: 'that is my favorite'
}

// var instructor = {
//     firstName: "Colt",
//     sayHi: function(){
//       return "Hi!";
//     },
//     sayBye: function(){
//       return this.firstName + " says bye!";
//     }
//   }

const instructor = {
    firstName: 'colt',
    sayHi(){
        return 'hi'
    },
    sayBye(){
        return this.firstName + ' says bye'
    }
}


function createAnimal(species,verb,noise){
    return {
        species,
        [verb](){
            return noise
        }
    }


}