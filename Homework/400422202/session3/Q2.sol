// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract Session3B {

    struct ColoredWallet {
        uint256 numberOfRedCoins;
        uint256 numberOfBlueCoins;
        address ownerAddress;
        bool isExist; 
    }

    ColoredWallet[] public walletArray;

    mapping(address => ColoredWallet) public addressToWallet;

    function createdWallet() public {
        // check wallet is not duplicate
        require(!addressToWallet[msg.sender].isExist, "the address exist yet");

        ColoredWallet memory newWallet = ColoredWallet(0, 100, msg.sender, true);
        addressToWallet[msg.sender] = newWallet;
        walletArray.push(newWallet);
    }

    function burnOneBlueGetTwoRedCoin() public {
        ColoredWallet memory wallet = addressToWallet[msg.sender];

        // check blue coin balance
        require(wallet.numberOfBlueCoins >= 1, "The blue coin is insufficient");

        // update wallets
        wallet.numberOfRedCoins += 2;
        wallet.numberOfBlueCoins -= 1;
        addressToWallet[msg.sender] = wallet;
    }

    function transferBlueCoin(uint256 amount, address _receiverAddress) public {

        ColoredWallet memory wallet = addressToWallet[msg.sender];
        ColoredWallet memory receiverWallet = addressToWallet[_receiverAddress];

        // check wallet exist
        require(wallet.isExist, "the address is not found");
        // check blue coin balance
        require(wallet.numberOfBlueCoins >= amount, "The blue coin is insufficient");

        // transfer blue coin
        wallet.numberOfBlueCoins -= amount;
        receiverWallet.numberOfBlueCoins += amount;

        // update wallets
        addressToWallet[msg.sender] = wallet;
        addressToWallet[_receiverAddress] = receiverWallet;
    }   


}