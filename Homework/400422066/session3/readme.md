# Blockchain Course |  Assignment 3 #


# Basic Functions 
Getter functions can be declared view or pure.  
View function declares that no state will be changed.  
Pure function declares that no state variable will be changed or read.  
Pure and view functions still cost gas if they are called internally from another function. They are only free if they are called externally, from outside of the blockchain.In this type of case, there won't be any transaction initiated because this will be like just querying the blockchain for its current state and nothing will be changed.



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

View on etherscan : [Smart Contract](https://goerli.etherscan.io/tx/0x189e6673b00020bdba3209d70d9387b83f7da3ab6ba7470768a10fc2471aa3e5)
 
  
More information : [Solidity by Example](https://solidity-by-example.org/). 



