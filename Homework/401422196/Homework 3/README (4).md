
# Homeworke3

this is my answer to the assignment number 3 
#section 1 
### what are pure functions ?
pure function can not read or write to the state variables
Pure functions can use the revert() and require() functions to revert potential state changes if an error occurs.
### When we call a function pure in solidity?
In Solidity, a function that doesn’t read or modify the variables of the state is called a pure function. It can only use local variables that are declared in the function and the arguments that are passed to the function to compute or return a value.
### what are the differences between Pure and View functions ?
the main difference is that In view function, we cannot modify state variable whereas in pure we also cannot modify state and also we can’t read state variable. Let's see the example code.
### write an example for the pure function 

```solidity
pragma solidity ^0.8.0;

contract Test {
   function getResult() public pure returns(uint product, uint sum){
      uint a = 1; 
      uint b = 2;
      product = a * b;
      sum = a + b; 
   }
}
```
#section 2 
write an smart conrtract 
## 🔗 Links
[Etherscan contract creathin ](https://goerli.etherscan.io/address/0x977406e54d76f96c876c41bce248f0a26569c8c1)
[contract address](https://goerli.etherscan.io/0x977406E54D76F96C876c41bce248F0A26569C8c1)
# Written by 
-[@niloofar vafa](https://github.com/niloofarvafa)
