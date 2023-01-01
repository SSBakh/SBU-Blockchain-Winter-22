// SPDX-License-Identifier: MIT
pragma solidity 0.8.0;
contract coin{

    uint private index = 0;

    struct ColoredWallet{
        uint numberOfRedCoins;
        uint numberOfBlueCoins;
    }

    ColoredWallet [] private wallets; //an array to save type ColoredWallet
    address [] public addresses; //array to save addresses of accounts who have made a wallet

    mapping(address => ColoredWallet) public AddressToWallet; //mapping from address of accounts to their wallet

    // first account who makes a wallet has index 0, second one index 2 and so on
    //this function finds the index of the address it's given
    function indexOfWallet(address x) private view returns(uint){ 
        for (uint i = 0; i<addresses.length; i++){
            if(addresses[i] == x){
                return i;
            }
        }
    }

    //checks if the address given has a wallet
    function checkIfExists(address x) private view returns (bool){
        for (uint i = 0; i < addresses.length; i++) {
            if (addresses[i] == x) {
                return false; //if returns false then the address is in the array
            }
        }
        return true; //if returns true, this is a new address 
    }

    //check: 1- if msg.sender has a wallet 2- if the wallet has at least 1 blue coin
    modifier checkBlueCoins() {
        address x = msg.sender;
        require(!checkIfExists(x) , "this account does not have a wallet");
        uint indexInWallet = indexOfWallet(x);
        ColoredWallet storage temp = wallets[indexInWallet];
        uint blue = temp.numberOfBlueCoins;
        require(blue>0 , "not enough blue coins");
        _;
    }

    //check: 1- if reciever has a wallet 2- if msg.sender has a wallet 3-if msg.sender has enough blue coins 
    modifier recieverExists(address reciever, uint bluesSent){
        //to check the reciever exists:
        require(!checkIfExists(reciever),"reciever does not have a wallet");
        //to check if the sender has a wallet
        address x = msg.sender;
        require(!checkIfExists(x) , "this account does not have a wallet");
        //to check if the sender has enough blue coins:
        uint indexInWallet = indexOfWallet(x);
        ColoredWallet storage temp = wallets[indexInWallet];
        uint blue = temp.numberOfBlueCoins;
        require(blue-bluesSent>0 , "not enough blue coins");
        _;
    }

    //make a wallet for msg.sender with initial amount of 100 blue coins and 0 red coins
    function makeWallet() public{ 
        address x = msg.sender;
        require(checkIfExists(x),"this account already has a wallet");
        wallets.push(ColoredWallet(0,100));
        AddressToWallet[x] = wallets[index];
        addresses.push(x);
        index = index+1;
    }

    //conver t 1 blue coin to 2 red coins
    function BlueToRed() public checkBlueCoins{
        address x = msg.sender;    
        AddressToWallet[x].numberOfBlueCoins -=1;
        AddressToWallet[x].numberOfRedCoins +=2;
    }
    
    //inputs are address of reciever of the coins and number of coins sender wants to transfer
    function transfer(address reciever, uint amount) public recieverExists(reciever, amount){
        address sender = msg.sender;
        AddressToWallet[sender].numberOfBlueCoins -= amount;
        AddressToWallet[reciever].numberOfBlueCoins += amount;
    }    

}