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

    People[] public peopleArray ;

    // mapping(string => address) public nameToAddress;
    // mapping(string => uint256) public nameToBlueCoinsBalance;
    mapping(string => People) public nameToPeople;

    function createColoredWallet(string memory _name) public {

        People memory newPerson = People(_name,msg.sender,defaultColoredWallet,true);
        peopleArray.push(newPerson);
        nameToPeople[newPerson.people_name] = newPerson ;
    }
    
    function blueToRedExchange(string memory _name) public {
        
        bool condition1 = nameToPeople[_name].people_address == msg.sender ;
        bool condition2 = nameToPeople[_name].people_coloredwallet.numberOfBlueCoins > 0 ;
        
        People memory person = nameToPeople[_name];

        require(condition1,"No Access!!");

        person.people_coloredwallet.numberOfBlueCoins -= 1;
        person.people_coloredwallet.numberOfRedCoins += 2;
        nameToPeople[_name] = person;
        require(condition2,"Sorry! Not Enough Blue Coin Balance To Complete The Exchange!");
    }

    function sendBlueCoin(string memory _sendername, string memory _receivername, uint256 _numberofbluecoinstosend) public {
        
        bool condition1 = nameToPeople[_sendername].people_address == msg.sender ;
        bool condition2 = nameToPeople[_sendername].people_coloredwallet.numberOfBlueCoins >= 0 ;
        bool condition3 = nameToPeople[_receivername].bool_exist ;

        People memory senderperson = nameToPeople[_sendername];
        People memory receiverperson = nameToPeople[_receivername];

        require(condition1,"No Access!!");

        senderperson.people_coloredwallet.numberOfBlueCoins -= _numberofbluecoinstosend;
        receiverperson.people_coloredwallet.numberOfBlueCoins += _numberofbluecoinstosend;
        nameToPeople[_sendername] = senderperson;
        nameToPeople[_receivername] = receiverperson;

        require(condition2,"Sorry! Not Enough Blue Coin Balance to Complete The Transaction!") ;
        require(condition3,"No Entries Found For The Destination Name!") ;


    }
}
