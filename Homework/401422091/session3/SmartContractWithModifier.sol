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

    function burnBlueCoin() public checkExistsWallet{
        ColoredWallet memory userWallet = addressToColoredWallet[msg.sender];

        if (userWallet.numberOfBlueCoins > 1) {
            userWallet.numberOfBlueCoins = userWallet.numberOfBlueCoins - 1;
            userWallet.numberOfRedCoins = userWallet.numberOfRedCoins + 2;

            addressToColoredWallet[msg.sender] = userWallet;
        }
    }

    modifier checkExistsWallet{
        require(addressToColoredWallet[msg.sender].exists, "You must first create a wallet");
        _;
    }

    function sendCoin(address receiverAddress, uint256 redCoinCount, uint256 blueCoinCount) public checkSafeTransaction(receiverAddress, redCoinCount, blueCoinCount){
        ColoredWallet memory receiverWallet = addressToColoredWallet[receiverAddress];
        ColoredWallet memory senderWallet = addressToColoredWallet[msg.sender];

        senderWallet.numberOfRedCoins -= redCoinCount;
        senderWallet.numberOfBlueCoins -= blueCoinCount;

        receiverWallet.numberOfRedCoins += redCoinCount;
        receiverWallet.numberOfBlueCoins += blueCoinCount;

        addressToColoredWallet[receiverAddress] = receiverWallet;
        addressToColoredWallet[msg.sender] = senderWallet;
    }

    modifier checkSafeTransaction(address receiverAddress, uint256 redCoinCount, uint256 blueCoinCount){
        require(addressToColoredWallet[receiverAddress].exists, "This wallet does not exist");
        require(addressToColoredWallet[msg.sender].exists, "You must first create a wallet");
        require(addressToColoredWallet[msg.sender].numberOfRedCoins > redCoinCount && addressToColoredWallet[msg.sender].numberOfBlueCoins > blueCoinCount, "You don't have enough coin");
        _;
    }
}
 