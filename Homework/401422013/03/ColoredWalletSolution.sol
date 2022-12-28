// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract ColoredWalletSolution {

    struct ColoredWallet {
        uint256 numberOfRedCoins;
        uint256 numberOfBlueCoins;
        bool isExists;
    }

    mapping(address => ColoredWallet) public addressToColoredWalletMapping;


    modifier isWalletExists(address _walletAddress) {
        ColoredWallet memory coloredWallet = addressToColoredWalletMapping[_walletAddress];
        require(coloredWallet.isExists, "Wallet doesn't exists.");

        _;
    }

    modifier burnCoinValidator() {
        uint256 numberOfBlueCoins = addressToColoredWalletMapping[msg.sender].numberOfBlueCoins;
        require(numberOfBlueCoins > 1, "You don't have enough blue coins.");

        _;
    }

    modifier transferBlueCoinValidator(uint256 _amount, address _destinationAddress) {
        require(msg.sender != _destinationAddress, "Destination Wallet Address must be different from Source.");

        ColoredWallet memory srcColoredWallet = addressToColoredWalletMapping[msg.sender];
        require(srcColoredWallet.numberOfBlueCoins >= _amount, "You don't have enough blue coins.");

        _;
    }


    function createColoredWallet() public {
        ColoredWallet memory coloredWallet = ColoredWallet(0, 100, true);
        addressToColoredWalletMapping[msg.sender] = coloredWallet;
    }

    function burnCoin() public isWalletExists(msg.sender) burnCoinValidator {
        ColoredWallet memory coloredWallet = addressToColoredWalletMapping[msg.sender];
        coloredWallet.numberOfBlueCoins -= 1;
        coloredWallet.numberOfRedCoins += 2;

        addressToColoredWalletMapping[msg.sender] = coloredWallet;
    }

    function transferBlueCoin(uint256 _amount, address _destinationAddress) public
        isWalletExists(msg.sender)
        isWalletExists(_destinationAddress)
        transferBlueCoinValidator(_amount, _destinationAddress) {
        ColoredWallet memory srcColoredWallet = addressToColoredWalletMapping[msg.sender];
        ColoredWallet memory destColoredWallet = addressToColoredWalletMapping[_destinationAddress];

        srcColoredWallet.numberOfBlueCoins -= _amount;
        destColoredWallet.numberOfBlueCoins += _amount;

        addressToColoredWalletMapping[msg.sender] = srcColoredWallet;
        addressToColoredWalletMapping[_destinationAddress] = destColoredWallet;
    }

}