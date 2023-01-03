/*
Pure Functions in Solidity
In Solidity, a pure function is a function that does not modify the state of the contract 
and does not depend on any external input or state. This means that a pure function always returns
the same result for the same input, and calling a pure function does not have any side effects.

Pure functions are useful when you want to perform calculations or make decisions based on the input,
without modifying the contract state. They are also more efficient than other types of functions
because they do not require any external data or modify the contract state, so they have a lower gas cost.

View functions are similar to pure functions, in that they do not modify the contract state and have a lower gas cost.
However, view functions can access and return the values of contract storage variables, while pure functions cannot.
Here is an example of a contract that uses pure functions:

*/

pragma solidity ^0.8.0;

contract Calculator {
    function add(uint x, uint y) public pure returns (uint) {
        return x + y;
    }

    function subtract(uint x, uint y) public pure returns (uint) {
        return x - y;
    }
}

/*
In this contract, the add and subtract functions are both pure functions because they do not modify the contract state
and do not depend on any external input or state. They simply perform the specified arithmetic calculations on 
the input values and return the result.
*/