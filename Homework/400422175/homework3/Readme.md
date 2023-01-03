in file 1:pure function in solidity doesn't change or doesn't read state variables,that can be used in doing calculations(without changing the state) and it can only uses it's local variables.
difference between pure & view :
a view function is read only but pure functions are not.
and in this code there is a sample of pure function.



file 2:this is a smart contract that hase 3 functions:

at first in //2-alef : here we have coloredwallet struct with two values in uint256 type called:numberOfRedCoins and numberOfBlueCoins.



then in //2-b (createPersonAndWallet):here we have a function for creating wallet by each user ,that has 0 red coins and 100 blue coins.



in part //2-p (burnAndGet) : here we have a function wich each user can burn one blue coin and get two red coins by this function.also it checks for ranning out of bluecoins.


in section //2-t: (send function) : the last function is designed for transfering blue coins between two persons,this function checks for receiver's address existing and gives accessiblity
for each user to send coins only from he/she 's wallet address.



