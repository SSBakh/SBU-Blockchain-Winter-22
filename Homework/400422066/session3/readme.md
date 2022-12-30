# Blockchain Course |  Assignment 3 #


# Basic Functions 
Getter functions can be declared view or pure.  
View function declares that no state will be changed.  
Pure function declares that no state variable will be changed or read.  

Example `Pure_View.sol` 

# Basic Wallet 
Build a simple wallet called ColoredWallet :
- initialize a wallet with BlueCoins(100) and RedCoins(0)
- Exchange BlueCoins to RedCoins
- Transfer BlueCoins between wallets

*check conditions in each step : wallet initializations, enough number of coins to transfer or exchange, receiver wallet existence and transaction validation*. 

Basic Wallet : `ColoredWallet.sol`. 


## Function Modifier
Modifiers are code that can be run before and / or after a function call.  
Modifiers can be used to:  
- Restrict access
- Validate inputs
- Guard against reentrancy hack. 

modifier and require are ideally the same, one could declare a modifier and append it before functions for using it several times.  

Basic Wallet using modifier : `ColoredWallet_modifier.sol`. 

 
  
More information : [Solidity by Example](https://solidity-by-example.org/)
