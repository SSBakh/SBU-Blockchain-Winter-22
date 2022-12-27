
# ReadME


## تعریف تابع pure:
توابع **pure**  محدودتر از توابع view هستند و حالت را تغییر نمی دهند و وضعیت بلاکچین  را نمی خوانند.
## این توابع در موارد زیر استفاده نمی شوند:

- خواندن متغیرهای State
- دسترسی Address(This).Balance یا address>.Balance>
- دسترسی به هر یک از متغیرهای خاص بلوک Tx، Msg ( Msg.Sig و Msg.Data قابل خواندن است).
- فراخوانی هر تابع که Pure مشخص نشده باشد.
- استفاده از Inline Assembly That Contains Certain Opcodes دسترسی به هر یک از متغیرهای خاص بلوک Tx، Msg ( Msg.Sig و Msg.Data قابل خواندن است).
-  فراخوانی هر تابع که Pure مشخص نشده باشد.
- استفاده از Inline Assembly That Contains Certain Opcodes

توابع **Pure** می توانند از توابع  ()Revert و ()Require برای بازگشت تغییرات State در صورت بروز خطا، استفاده کنند.


## تفاوت تابع pure و view :

توابع view فقط خواندنی هستند و وضعیت بلاکچین را تغییر نمی دهند. به عبارت دیگر اگر می خواهید داده ها را از بلاکچین بخوانید میتوانید از view استفاده کنید اما توابع pure نمیتوانند دیتای بلاکچین را بخوانند و نمیتوانند حالتی را تغییر دهند.


## مثالی از تابع pure :
```
contract pureSample {

function get() public pure returns(uint sum){

uint num1 = 5;

uint num2 = 7;

sum = num1 + num2;
}

}
```

## لینک EtherScan:

[smart contract](https://goerli.etherscan.io/tx/0x54acb51cf7a1beeef726b9dd0ffb73eceb7e101169a7f3ab16fa29b81fce2c06)

[smart contract craetion](https://goerli.etherscan.io/address/0x8044168061e57a94e300c0ebff5aed4e031df6bc)