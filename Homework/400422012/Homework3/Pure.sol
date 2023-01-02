// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ViewAndPure {
    uint256 public x = 1;

    function View (uint256 y) public view returns (uint256) {
        return x + y;
    }

    // it returns sum of two numbers that are passed as parameter 
    function Pure (uint256 i, uint256 j) public pure returns (uint256) {
        return i + j;
    }
}