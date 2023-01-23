// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;


contract smartContract {

    struct ColoredWallet {
        uint256 numberOfRedCoins; 
        uint256 numberOfBlueCoins;
        bool existance;
    }

    mapping(address => ColoredWallet) private addressToWallet;

    modifier checkWalletExistance {
        require(!addressToWallet[msg.sender].existance, "You already have signed up.");
        _;
    }

    modifier checkNumberOfBlueCoins(uint256 _numberOfBlueCoins) {
        require(_numberOfBlueCoins < addressToWallet[msg.sender].numberOfBlueCoins, "Error! Insufficient amount of Blue Coins.");
        _;
    }

    modifier checkAddressValidity(address receiverAddress){
         require(!addressToWallet[receiverAddress].existance, "The address specified is invalid.");
        _;
    }

    function createWallet() public checkWalletExistance {
        ColoredWallet memory wallet = ColoredWallet(0, 100, true);
        addressToWallet[msg.sender] = wallet;
    }

    function exchangeOneBlueCoinWithRedCoins() public {
        ColoredWallet memory wallet = addressToWallet[msg.sender];
        if (wallet.numberOfBlueCoins > 1) {
            wallet.numberOfBlueCoins = wallet.numberOfBlueCoins - 1;
            wallet.numberOfRedCoins = wallet.numberOfRedCoins + 2;
            addressToWallet[msg.sender] = wallet;
        }
    }

    function sendBlueCoins (uint256 _numberOfBlueCoins, address receiverAddress) public checkNumberOfBlueCoins(_numberOfBlueCoins) checkAddressValidity(receiverAddress){
        ColoredWallet memory wallet = addressToWallet[msg.sender];
        ColoredWallet memory receiver = addressToWallet[receiverAddress];
        wallet.numberOfBlueCoins = wallet.numberOfBlueCoins - _numberOfBlueCoins;
        addressToWallet[msg.sender] = wallet;
        receiver.numberOfBlueCoins = receiver.numberOfBlueCoins + _numberOfBlueCoins;
        addressToWallet[receiverAddress] = receiver;
    }
}
