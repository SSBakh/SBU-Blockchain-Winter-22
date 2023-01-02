//SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract SmartContract {

    struct ColoredWallet {
        uint256 numberOfRedCoins;
        uint256 numberOfBlueCoins;
        address walletAddress;
    }

    //Variable to store info of one wallet
    ColoredWallet wallet;


    //Mapping to store wallets by their address as a key
    mapping (address => ColoredWallet) public ColoredWallets;
    function setColoredWallets(address _wallet, ColoredWallet memory _walletValue) private {
        ColoredWallets[_wallet]= _walletValue;
    }


    //Mapping to store existing addresses as a key and a corresponding boolean flag
    mapping (address => bool) private Wallets;
    function setWallet(address _wallet) private{
        Wallets[_wallet]=true;
    }
    //to check if a specefic address exists
    function contains(address _wallet) private view returns (bool){
        return Wallets[_wallet];
    }


    //Function to create a wallet with default values & store it in the mapping of addresses
    function createColoredWallet() public {
		wallet = ColoredWallet(0, 100, msg.sender);
        setColoredWallets(msg.sender, wallet);
        setWallet(msg.sender);
	}


    function burnBlueAndGetRedCoins() public {
		require(wallet.walletAddress == msg.sender, "You're not allowed to do this!!!");
        require(wallet.numberOfBlueCoins > 0, "You don't have enough blue coins!!!");
        wallet.numberOfBlueCoins = wallet.numberOfBlueCoins - 1;
		wallet.numberOfRedCoins = wallet.numberOfRedCoins + 2;
	}

    //Printing number of red coins
    function getRedCoins() public view returns(uint256) {
        require(msg.sender == wallet.walletAddress, "You're not allowed to see the balance of Red coins");
        return wallet.numberOfRedCoins;
    }

    //Printing number of blue coins
    function getBlueCoins() public view returns(uint256) {
        require(msg.sender == wallet.walletAddress, "You're not allowed to see the balance of Blue coins");
        return wallet.numberOfBlueCoins;
    }

    function sendBlueCoin(address receiver, uint256 _numOfBlueCoinsToSend) public {
        require(msg.sender == wallet.walletAddress, "You're not allowed to do this!!!");
        require(contains(receiver), "There's no such address");
        require(wallet.numberOfBlueCoins > _numOfBlueCoinsToSend, "You don't have enough blue coins");
        wallet.numberOfBlueCoins = wallet.numberOfBlueCoins - _numOfBlueCoinsToSend;
        ColoredWallets[receiver].numberOfBlueCoins = ColoredWallets[receiver].numberOfBlueCoins + _numOfBlueCoinsToSend;
    }

}