//SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract ColoredCoins {

    //create struct of Colored Wallet
    struct ColoredWallet {
        uint256 numberOfRedCoins;
        uint256 numberOfBlueCoins;
        bool Initialized;
    }


    //saving ColoredWallets in Mapping
    mapping (address => ColoredWallet) public AddressToColoredWalletMapping;

    //checking existence of wallet
    modifier NoWalletExists(address _Address){
        string memory Message = string("Error : There is no Colored Wallet with this Address");
        require(AddressToColoredWalletMapping[_Address].Initialized , Message );
        _;
    }

    modifier WalletExists(address _Address){
        string memory Message = string("Error : Colored Wallet has already been Initialized");
        require(!AddressToColoredWalletMapping[_Address].Initialized , Message );
        _;
    }

    // Initializing
    function Init() public WalletExists(msg.sender) {
        ColoredWallet memory CW = ColoredWallet(0,100,true);
        AddressToColoredWalletMapping[msg.sender] = CW;
    }

    //Checking the Burning condition
    modifier Validator(uint256 _amount) {
        require(_amount <= AddressToColoredWalletMapping[msg.sender].numberOfBlueCoins, "Error : not enough blue coins in the wallet");
        _;
    }


    //Burn
     function Burn(uint256 _amount) public NoWalletExists(msg.sender) Validator(_amount) {
        ColoredWallet memory wallet = AddressToColoredWalletMapping[msg.sender];
        wallet.numberOfBlueCoins = wallet.numberOfBlueCoins - _amount;
        wallet.numberOfRedCoins = wallet.numberOfRedCoins + (_amount * 2);
        AddressToColoredWalletMapping[msg.sender] = wallet;
    }

    
    //transfer blue coins
    function Transfer(uint256 _amount, address _destination) public
        NoWalletExists(msg.sender) NoWalletExists(_destination) Validator(_amount) {

        ColoredWallet memory Sender =  AddressToColoredWalletMapping[msg.sender];
        ColoredWallet memory Receiver =  AddressToColoredWalletMapping[_destination];

        Sender.numberOfBlueCoins = Sender.numberOfBlueCoins- _amount;
        AddressToColoredWalletMapping[msg.sender] = Sender;

        Receiver.numberOfBlueCoins = Receiver.numberOfBlueCoins + _amount;
        AddressToColoredWalletMapping[_destination] = Receiver;
    }
// Mojtaba Alehosseini , st# 401422018, 12/30/2022
}
