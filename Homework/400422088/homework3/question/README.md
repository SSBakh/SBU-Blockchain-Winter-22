/* difference between pure and view modifiers
view indicates that the function will not alter the storage state in any way.
But it allows you to "view" it or read it
pure is even more strict, indicating that it will not even read the storage state.
A pure function is a function which given the same input, always returns the same 
output. But the state of the contract keeps changing as users interact with it. 
So if you pass a state variable as an argument to the function, since the state 
is changing, that function will not be pure. That's why pure functions cannot 
access to state.
"pure" functions are heavily used in mathematical libraries. 
For example SafeMath.sol
Also inside pure functions, you cannot
    use address(this).balance
    call other functions except pure functions
if you call view or pure functions externally, you do not pay a gas fee. 
However, they do cost gas if called internally by another function.
*/


