// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract MyColoredContract {

    struct ColoredWallet{
        uint256 numberOfRedCoins;
        uint256 numberOfBlueCoins;
    }

    mapping(address => ColoredWallet) addressToWalletMapping;
    mapping(address => bool) registeredAddresses;

    function createColoredWallet() public {
        require(!registeredAddresses[msg.sender], "Error: You have allredy created your wallet!");
        ColoredWallet memory cw = ColoredWallet(0, 100);
        addressToWalletMapping[msg.sender] = cw;
        registeredAddresses[msg.sender] = true;
    }

    function getNumberOfRedCoins() public view returns(uint256) {
        require(registeredAddresses[msg.sender], "Error: You must create wallet first!");
        return addressToWalletMapping[msg.sender].numberOfRedCoins;
    }

    function getNumberOfBlueCoins() public view returns(uint256) {
        require(registeredAddresses[msg.sender], "Error: You must create wallet first!");
        return addressToWalletMapping[msg.sender].numberOfBlueCoins;
    }

    function convertBlueCoinToRedCoin() public {
        require(registeredAddresses[msg.sender], "Error: You must create wallet first!");
        ColoredWallet memory cw = addressToWalletMapping[msg.sender];
        require(cw.numberOfBlueCoins > 0, "Error: You don't have enough blue coins!!!");
        cw.numberOfBlueCoins = cw.numberOfBlueCoins - 1;
        cw.numberOfRedCoins = cw.numberOfRedCoins + 2;
        addressToWalletMapping[msg.sender] = cw;
    }

    function sendBlueCoinToAnotherWallet(address _anotherWallet) public {
        require(_anotherWallet != msg.sender, "Error: You cann't send coin to yourself!!!");

        require(registeredAddresses[msg.sender], "Error: You must create wallet first!");
        require(registeredAddresses[_anotherWallet], "Error: Another wallet dosn't exists!");

        ColoredWallet memory cw = addressToWalletMapping[msg.sender];
        require(cw.numberOfBlueCoins > 0, "Error: You don't have enough blue coins!!!");

        ColoredWallet memory anotherCw = addressToWalletMapping[_anotherWallet];
        cw.numberOfBlueCoins = cw.numberOfBlueCoins - 1;
        anotherCw.numberOfBlueCoins = anotherCw.numberOfBlueCoins + 1;
        addressToWalletMapping[msg.sender] = cw;
        addressToWalletMapping[_anotherWallet] = anotherCw;
    }

}
