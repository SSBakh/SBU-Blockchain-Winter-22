# Dependencies
[![https://docs.soliditylang.org/en/v0.8.17/](https://img.shields.io/badge/solidity-0.8.0-blue)](https://github.com/ethereum/solidity/blob/v0.8.17/docs/index.rst)
[![https://docs.soliditylang.org/en/v0.8.17/](https://img.shields.io/readthedocs/solidity?logo=solidity)](https://docs.soliditylang.org/en/v0.8.17/)
[![https://spdx.org/licenses/](https://img.shields.io/badge/License-SPDX--License--Identifier%3A%20MIT-green)](https://spdx.org/licenses/)
[![https://remix.ethereum.org/](https://img.shields.io/badge/Remix-remix.ethereum.org-blue)](https://remix.ethereum.org/)
[![https://goerli.etherscan.io/address/0x9a0dfa10de1d40c50f313ca44b201be4d3f9abaf](https://img.shields.io/badge/Goerli-Testnet%20Network-blue)](https://goerli.etherscan.io/address/0x9a0dfa10de1d40c50f313ca44b201be4d3f9abaf)



# Description
## 1. What is a `pure` function and when is it used? what's the difference between `pure` and `view`? take a simple example.
> `view` indicates that the function will not alter the storage state in any way. But it allows you to "view" it or read it.
> 
> `pure` is even more strict, indicating that it will not even read the storage state.
> 
> A pure function is a function that given the same input, always returns the same output. But the state of the contract keeps changing as users interact with it. So if you pass a state variable as an argument to the function, since the state is changing, that function will not be pure. That's why pure functions cannot access to state.
> 
> "pure" functions are heavily used in mathematical libraries. For example [SafeMath.sol](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/utils/math/SafeMath.sol)
> 
> Also inside pure functions, you cannot
> 
> - use `address(this).balance`
> 
> - call other functions except for pure functions
> 
> if you call to `view` or `pure` functions externally, you do not pay a gas fee. However, they do cost gas if called internally by another function.
>
A simple example:
```
pragma solidity ^0.7.0;

contract viewSample {

    //view is specified and function reads data from block chain
    function getBlock() public view returns (uint){
        uint blocknumber = block.number;
        return blocknumber;
    }    
}
```

```
pragma solidity ^0.7.0;

contract pureSample {

   //pure is specified
   //this functions is only concerned about the variables and arithmetic in this function
   function getResult() public pure returns(uint sum){
      uint a = 5; 
      uint b = 7;
      sum = a + b; 
   }
}
```

### Comparison of Pure and View

|  | DEFAULT(NOT SPECIFIED IN FUNCTION) | VIEW | PURE |
| :---: | :---: | :---: | :---: |
| Ideal For | Transactions that alter data on the block chain | Getter functions to view data on the block chain | Defined to the scope of the function and do not alter or view data on the block chain |
| Data Access | read / write | read | None |
| Transaction Type | Send | Call | Call |

## 2.
> Smart Contract:
> - a struct (named: ColoredWallet) with two values (unit256):
>   - numberOfRedCoins
>   - numberOfBlueCoins
> 
> - a function for:
>   - users can build their ColoredWallet
>   - init values of redcoin and blue coin are 0 and 100
>
> - a function for:
>   - users can Burn one blue coin and receive two red coins
>   - check enough blue coin existence
> 
> - a function for:
>   - transfer bluecoin between ColoredWallet
>   - check receiver ColoredWallet existence
>   - each user only has access to their wallet
> 
> - Bounce question:
>   - find out what's the modifier? solve q2 with it.
> 
### smart contract link on Goerli Testnet Network:

contract: https://goerli.etherscan.io/address/0x9a0dfa10de1d40c50f313ca44b201be4d3f9abaf

contract creation: https://goerli.etherscan.io/tx/0x6d214c3e9e09fc386b0f5b2524da442c69ef8c5b5eaa128067fd3397ca471c1c


