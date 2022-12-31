// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract Wallet{
    struct ColoredWallet{
        uint256 NumberOfRedCoins;
        uint256 NumberOfBlueCoins;
        bool walletInitialized;
    }

    mapping(address => ColoredWallet) public AddressToWallet;

    

    modifier CheckWalletInitialization{
        // check if the wallet is already initialized
        require(!AddressToWallet[msg.sender].walletInitialized  , "Wallet has already initialized");
        _;
    }

    modifier CheckNumberOfBlueCoins(uint256 _NumberOfBlueCoins){
        // check if the wallet has enough blue coins for transaction
        require(AddressToWallet[msg.sender].NumberOfBlueCoins >_NumberOfBlueCoins , "Error, you don't have enough blue coins!");
        _;
    }

    modifier CheckWalletExistence(address _WalletAddress){
        // check if the user has initialied a wallet or not
        require(AddressToWallet[_WalletAddress].walletInitialized, "Error , No Wallet Exists");
        _;
    }

    modifier TransactionValidation(address _WalletAddress){
        // check if the user send coins to its own wallet ( addresses must be different)
        require( msg.sender != _WalletAddress ,"Error, you are not allowed !");
        _;
    }


    function initialize() public CheckWalletInitialization{
        // initialize a wallet : 0 :NumberOfRedCoins, 100:NumberOfBlueCoins
        ColoredWallet memory PersonColloredWallet = ColoredWallet(0,100,true);
        AddressToWallet[msg.sender] = PersonColloredWallet;

    }

    
    function ExchangeBlueToRed(uint256 _NumberOfBlueCoins) public
    CheckWalletExistence(msg.sender) 
    CheckNumberOfBlueCoins(_NumberOfBlueCoins){
        // Each wallet can burn _NumberOfBlueCoins and receive double of RedCoins,then update its wallet
        ColoredWallet memory PersonColloredWallet = AddressToWallet[msg.sender];
        PersonColloredWallet.NumberOfBlueCoins = PersonColloredWallet.NumberOfBlueCoins - _NumberOfBlueCoins ;
        PersonColloredWallet.NumberOfRedCoins = PersonColloredWallet.NumberOfRedCoins + _NumberOfBlueCoins * 2 ;
        AddressToWallet[msg.sender] = PersonColloredWallet;
    }

    function SendBlueCoins(uint256 _NumberOfBlueCoins , address _reciever) public 
    CheckWalletExistence(_reciever)
    CheckWalletExistence(msg.sender)
    CheckNumberOfBlueCoins(_NumberOfBlueCoins) 
    TransactionValidation(_reciever)  {
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