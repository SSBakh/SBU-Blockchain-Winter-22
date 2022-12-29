//SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract ColoredWalletSmartContract{

    //create struct of colored wallet
    struct ColoredWallet{
        uint256 numberOfRedCoins;
        uint256 numberOfBlueCoins;
        bool hasValue;
    }

    //saving coloredWallets in mappig
    mapping(address => ColoredWallet) addressToColoredWallet;

    //get info about the user colored wallet
    function getMyWallet() public view returns(ColoredWallet memory){
        DoesNotExistWallet( msg.sender , "your" );
        return addressToColoredWallet[msg.sender];
    }

    //this function create colored wallet for user
    function createWallet() public {
        existWallet( msg.sender , "your" );
        ColoredWallet memory coloredWallet = ColoredWallet(0 , 100 , true );
        addressToColoredWallet[msg.sender] = coloredWallet;
    }

    //this function change the blue coin to red coin
    function changeBlueToRed(uint256 amountOfChanging) public {
        DoesNotExistWallet( msg.sender , "your");
        sufficientNumber(msg.sender , amountOfChanging ,"change to red coins...");
        addressToColoredWallet[msg.sender].numberOfBlueCoins -= amountOfChanging;
        addressToColoredWallet[msg.sender].numberOfRedCoins += (amountOfChanging * 2);
    }

    //this function send blue coin to another user
    function sendBlueCoin(uint256 amountOfSending,address receiverAddress) public {
        DoesNotExistWallet( msg.sender , "your");
        checkAddresses(msg.sender , receiverAddress);
        sufficientNumber(msg.sender , amountOfSending,"send...");
        DoesNotExistWallet( receiverAddress , "the reciver");
        transfer(msg.sender,receiverAddress,amountOfSending);
    }

    //This function checks the existence of the colored wallet
    function existWallet(address _Address , string memory nameOfAddress ) private view {
        string memory errorMessage = string.concat(
            "Error : There is a colored wallet in " , nameOfAddress , " address, you cannot create it again...");
        require( !addressToColoredWallet[_Address].hasValue , errorMessage );
    }

    //This function checks if the colored wallet does not exist
    function DoesNotExistWallet(address _Address,string memory nameOfAddress) private view{
        string memory errorMessage = string.concat(
            "Error : There is no colored wallet in " , nameOfAddress , " address...");
        require( addressToColoredWallet[_Address].hasValue , errorMessage );
    }

    //This function checks that we have enough blue coins for the tasks we want to do
    function sufficientNumber(address _Address , uint256 _amountOfChanging, string memory Complementary) private view {
        require(_amountOfChanging > 0 , "Error : You cannot choose zero number of coins");
        string memory errorMessage=string.concat("Error : You don't have enough blue coins to ",Complementary);
        require(addressToColoredWallet[_Address].numberOfBlueCoins >= _amountOfChanging,errorMessage);
    }

    //This function checks that the sender and receiver addresses are not the same
    function checkAddresses (address firstAddress , address secondAddress) private pure{
        require(firstAddress != secondAddress,"Error : You cannot choose the same address as your own...");
    }

    //This function privately changes the values of blue coins in receiver and sender
    function transfer (address userAdress,address receiverAddress,uint256 _amountOfSending) private{
        addressToColoredWallet[userAdress].numberOfBlueCoins -= _amountOfSending;
        addressToColoredWallet[receiverAddress].numberOfBlueCoins += _amountOfSending;
    }

}