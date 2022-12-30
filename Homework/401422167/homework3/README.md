# Homework 3

## 1
The `pure` functions are similar to the `view` function but the main difference is that a `view` function can read the state but cannot modify it, while a `pure` function cannot read nor modify the state of the blockchain or the contract.

| Function         | Read Access | Write Access |
| ---------------- | ----------- |------------- |
| Normal Functions | ✅          | ✅           |
| `view` Functions | ✅          | ❌           |
| `pure` Functions | ❌          | ❌           |

For example assume we have the following contract.
```sol
contract PureFunctionDemonstration {
    uint256 public num;
    // functions here
}
```

the following function is a `view` function but not a `pure` function
```solidity
function getNum() public view returns(uint256) {
    return num;
}
```

Writing this function in the following way will result in error.

```solidity
function getNum() public pure returns(uint256) {
    return num;
}
```

The error is
```
TypeError: Function declared as pure, but this expression (potentially) reads from the environment or state and thus requires "view".
return num;
^^^
```

However, the following function is a `pure` function.

```solidity
function sum(uint256 _a, uint256 _b) public pure returns(uint256) {
    return _a + _b;
}
```

The following is an example of a function being not `pure` nor `view`.

```solidity
function setNum(uint256 _num) public {
    num = _num;
}
```

## 2
### Aleph
In a `contract` named `ColoredWalletManager`, we add a `struct`, and two `private` attributes, to manage the colored wallets.

```solidity
struct ColoredWallet {
    uint256 numberOfRedCoins;
    uint256 numberOfBlueCoins;
}

mapping(address => ColoredWallet) wallets;
mapping(address => bool) walletExists;
```

The attribute `wallets` holds the actual data of each wallet paired to an _address_, and the attribute `walletExists` is responsible for holding the data about if a wallet for an address is initiated already or not.

### Be
We add two functions, one for creating a new wallet, and the other for enquiring the wallet info.

```solidity
function createWallet() public {
    require(!walletExists[msg.sender], "A wallet with this address already exists.");
    walletExists[msg.sender] = true;
    wallets[msg.sender] = ColoredWallet(0, 100);
}

function getWallet() public view returns(ColoredWallet memory) {
    require(walletExists[msg.sender], "No wallet with this address exists, call createWallet function to create one.");
    return wallets[msg.sender];
}
```

### Pe
We add a function for exchanging 1 blue coin with 2 red coins.

```solidity
function exchangeBlueCoinWithRedCoin() public {
    require(walletExists[msg.sender], "No wallet with this address exists, call createWallet function to create one.");
    require(wallets[msg.sender].numberOfBlueCoins >= 1, "You need to have at least one blue coin to call this function.");
    wallets[msg.sender].numberOfBlueCoins -= 1;
    wallets[msg.sender].numberOfRedCoins += 2;
}
```

### Te
And the last function for sending an amount of blue coins to another wallet.

```solidity
function sendBlueCoin(uint256 amount, address destination) public {
    require(walletExists[msg.sender], "No wallet with this address exists, call createWallet function to create one.");
    require(walletExists[destination], "No wallet with destination address exists, ask them to call createWallet function to create one.");
    require(wallets[msg.sender].numberOfBlueCoins >= amount, "Insufficient Funds.");
    wallets[msg.sender].numberOfBlueCoins -= amount;
    wallets[destination].numberOfBlueCoins += amount;
}
```

### Bonus
As observed, we are repeating the following same line in most of our functions (the only exception is `createWallet`).

```solidity
require(walletExists[msg.sender], "No wallet with this address exists, call createWallet function to create one.");
```

We can use a `modifier` to avoid this code duplication.

```solidity
modifier walletMustExist() {
    require(walletExists[msg.sender], "No wallet with this address exists, call createWallet function to create one.");
    _;
}
```

Using this modifier we can remove that first line from other functions and change the function signatures like this.

```solidity
function getWallet() public view walletMustExist returns(ColoredWallet memory);

function exchangeBlueCoinWithRedCoin() public walletMustExist;

function sendBlueCoin(uint256 amount, address destination) public walletMustExist;
```

The final code exists in the file [ColoredWalletManager.sol](ColoredWalletManager.sol), and is deployed on the Goerli Test Network visible under [this address](https://goerli.etherscan.io/address/0xed67bf3eaee0f22995c2b4fe7f0addd9520a46bf) with creation under [this address](https://goerli.etherscan.io/tx/0xd8f52798098c9f9a9112673a9943be62cbfffb0057cf9f3b6c2fb8606811be98).
