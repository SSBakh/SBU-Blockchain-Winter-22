// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract Wallet{
    struct ColoredWallet{
        uint256 NumberOfRedCoins;
        uint256 NumberOfBlueCoins;
        bool walletInitialized;
    }

    mapping(address => ColoredWallet) public AddressToWallet;

    function initialize() public {
        // initialize a wallet : 0 :NumberOfRedCoins, 100:NumberOfBlueCoins
        // But first :check if the wallet has already initialized
        require(!AddressToWallet[msg.sender].walletInitialized  , "Wallet has already initialized");

        ColoredWallet memory PersonColloredWallet = ColoredWallet(0,100,true);
        AddressToWallet[msg.sender] = PersonColloredWallet;

    }

    
    function ExchangeBlueToRed(uint256 _NumberOfBlueCoins) public {
        // Each wallet can burn _NumberOfBlueCoins and receive double of RedCoins,then update its wallet
        // check if the user has initialied a wallet or not
        require(AddressToWallet[msg.sender].walletInitialized, "Error , No Wallet Exists");
        // check if the wallet has enough blue coins for transaction
        require(AddressToWallet[msg.sender].NumberOfBlueCoins >_NumberOfBlueCoins , "Error, you don't have enough blue coins!");


        ColoredWallet memory PersonColloredWallet = AddressToWallet[msg.sender];
        PersonColloredWallet.NumberOfBlueCoins = PersonColloredWallet.NumberOfBlueCoins - _NumberOfBlueCoins ;
        PersonColloredWallet.NumberOfRedCoins = PersonColloredWallet.NumberOfRedCoins + _NumberOfBlueCoins * 2 ;
        AddressToWallet[msg.sender] = PersonColloredWallet;
    }


    function SendBlueCoins(uint256 _NumberOfBlueCoins , address _reciever) public {
        // check if the user has initialied a wallet or not
        require(AddressToWallet[msg.sender].walletInitialized, "Error , No Wallet Exists");
        require(AddressToWallet[_reciever].walletInitialized, "Error , No Wallet Exists");
        // check if the wallet has enough blue coins for transaction
        require(AddressToWallet[msg.sender].NumberOfBlueCoins >_NumberOfBlueCoins , "Error, you don't have enough blue coins!");
        // check if the user sends coins to its own wallet ( addresses must be different)
        require( msg.sender != _reciever ,"Error, you are not allowed !");

        
        // intialize a wallet for sender, send _NumberOfBlueCoins from its address, update its wallet.
        ColoredWallet memory SenderColloredWallet = AddressToWallet[msg.sender];
        SenderColloredWallet.NumberOfBlueCoins -= _NumberOfBlueCoins;
        AddressToWallet[msg.sender] = SenderColloredWallet;
        // intialize a wallet for receiver, receive  _NumberOfBlueCoins, update its wallet.
        ColoredWallet memory RecieverColloredWallet = AddressToWallet[_reciever];
        RecieverColloredWallet.NumberOfBlueCoins += _NumberOfBlueCoins;
        AddressToWallet[_reciever] = RecieverColloredWallet;
    }
}