// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract MainContract {

    //Question 2 - A
    struct ColoredWallet {
        uint256 numberOfRedCoins;
        uint256 numberOfBlueCoins;
        address owner;
        bool active;
    }

    mapping(address => ColoredWallet) public ownerToColoredWallet;

    //Question 2 - B
    function createColoredWallet () public {

        // Check if the wallet already exists 
        require(!ownerToColoredWallet[msg.sender].active , "You cannot create a new wallet when you already have one!");
        ColoredWallet memory newColoredWallet = ColoredWallet(0, 100, msg.sender, true);
        ownerToColoredWallet[msg.sender] = newColoredWallet;
    }

    //Question 2 - C
    function getRedCoins () public {
        // Check if the wallet exists 
        require(ownerToColoredWallet[msg.sender].active , "You don not have any active wallet!");

        //Check the number of blue coins 
        require(ownerToColoredWallet[msg.sender].numberOfBlueCoins >= 1 , "You do not have enought blue coins!");

        ColoredWallet memory foundColoredWallet = ownerToColoredWallet[msg.sender];
        foundColoredWallet.numberOfBlueCoins = foundColoredWallet.numberOfBlueCoins - 1;
        foundColoredWallet.numberOfRedCoins = foundColoredWallet.numberOfRedCoins + 2;
        ownerToColoredWallet[msg.sender] = foundColoredWallet;
    }

    function showMyAddress () public view returns(address){
        return msg.sender;
    }


    //Question 2 - D    
    function sendBlueCoin(address _toWalletAddress, uint256 _numberOfBlueCoins) public{
        // Check if the wallet both sender and receiver wallets exist   
        require(ownerToColoredWallet[msg.sender].active , "You don not have any active wallet!");
        require(ownerToColoredWallet[_toWalletAddress].active , "Couldn't find the receiver wallet!");

        //Check the difference between sender and receiver
        require(msg.sender != _toWalletAddress , "You cannot send blue coins to yourself!");


        ColoredWallet memory senderColoredWallet = ownerToColoredWallet[msg.sender];

        //Check the balance
        require(senderColoredWallet.numberOfBlueCoins >= _numberOfBlueCoins , "You do not have enough blue coins!");
        
        senderColoredWallet.numberOfBlueCoins = senderColoredWallet.numberOfBlueCoins - _numberOfBlueCoins;

        ColoredWallet memory receiverColoredWallet = ownerToColoredWallet[_toWalletAddress];
        receiverColoredWallet.numberOfBlueCoins = receiverColoredWallet.numberOfBlueCoins + _numberOfBlueCoins;
        ownerToColoredWallet[_toWalletAddress] = receiverColoredWallet;

        ownerToColoredWallet[msg.sender] = senderColoredWallet;
    }
}
