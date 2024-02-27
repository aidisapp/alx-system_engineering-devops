# 0x04. Loops, conditions, and parsing

## Description
This repository contains a collection of Bash scripts focused on practicing loops, conditions, and parsing in shell scripting.

## Learning Objectives
- Creating SSH keys
- Using while, until, and for loops
- Implementing if, else, elif, and case condition statements
- Utilizing the `cut` command
- Understanding comparison operators for files and other data
- Ensuring script portability and correctness

## Requirements
- Allowed editors: vi, vim, emacs
- Scripts should be interpreted on Ubuntu 20.04 LTS
- Scripts should end with a new line
- All Bash script files must be executable
- Do not use `awk`
- Scripts must pass Shellcheck (version 0.7.0) without any errors
- The first line of each script should be `#!/usr/bin/env bash`
- Include a `README.md` file at the root of the project directory

## Tasks
- **0. Create a SSH RSA key pair:** Generate an RSA key pair and share the public key.
- **1. For Best School loop:** Display "Best School" 10 times using a for loop.
- **2. While Best School loop:** Display "Best School" 10 times using a while loop.
- **3. Until Best School loop:** Display "Best School" 10 times using an until loop.
- **4. If 9, say Hi!:** Display "Best School" 10 times, but say "Hi" on the 9th iteration.
- **5. 4 bad luck, 8 is your chance:** Loop from 1 to 10, display "bad luck" on the 4th iteration and "good luck" on the 8th.
- **6. Superstitious numbers:** Display numbers from 1 to 20, with special messages on the 4th, 9th, and 17th iterations.
- **7. Clock:** Display the time for 12 hours and 59 minutes using a while loop.
- **8. For ls:** Display the content of the current directory in a list format.
- **9. To file, or not to file:** Provide information about a file, including existence, emptiness, and type.
- **10. FizzBuzz:** Display numbers from 1 to 100, with specific messages for multiples of 3, 5, and both.
- **11. Read and cut:** Display specific information from the `/etc/passwd` file using a while loop.
- **12. Tell the story of passwd:** Display formatted information from the `/etc/passwd` file using a while loop and IFS.
- **13. Let's parse Apache logs:** Parse and display visitor IP addresses and HTTP status codes from an Apache log file using awk.
- **14. Dig the data:** Group visitor IPs by HTTP status code and display the data in descending order of occurrence count.

## Files
1. 0-RSA_public_key.pub
2. 1-for_best_school
3. 2-while_best_school
4. 3-until_best_school
5. 4-if_9_say_hi
6. 5-4_bad_luck_8_is_your_chance
7. 6-superstitious_numbers
8. 7-clock
9. 8-for_ls
10. 9-to_file_or_not_to_file
11. 10-fizzbuzz
12. 100-read_and_cut
13. 101-tell_the_story_of_passwd
14. 102-lets_parse_apache_logs
15. 103-dig_the-data
