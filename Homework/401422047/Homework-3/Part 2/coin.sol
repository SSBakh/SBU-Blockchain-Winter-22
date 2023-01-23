// SPDX-License-Identifier: MIT

pragma solidity ^0.8.7;

contract mycoin {


    struct my_wallet {
        uint256 n_Blue_Coin;
        uint256 n_Red_Coin;
        bool verify;
    }
    
    
    mapping (address => my_wallet) public The_wallet;
    
    
    address i = msg.sender;    
    
    
    function Colored_wallet() public {
    
        my_wallet memory wallets = my_wallet(0,100,true);
        
        The_wallet[i] = wallets;
        
        
    }
    
    
    modifier enough_Blue_Coin(uint256 _n_Blue_Coin) {
        require(_n_Blue_Coin < The_wallet[i].n_Blue_Coin,
        "blue coins not enough!");
        _;
        
        
    }
    
    
    modifier exist_wallet(address reciever) {
        require(!The_wallet[reciever].verify,
        "your friend has no colored wallet.");
        _;
        
        
    }
    
    
    modifier check_address(address reciever) {
    
        require(i != reciever,
        "same wallet address.");
        _;
        
    }
    
    
    function add_b_coin(uint256 _n_Blue_Coin) public{
    
        my_wallet memory wallet = The_wallet[i];
        
        wallet.n_Blue_Coin = wallet.n_Blue_Coin+ _n_Blue_Coin;
        
        The_wallet[i] = wallet;
        
    }
    
    
    function add_r_Coin(uint256 _n_Red_Coin) public{
    
        my_wallet memory wallet = The_wallet[i];
        
        wallet.n_Red_Coin = wallet.n_Red_Coin+ _n_Red_Coin;
        
        The_wallet[i] = wallet;
        
    }


    function remove_blue_coin(uint256 burn_b) public enough_Blue_Coin(burn_b){
    
        my_wallet memory wallet = The_wallet[i];
        
        wallet.n_Blue_Coin = wallet.n_Blue_Coin-burn_b;
            
        wallet.n_Red_Coin = wallet.n_Red_Coin+2*burn_b;
            
        The_wallet[i] = wallet;
        
    }
    

    function send_coin(address reciever, uint256 coin) 
    public enough_Blue_Coin(coin)
    check_address(reciever) exist_wallet(reciever)
    {
            my_wallet memory wallet =  The_wallet[i];
            
            my_wallet memory to_Wallet =  The_wallet[reciever];
             
            wallet.n_Blue_Coin = wallet.n_Blue_Coin- coin;
            
            The_wallet[i] = wallet;
            
            to_Wallet.n_Blue_Coin = to_Wallet.n_Blue_Coin + coin;
            
            The_wallet[reciever] = to_Wallet;
    }
}
