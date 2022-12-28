# Exercise 3 
## View Functions
View functions ensure that they will not modify the state. A function can be declared as view. The following statements if present in the function are considered modifying the state and compiler will throw warning in such cases.
Modifying state variables.
+ Emitting events.
+ Creating other contracts.
+ Using selfdestruct.
+ Sending Ether via calls.
+ Calling any function which is not marked view or pure.
+ Using low-level calls.
+ Using inline assembly containing certain opcodes.

## Pure Functions
Pure functions ensure that they not read or modify the state. A function can be declared as pure. The following statements if present in the function are considered reading the state and compiler will throw warning in such cases.
+ Reading state variables.
+ Accessing address(this).balance or <address>.balance.
+ Accessing any of the special variable of block, tx, msg (msg.sig and msg.data can be read).
+ Calling any function not marked pure.
+ Using inline assembly that contains certain opcodes.
### Pure Function Example
```
pragma solidity ^0.5.0;

contract Test {
   function getResult() public pure returns(uint product, uint sum){
      uint a = 1; 
      uint b = 2;
      product = a * b;
      sum = a + b; 
   }
}
```
## Difference 
Pure, view and payable dictate a Solidity functions behavior. If the behavior of a function is not specified by default it will read and modify the the state of the block chain. View functions are read only function and do not modify the state of the block chain (view data on the block chain). Pure functions do not read and do not modify state of the block chain. All the data the pure function is concerned with is either passed in or defined in the functions scope.

---
# Bonus Question
## What is modifier?
A modifier is a special type of Solidity function that is used to modify the behavior of other functions. For example, developers can use a modifier to check that a certain condition is met before allowing the function to execute. 

Modifiers are similar to functions, in that they can take arguments and have a return type. Modifiers can also be chained together, meaning that you can have multiple modifiers on a single function. 

However, modifiers can only modify contract logic, and they cannot modify a contract’s storage, which includes structs. Modifiers reduce the amount of boilerplate code that developers have to write, and can make your Solidity code more readable.
