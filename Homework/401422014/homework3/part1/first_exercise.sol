// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract pureSample {

   //View functions are read only and do not modify the state of the blockchain. if you want to read data from the blockchain , you can use view keyword.
   //Pure functions is more strict, indicating that it will not even read the state ,this functionts are heavily used in mathematical libraries. 

   //Data access of view ==> read , Data access of pure ==> none

   function sumOf2number() public pure returns(uint sum){
      uint a = 1; 
      uint b = 2;
      sum = a + b; 
   }
}