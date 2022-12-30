// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ColoredWalletContract {
    struct ColoredWallet {
        uint256 numberOfRedCoins;
        uint256 numberOfBlueCoins;
        bool exists;
    }
    mapping (address => ColoredWallet) public addressToColoredWallet;

    function createColoredWallet() public {
        ColoredWallet memory newColoredWallet = ColoredWallet(0, 100, true);

        addressToColoredWallet[msg.sender] = newColoredWallet;
    }
    
    function burnBlueCoin() public{
        ColoredWallet memory userWallet = addressToColoredWallet[msg.sender];

        require(userWallet.exists, "You must first create a wallet");

        if (userWallet.numberOfBlueCoins > 1) {
            userWallet.numberOfBlueCoins = userWallet.numberOfBlueCoins - 1;
            userWallet.numberOfRedCoins = userWallet.numberOfRedCoins + 2;

            addressToColoredWallet[msg.sender] = userWallet;
        }
    }

    function sendCoin(address receiverAddress, uint256 redCoinCount, uint256 blueCoinCount) public {
        ColoredWallet memory receiverWallet = addressToColoredWallet[receiverAddress];
        ColoredWallet memory senderWallet = addressToColoredWallet[msg.sender];

        require(receiverWallet.exists, "This wallet does not exist");
        require(senderWallet.exists, "You must first create a wallet");
        require(senderWallet.numberOfRedCoins > redCoinCount && senderWallet.numberOfBlueCoins > blueCoinCount, "You don't have enough coin");
        senderWallet.numberOfRedCoins -= redCoinCount;
        senderWallet.numberOfBlueCoins -= blueCoinCount;

        receiverWallet.numberOfRedCoins += redCoinCount;
        receiverWallet.numberOfBlueCoins += blueCoinCount;

        addressToColoredWallet[receiverAddress] = receiverWallet;
        addressToColoredWallet[msg.sender] = senderWallet;
    }
}
 