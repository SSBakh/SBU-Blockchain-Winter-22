// SPDX-License-Identifier: MIT

pragma solidity ^0.8.7;
//Contract with modifier
contract coin {
    //Define a struct
    struct ColoredWallet {
        uint256 numberOfRedCoins;
        uint256 numberOfBlueCoins;
        bool check;
    }
    mapping (address => ColoredWallet) public check_wallet;
    //Sender wallet address
    address me = msg.sender;    
    //Function for initialized Colored wallet coins
    function a_create_Colored_wallet() public {
        // Initilize struct values
        ColoredWallet memory wallets = ColoredWallet(0,100,true);
        check_wallet[me] = wallets;
    }
    //Check Sufficient number of Blue Coins in your wallet
    modifier SufficientBlueCoin(uint256 _numberOfBlueCoins) {
        require(_numberOfBlueCoins < check_wallet[me].numberOfBlueCoins,"You have insufficient blue conis.");
        _;
    }
    //Check existence of colored wallet
    modifier check_existence_of_colored_wallet(address to) {
        require(!check_wallet[to].check, "Receiver has no colored wallet.");
        _;
    }
    //Check sender doesn't send Blue Coins to himself
    modifier check_Receiver_Wallet_address(address to) {
        require(me != to, "Check the receiver's wallet address, it's same as your wallet address.");
        _;
    }
    //Function for adding more blue coins to your wallet
    function b_add_Blue_Coins(uint256 _numberOfBlueCoins) public{
        ColoredWallet memory wallet = check_wallet[me];
        wallet.numberOfBlueCoins = wallet.numberOfBlueCoins+ _numberOfBlueCoins;
        check_wallet[me] = wallet;
    }
    //Function for adding more red coins to your wallet
    function c_add_Red_Coins(uint256 _numberOfRedCoins) public{
        ColoredWallet memory wallet = check_wallet[me];
        wallet.numberOfRedCoins = wallet.numberOfRedCoins+ _numberOfRedCoins;
        check_wallet[me] = wallet;
    }
    //Function for burning Blue coins
    function d_burn_Blue_Coins(uint256 burnBlueCoins) public SufficientBlueCoin(burnBlueCoins){
        ColoredWallet memory wallet = check_wallet[me];
            wallet.numberOfBlueCoins = wallet.numberOfBlueCoins-burnBlueCoins;
            wallet.numberOfRedCoins = wallet.numberOfRedCoins+2*burnBlueCoins;
            check_wallet[me] = wallet;
    }
    //Function for sending Blue Coins
    function e_send_coin(address to, uint256 amount) payable public SufficientBlueCoin(amount)
    check_Receiver_Wallet_address(to) check_existence_of_colored_wallet(to)
    {
            ColoredWallet memory wallet =  check_wallet[me];
            ColoredWallet memory to_Wallet =  check_wallet[to];
            //send Blue Coins
            wallet.numberOfBlueCoins = wallet.numberOfBlueCoins- amount;
            check_wallet[me] = wallet;
            to_Wallet.numberOfBlueCoins = to_Wallet.numberOfBlueCoins + amount;
            check_wallet[to] = to_Wallet;
    }
}

