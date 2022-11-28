
## مسئله یک
### بخش الف
### توضیح پیاده سازی
- main.py

یک تابع با نام زیر تعریف شده

generate_key_pairs

که وظیفه تولید جفت کلیدهای عمومی و خصوصی را دارد و همچنین این کلیدها را در فایل های مجزا ذخیره می کند و درنهایت هر دوکلید را بصورت یک لیست برمی گرداند که اندیس صفرم لیست کلید خصوصی و اندیس اول کلید عمومی خواهد بود

### نحوه اجرا
کد زیر صرفا جفت کلیدها را تولید و در فایل های مجزا ذخیره می کند و بصورت آرایه بر می گرداند و چیزی را پرینت نمی کند.
```bash
generate_key_pairs()
```
###### بعد از اجرای این تابع می توانیم نتیجه را درفایلهای مربوطه ببینیم که با فرمت پم ذخیره شده اند

### وابستگی ها

```bash
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
```
------------------------------------------
# مسئله یک
### بخش ب
### توضیح پیاده سازی
- main.py

یک تابع با نام زیر تعریف شده است

sign_message

که دو ورودی تحت عنوان پیام و کلید خصوصی را دریافت می کند در بدنه تابع با استفاده از متد ساین از کلید خصوصی می توانیم به امضای پیغام بپردازیم در نهایت کلید تولید شده را از تابع برمی گردانیم

### نحوه اجرا
قبل از این که بتوانیم تابع را اجرا کنیم ابتدا نیاز داریم کلید خصوصی را از فایل بخوانیم

```bash
with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )
```

سپس تابع را فراخوانی می کنیم

```bash
message = b"You'll never walk alone"
signature = sign_message(message, private_key)
print(signature)
```

### وابستگی ها

```bash
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import padding
```

------------------------------------------

# مسئله یک
### بخش پ
### نحوه پیاده سازی
- main.py

یک تابع با نام زیر تعریف شده

validate_signature

که سه ورودی امضای مرحله قبل پیام و کلید عمومی را دریافت می کند و تعیین می کند که آیا امضا معتبر است یا خیر

برای انجام این کار از متد اعتبارسنجی کلید عمومی در بدنه تابع استفاده شده

### نحوه اجرا
```bash
# Read public key from file
with open("public_key.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

message = b"You'll never walk alone"
# signature from previous step (function)
validate_signature(message, public_key, signature)
```


### وابستگی ها

```bash
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import padding
```

------------------------------------------
# مسئله دو
### توضیح پیاده سازی
- mine.py

یک تابع به نام (ماین) تعریف شده که شماره بلاک و دیتایی را که رشته می باشد دریافت می کند (نانس به صورت پیش فرض از صفر آغاز خواهد شد) در بدنه تابع نانس را تا جایی افزایش می دهیم که به هش دلخواه برای بلاک برسیم. که شروع 
شدن هش با چهار صفر می باشد.
خروجی کد هش بلاک و نانس بصورت پرینت آن ها می باشد
### نحوه اجرا
برای اجرا کافی است تابع مورد نظر را با دو ورودی شماره بلاک و داده ی رشته فراخوانی کنیم
```bash
block_number = 10
data = "You'll never walk alone"
mine(block_number, data)
```
### وابستگی ها پروژه
- hashlib

فقط از این کتابخانه برای دسترسی به توابع هش استفاده کرده ایم

------------------------------------
