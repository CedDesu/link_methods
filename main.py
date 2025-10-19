from linkedlist import LinkedList

sushi_preparation = LinkedList()
sushi_preparation.insert_at_end("prepare")
sushi_preparation.insert_at_end("roll")
sushi_preparation.insert_at_beginning("assemble")

print("Initial list:")
sushi_preparation.display()

# Remove beginning
removed = sushi_preparation.remove_beginning()
print(f"\nRemoved at beginning: {removed}")
sushi_preparation.display()

# Remove at end
removed = sushi_preparation.remove_at_end()
print(f"\nRemoved at end: {removed}")
sushi_preparation.display()

# Remove specific item ("prepare")
removed = sushi_preparation.remove_at("prepare")
print(f"\nRemoved 'prepare': {removed}")
sushi_preparation.display()

# Try removing a non-existent item
removed = sushi_preparation.remove_at("mixing")
print(f"\nRemoved 'mixing': {removed}")
