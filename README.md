# Base64 Searcher

This tool is designed to search for a string within base64-encoded string.<br>
It takes a string and the desired number of encoding iterations as input and performs base64 encoding accordingly.<br>
The tool helps identify matches by considering the different possibilities of where the data begins and ends within the base64 encoding cycle.

## Theory

In base64 encoding, 24 bits (3 bytes) are converted into four 6-bit Base64 digits. When searching for a string within base64-encoded data, we don't know exactly where our data begins in the 3-byte cycle. Therefore, we have three possibilities to consider:

1. The data begins at the beginning of the cycle.
2. The data begins in the second byte, requiring the first two digits to be discarded after the encoding process as the first digit doesn't belong to our data and the second one have two bits of data that we don't know what they will be.
3. The data begins in the third byte, requiring the first three digits to be discarded (same as case 2).

Using this logic, we can determine where to stop.<br>
Then output of the itration are feed to the next one (if any).

## Usage

```bash
python base64_search.py [string] [iterations]
```

Replace [string] with the string you want to search for within base64-encoded string, and [iterations] with the desired number of encoding iterations.

The script will output an array of strings, the strings are indexed acording to the times you want to encode the string.
so if you want to encode a string 3 times, then the array will contain 3 strings.<br>
the first one have 3 Base-64 encoded string separeted by pipe "|".<br>
the second one have 9 Base-64 encoded string.<br>
the third will have 27 etc...<br>
each itration, string will generate 3 strings in the next itration.
## Example

Let's say you want to search for the string "example" within base64-encoded strings that have been encoded 2 times. You would run the following command:

```bash
python base64_search.py example 2
```
The script will perform the search and display the results.
