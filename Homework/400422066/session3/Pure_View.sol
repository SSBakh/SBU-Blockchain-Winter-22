// SPDX-License-Identifier:MIT

pragma solidity ^0.8.0;

contract Basics{
    uint256 public x = 1;

    function PURE(uint256 _x , uint256 _y) public pure returns(uint256 sum){
        sum = _x +_y;
    }
    function VIEW(uint256 _y) public view returns(uint256 sum){
        sum = x + _y;
    } 
}
