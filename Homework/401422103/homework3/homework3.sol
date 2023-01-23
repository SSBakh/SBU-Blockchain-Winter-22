// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Assinment{
    struct ColoredWallet{
        address owner;
        uint256 numberOfRedCoins;
        uint256 numberOfBlueCoins;
    }

    ColoredWallet[] walletArray;
    mapping(address => ColoredWallet) getWallet;
    modifier alreadyExist() {
        ColoredWallet memory tempWallet = getWallet[msg.sender];
        require(tempWallet.owner == address(0), "Wallet Already Exists!");
        _;
    }
    modifier noWallet(){
        ColoredWallet memory tempWallet = getWallet[msg.sender];
        require(tempWallet.owner != address(0), "You Don't Have a Wallet!");
        _;
    }
    modifier onlyOwner() {
        ColoredWallet memory tempWallet = getWallet[msg.sender];
        require(msg.sender == tempWallet.owner, "Not owner");
        _;
    }
    function createWallet() public alreadyExist{
        uint256 _redCoins = 0;
        uint256 _blueCoins = 100;
        ColoredWallet memory newWallet = ColoredWallet(msg.sender, _redCoins, _blueCoins);
        getWallet[msg.sender] = newWallet;
    }

    function blueGetfun() public noWallet onlyOwner view returns(uint256){
        ColoredWallet memory tempWallet = getWallet[msg.sender];

        return tempWallet.numberOfBlueCoins;
    }
    function redGetfun() public noWallet onlyOwner view returns(uint256){
        ColoredWallet memory tempWallet = getWallet[msg.sender];

        return tempWallet.numberOfRedCoins;
    }
    function blueToRed() public noWallet onlyOwner{
        ColoredWallet memory tempWallet = getWallet[msg.sender];
        if (tempWallet.numberOfBlueCoins > 0){
            tempWallet.numberOfBlueCoins = tempWallet.numberOfBlueCoins - 1;
            tempWallet.numberOfRedCoins = tempWallet.numberOfRedCoins + 2;
        }
        getWallet[msg.sender] = tempWallet;
    }
    function sendBlue(address _to, uint256 amount) public {
        ColoredWallet memory tempWallet = getWallet[msg.sender];
        require(tempWallet.owner == msg.sender, "This is not Your Wallet!!!");
        require(tempWallet.numberOfBlueCoins > amount, "You Dont Have Enough Balance!!");
        ColoredWallet memory targetWallet = getWallet[_to];
        require(targetWallet.owner != address(0), "There Is no Wallet TO Recieve The Blue Coins!!");
        tempWallet.numberOfBlueCoins = tempWallet.numberOfBlueCoins - amount;
        targetWallet.numberOfBlueCoins = targetWallet.numberOfBlueCoins + amount;
        getWallet[msg.sender] = tempWallet;
        getWallet[_to] = targetWallet;
    }



}