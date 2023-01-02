# README


## What is pure function?

In computer programming, a pure function is a function that has the following properties

the function return values are identical for identical arguments (no variation with local static variables, non-local variables, mutable reference arguments or input streams), and
the function has no side effects (no mutation of local static variables, non-local variables, mutable reference arguments or input/output streams).
Thus a pure function is a computational analogue of a mathematical function.

view indicates that the function will not alter the storage state in any way. But it allows you to "view" it or read it
pure is even more strict, indicating that it will not even read the storage state.

A pure function is a function which given the same input, always returns the same output. But the state of the contract keeps changing as users interact with it. So if you pass a state variable as an argument to the function, since the state is changing, that function will not be pure. That's why pure functions cannot access to state.

if you call view or pure functions externally, you do not pay a gas fee. However, they do cost gas if called internally by another function.

pure does not view nor modify state. i.e. it can only use what is provided to it to run. view cannot modify state, but can look it up. 

## Example:
...
 pragma solidity ^0.8.0;
contract mycontract
{

   function add(uint c, uint d) public pure returns(uint)
  { uint e=c+d;


   return e;

  } 
   function add(uint j, uint k) public view returns(uint)
  { uint f=j+k;


   return f;

  } 

}
...
## modifier
A modifier is a special type of Solidity function that is used to modify the behavior of other functions. For example, developers can use a modifier to check that a certain condition is met before allowing the function to execute.
A function modifier is a compile-time source code roll-up.
It can be used to amend the semantics of functions in a declarative way.
From this definition, we can understand that a modifier aims to change the behaviour of the function to which it is attached.
Modifiers are useful because they reduce code redundancy. You can re-use the same modifier in multiple functions if you are checking for the same condition over your smart contract.

When to use a modifier in Solidity?
The main use case of modifiers is for automatically checking a condition, prior to executing a function. If the function does not meet the modifier requirement, an exception is thrown, and the function execution stops.

Zahra ahmadnezhad
400422011
