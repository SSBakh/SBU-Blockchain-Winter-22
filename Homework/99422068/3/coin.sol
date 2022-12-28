// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract coin {
    struct ColoredWallet {
        uint256 numberOfRedCoins;
        uint256 numberOfBlueCoins;
        bool initialized;
    }

    mapping(address => ColoredWallet) public ColoredWallets;

    function init() public noWallet {
        ColoredWallet memory coloredWallet = ColoredWallet(0, 100, true);
        ColoredWallets[msg.sender] = coloredWallet;
    }

    modifier noWallet() {
        require(
            !ColoredWallets[msg.sender].initialized,
            "Your wallet already initialized!"
        );
        _;
    }

    function convertBlueToReds(uint256 _numberOfBlueCoins)
        public
        checkMinimumBlueCoin(_numberOfBlueCoins)
    {
        ColoredWallet memory wallet = ColoredWallets[msg.sender];
        wallet.numberOfBlueCoins =
            wallet.numberOfBlueCoins -
            _numberOfBlueCoins;
        wallet.numberOfRedCoins =
            wallet.numberOfRedCoins +
            _numberOfBlueCoins *
            2;
        ColoredWallets[msg.sender] = wallet;
    }

    modifier checkMinimumBlueCoin(uint256 blueCoin) {
        require(
            blueCoin < ColoredWallets[msg.sender].numberOfBlueCoins,
            "You don't have enough blue conis!"
        );
        _;
    }

    function transfer(uint256 _numberOfBlueCoins, address receiver)
        public
        checkMinimumBlueCoin(_numberOfBlueCoins)
        checkReceive(receiver)
        checkReceiverWallet(receiver)
    {
        ColoredWallet memory wallet = ColoredWallets[msg.sender];
        wallet.numberOfBlueCoins =
            wallet.numberOfBlueCoins -
            _numberOfBlueCoins;
        ColoredWallets[msg.sender] = wallet;
        ColoredWallet memory receiverWallet = ColoredWallets[receiver];
        receiverWallet.numberOfBlueCoins =
            receiverWallet.numberOfBlueCoins +
            _numberOfBlueCoins;
        ColoredWallets[receiver] = receiverWallet;
    }

    modifier checkReceive(address receiver) {
        require(
            !ColoredWallets[receiver].initialized,
            "Receiver does not have wallet!"
        );
        _;
    }

    modifier checkReceiverWallet(address receiver) {
        require(
            msg.sender != receiver,
            "Sender and receiver have the same address!"
        );
        _;
    }
}
