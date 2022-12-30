//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Sepehr{

    struct ColoredWallet{
        uint256 numberOfRedCoins ;
        uint256 numberOfBlueCoins;
    }

    // store user's address
    address public owner;
    // store user's wallet
    ColoredWallet public ownerWallet ;
    // used to store wallets
    mapping(address => ColoredWallet) public addressToWallet ;

    // this method will create wallet for owner
    function createColoredWallet() public  {
        ownerWallet = ColoredWallet(0,200);
        owner = msg.sender;
        addressToWallet[msg.sender] = ownerWallet ;
    }

    // this method will create wallet for others with their address
    function createColoredWalletForOthers(address _address) public  {
        ColoredWallet memory temp = ColoredWallet(0,200);
        addressToWallet[_address] = temp ;
    }

    // remove blue coins
    function removeBlueCoin() public {
        if(ownerWallet.numberOfBlueCoins > 0){
            ownerWallet.numberOfRedCoins = ownerWallet.numberOfRedCoins + 2;
            ownerWallet.numberOfBlueCoins = ownerWallet.numberOfBlueCoins - 1;
        }
        addressToWallet[msg.sender] = ownerWallet ;
    }

    // remove blue coins for others(implemented with require instead of if)
    function removeBlueCoinForOthers(address _address) public {
        ColoredWallet memory temp = addressToWallet[_address];
        require(temp.numberOfBlueCoins > 0,"not enough blue coins");
        temp.numberOfRedCoins = temp.numberOfRedCoins + 2;
        temp.numberOfBlueCoins = temp.numberOfBlueCoins - 1;
        addressToWallet[_address] = temp ;
    }
    

    // send blue coin to another address
    function sendBlueCoin(address _address, uint256 _blue) public  {

        ColoredWallet memory userWallet = addressToWallet[owner];
        require(userWallet.numberOfBlueCoins > _blue,"not enough blue cloins");

        ColoredWallet memory destinationWallet = addressToWallet[_address];
        require(destinationWallet.numberOfBlueCoins >= 0,"no wallet for this address");
        
        
        userWallet.numberOfBlueCoins = (userWallet.numberOfBlueCoins - _blue);
        addressToWallet[msg.sender] = userWallet ;

        
        destinationWallet.numberOfBlueCoins = destinationWallet.numberOfBlueCoins + _blue ;
        addressToWallet[_address] = destinationWallet;
    }


    

}
