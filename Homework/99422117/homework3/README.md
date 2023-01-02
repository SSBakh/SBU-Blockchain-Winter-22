# تکلیف جلسه سه

## 1) تفاوت view و pure

view keyword:

توابع ویو را زمانی استفاده می کنیم که هدف از تابع فقط خواندن دیتا یا استیت می باشد و خب چون تغییری را روی بلاکچین انجام نمی دهیم نیازی هم به مصرف گس نمی باشد بنابراین همچنین توابعی را بصورت ویو تعریف می کنیم. توابع گتر که در مفهوم شی گرایی وجود دارد و در اسمارت کنترکت هم از این مفهوم استفاده می شود را می توان از این نمونه در نظر بگیریم.

pure keyword:

توابع پیور یا خالص نه مقداری یا استیتی از بلاکچین را می خوانند و نه مقداری یا استیتی از بلاکچین را تغییر می دهند

مثال از تابع پیور:

```bash
function getAverage() public pure returns(uint avg) {
      uint a = 5; 
      uint b = 7;
      avg = (a + b) / 2; 
}
```
این تابع پیور هست چون نه استیتی از بلاکچین را در بدنه تابع می خوانیم یا آن را تغییر می دهیم.

در کل هر دوی این دو کلید واژه رفتار توابع سالیدیتی را مشخص می کنند.

<hr>

## 2) پیاده سازی smart contract

### الف) طراحی struct
```bash
struct ColoredWallet {
        uint256 numberOfRedCoins;
        uint256 numberOfBlueCoins;
        address walletAddress;
}

//mapping to store wallets
mapping (address => ColoredWallet) public ColoredWallets;
function setColoredWallets(address _wallet, ColoredWallet memory _walletValue) public{
        ColoredWallets[_wallet]= _walletValue;
}
```
<hr/>

### ب) یک تابع‌ای درست کنید که کاربران می‌توانند ColoredWallet خودشان رو درست کنند. در ابتدا هر کاربرد صفر redCoin و 100تا blue coin دارد
```bash
ColoredWallet wallet;

function createColoredWallet() public {
	wallet = ColoredWallet(0, 100, msg.sender);
    // mapping address to actual wallets
    setColoredWallets(msg.sender, wallet);
    // mapping address to boolean (to check for existence of addresses)
    setWallet(msg.sender);
}
```
<hr/>

### پ)  یک تابع‌ای تعریف کنید که با استفاده از آن تابع، کاربر می‌تواند یکی از blue coinها‌یی که دارد را بسوزاند و در ازای آن ۲تا red coin دریافت کند. حتما چک کنید که کاربر به حد نصاب blue coin داشته باشد.
```bash
function burnBlueAndGetRedCoins() public {
		require(wallet.walletAddress == msg.sender, "You're not allowed to do this!!!");
        require(wallet.numberOfBlueCoins > 0, "You don't have enough blue coins!!!");
        wallet.numberOfBlueCoins = wallet.numberOfBlueCoins - 1;
		wallet.numberOfRedCoins = wallet.numberOfRedCoins + 2;
	}

//get the number of blue coins to see if it works
function getBlueCoins() public view returns(uint256) {
    require(msg.sender == wallet.walletAddress, "You're not allowed to see the balance of Red coins");
    return wallet.numberOfBlueCoins;
}

//check how many red coin we currently have
function getRedCoins() public view returns(uint256) {
    require(msg.sender == wallet.walletAddress, "You're not allowed to see the balance of Red coins");
    return wallet.numberOfRedCoins;
}
```
<hr/>

### ت)یک تابع‌ای تعریف کنید که با استفاده از آن، کاربران می‌توانند برای هم دیگر blue coin ارسال کنند. حتما باید در این تابع چک شود که به ازای آدرس گیرنده یک والت ColoredWallet وجود دارد. در ضمن، این تابع باید طوری طراحی شده باشد که هر شخص فقط می‌تواند به والت خودش دسترسی داشته باشد.
```bash
//Mapping of address to boolean flag to check for existence of addresses
mapping (address => bool) public Wallets;

function setWallet(address _wallet) public{
    Wallets[_wallet]=true;
}

function contains(address _wallet) public returns (bool){
    return Wallets[_wallet];
}

function sendBlueCoin(address receiver, uint256 _numOfBlueCoinsToSend) public {
    require(msg.sender == wallet.walletAddress, "You're not allowed to do this!!!");
    require(contains(receiver), "There's no such address");
    require(wallet.numberOfBlueCoins > _numOfBlueCoinsToSend, "You don't have enough blue coins");
    wallet.numberOfBlueCoins = wallet.numberOfBlueCoins - _numOfBlueCoinsToSend;
    ColoredWallets[receiver].numberOfBlueCoins = ColoredWallets[receiver].numberOfBlueCoins + _numOfBlueCoinsToSend;
}
```
<hr/>
Etherscan Info:

Transaction Hash: 0xf614c5fe07f5f4ac47a389be9a1dc9bf47b066a0a9d4fe4a66edad8b4cb1fe9c

[Etherscan Link](https://goerli.etherscan.io/tx/0xf614c5fe07f5f4ac47a389be9a1dc9bf47b066a0a9d4fe4a66edad8b4cb1fe9c)
