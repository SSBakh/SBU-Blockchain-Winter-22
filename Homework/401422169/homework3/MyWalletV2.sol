// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract MyWallet{
    struct ColoredWallet{
        uint256 numberOfRedCoins;
        uint256 numberOfBlueCoins;
        bool isCreated;
    }

    // Modifier functions
    modifier WalletAlreadyExists(address _address){
        require(!Wallets[_address].isCreated , "Error: This address already has a colored wallet!");
        _;
    }

    modifier WalletNotFound(address _address){
        require(Wallets[_address].isCreated, "Error: This address does not have a colored wallet!");
        _;
    }

    modifier InsufficientBlueCoin(address _address, uint256 _amount){
        require(Wallets[_address].numberOfBlueCoins > _amount, "Error: Insufficient blue coin!");
        _;
    }

    // Mapping to get colored wallet from address(A structure to store wallets too!)
    mapping (address => ColoredWallet) public Wallets;

    // This function creates a colored wallet for message sender
    function createColoredWallet() public WalletAlreadyExists(msg.sender) {
        ColoredWallet memory wallet = ColoredWallet(0, 100, true);
        Wallets[msg.sender] = wallet;
    }

    // This function burns blue coin of message sender to get red coin 
    function burnBlueCoinToGetRedCoin() public WalletNotFound(msg.sender) InsufficientBlueCoin(msg.sender, 0){
        Wallets[msg.sender].numberOfBlueCoins -= 1;
        Wallets[msg.sender].numberOfRedCoins += 2;
    }

    // This function transfers blue coin from message sender colored wallet to receiver colored wallet
    function sendBlueCoin(uint256 _amount, address _receiver) public WalletNotFound(msg.sender) WalletNotFound(_receiver) InsufficientBlueCoin(msg.sender, _amount){
        Wallets[msg.sender].numberOfBlueCoins -= _amount;
        Wallets[_receiver].numberOfBlueCoins += _amount;
    }
}