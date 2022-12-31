<div dir="rtl">
لینک اتراسکن:
</div>

````
https://goerli.etherscan.io/tx/0x8825256037042b9e82ee0365e8add42bb958fa02365156d0adedab9d5c552ab0
````

<div dir="rtl">
ابتدا یک struct درست می کنیم که شامل دو ارزش برای تعداد کوین ها و یک متغیر دیگر برای چک کردن اجرای قرارداد در یک آدرس است:
</div>

````
  struct ColoredWallet {
      uint256 numberOfRedCoins;
      uint256 numberOfBlueCoins;
      bool check;
  }
````

<div dir="rtl">
  تابعی برای مقدار دهی اولیه ایجاد می کنیم:
</div>

````  
  function a_create_Colored_wallet() public {
      // Initilize struct values
      ColoredWallet memory wallets = ColoredWallet(0,100,true);
      check_wallet[me] = wallets;
  }
````

<div dir="rtl">
  تابعی برای افزودن دلخواه مقدار کوین آبی و قرمز توسط صاحب کیف پول ایجاد می کنیم:
</div>

````
  function b_add_Blue_Coins(uint256 _numberOfBlueCoins) public{
      ColoredWallet memory wallet = check_wallet[me];
      wallet.numberOfBlueCoins = wallet.numberOfBlueCoins+ _numberOfBlueCoins;
      check_wallet[me] = wallet;
  }
  //Function for adding more red coins to your wallet
  function c_add_Red_Coins(uint256 _numberOfRedCoins) public{
      ColoredWallet memory wallet = check_wallet[me];
      wallet.numberOfRedCoins = wallet.numberOfRedCoins+ _numberOfRedCoins;
      check_wallet[me] = wallet;
  }
  ````
  
  <div dir="rtl">
  تابعی برای سوزندان تعدادی کوین آبی و دریافت 22 کوین قرمز به ازای هر کوین سوزانده شده ایجاد می کنیم که در این تابع قبل از سوزاندن کوین آبی از کافی بودن مقدار آن در کیف پول دارنده اطمینان حاصل می کنیم:
  </div>
  
  ````
  //Error for insufficient balance of Blue Coins
  error Insufficient_Balance(uint256 available);
  //Function for burning Blue coins
  function d_burn_Blue_Coins(uint256 burnBlueCoins) public{
      ColoredWallet memory wallet = check_wallet[me];
      //Check Sufficient number of Blue Coins in your wallet
      if(wallet.numberOfBlueCoins >= burnBlueCoins){
          wallet.numberOfBlueCoins = wallet.numberOfBlueCoins-burnBlueCoins;
          wallet.numberOfRedCoins = wallet.numberOfRedCoins+2*burnBlueCoins;
          check_wallet[me] = wallet;
      }else{
          revert Insufficient_Balance({
              available: wallet.numberOfBlueCoins
          });
      }
  }
 ````
 
<div dir="rtl"> 
  تابعی برای ارسال مقداری کوین آبی توسط دارنده آن به آدرس دیگر ایجاد می کنیم که در این تابع قبل از ارسال از داشتن مقدار کافی کوین آبی توسط فرستنده اطمینان حاصل می کنیم:
</div>

````
 function e_send_coin(address to, uint256 amount) payable public{
      //Check existence of colored wallet or don't send to same wallet
      if(check_wallet[to].check && to!=me){
          ColoredWallet memory wallet =  check_wallet[me];
          ColoredWallet memory to_Wallet =  check_wallet[to];
          // Check sufficiency of Blue Coins in your wallet
          if(wallet.numberOfBlueCoins >= amount){
              //send Blue Coins
              wallet.numberOfBlueCoins = wallet.numberOfBlueCoins- amount;
              check_wallet[me] = wallet;
              to_Wallet.numberOfBlueCoins = to_Wallet.numberOfBlueCoins + amount;
              check_wallet[to] = to_Wallet;
          }else{
              revert Insufficient_Balance_transfer({
                  available: wallet.numberOfBlueCoins
              });
          }
      }else{
          revert No_Colored_Wallets_or_same_wallet({
              ewallet: to
          });
      } 
  }
````
