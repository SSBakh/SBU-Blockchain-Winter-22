// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

//Question 1: What is a pure function?
//In Solidity, a function that doesn’t read or modify the variables of 
//the state is called a pure function. It can only use local variables 
//that are declared in the function and the arguments that are passed 
//to the function to compute or return a value.

contract SessionThreeExcersice {

    mapping(address => ColoredWallet) private addressMapper;


   modifier shouldBeRegistered {
        require(addressMapper[msg.sender].userAddress != address(0x0), "You have not registered in colored wallet!");
        _;
   }

    struct ColoredWallet {
        uint256 numberOfRedCoins;
        uint256 numberOfBlueCoins;
        address userAddress;
    }

    function createWallet() public{
        require(addressMapper[msg.sender].userAddress == address(0x0), "You have already registered in colored wallet!");
        ColoredWallet memory cw = ColoredWallet(0, 100, msg.sender);
        addressMapper[msg.sender] = cw;
    }

    function convertOneBlueToRed() public shouldBeRegistered{
        require(addressMapper[msg.sender].numberOfBlueCoins > 1, "You have insufficient blue coins to convert to red ones!");
        ColoredWallet memory cw = addressMapper[msg.sender];
        cw.numberOfBlueCoins = cw.numberOfBlueCoins - 1;
        cw.numberOfRedCoins = cw.numberOfRedCoins + 2;
        addressMapper[msg.sender] = cw;
    }

    function sendBlueCoin(uint256 coins, address addr) public shouldBeRegistered{
        require(addressMapper[addr].userAddress != address(0x0), "Target wallet has not registered in colored wallet!");
        require(msg.sender != addr, "You cannot send coins to yourself!");
        require(addressMapper[msg.sender].numberOfBlueCoins > coins, "You have insufficient blue coins to convert to red ones!");
        ColoredWallet memory source = addressMapper[msg.sender];
        ColoredWallet memory target = addressMapper[addr];
        source.numberOfBlueCoins = source.numberOfBlueCoins - coins;
        target.numberOfBlueCoins = target.numberOfBlueCoins + coins;
        addressMapper[msg.sender] = source;
        addressMapper[addr] = target;
    }

    function getWallet() view public returns(ColoredWallet memory){
        require(addressMapper[msg.sender].userAddress != address(0x0), "You have not registered in colored wallet!");
        return addressMapper[msg.sender];
    }

    //Pure function example
    function pureFunctionExample(uint256 a, uint256 b) pure public returns(uint256){
        return a + b;
    }
}
