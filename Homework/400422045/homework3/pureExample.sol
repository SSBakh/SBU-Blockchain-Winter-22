// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract pureSample {

    function get() public pure returns(uint sum){
        uint num1 = 6;
        uint num2 = 9;
        sum = num1 + num2;
    }

}