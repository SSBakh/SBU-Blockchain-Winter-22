In Solidity, a function that doesn’t read or modify the variables of the state is called a
 pure function. It can only use local variables that are declared in the function and the
 arguments that are passed to
 the function to compute or return a value. 
Simple illustration for pure functions


If the pure function is doing any of the following, the compiler will consider them
 as reading state variables and will throw a warning:

   1- Reading state variables
   2- Accessing balance or address
   3- Invoking a function that is not pure
   4- Accessing a global variable, message, or block
   5- Using certain opcodes in inline assembly


Example:

contract Test {
   function getResult() public pure returns(uint product, uint sum){
      uint a = 15; 
      uint b = 8;
      product = a * b;
      sum = a + b; 
   }
}


Output:

0: uint256: product 120
1: uint256: sum 23


-------------------------------------------------------------

In Solidity, Modifiers express what actions are occurring in 
a declarative and readable manner. They are similar to the decorator 
pattern used in Object Oriented Programming.

The Solidity documentation define a modifier as follow:

   1- A function modifier is a compile-time source code roll-up.

   2- It can be used to amend the semantics of functions in a declarative way.

Example:

modifier onlyOwner {
    require(msg.sender == owner);
    _;
}
