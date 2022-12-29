//SPDX-License-Identifier: MIT

pragma solidity ^0.8.16;

contract PureFunctionTest{

    //This function checks that the 2 addresse are not the same
    function checkAddresses (address firstAddress , address secondAddress) public pure{
        require(firstAddress != secondAddress,"Error : You cannot choose the same addresses...");
    }
}