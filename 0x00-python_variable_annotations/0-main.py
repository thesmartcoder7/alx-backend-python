#!/usr/bin/env python3
to_str = __import__("3-to_str").to_str

pi_str = to_str(3.14)
print(pi_str == str(3.14))
print(to_str.__annotations__)
print(f"to_str(3.14) returns {pi_str} which is a {type(pi_str)}")
