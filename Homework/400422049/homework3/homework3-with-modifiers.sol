// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract MyContract {

    struct ColoredWallet {

        uint256 numberOfRedCoins ;
        uint256 numberOfBlueCoins ;
    }


    ColoredWallet defaultColoredWallet = ColoredWallet(0,100);


    struct People {

        string people_name;
        address people_address;
        ColoredWallet people_coloredwallet;
        bool bool_exist ; 
    }


    modifier onlyOwner(string memory _name) {
        bool condition1 = nameToPeople[_name].people_address == msg.sender ;
        require(condition1 , "No Access!!");
        _;
    }


    modifier blueBalanceCheckForExchange(string memory _name) {
        bool condition2 = nameToPeople[_name].people_coloredwallet.numberOfBlueCoins > 0 ;
        require(condition2,"Sorry! Not Enough Blue Coin Balance To Complete The Exchange!");
        _;
    }


    modifier accountExistanceCheck(string memory _receivername) {
        bool condition3 = nameToPeople[_receivername].bool_exist ;
        require(condition3,"No Entries Found For The Destination Name!") ;
        _;
    }


    People[] public peopleArray ;


    mapping(string => People) public nameToPeople;


    function createColoredWallet(string memory _name) public {

        People memory newPerson = People(_name,msg.sender,defaultColoredWallet,true);
        peopleArray.push(newPerson);
        nameToPeople[newPerson.people_name] = newPerson ;
    }
    

    function blueToRedExchange(string memory _name) public onlyOwner(_name) blueBalanceCheckForExchange(_name){
        
        People memory person = nameToPeople[_name];

        person.people_coloredwallet.numberOfBlueCoins -= 1;
        person.people_coloredwallet.numberOfRedCoins += 2;
        nameToPeople[_name] = person;
    }


    function sendBlueCoin(string memory _sendername, string memory _receivername, uint256 _numberofbluecoinstosend) public onlyOwner(_sendername) accountExistanceCheck(_receivername){
        
        People memory senderperson = nameToPeople[_sendername];
        People memory receiverperson = nameToPeople[_receivername];

        senderperson.people_coloredwallet.numberOfBlueCoins -= _numberofbluecoinstosend;
        receiverperson.people_coloredwallet.numberOfBlueCoins += _numberofbluecoinstosend;
        nameToPeople[_sendername] = senderperson;
        nameToPeople[_receivername] = receiverperson;
    }
}
