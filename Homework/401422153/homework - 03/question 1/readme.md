<div dir="rtl">

# توابع view و pure 

### تابع view :
تابعی که بروی هیچ متغیری از نوع حالت یا state (متغیری که قبل از تعریف توابع، تعریف می شود)، تغییری ایجاد نمی کند و با بلاکچین تعامل ندارد، ولی می تواند به متغیر حالت دسترسی داشته باشد (می تواند آن را بخواند).

### تابع pure :
تابعی که بروی هیچ متغیری از نوع حالت یا state، تغییری ایجاد نمی کند و با بلاکچین تعامل ندارد، همچنین نمی تواند به متغیر حالت دسترسی داشته باشد (نمی تواند آن را بخواند).
    
### مقایسه:
    
<table>
    <tr>
        <td>نوع تابع</td>
        <td>پیش فرض</td>
        <td>view</td>
        <td>pure</td>
    </tr>
    <tr>
        <td>دسترسی به متعیر حالت</td>
        <td>خواندن/ نوشتن</td>
        <td>خواندن</td>
        <td>-</td>
    </tr>
    
</table>    
    
-------------------------------------------------
    
برای مثال در قطعه کد زیر، تابع view_function می تواند به متغیر حالت فقط برای خواندن آن دسترسی داشته باشد.
</div>

```
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.7;

contract view {

    //decalre state variable
    uint c=5;
    
    function view_Function(uint b) view public returns(uint){
        return b + c;
    }

}
```
<div dir="rtl">
و اگر آن را به صورت زیر تغییر دهیم: 
</div>
<br>

```
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.7;

contract view {

    //decalre state variable
    uint c=5;

    function view_Function(uint b) view public returns(uint){
        return c= b + c;
    }

}
```
<div dir="rtl">
با خطای زیر مواجه خواهیم شد (یعنی اجازه تغییر متغیر حالت را در این نوع تابع نداریم):
</div>
<br>

```
TypeError: Function declared as view, but this expression (potentially) modifies 
the state and thus requires non-payable (the default) or payable.
|
* | return c= b + c;
| ^
```
-------------------------------------------------

<div dir="rtl">
حال اگر در همان قطعه کد قبل، تابع view_function را به حالت pure قرار دهیم:
</div>
<br>

```
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.7;

contract view {

    //decalre state variable
    uint c=5;

    function view_Function(uint b) pure public returns(uint){
        return b + c;
    }

}
```
<div dir="rtl">
 با خطایی مبنی بر عدم اجازه دسترسی جهت خواندن متغیر حالت مواجه می شویم:
</div>
<br>

```
TypeError: Function declared as pure, but this expression (potentially) reads
 from the environment or state and thus requires "view".
|
* | return b + c;
| ^
```
