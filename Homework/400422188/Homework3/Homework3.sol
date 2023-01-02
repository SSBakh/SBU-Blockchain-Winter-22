//SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract coin {
    struct ColoredWallet {
    uint256 NumberOfRedCoins;
    uint256 NumberOfBlueCoins;
}

ColoredWallet public firstcoin;

function setCoin1() public {
    firstcoin.NumberOfRedCoins = 0;
    firstcoin.NumberOfBlueCoins = 100;
}



function transfer(address reciever, uint256 NumberOfRedCoins) public {
        require(sender != address(0), "ERROR 1 ");

function burn(address count, uint256 NumberOfBlueCoins, uint256 NumberOfRedCoins) internal {
        require(count != address(0), "ERROR 2");

        uint256 countBalance = _balances[account];
        require(countBalance >= NumberOfBlueCoins, "ERROR 3");
        unchecked {
            _balances[count] = countBalance - NumberOfBlueCoins;
        }
        _totalSupply -= NumberOfRedCoins;

        emit Transfer(count, address(0), NumberOfRedCoins);
    }
 
mapping (address => bool) members;
   constructor() public Ownable() {
   }
   function addMember(address _member)
       public
       onlyOwner
   {
       members[_member] = true;
   }

   function isMember(address _member) public view returns(bool);
function addMember(address _member) public onlyOwner;
function removeMember(address _member) public onlyOwner;

Whitelist witelist;

   constructor(address _whitelistAD) public {
       witelist = Whitelist(_whitelistAD);
   }

   function transfer(address count, uint256 amount) public {
       require(witelist.isMember(count), "Count's not whitelisted");
       super._transfer(count, amount);
   }
   }



