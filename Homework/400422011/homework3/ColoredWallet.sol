//SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;


contract ColoredCoins {
    //create struct
    struct ColoredWallet {
        uint256 numberOfRedCoins;
        uint256 numberOfBlueCoins;
        bool Initialized;
    }


    //we map the wallets to keep them
     mapping (address => ColoredWallet) public AddressToColoredWalletMapping;


    //checking this Address has a wallet or not 
    modifier NoWalletExists(address _Address){
        string memory Message = string("Error : There is no Colored Wallet with this Address");
        require(!AddressToColoredWalletMapping [_Address].Initialized , Message );
        _;
    }

    modifier WalletExists(address _Address){
        string memory Message = string("Error : your Wallet has already been Initialized!!");
        require(!AddressToColoredWalletMapping[_Address].Initialized , Message );
        _;
    }


    function init() public WalletExists(msg.sender) {
        ColoredWallet memory coloredWallet = ColoredWallet(0,100, true);
        AddressToColoredWalletMapping[msg.sender] = coloredWallet;
    }


    modifier Validator(uint256 blueCoin) {
        require(blueCoin <= AddressToColoredWalletMapping[msg.sender].numberOfBlueCoins, "Error : You don't have enough blue conis!!");
        _;
    }

      function convertBlueToReds(uint256 _numberOfBlueCoins) public checkMinimumBlueCoin(_numberOfBlueCoins) {
        ColoredWallet memory wallet =  AddressToColoredWalletMapping[msg.sender];
        wallet.numberOfBlueCoins = wallet.numberOfBlueCoins - _numberOfBlueCoins;
        wallet.numberOfRedCoins = wallet.numberOfRedCoins + _numberOfBlueCoins * 2;
        AddressToColoredWalletMapping[msg.sender] = wallet;
    }

     modifier checkMinimumBlueCoin(uint blueCoin){
        require(blueCoin < AddressToColoredWalletMapping[msg.sender].numberOfBlueCoins , "You don't have enough blue conis!");
        _;
    }


        //transfer blue coins
        function transfer(uint256 _numberOfBlueCoins, address receiver)
        public checkMinimumBlueCoin(_numberOfBlueCoins) checkReceive(receiver) checkReceiverWallet(receiver) {
        ColoredWallet memory wallet = AddressToColoredWalletMapping[msg.sender];
        wallet.numberOfBlueCoins = wallet.numberOfBlueCoins - _numberOfBlueCoins;
        AddressToColoredWalletMapping[msg.sender] = wallet;
        ColoredWallet memory receiverWallet = AddressToColoredWalletMapping[receiver];
        receiverWallet.numberOfBlueCoins =
            receiverWallet.numberOfBlueCoins +
            _numberOfBlueCoins;
        AddressToColoredWalletMapping[receiver] = receiverWallet;
    }

    modifier checkReceive(address receiver) {
        require(
            !AddressToColoredWalletMapping[receiver].Initialized,"Receiver does not have wallet!" );
        _;
    }

    modifier checkReceiverWallet(address receiver) {
        require(
            msg.sender != receiver,
            "Sender and receiver have the same address!");
        _;
    }
   
}

