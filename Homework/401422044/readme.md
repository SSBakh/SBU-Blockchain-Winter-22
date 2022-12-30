۱. فرق view و pure
تابع های pure به شکلی هستند که متغیر ها نه تغییر میکنند و نه خوانده میشوند. در حالی که تابع های view به ما میگویند با اجرای برنامه هیج داده ای تغییر یا ذخیره نمیشوند.
در واقع تابع های pure نه داده ای را روی بلاکچین ذخیره میکنند و نه داده ای را از بلاکچین میخوانند.
تابع های pure استفاده زیاده در کتابخانه های ریاضی دارند. به عنوان مثال safeMath.sol
مثال:
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;

contract ViewAndPure {
    uint public x = 1;

    // Promise not to modify the state.
    function addToX(uint y) public view returns (uint) {
        return x + y;
    }

    // Promise not to modify or read from the state.
    function add(uint i, uint j) public pure returns (uint) {
        return i + j;
    }
}

d
