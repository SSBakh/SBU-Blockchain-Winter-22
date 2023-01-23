# HomeWork #3

## 
In this assignment a simple smart contract is created. 
Once the code is deployed, three functions could be used;
 1. A function to create a wallet.
 2. A function to exchange a blue coin with two red coins.To exchange more than one blue coin, it should be called multiple times depending on the number of desired coins.
 3. A function to transfer blue coins to a receiver.

Also, three modifiers are used;
 1. A modifier to check wallet existance when creating a wallet.
 2. A modifier to check the number of blueCoins when calling ```sendBlueCoins``` function.
 3. A modifier to check the validity of receiver address.

Note: It is assumed that only people with an account can call the functions, so no need to check for wallet existance when calling other functions except when creating one. 

## Structure

The answer to question1 exists in file Q1.txt
The code of question2 exists in hw3WithModifier.sol file.

## Etherscan link

 [contract creation](https://goerli.etherscan.io/tx/0xf6625325dc6d211bba3813be86a03a33f84632ba819953f27a9f7e13a86fcc86)
 [5 bluecoins sent](https://goerli.etherscan.io/tx/0x5486e9f583601911956cb576ac007c211500c781bc700055bfd9bab2d72cde70)

