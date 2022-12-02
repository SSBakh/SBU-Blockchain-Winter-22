# HomeWork

## System Requirements
1. python 3 and pip

## Create and Activate a virtual environment (Optional)
1. Install virtualenv from pip with 
   ```
    pip install virtualenv
   ```
2. Run this command in your project directory to create a virtual env
   
   ```bash
   python3 -m virtualenv venv 
   ```

   OR
   ```bash
    virtualenv -p python3 venv
   ```
3. Activate/Deactivate virtualenv
    Activation - Mac/Linux
    ```bash
    source venv/bin/activate
    ```
    Activation - Windows
    ```bash
    .\venv\Scripts\activate
    ```

    Deactivation - Any OS
    ```bash
    deactivate
    ```

## Install Required Dependencies
Install required dependencies with following command:

```bash
pip install -r requirements.txt
```

## Run Project
To run project, run the `main.py`, you can run it with following command:

```bash
python main.py
```

OR 

```bash 
python3 main.py
```

Then go through menu to do what you want

## How It Works?
### Generate RSA key pair
This feature will generate an RSA key pair and saves them into `private_key.pem` and `public_key.pem` in your current working directory

### Sign a text with private key
This feature will take a private key file and a message and signs the message with private key

### Verify message and signature
This feature will take a public key, message and signature (from previous step) and verifies if signature matches with message and public key

### Mine single block
This feature will take a block number, and data then returns nonce and hash of the block