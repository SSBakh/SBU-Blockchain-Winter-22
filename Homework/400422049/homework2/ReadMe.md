# On How Code Files and Directories Are Organized

<div id=1 align="justify">
As you might have noticed, in order to consider reusability and modularity, the structure of files and directories is organized as followings:

[Module Directory](Modules/): Consists of all the submodules that I wrote - including classes - for each task, namely [Homemadersa](Modules/Homemadersa.py) (mostly related to exercise 1 tasks), [Block](Modules/Block.py) (mostly related to exercise 2 tasks).

Also one can check the flow of operations by running python scripts as programs:

[PublicKeyCryptographyProgram.py](PublicKeyCryptographyProgram.py)

[BlockMiningProgram.py](BlockMiningProgram.py)

In order to have a better interaction with programs, 2 more files were added in _".ipynb"_ format:

[PublicKeyCryptographyProgram.ipynb](PublicKeyCryptographyProgram.ipynb)

[BlockMiningProgram.ipynb](BlockMiningProgram.ipynb)

## A Few Notes
- Codes are mostly well-documented with comments and Docstrings
- There were absolutely more compact ways to do many sections here, but I personally prefered to learn new stuff by acting a little more complicated! (i.e. [Auto Docstring - Python Extension for VSCode](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) was one of them.) 
- By creating a **virtual environment** using `python -m venv myvenv` command and activating it by executing `myenv\Scripts\activate` command; it makes a more secure way to add required packages to this isolated environment, without the risk of any conflicts with prior packages on the system.
- Both tasks heavily rely on [cryptography package](https://cryptography.io/en/latest/) by which the methods are able to compute RSA-related stuff and hashing operations.
- [requirements.txt](requirements.txt) is a list of dependencies to install to have the code run properly.

# Exercise 1 : Public-key Cryptography (RSA) Task
1. Create a pair of public/private key using RSA algorithm.(recommended package: [cryptography package](https://cryptography.io/en/latest/))
2. Sign a message by applying the private key
3. Define a function to get a message, a signature and a public key and verify the signature.

# Exercise 2 : Block Mining Task

1. Input: A block consisting of *block number*, *nonce*, *data*. Mine the block such that the block's hash starts with "0000"   

</div id=1>