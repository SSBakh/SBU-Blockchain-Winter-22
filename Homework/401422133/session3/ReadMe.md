# Homework3

## pure vs view

View function can be declared view in which case they promise not to modify the state. they can view the state variable but can't modify it

Pure function declares that no state variable will be changed or read.

view tells us that by running the function, no data will be saved/changed.

pure tells us that not only does the function not save any data to the blockchain, but it also doesn't read any data from the blockchain.

Both of these don't cost any gas to call if they're called externally from outside the contract (but they do cost gas if called internally by another function).

e.g
---
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;

contract ViewAndPure {
    uint public x = 1;

    // Promise not to modify the state.
    function addToX(uint y) public view returns (uint) {
        return x + y;
    }

    // Promise not to modify or read from the state.
    function add(uint i, uint j) public pure returns (uint) {
        return i + j;
    }
---

# Etherscan link:

https://goerli.etherscan.io/tx/0x1e39ecf8cc0001dde452fcb1ada21c8c9bdd2767819072f60e0d5894b3f6ac84

Transaction Hash:
0x1e39ecf8cc0001dde452fcb1ada21c8c9bdd2767819072f60e0d5894b3f6ac84
