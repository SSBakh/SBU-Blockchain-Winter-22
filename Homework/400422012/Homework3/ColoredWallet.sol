// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract SimpleWallet{
    struct ColoredWallet {
        uint256 NumberOfRedCoins;
        uint256 NumberOfBlueCoins;
    }

    mapping(address => ColoredWallet) public AddressToWallet;
    mapping(address => bool) exsited;

    //This function creates a wallet initialized with 0 RedCoin and 100 BlueCoins
    function CreateWallet() public{
        AddressToWallet[msg.sender] = ColoredWallet(0,100);
        exsited[msg.sender] = true;
    }

    //This function exchanges 1 BlueCoin with 2 RedCoins
    function Exchange() public{
        ColoredWallet memory wallet = AddressToWallet[msg.sender];
        require(wallet.NumberOfBlueCoins > 0 , "ERROR: Insuffcient Bluecoin");
        wallet.NumberOfBlueCoins -= 1 ;
        wallet.NumberOfRedCoins += 2 ;
        AddressToWallet[msg.sender] = wallet;
    } 

    //This function transfers "amount" number of BlueCoins from a sender to a receiver
    function Transfer(address _sender, address _receiver, uint256 amount) public{
        require(_sender == msg.sender, "ERROR: You're not allowed to do this!");    
        require(AddressToWallet[_sender].NumberOfBlueCoins > 0 , "ERROR: Insuffcient Bluecoin!");
        require(exsited[_receiver] == true, "ERROR: Receiver does not exist!");
        require(amount > 0, "ERROR: amount should be non-negative!");

        AddressToWallet[_sender].NumberOfBlueCoins -= amount ;
        AddressToWallet[_receiver].NumberOfBlueCoins +=  amount;
    }

}



