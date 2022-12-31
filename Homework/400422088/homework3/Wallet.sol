// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;


contract Wallet{

    struct ColoredWallet {
    uint256 numberOfRedCoins;
    uint256 numberOfBlueCoins;
    bool exit;
    }


    mapping(address => ColoredWallet) addressToWallet;

    function createWallet() public {
        ColoredWallet memory wallet = addressToWallet[msg.sender];
        require(wallet.exit == false, "Error: You have wallet");
        addressToWallet[msg.sender] = ColoredWallet(0, 100, true);
    }

    function checkWalletBalance() view public returns(ColoredWallet memory){
        ColoredWallet memory wallet = addressToWallet[msg.sender];
        require(wallet.exit == true, "Error: You don't have wallet");
        return(wallet);
    }

    function burnMint() public{
        ColoredWallet memory wallet = checkWalletBalance();
        require(wallet.numberOfBlueCoins > 0, "Error: You don't have enough BlueCoin");
        wallet.numberOfBlueCoins -= 1;
        wallet.numberOfRedCoins  += 2;
        addressToWallet[msg.sender] = wallet;
    }

    function transferBlueCoin(address _address, uint256 _numberOfBlueCoin) public payable{
        ColoredWallet memory senderWallet = checkWalletBalance();
        require(senderWallet.numberOfBlueCoins >= _numberOfBlueCoin, "Error: You don't have enough BlueCoin");
        require(_address != msg.sender, "Error; Same address");
        ColoredWallet memory reciverWallet = addressToWallet[_address];
        require(reciverWallet.exit == true, "Error: That account doesn't have wallet");
        senderWallet.numberOfBlueCoins -= _numberOfBlueCoin;
        addressToWallet[msg.sender] = senderWallet;
        reciverWallet.numberOfBlueCoins += _numberOfBlueCoin;
        addressToWallet[_address] = reciverWallet;
}

}

