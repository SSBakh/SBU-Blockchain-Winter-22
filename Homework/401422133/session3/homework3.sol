// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract ProjectContract {


    struct ColoredWallet {
        uint256 numberOfRedCoins;
        uint256 numberOfBlueCoins;
        bool condition;
    }


    mapping (address => ColoredWallet) public WalletDictionary;


    modifier SenderHasNotClaimed {
        require(WalletDictionary[msg.sender].condition != true, "Sender has the coins");
        _;
    }


    function Receive() public SenderHasNotClaimed {
        ColoredWallet memory TheWallet  = ColoredWallet(0,100,true);
        WalletDictionary[msg.sender] = TheWallet;
    }


    modifier EnoughBlueCoins(uint256 Amount) {
        require(WalletDictionary[msg.sender].numberOfBlueCoins > Amount, "Doesn't have enough BlueCoins");
        _;
    }

    function BlueToRed(uint256 Amount) public  EnoughBlueCoins(Amount) {
        ColoredWallet memory TheWallet =  WalletDictionary[msg.sender];
        TheWallet.numberOfBlueCoins = TheWallet.numberOfBlueCoins - Amount;
        TheWallet.numberOfRedCoins = TheWallet.numberOfRedCoins +  2 * Amount;
        WalletDictionary[msg.sender] = TheWallet;
    }


    modifier ReceiverClaimed(address Receiver) {
        require(WalletDictionary[Receiver].condition == true, "Receiver hasn't claimed");
        _;
    }

    modifier SenderAndReceiverAreNotSame(address Receiver) {
        require(Receiver != msg.sender, "Sender and receiver are same");
        _;

    }


    function Transfer(uint256 Amount, address Receiver) public  ReceiverClaimed(Receiver)  SenderAndReceiverAreNotSame(Receiver)  {
        ColoredWallet memory SenderWallet =  WalletDictionary[msg.sender];
        ColoredWallet memory ReceiverWallet =  WalletDictionary[Receiver];

        SenderWallet.numberOfBlueCoins = SenderWallet.numberOfBlueCoins - Amount;
        WalletDictionary[msg.sender] = SenderWallet;

        ReceiverWallet.numberOfBlueCoins = ReceiverWallet.numberOfBlueCoins + Amount;
        WalletDictionary[Receiver] = ReceiverWallet;
    }

    }


    