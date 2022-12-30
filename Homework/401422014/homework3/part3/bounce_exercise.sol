// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract secondExercise {

    //It would be better if we can add personAddress variable to this struct but because of question instruction , we prevent this.
    struct ColoredWallet {
        uint256 numberOfRedCoins;
        uint256 numberOfBlueCoins;
    }

    //We create this mapping because we want to access users coloredWallet with their address.
    mapping(address => ColoredWallet) usersWallet;
    
    //We have to create this mapping because we want to prevent from creating wallet with existing address. (This mapping is unnecessary if we were allowed to add personAddress variable to ColoredWidget struct.)
    mapping(address => bool) isColoredWalletExists;

    
    
    modifier checkColoredWlletisExist (address _walletAddress) {
        require(isColoredWalletExists[_walletAddress] == false,"Wallet with this address already exists.");
        _;
    }

    modifier checkColoredWlletisNotExist (address _walletAddress) {
        string memory message = "";
        if(_walletAddress == msg.sender){
            message = "You first need to create a ColoredWallet !";
        }else{
            message = "Destination address does not have a ColoredWallet";
        }
        require(isColoredWalletExists[_walletAddress] == true,message);
        _;
    }

    modifier checkWalletBlucCoinBalance (uint256 _amount) {
        require(usersWallet[msg.sender].numberOfBlueCoins >= _amount,"Your blue coins is not enough to do this operation !");
        _;
    }

    //Create colored wallet
    function createColoredWallet () public checkColoredWlletisExist(msg.sender){
        ColoredWallet memory coloredWallet = ColoredWallet(0,100);
        usersWallet[msg.sender] = coloredWallet;
        isColoredWalletExists[msg.sender] = true;
    }

    function getWalletNumberOfRedCoins() public view checkColoredWlletisNotExist(msg.sender) returns(uint256){
        
        return usersWallet[msg.sender].numberOfRedCoins;
    }

    function getWalletNumberOfBlueCoins() public view checkColoredWlletisNotExist(msg.sender) returns(uint256){
    
        return usersWallet[msg.sender].numberOfBlueCoins;
    }

    //Convert 1 blue coin to 2 red coin
    function convertBlueCoinToRedCoin() public checkColoredWlletisNotExist(msg.sender) checkWalletBlucCoinBalance(0){
    
        usersWallet[msg.sender].numberOfBlueCoins -= 1;
        usersWallet[msg.sender].numberOfRedCoins += 2;
    }

    function sendBlueCoinToOthers(uint256 _sendingAmount , address _destinationWallet) public checkColoredWlletisNotExist(msg.sender) checkColoredWlletisNotExist(_destinationWallet) checkWalletBlucCoinBalance(_sendingAmount){
    
        usersWallet[msg.sender].numberOfBlueCoins -= _sendingAmount;
        usersWallet[_destinationWallet].numberOfBlueCoins += _sendingAmount;
    }


}