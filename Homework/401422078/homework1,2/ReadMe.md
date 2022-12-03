# cryptography and block mining 

This project was done for the purpose of testing one cryptography python library and also getting insight from the blockchain mechanism 

## Description

In this project, we use one of the famous cryptography python libraries and use the standard hashlib library. And we try different modules and methods of these libraries for purpose of encryption, decryption, signing, verification, and creating a simple blockchain and study different concepts that are used for chaining blocks and mining them. 

## Getting Started

### Dependencies

* All of the dependencies are mentioned in the requirements.txt file. We used python3.9 for running codes and used just one external library pycrypto, and a bunch of standard libraries like time, JSON, hashlib that didn't need separate installation and, by default, those are in the python ecosystem.

* Note: pycrypto library has difficulty installing in the windows operating system. So we need to install pycryptodome library.

### Installing

* You can clone my project and go to my project's directory and run the below script in command line to install the necessary libraries before running the code

```python
pip install -r requirements.txt

```


### Executing program

* For the cryptography exercise, you need to run the below script in the command line and the directory of the project.  

```python
python tamrin1.py

```

At the end of this file, we have called functions like encrypt(), decrypt(), sign(), and verify(). You can change the argument of these functions and then rerun this file.


* For the mining block exercise, you need to run the below script in the command line and the directory of the project. 


```
python tamrin2.py 
```
At the end of this file, we have called functions like encrypt(), decrypt(), sign(), and verify(). You can change the argument of these functions and then rerun this file.
## Help

With a tiny probability, there may be a conflict between the installed libraries and the version of Python, so it is better to use Python version 3.9 like me. With this version, install libraries and run codes.

## Authors

This project has just one contributor. if you have any question, you can send me email. 

* saqar khalilpour

* [saqarkpr@gmail.com](saqarkpr@gmail.com)

## Version History


* 0.1
    * Initial Release

## License

This project is licensed under the MIT License

## Acknowledgments

Thanks to these documents that give me insight and code snippets
* [pycrypto](https://www.pycrypto.org/)
* [hashlib](https://docs.python.org/3/library/hashlib.html)
* [time](https://docs.python.org/3/library/time.html)
* [json](https://www.w3schools.com/python/python_json.asp)