// SPDX-License-Identifier : MIT
pragma solidity ^0.8.0;
contract firstcontract{
    struct coloredwallet {
        uint256  numberofredcoins;
        uint256 numberofbluecoins;
        address UsersAddress;
    }
    coloredwallet[] public UsersArray;
    function createuser(uint256 _numberofbluecoins, uint256 _numberofredcoins)public{
        _numberofredcoins = 0;
        _numberofbluecoins = 100;
        coloredwallet memory newuser=coloredwallet(_numberofbluecoins, _numberofredcoins, msg.sender);
        UsersArray.push(newuser);
    }
    
}
 library SafeMath {
    function conversion(uint256 a, uint256 b)public pure returns(uint256){
        if (a == 0){
            return 0;
        }
        else {
            a -= 1;
            b += 2;
        }
    }

}
   contract Sendcoin {
   function sendViaSend(address payable _to) public payable {
        bool sent = _to.send(msg.value);
        require(sent, "Failed to send Ether");
    }

    function sendViaCall(address payable _to) public payable {
        (bool sent, bytes memory data) = _to.call{value: msg.value}("");
        require(sent, "Failed to send Ether");
    }
   
   function sendcoin(uint256 _numberofbluecoins) public payable {
       uint256 fee = 0.00001 ether;
       require(msg.value == fee, 'Insufficient to cover fees');
       payable(msg.sender).transfer(_numberofbluecoins);
   }
}
