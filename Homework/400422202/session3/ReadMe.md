# Homework 3

Homework 3 has two section:

## section 1
Question:
What is pure function in solidity ?

Answer:
- The view functions are read-only function and state variables cannot be modified.
The pure functions do not read or modify the state variables.

example : 

    contract ViewAndPure {
    uint256 public x = 1;

    function addToX(uint256 y) public view returns(uint256) {
        return x + y;
    }

    function add(uint256 i, uint256 j) public pure returns(uint256) {
        return i + j;
    }
}

## section 2
Design a smart contract
   - there is a class for colored wallet which has four value : 
      - number of blue coin 
      - number of red coin
      - address of creator
      - isExist flag 

 this contract has three function:
   - Create wallet : wallet is created by caller address and is created just one time 
   - Burn a blue coin and receive two red coin (the wallet should have sufficient blue coin) 
   - Transfer some blue coin. This function gives two argument
        - amount of blue coin (the wallet should have sufficient blue coin) 
        - destination address. (the address should exist)
       

This is link of smart contract on goerli test net : 
https://goerli.etherscan.io/tx/0x5b8c42f43b6c691ece52ea8b61afb6c16b9696a83c419c2e5597302da6a18994