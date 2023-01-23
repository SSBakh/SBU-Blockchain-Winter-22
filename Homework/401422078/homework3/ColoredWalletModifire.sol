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

/////////This function creates a colored wallet for the user
    function buildColoredWallet()public haveNotCreatedWallet() {
        ColoredWallet memory newColoredWallet = ColoredWallet(defaultValueForNumberOfRedCoins,defaultValueForNumberOfBlueCoins,true);
        addressToColoredWalletmapping[msg.sender]=newColoredWallet;
    }

    //This modifier checks that you have not created a wallet before
    modifier haveNotCreatedWallet() {
        require(!addressToColoredWalletmapping[msg.sender].created," You already have a colored wallet!!!");
        _;
    }

 /////////This function shows the status of the wallet
    function getColoredWallet() public view createdWallet() returns(ColoredWallet memory){
            return addressToColoredWalletmapping[msg.sender];
    }

    //This modifier checks that you have created a wallet
    modifier createdWallet() {
        require(addressToColoredWalletmapping[msg.sender].created,"you don't have colored wallet please build it!!!");
        _;
    }

 ////////This function converts the blue coins in the wallet into red coins
    function changingBlueToRed(uint256 numberOfBlueCoinsToChanging) public createdWallet(){
        ColoredWallet memory _collerdWallet = addressToColoredWalletmapping[msg.sender];
        require(_collerdWallet.numberOfBlueCoins>=numberOfBlueCoinsToChanging,"You don't have enough blue coins!!!");
        _collerdWallet.numberOfBlueCoins-=numberOfBlueCoinsToChanging;
        _collerdWallet.numberOfRedCoins+=(numberOfBlueCoinsToChanging*2);
        addressToColoredWalletmapping[msg.sender]=_collerdWallet;
    }

////////This function sends blue coins without accessing the destination wallet
    function transferBlueCoin(uint256 numerOfTransferBlueCoin , address destinationAddress) public createdWallet()
    destinationAndSenderAddressCheck(destinationAddress)
    destinationCreatedWallet(destinationAddress){
        ChangingValueOfBlueCoins(destinationAddress,msg.sender,numerOfTransferBlueCoin);
    }

    // this modifier Checks that the destination and sender addresses are not the same
    modifier destinationAndSenderAddressCheck(address _Address){
        require(_Address!=msg.sender,"You can't because the address of the destination and the sender are the same!!!");
        _;
    }

    //This modifier checks if the destination has a wallet or not
    modifier destinationCreatedWallet(address _Address) {
        require(addressToColoredWalletmapping[_Address].created,"there is no colored wallet in destination Address!!!");
        _;
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