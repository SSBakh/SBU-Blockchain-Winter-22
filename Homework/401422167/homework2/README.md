# Homework 2

> In the following commands we assume that the current working directory is the project directory. Run the following
> command from the repository root to change the `cwd`.
> 
> ```bash
> cd Homework/401422167/homework2/
> ```

## Dependencies

```bash
pip install -r requirements.txt
```

## 1

Including parts aleph (الف), be (ب), and pe (پ).

One can change the `DATA` variable and run the program via

```bash
python3 1.py
```

the `main` procedure will generate a pair of private and public RSA keys, and uses the private one to sign the `DATA`,
then it shuffles the bytes of signature to create an invalid signature and then checks both signatures.

## 2
One can change the `DATA` variable and run the program via

```bash
python3 2.py
```

The variable `REQUIRED_DOUBLE_ZEROS` must store the half of the number of zeros we want the hash to have as a prefix.
This is because each byte is 8 bits or 2 hexadecimal digits, and for better performance and computation, it's better to
check if the bytes array starts with specific zero bytes which forces this number to be even.