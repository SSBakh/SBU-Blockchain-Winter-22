from block import Block

block_id = int(input('Please enter block id: '))
data = input('Please enter block data: ')

print('\nResult:')
block = Block(block_id, data)
block.mine()
print(block)
