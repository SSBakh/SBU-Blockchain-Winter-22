// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract MyWallet{
    struct ColoredWallet{
        uint256 numberOfRedCoins;
        uint256 numberOfBlueCoins;
        bool isCreated;
    }

    // Mapping to get colored wallet from address(A structure to store wallets too!)
    mapping (address => ColoredWallet) public Wallets;

    // This function creates a colored wallet for message sender
    function createColoredWallet() public {
        require(Wallets[msg.sender].isCreated == false, "Error: You already have a colored wallet!");

        ColoredWallet memory wallet = ColoredWallet(0, 100, true);
        Wallets[msg.sender] = wallet;
    }

    // This function burns blue coin of message sender to get red coin 
    function burnBlueCoinToGetRedCoin() public {
        require(Wallets[msg.sender].isCreated == true, "Error: You don`t have a colored wallet!");
        require(Wallets[msg.sender].numberOfBlueCoins > 0, "Error: Insufficient blue coin to get red coin!");

        Wallets[msg.sender].numberOfBlueCoins -= 1;
        Wallets[msg.sender].numberOfRedCoins += 2;
    }

    // This function transfers blue coin from message sender colored wallet to receiver colored wallet
    function sendBlueCoin(uint256 _amount, address _receiver) public {
        require(Wallets[msg.sender].isCreated == true, "Error: You don`t have a colored wallet!");
        require(Wallets[_receiver].isCreated == true, "Error: Receiver address does not have a colored wallet!");
        require(Wallets[msg.sender].numberOfBlueCoins >= _amount, "Error: Insufficient blue coin for transfer!");

        Wallets[msg.sender].numberOfBlueCoins -= _amount;
        Wallets[_receiver].numberOfBlueCoins += _amount;
    }
}