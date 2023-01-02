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


    // modifier checking if user has blue
    modifier hasBlue {
        require (address2wallet[msg.sender].numberOfBlueCoins>0,"You do not have enough blue coins to convert");
      _;
    }
    // modifier checking if user wallet had been created
    modifier userExist(address _receiver) {
        require (address2wallet[_receiver].exists,"Your receiver does not exists");
      _;
    }


    // be
    function createWallet() public
    {
        ColoredWallet memory new_wallet = ColoredWallet(0, 100, msg.sender, true);
        address2wallet[msg.sender] = new_wallet;
    }

    // pe
    function burnABlue() public hasBlue
    {

        address2wallet[msg.sender].numberOfBlueCoins = address2wallet[msg.sender].numberOfBlueCoins - 1;
        address2wallet[msg.sender].numberOfRedCoins = address2wallet[msg.sender].numberOfRedCoins + 2;
    }

    // te
    // Everyone can only use his/her own wallet
    // check conditions with the modifier (hasBlue) check if the current user has blue / userExist check if the receiver is there
    function sendABlue(address _receiver) public hasBlue userExist(_receiver)
    {

        address2wallet[msg.sender].numberOfBlueCoins = address2wallet[msg.sender].numberOfBlueCoins - 1;
        address2wallet[_receiver].numberOfBlueCoins = address2wallet[_receiver].numberOfBlueCoins + 1;
    }

    function  getMyCoins() public view returns(uint256,uint256){
        return (address2wallet[msg.sender].numberOfRedCoins, address2wallet[msg.sender].numberOfBlueCoins);
    }


}
