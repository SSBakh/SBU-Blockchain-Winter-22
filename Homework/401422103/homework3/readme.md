# Smart Contract Assignment
## بخش اول تکلیف
در توابع 
view
ما هیچ مقداری رو تغییر نمی دهیم و تنها دیتا می گیریم.
در توابع 
pure
ما نه تنها مقداری رو تغییر نمی دهیم بلکه متغیرهای قرارداد را هم باز نمی گردانیم.

وقتی از توابع 
pure
استفاده می کنیم که می خواهیم اطلاعاتی از جمله متغیرها، را پردازش کرده و نتیجه ی پردازش را بازگردانیم.
در این صورت نیازی به برزگرداندن متغیرهای نداریم و فقط روی آن ها پردازش انجام می دهیم.
در مثال زیر ما فقط می خواهیم بدانیم شخص، موجودی دارد یا خیر:
```bash
    function checkBalance() public pure returns(bool){
        ColoredWallet memory yourWallet = getWallet[msg.sender];
        if (yourWallet.numberOfBlueCoins > 0){
            return true;
        return false;
    }
```

## بخش دوم تکلیف
الف. ما یک Struct ساختیم. تعداد سکه های قرمز و آبی و همین طور آدرس دارنده کیف پول رو در آن قرار دادیم.
ب. با تابع createWallet کاربر می تواند یک کیف برای خود بسازد. مقادیر سکه های قرمز و آبی به طور پیش فرض تنظیم می شوند و آدرس کاربر، روی کیف، با استفاده از msg.sender تنظیم می گردد.
پ. با استفاده از تابع blueToRed کاربر می تواند یک سکه آبی را سوزانده و دو سکه قرمز دریافت کند. در این تابع ابتدا کیف کاربر فراخوانده شده سپس موجودی سکه های آبی وی بررسی می گردد. در صورت داشتن اعتبار کافی، عملیات انجام شده و در پایان کیف، به روز می شود.
ت. آخرین تابع این تکلیف تابع sendBlue برای ارسال سکه های آبی به دیگران است. در این تابع آدرس گیرنده و مقدار سکه برای ارسال دریافت می شود. سپس کیف ارسال کننده فراخوانی می شود. سپس بررسی می کنیم که آدرس کاربر (msg.sender) با آدرس کیف مطابقت داشته باشد. این بررسی با دستور require انجام می شود.
با دستور require میزان موجودی گیف با مقدار amount مقایسه شده و در صورت کمبود موجوی، اخطار داده می شود. 
سپس کیف مقصد فراخوانی شده بررسی می کنیم که آدرس آن 0 نباشد.
سکه های مورد نظر از کیف مبدا کاسته و به کیف مقصد اضافه می شوند.
سپس هر دو کیف ذخیره می گردند. 

## سوال امتیازی:
modifier ها تکه کدهایی هستند که از آن ها می توان برای محدود کردن دسترسی و همین طور اعتبارسنجی استفاده کرد.
توجه داشته باشید که در فایل ارسال شده، modifier های زیر نوشته شده اند:
noWallet برای بررسی موجود بودن کیف در تابع sendBlue. به این ترتیب ما مطمئن می شویم که کیفی وجود دارد که سکه ها را دریافت کند.
alreadyExist برای اطمینان از این که کاربر به طور مرتب برای خود کیف نمی سازد. بدون وجود این اعتبارسنجی، هر بار که کاربر کیف می سازد مقادیر سکه های ریسِت می شوند.
onlyOwner برای اطمینان از این که شخص درخواست دهنده همان صاحب کیف است.

دو تابع blueGetfun و redGetfun برای دریافت موجودی کیف شخص استفاده می شود.
تنها تابعی که مقدار می گیرد، تابع sendBlue است.