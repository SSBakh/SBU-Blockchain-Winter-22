به نام خدا

تمرین ۳ - مشکات احمدی
—--------------------------------------------------------------------------------------------------

۱.
الف) توابع pure چی هستند؟
تابع pure تابعی است که برای این به کار می‌رود که اطمینان بده که تابع state را نه می‌خواند و نه در آن تغییری می‌دهد. 

ب) چه موقع‌ای میتونیم یک تابع رو pure تعریف کنیم؟ 
وقتی که تابع state variableها را تغییری ندهد یا به آدرسها دسترسی نداشته باشد. در این صورت باید بدون هزینه این صدا زدن انجام شود. تابع‌های pure باید خودشان تابع‌های pure را صدا بزنند.

ج) تفاوت تابع pure با تابع view چی هست؟
شباهت pure و view در این است که به کامپایلر می‌گوییم که نمی‌خواهیم تغییری در state variable‌ها ایجاد کنیم و بدون هزینه این کار باید انجام شود. تفاوت در اینجاست که  از view وقتی استفاده می‌کنیم که state variable‌ها را بدون هزینه بخوانیم اما با pure, حتی این توابع را نمی‌خواهیم بخوانیم. مثلا وقتی می‌خواهیم یک تابع بنویسیم که اعمال ریاضی رو دو ورودی انجام بدهد که رابطه‌ای با state اصلا ندارد.

د)  یک تابع pure مثال بزنید.
// SPDX-License-Identifier: MIT
 
pragma solidity ^0.8.0;
 
contract Test {
  function multiply(uint x, uint y) public pure returns(uint){
   return x*y;
  }
}



Q2)

(Requested Links in etherscan)
https://goerli.etherscan.io/tx/0x2aafc72a96e3ea65290eb471b136674141444f43d6dd5935c4207f2442a460e2
0x751bc0235b86bba9bbe2b851b1ca48350e0f3e08

Code explanation
A)
Here we create the wallet struct containing numberOfRedCoins, numberOfBlueCoins, we also keep the owner address "owner_address" (who creates the wallet).
We also keep a boolean variable to indicate whether user exists or not which is by default True at creation.
======================
    // alef
    struct ColoredWallet {
        uint256 numberOfRedCoins;
        uint256 numberOfBlueCoins;
        address owner_address;
        // to check if the person exists
        bool exists;
    }
=======================


B)
We keep a mapping from address to wallet to let users access their wallets
=======================
mapping (address => ColoredWallet) address2wallet;
=======================


C)
Here we let  user to create a wallet with own address and add it to the mapping

=======================
// be
function createWallet() public
{
    ColoredWallet memory new_wallet = ColoredWallet(0, 100, msg.sender, true);
    address2wallet[msg.sender] = new_wallet;
}
=======================


D)
Here we let  user to burn owm blues to have more reds. In case of having insufficient blues the require throws an error

=======================
// pe
function burnABlue() public
{
    require (address2wallet[msg.sender].numberOfBlueCoins>0,"You do not have enough blue coins to convert");
    address2wallet[msg.sender].numberOfBlueCoins = address2wallet[msg.sender].numberOfBlueCoins - 1;
    address2wallet[msg.sender].numberOfRedCoins = address2wallet[msg.sender].numberOfRedCoins + 2;
}
=======================


E)
Here we let  user to burn owm blues to have more reds. In case of having insufficient blues the require throws an error

=======================
// pe
function burnABlue() public
{
    require (address2wallet[msg.sender].numberOfBlueCoins>0,"You do not have enough blue coins to convert");
    address2wallet[msg.sender].numberOfBlueCoins = address2wallet[msg.sender].numberOfBlueCoins - 1;
    address2wallet[msg.sender].numberOfRedCoins = address2wallet[msg.sender].numberOfRedCoins + 2;
}
=======================



F) Here we let the user specify the receiver address
first we check if the user has enough blue coins, second we check if receiver address is valid and created
if the code passes two "require"s then it subtract from the owner and sends to the receiver.

=======================
// te
// Everyone can only use his/her own wallet
function sendABlue(address receiver) public
{
    // check if we have enough blue
    require (address2wallet[msg.sender].numberOfBlueCoins>0,"You do not have enough blue coins to send");
    // check if the receiver exists is checked
    require (address2wallet[receiver].exists,"Your receiver does not exists");
    address2wallet[msg.sender].numberOfBlueCoins = address2wallet[msg.sender].numberOfBlueCoins - 1;
    address2wallet[receiver].numberOfBlueCoins = address2wallet[receiver].numberOfBlueCoins + 1;
}
========================


G)

At the end we use a function to access own coins
========================
function  getMyCoins() public view returns(uint256,uint256){
    return (address2wallet[msg.sender].numberOfRedCoins, address2wallet[msg.sender].numberOfBlueCoins);
}
========================
