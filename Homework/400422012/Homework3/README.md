
## Overview

Simple solidity programs that 1. Show an example of pure/view functions and 2. run a simple payment smart contract
 
## Features
* Pure function
* Smart contract

## Pure function
Pure functions are functions that are not accessing any state variables. They can only use local variables that are declared in the function and the arguments.
The view function declares that no state will be changed however Pure function declares that no state variable will be changed or read. 

Example: pure.sol


## Smart contract
* Create a wallet called ColeredWallet initialized with 0 RedCoin and 100 BlueCoins
```python
CreateWallet()
```
* Exchange 1 BlueCoin with 2 RedCoins
```python
Exchange()
```
* Transfer "amount" number of BlueCoins from a valid sender to a receiver
```python
Transfer(address _sender, address _receiver, uint256 amount)
```
Simple wallet: ColoredWallet.sol

Check in etherscan [here](https://goerli.etherscan.io/tx/0xb8cc24dc8e56b36c49d27db2039bc2afc76541ee15ff91ce4e141c3cff177c88).