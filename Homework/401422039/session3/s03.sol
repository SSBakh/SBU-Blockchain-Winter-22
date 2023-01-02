//SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract Coins{
    struct ColoredWallet{
        uint256 numberOfBlueCoins;  
        uint256 numberOfRedCoins;  
        address Person_address;        
    }
    
    mapping (address=>ColoredWallet)  Wallets; 
    modifier NotHaveAccount{
        require(Wallets[msg.sender].Person_address==0x0000000000000000000000000000000000000000,"you have already account!");
        _;
    }
    modifier HaveAccount{
        require(Wallets[msg.sender].Person_address!=0x0000000000000000000000000000000000000000,"you have already account!");
        _;
    }
    modifier CheackHaveAccount(address address_p){
        require(Wallets[address_p].Person_address!=0x0000000000000000000000000000000000000000,"you have already account!");
        _;
    }
    modifier HaveBlueCoins{
        require(Wallets[msg.sender].numberOfBlueCoins>0,"you have not Blue Coins  account!");
        _;
    }
    
    modifier HaveEnoughBlueCoins(uint256 _numberOfBlueCoins){
        require(_numberOfBlueCoins>0,"  number of   Blue Coins not valid !");
        require(Wallets[msg.sender].numberOfBlueCoins>=_numberOfBlueCoins,"you have enough  Blue Coins !");
        _;
    }
    
    function CreateWallet() public NotHaveAccount returns(ColoredWallet memory) {
        ColoredWallet memory new_wallet=ColoredWallet(100,0,msg.sender);
        Wallets[msg.sender]=new_wallet;
        return new_wallet;
    }

    function convert_blue_to_red() public HaveAccount HaveBlueCoins returns(ColoredWallet memory){
        
        Wallets[msg.sender].numberOfBlueCoins= Wallets[msg.sender].numberOfBlueCoins-1;
        Wallets[msg.sender].numberOfRedCoins= Wallets[msg.sender].numberOfRedCoins+2;
        return  Wallets[msg.sender];
        
    }
    function send_blue_coin(address wallet,uint256 _numberOfBlueCoins) public HaveAccount HaveEnoughBlueCoins(_numberOfBlueCoins) HaveBlueCoins CheackHaveAccount(wallet) returns(ColoredWallet memory){

        Wallets[msg.sender].numberOfBlueCoins=Wallets[msg.sender].numberOfBlueCoins-_numberOfBlueCoins;
        Wallets[wallet].numberOfBlueCoins=Wallets[wallet].numberOfBlueCoins+_numberOfBlueCoins;

        return Wallets[msg.sender];
    }
    function MyWallet()public HaveAccount view returns(ColoredWallet memory){
        return Wallets[msg.sender];
    }

}