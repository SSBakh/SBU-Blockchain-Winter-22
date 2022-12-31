// SPDX-License-Identifier: MIT

pragma solidity ^0.8.7;
//Contract without modifier
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
    //Error for insufficient balance of Blue Coins
    error Insufficient_Balance(uint256 available);
    //Function for burning Blue coins
    function d_burn_Blue_Coins(uint256 burnBlueCoins) public{
        ColoredWallet memory wallet = check_wallet[me];
        //Check Sufficient number of Blue Coins in your wallet
        if(wallet.numberOfBlueCoins >= burnBlueCoins){
            wallet.numberOfBlueCoins = wallet.numberOfBlueCoins-burnBlueCoins;
            wallet.numberOfRedCoins = wallet.numberOfRedCoins+2*burnBlueCoins;
            check_wallet[me] = wallet;
        }else{
            revert Insufficient_Balance({
                available: wallet.numberOfBlueCoins
            });
        }
    }
    //Error for no colored wallet or send coin to same wallet
    error No_Colored_Wallets_or_same_wallet(address ewallet);
    //Error for insufficient balance of Blue Coins
    error Insufficient_Balance_transfer(uint256 available);
    //Function for sending Blue Coins
    function e_send_coin(address to, uint256 amount) payable public{
        //Check existence of colored wallet or don't send to same wallet
        if(check_wallet[to].check && to!=me){
            ColoredWallet memory wallet =  check_wallet[me];
            ColoredWallet memory to_Wallet =  check_wallet[to];
            // Check sufficiency of Blue Coins in your wallet
            if(wallet.numberOfBlueCoins >= amount){
                //send Blue Coins
                wallet.numberOfBlueCoins = wallet.numberOfBlueCoins- amount;
                check_wallet[me] = wallet;
                to_Wallet.numberOfBlueCoins = to_Wallet.numberOfBlueCoins + amount;
                check_wallet[to] = to_Wallet;
            }else{
                revert Insufficient_Balance_transfer({
                    available: wallet.numberOfBlueCoins
                });
            }
        }else{
            revert No_Colored_Wallets_or_same_wallet({
                ewallet: to
            });
        } 
    }
}

