# Homework 3

## Part 1
You can find answers of part1 in **Part1.txt** file.

## Part 2
Normal implementation is in **MyWallet.sol** file.\
Implementation with _modifiers_ is in **MyWalletV2.sol** file.

### **What are modifires?**
A modifier is a special type of Solidity function that is used to modify the behavior of other functions. For example, we can use a modifier to check that a certain condition is met before allowing the function to execute.

`Note:`
    We can use multiple modifiers on a single Solidity function.

### **Types of modifiers:**
1.**Gate Checks** (checks if a certain condition is true before allowing a function to execute)\
2.**Prerequisites** (ets up the environment for a function to execute, rather than checking if a certain condition is true)\
3.**Filters** (checks if a certain condition is true, and, if it is, allows the function to execute. If the condition is not true, then the function will not execute)\
4.**Reentrancy Attack Prevention** (A reentrancy attack is a type of attack where a malicious actor tries to execute a function multiple times, via a recursive call, in order to exploit it)

### **Smart contract links:**
Contract creation: https://goerli.etherscan.io/tx/0x12e2f6fb1a936636186a8d0a600be8a4e4eb4be6d50a68ce93546b4ea6e70fef\
Contract: https://goerli.etherscan.io/address/0x92e0a6e439bdf532cc2272829cad8a76ea839533