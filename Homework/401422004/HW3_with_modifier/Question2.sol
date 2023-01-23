// SPDX-License-Identifier: MIT
// Meshkat Ahmadi
// 401422004

pragma solidity ^0.8.0;

contract MeshkatHW3Contract {

    // alef
    struct ColoredWallet {
        uint256 numberOfRedCoins;        
        uint256 numberOfBlueCoins;
        address owner_address;
        // to check if the person exists
        bool exists;
    }

    mapping (address => ColoredWallet) address2wallet;

    // be    
    function createWallet() public
    {
        ColoredWallet memory new_wallet = ColoredWallet(0, 100, msg.sender, true);
        address2wallet[msg.sender] = new_wallet;
    }

    // pe
    function burnABlue() public
    {
        require (address2wallet[msg.sender].numberOfBlueCoins>0,"You do not have enough blue coins to convert");
        address2wallet[msg.sender].numberOfBlueCoins = address2wallet[msg.sender].numberOfBlueCoins - 1;
        address2wallet[msg.sender].numberOfRedCoins = address2wallet[msg.sender].numberOfRedCoins + 2;
    }

    // te
    // Everyone can only use his/her own wallet
    function sendABlue(address receiver) public
    {
        // check if we have enough blue
        require (address2wallet[msg.sender].numberOfBlueCoins>0,"You do not have enough blue coins to send");
        // check if the receiver exists is checkted
        require (address2wallet[receiver].exists,"Your receiver does not exists");
        address2wallet[msg.sender].numberOfBlueCoins = address2wallet[msg.sender].numberOfBlueCoins - 1;
        address2wallet[receiver].numberOfBlueCoins = address2wallet[receiver].numberOfBlueCoins + 1;
    }

    function  getMyCoins() public view returns(uint256,uint256){
        return (address2wallet[msg.sender].numberOfRedCoins, address2wallet[msg.sender].numberOfBlueCoins);
    }

   
}