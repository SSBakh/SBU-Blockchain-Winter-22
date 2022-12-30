//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ColoredWalletContract{
    // we are create struct of colored wallet
    struct ColoredWallet{
        uint256 numberOfRedCoins;
        uint256 numberOfBlueCoins;
        bool created;
    }

    //We determine the initial amount of coins
    uint256 defaultValueForNumberOfRedCoins = 0 ;
    uint256 defaultValueForNumberOfBlueCoins = 100 ;

    //To keep the wallets, we map them
    mapping(address=>ColoredWallet) addressToColoredWalletmapping;

    //This function creates a colored wallet for the user
    function buildColoredWallet()public{
        require(!addressToColoredWalletmapping[msg.sender].created," You already have a colored wallet!!!");
        ColoredWallet memory newColoredWallet = ColoredWallet(defaultValueForNumberOfRedCoins,defaultValueForNumberOfBlueCoins,true);
        addressToColoredWalletmapping[msg.sender]=newColoredWallet;
    }

    //This function shows the status of the wallet
    function getColoredWallet() public view returns(ColoredWallet memory){
        require(addressToColoredWalletmapping[msg.sender].created,"you don't have colored wallet please build it!!!");
        return addressToColoredWalletmapping[msg.sender];
    }

    //This function converts the blue coins in the wallet into red coins
    function changingBlueToRed(uint256 numberOfBlueCoinsToChanging) public{
        require(addressToColoredWalletmapping[msg.sender].created,"you don't have colored wallet please build it!!!");
        ColoredWallet memory _collerdWallet = addressToColoredWalletmapping[msg.sender];
        require(_collerdWallet.numberOfBlueCoins>=numberOfBlueCoinsToChanging,"You don't have enough blue coins!!!");
        _collerdWallet.numberOfBlueCoins-=numberOfBlueCoinsToChanging;
        _collerdWallet.numberOfRedCoins+=(numberOfBlueCoinsToChanging*2);
        addressToColoredWalletmapping[msg.sender]=_collerdWallet;
    }

    //This function sends blue coins without accessing the destination wallet
    function transferBlueCoin(uint256 numerOfTransferBlueCoin , address destinationAddress)public{
        require(addressToColoredWalletmapping[msg.sender].created,"you don't have colored wallet please build it!!!");
        require(destinationAddress!=msg.sender,"You can't because the address of the destination and the sender are the same!!!");
        chekingWallet(destinationAddress);
        ChangingValueOfBlueCoins(destinationAddress,msg.sender,numerOfTransferBlueCoin);
    }
    //This function checks if the destination has a wallet or not
    function chekingWallet(address _address)private view{
        require(addressToColoredWalletmapping[_address].created,"there is no colored wallet in destination Address!!!");
    }

    //This function changes the value of blue coins in the destination and sender wallet without external user access
    function ChangingValueOfBlueCoins(address _destination,address sender, uint256 _numerOfTransferBlueCoin)private{
       ColoredWallet memory _collerdWalletSender = addressToColoredWalletmapping[sender];
       ColoredWallet memory _collerdWalletDestination = addressToColoredWalletmapping[_destination];
        require(_collerdWalletSender.numberOfBlueCoins>=_numerOfTransferBlueCoin,"You don't have enough blue coins!!!"); 
       _collerdWalletSender.numberOfBlueCoins-=_numerOfTransferBlueCoin;
       _collerdWalletDestination.numberOfBlueCoins+=_numerOfTransferBlueCoin;
       addressToColoredWalletmapping[sender]=_collerdWalletSender;
       addressToColoredWalletmapping[_destination]=_collerdWalletDestination;
    }
}