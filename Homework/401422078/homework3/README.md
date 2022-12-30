# homework 1
## what is pure function?
Functions that neither read nor change 
smart contract variables are called 
Pure functions.
In the view function, we can read the variables inside the smart contract, such as the address of the person who uses the function, but we cannot change it.


### Example

```solidity
pragma solidity ^0.8.17;

contract PureFunction{
    function Hello(string memory name)public pure returns(string memory){
        return string.concat("hello ",name);
    }
}
```

# homework 2
 this homework for create a smart contract with modifier and without modifier.
## links

- [etherscan  smart contract creation link  ](https://goerli.etherscan.io/tx/0x88a118358cacd4bf94cd8d0cb4637c4deb15c53319a961936d0d38dd8fe0ad32)
- [etherscan smart contract link](https://goerli.etherscan.io/address/0x45cae19f4ae03ec04e3987b91f7716be19a2c9a4)
## Authors


if you have any question, you can send me email. 

* saqar khalilpour

* [saqarkpr@gmail.com](saqarkpr@gmail.com)

