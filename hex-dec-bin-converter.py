#!/usr/bin/python3
"""
This script prints a hex, decimal, and binary representation of your input.
"""


import sys
import binascii


def hex_converter(input_hex):
    print("Hex:", hex(int(input_hex, 16)))
    print("Decimal:", int(input_hex, 16))
    print("Binary:", bin(int(input_hex, 16))[2:])


def dec_converter(input_dec):
    print("Hex:", hex(int(input_dec, 10)))
    print("Decimal:", int(input_dec, 10))
    print("Binary:", bin(int(input_dec, 10))[2:])


def bin_converter(input_bin):
    print("Hex:", hex(int(input_bin, 2)))
    print("Decimal:", int(input_bin, 2))
    print("Binary:", bin(int(input_bin, 2))[2:])


def print_usage():
    print("Usage: ./hex-dec-bin-converter.py input-type input")
    print("Input Types: hex, dec, or bin")
    print("Example: ./hex-dec-bin-converter.py hex ff123ad")
    print("Example: ./hex-dec-bin-converter.py dec 1456312")
    print("Example: ./hex-dec-bin-converter.py bin 0111010")

def main():
    if len(sys.argv) != 3:
        print_usage()
        exit(1)
    if sys.argv[1] != "hex" and sys.argv[1] != "dec" and sys.argv[1] != "bin":
        print_usage()
        exit(1)
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print_usage()
        exit(0)

    input_type = sys.argv[1]
    input_value = sys.argv[2]

    if (input_type == "hex"):
        hex_converter(input_value)
    elif (input_type == "dec"):
        dec_converter(input_value)
    elif (input_type == "bin"):
        bin_converter(input_value)


main()