# Importing class "Block" from "Block" module from "/Modules" directory
from Modules.Block import Block

# At first let's instantiate an object from the "Block" class using its constructor.
myblock = Block(blocknumber = 1, data = "this is a record!")


# Then let's check what the current digest of the block is (default nonce = 0 and without invoking the mining function)
myblock.blockdigestfunction()
print(f"Current nonce of the block before mining: {myblock.nonce}")
print(f"Current digest of the block before mining: {myblock.finalhash}")


# Now let's mine the block and print the final nonce and the final hash. The final hash is expected to start with "0000")
print(f"Final nonce of the block after mining:{myblock.mine()}")
print(f"Final hash of the block after mining: {myblock.finalhash}")
