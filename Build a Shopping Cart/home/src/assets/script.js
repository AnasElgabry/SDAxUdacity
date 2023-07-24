/* Create an array named products which you will use to add all of your product object literals that you create in the next step. */

let products = [

/* Create 3 or more product objects using object literal notation 
   Each product should include five properties
   - name: name of product (string)
   - price: price of product (number)
   - quantity: quantity in cart should start at zero (number)
   - productId: unique id for the product (number)
   - image: picture of product (url string)
*/

  {
    name: "cherry", price: 6, quantity: 0, productId: 1, image: "images/cherry.jpg"
  },
  {
    name: "orange", price: 3, quantity: 0, productId: 2, image: "images/orange.jpg"
  },
  {
    name: "strawberry", price: 8, quantity: 0, productId: 3, image: "images/strawberry.jpg"
  }
]

/* Images provided in /images folder. All images from Unsplash.com
   - cherry.jpg by Mae Mu
   - orange.jpg by Mae Mu
   - strawberry.jpg by Allec Gomes
*/

/* Declare an empty array named cart to hold the items in the cart */

let cart = [
]

/* Create a function named addProductToCart that takes in the product productId as an argument
  - addProductToCart should get the correct product based on the productId
  - addProductToCart should then increase the product's quantity
  - if the product is not already in the cart, add it to the cart
*/

function addProductToCart(productId) {

  let empty = null;
  for (let i = 0; i < products.length; i++) {
    if (products[i].productId === productId) {
      empty = i;
      break;
    }
  }

  let found = false;
  for (let i = 0; i < cart.length; i++) {
    if (cart[i].productId === productId) {
      cart[i].quantity = cart[i].quantity + 1;
      products[empty].quantity = cart[i].quantity;
      found = true;
      break;
    }
  }

  if (found === false) {
    products[empty].quantity=1;
    cart.push({
      productId: productId,
      name: products[empty].name,
      quantity: 1,
      price: products[empty].price,
      image: products[empty].image
    });
  }
}

/* Create a function named increaseQuantity that takes in the productId as an argument
  - increaseQuantity should get the correct product based on the productId
  - increaseQuantity should then increase the product's quantity
*/

function increaseQuantity(productId) {
  for (let i = 0; i < cart.length; i++) {
    if (cart[i].productId === productId) {
      cart[i].quantity++;

      for (let i = 0; i < products.length; i++) {
        if (products[i].productId === productId) {
          products[i].quantity++;
        }
      }
      cart[i].total = cart[i].price * cart[i].quantity;
      break;
    }
  }
}

/* Create a function named decreaseQuantity that takes in the productId as an argument
  - decreaseQuantity should get the correct product based on the productId
  - decreaseQuantity should decrease the quantity of the product
  - if the function decreases the quantity to 0, the product is removed from the cart
*/

function decreaseQuantity(productId) {
  for (let i = 0; i < cart.length; i++) {
    if (cart[i].productId === productId) {
      cart[i].quantity--;
      
      for (let k = 0; k < products.length; k++) {
        if (products[k].productId === productId) {
          products[k].quantity = cart[i].quantity;
        }
      }
      
      if (cart[i].quantity == 0) {
        removeProductFromCart(productId);
        break;
      }
      cart[i].total = cart[i].price * cart[i].quantity;
      break;
    }
  }
}

/* Create a function named removeProductFromCart that takes in the productId as an argument
  - removeProductFromCart should get the correct product based on the productId
  - removeProductFromCart should update the product quantity to 0
  - removeProductFromCart should remove the product from the cart
*/

function removeProductFromCart(productId) {
  for (let i = 0; i < cart.length; i++) {
    if (cart[i].productId === productId) {
      cart.splice(i, 1);
      break;
    }
  }

  for (let i = 0; i < products.length; i++) {
    if (products[i].productId === productId) {
      products[i].quantity = 0;
    }
  }
}

/* Create a function named cartTotal that has no parameters
  - cartTotal should iterate through the cart to get the total of all products
  - cartTotal should return the sum of the products in the cart
*/

function cartTotal() {
  let sum = 0;
  cart.forEach(function(item) {
    sum += item.price * item.quantity;
  })
  return sum;
}

/* Create a function called emptyCart that empties the products from the cart */

function emptyCart() {
  cart = [];
}

/* Create a function named pay that takes in an amount as an argument
  - pay will return a negative number if there is a remaining balance
  - pay will return a positive number if money should be returned to customer
*/

totalPaid = 0;

function pay(amount) {
  totalPaid += amount;
    return totalPaid - cartTotal();  
}

/* Place stand out suggestions here (stand out suggestions can be found at the bottom of the project rubric.)*/

/* The following is for running unit tests. 
   To fully complete this project, it is expected that all tests pass.
   Run the following command in terminal to run tests
   npm run test
*/

module.exports = {
  products,
  cart,
  addProductToCart,
  increaseQuantity,
  decreaseQuantity,
  removeProductFromCart,
  cartTotal,
  pay,
  emptyCart,

  /* Uncomment the following line if completing the currency converter bonus */
  // currency
}