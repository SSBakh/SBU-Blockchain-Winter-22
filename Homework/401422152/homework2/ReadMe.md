Let’s proceed to build our first blockchain.
We begin by launching our IDE and installing Flask in our virtual environment.
After setting up our environment, we create a new file for our code, and name it blockchain.py.
Initializing packages
In the blockchain.py file, we import the following packages as they are required in building our blockchain:
We use the DateTime library to attach a timestamp to each block that is created or mined.
The hahshlib will be used to hash a block, JSON will be used to encode the block before we hash it.
jsonify from the Flask library will be used to return messages to Postman.
The Genesis block
To start building our blockchain, we create a Blockchain class. The __init__ method will consist of a variable called chain to store a list of all the blocks in the blockchain.
The create_blockchain() method will allow us to create our Genesis block on instantiation of the class.
The create_blockchain() method will take two default arguments which are proof with a value of one(1), and the previous_hash with a value of zero(0).
This aspect of the code shows the importance of having a background on how blockchain works.
In a blockchain, there is always a first block called the Genesis block, and this block does not have any previous_hash.
The create_blockchain function
Next, we define a create_blockchain method that extends the Genesis block. The only difference here is that we will pass in three parameters which are self, proof, and previous_hash.
All parameters are without a default value.
Within the create_blockchain function, we include a block variable of type dictionary that will be used to define each block in a blockchain.
The dictionary will take the following key-value pairs:
•	Index: An index key will store the blockchain’s length. It is represented by the chain variable in the __init__ method with an added value of one(1). We will use this variable to access each block in the chain.
•	Timestamp: The timestamp key will take a value of the current Date and Time the block was created or mined.
•	Proof: This key will receive a proof value that will be passed to the function when called. Note that this variable refers to the proof of work.
•	Previous hash: Lastly, the previous hash key takes a value of previous_hash from the function which is equivalent to the hash of the previous block.
By adding these key-value pairs, we then append this block to the chain and return the block itself. 
The proof of work function
In the create_blockchain() function, we had a variable called proof. This variable represents the proof of work done to mine a block.
As the programmer of the blockchain, we need to create an algorithm that the miners will solve to mine a block successfully. You can read more about this process here.
We start by creating a new method called proof_of_work() and then we pass two parameters which are self and previous_proof.
In the method, we create a variable to store the proof submitted by miners. We call it new_proof and set the value to one(1).
Next, we create a control statement to check the status of the proof of work, which by default will be False.
Therefore, we create a new variable called check_proof and assign it a False value
Next, we proceed to the algorithm that needs to be solved by the miner. We encapsulate the algorithm in a while statement because this section should repeat until the proof is found.
We start by creating a while statement and set the condition of check_proof as False. If the program hasn’t checked the proof of work, then it has to run through the body of the while loop.
Next, in the while loop, we define the problem/algorithm to be solved which will be based on the previous proof that was successful and the new proof submitted by the miner.
In this aspect of the program, you can define how complex you want this problem to be. In this tutorial, we will make it simple to test if our code works.
Moving forward, we create a new variable called hash_operation, and we assign a value of hashlib.sha256(str(the algorithm).encode()).hexdigest().
This is how we encode the problem in a cryptographic hexadecimal digit with the use of the SHA256 hash library.
Now, we need to replace the algorithm for mining a block.
The algorithm takes the new proof submitted by the user and raises it to the power of 2, then subtracts it from the exponent of the previous proof raised to the power of 2.
Checking the miner’s Solution to the problem
Next, we evaluate the miner’s solution to the problem by checking the hash_operation first 4 characters.
For our code, we check if the first 4 characters are equal to zeros.
If the check returns True, then we’ve checked the proof, and it’s valid. We can then assign it a value of True.
If the result is False we increment the new_proof by 1 which gives the miner another chance to try again and then we return the new proof.
Why do we need four leading zeros for hash operation
Now, why four(4) leading zeros? why not five(5) or six()6 or more.
Note that the more leading zeros we require the more difficult it will be to mine a block. For the sake of this tutorial, we have it at 4 to ensure that we can mine a block faster.
Also, the hash_operation algorithm we pass in must be non-symmetrical such that if the order of operation were to be reversed it wouldn’t result in the same value. For instance, a+b is equal to b+a, but a-b is not equal to b-a.
Lastly, in our algorithm, we require both the new proof submitted and the previous proof from the existing block to effectively define an algorithm for miners to solve. The process is, therefore, continuous and linked to the existing blocks.
Generating a hash
In this step, we generate a hash for the entire block itself. We create a hash() method that takes two parameters (self and block).
In this function, we use JSON dumps to encode the block and return a cryptographic hash of the entire block.
We start by creating a is_chain_valid method that takes self and chain as parameters.
We start by creating a while loop that takes a conditional statement of True if the block_index is equal to the length of the chain and False if the block_index is less than the length of the chain.
Next, we check if the current block’s previous hash field is not similar to the hash field of the previous block. If it does, then it returns True else False:
Next, we get the proof from the previous block, and we also get the proof from the current block. Both values are required for our hash operation in our algorithm:
We further proceed by running the proof data through the algorithm, then we check if the first four leading characters are not equal to four zeros.
If the hash operation is invalid, then we return False, else, we set the previous_block value to the current block that just completed its check, and we increment the block index by 1, then return True as a positive validation check.
Next, we get the proof from the previous block, and we also get the proof from the current block. Both values are required for our hash operation in our algorithm:
we further proceed by running the proof data through the algorithm, then we check if the first four leading characters are not equal to four zeros.
If the hash operation is invalid, then we return False, else, we set the previous_block value to the current block that just completed its check, and we increment the block index by 1, then return True as a positive validation check.
By following the above steps, we’ve built our blockchain. However, we need to interact with it to mine our block and display some details using Flask and Postman.
