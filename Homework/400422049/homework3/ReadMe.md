# Homework 3
This is a read me file for homework 3.

## Part I

**Question**:

What is the difference between *view* and *pure* keywords when it comes to functions' behaviour in Solidity?
- One can declare a function as *view* in cases when they promise not to modify any state variables. They can view the state variables but can't modify them.

- One can declare a function as *pure* in cases when they promise neither to modify nor to read any state variables.

## Part II

Program a smart-contract in which:

a) There's a struct with 2 members: numberOfRedCoins , numberOfBlueCoins, both of type uint256. Call the struct ColoredWallet.

b) There's a function by which each user would be able to create their own ColoredWallet. By default each user has 0 redCoins and 100 blueCoins which are assigned to numberOfRedCoins and numberOfBlueCoins variables respectively.

c) There's a function by which each user whould be able to spend one blue coin in exchange for two red coins. Make sure that the user have enough blue coins to complete the exchange. 

d) There's a function by which users would be able to send each other blue coins. Make sure that each user only has access to their own wallet. Also make sure that the address for destination wallet do exist in the records.

File: [homework3.sol](homework3.sol)

[Goerli Etherscan link](https://goerli.etherscan.io/tx/0x11273340b1020685c7a74a1dad5a98583ca49cc6112801fd8a54a82cef9b7b51) 


Bonus:
What is a **modifier** in Solidity? When it comes in handy? Try yo rewrite the **Part II** using modifiers.

- 

File: [homework3-with-modifiers.sol](homework3-with-modifiers.sol)

[Goerli Etherscan link](https://goerli.etherscan.io/tx/0x5b5e526afafcd2a57caf1b80a0479c206bdcb84c7a5545bd7099a081dd74ae20)





