# Checking that pytest is working as expected


# Step 2: Add "add" function now, then run test, it will pass now.
def add(a, b):
    return a + b;

# Step 1: Add test and run it, it will fail, becuase no "add" function is defined
def test_sum():
    assert add(1, 2) == 3