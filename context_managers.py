"""
context managers
"""


class DummyContext:
    def __enter__(self):
        print("Starting...\n")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("\n...ending")


with DummyContext() as cm:
    print("HELLO!!!")
