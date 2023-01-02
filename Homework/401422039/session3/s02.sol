//SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract Coins{
    struct ColoredWallet{
        uint256 numberOfBlueCoins;  
        uint256 numberOfRedCoins;  
        address Person_address;        
    }
    mapping (address=>ColoredWallet)  Wallets; 
    function CreateWallet() public returns(ColoredWallet memory){
        require(Wallets[msg.sender].Person_address==0x0000000000000000000000000000000000000000,"you have already account!");
        ColoredWallet memory new_wallet=ColoredWallet(100,0,msg.sender);
        Wallets[msg.sender]=new_wallet;
        return new_wallet;
    }
    function convert_blue_to_red() public returns(ColoredWallet memory){
        require(Wallets[msg.sender].Person_address!=0x0000000000000000000000000000000000000000,"you have not  account!");
        require(Wallets[msg.sender].numberOfBlueCoins>0,"you have not Blue Coins  account!");
        Wallets[msg.sender].numberOfBlueCoins= Wallets[msg.sender].numberOfBlueCoins-1;
        Wallets[msg.sender].numberOfRedCoins= Wallets[msg.sender].numberOfRedCoins+2;
        return  Wallets[msg.sender];
        
    }
    function send_blue_coin(address wallet,uint256 _numberOfBlueCoins) public returns(ColoredWallet memory){
        require(Wallets[msg.sender].Person_address!=0x0000000000000000000000000000000000000000,"you have not  account!");

        require(Wallets[wallet].Person_address!=0x0000000000000000000000000000000000000000,"this  account not exist");

        require(_numberOfBlueCoins>0,"  number of   Blue Coins not valid !");

        require(Wallets[msg.sender].numberOfBlueCoins>=_numberOfBlueCoins,"you have enough  Blue Coins !");

        Wallets[msg.sender].numberOfBlueCoins=Wallets[msg.sender].numberOfBlueCoins-_numberOfBlueCoins;
        Wallets[wallet].numberOfBlueCoins=Wallets[wallet].numberOfBlueCoins+_numberOfBlueCoins;

        return Wallets[msg.sender];
    }
    function MyWallet()public view returns(ColoredWallet memory){
        require(Wallets[msg.sender].Person_address!=0x0000000000000000000000000000000000000000,"you have not  account!");
        return Wallets[msg.sender];
    }

}