//SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract Coins{
    function sum(uint256 num1,uint256 num2) public pure returns(uint256) {
        return num1+num2;
    }
    function div(uint256 num1,uint256 num2) public pure returns(uint256) {
        return num1/num2;
    }
    function mul(uint256 num1,uint256 num2) public pure returns(uint256) {
        return num1*num2;
    }

}