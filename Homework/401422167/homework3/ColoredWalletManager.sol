// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract ColoredWalletManager {
    // aleph
    struct ColoredWallet {
        uint256 numberOfRedCoins;
        uint256 numberOfBlueCoins;
    }

    mapping(address => ColoredWallet) wallets;
    mapping(address => bool) walletExists;

    // be
    function createWallet() public {
        require(!walletExists[msg.sender], "A wallet with this address already exists.");
        walletExists[msg.sender] = true;
        wallets[msg.sender] = ColoredWallet(0, 100);
    }

    function getWallet() public view walletMustExist returns(ColoredWallet memory) {
        return wallets[msg.sender];
    }

    // pe
    function exchangeBlueCoinWithRedCoin() public walletMustExist {
        require(wallets[msg.sender].numberOfBlueCoins >= 1, "You need to have at least one blue coin to call this function.");
        wallets[msg.sender].numberOfBlueCoins -= 1;
        wallets[msg.sender].numberOfRedCoins += 2;
    }

    // te
    function sendBlueCoin(uint256 amount, address destination) public walletMustExist {
        require(walletExists[destination], "No wallet with destination address exists, ask them to call createWallet function to create one.");
        require(wallets[msg.sender].numberOfBlueCoins >= amount, "Insufficient Funds.");
        wallets[msg.sender].numberOfBlueCoins -= amount;
        wallets[destination].numberOfBlueCoins += amount;
    }

    // bonus
    modifier walletMustExist() {
        require(walletExists[msg.sender], "No wallet with this address exists, call createWallet function to create one.");
        _;
    }
}