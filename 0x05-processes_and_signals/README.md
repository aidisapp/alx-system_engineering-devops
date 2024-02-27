# Processes and Signals

## Description
This repository contains a series of Bash scripts and a C program aimed at understanding processes, signals, and process management in Linux.

## Table of Contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Tasks](#tasks)
* [License](#license)

## General Info
The scripts included in this repository cover various aspects of process management and signal handling in Linux. Each script serves a specific purpose outlined in the project requirements.

## Technologies
The scripts are written in Bash, adhering to specific requirements such as using Ubuntu 20.04 LTS, passing Shellcheck, and employing specific commands and restrictions as per project guidelines.

## Setup
To run these scripts, ensure you have Bash installed on your system. Clone the repository to your local machine and navigate to the appropriate directory. Make sure the scripts are executable. You may need to adjust permissions using `chmod +x <script_name>`.

## Tasks
### 0. What is my PID
- Script: `0-what-is-my-pid`
- Description: Displays its own PID.

### 1. List your processes
- Script: `1-list_your_processes`
- Description: Displays a list of currently running processes with hierarchy.

### 2. Show your Bash PID
- Script: `2-show_your_bash_pid`
- Description: Displays lines containing the word "bash" to get the PID of the Bash process.

### 3. Show your Bash PID made easy
- Script: `3-show_your_bash_pid_made_easy`
- Description: Displays the PID and process name of processes containing the word "bash".

### 4. To infinity and beyond
- Script: `4-to_infinity_and_beyond`
- Description: Displays "To infinity and beyond" indefinitely with a sleep interval.

### 5. Don't stop me now!
- Script: `5-dont_stop_me_now`
- Description: Stops the `4-to_infinity_and_beyond` process using the `kill` command.

### 6. Stop me if you can
- Script: `6-stop_me_if_you_can`
- Description: Stops the `4-to_infinity_and_beyond` process without using `kill`.

### 7. Highlander
- Script: `7-highlander`
- Description: Displays "To infinity and beyond" indefinitely and handles signals.

### 8. Beheaded process
- Script: `8-beheaded_process`
- Description: Kills the `7-highlander` process.

### 9. Process and PID file
- Script: `100-process_and_pid_file`
- Description: Manages process, displays messages, and handles signals. Creates/deletes PID file.

### 10. Manage my process
- Scripts: `101-manage_my_process`, `manage_my_process`
- Description: Manages a process, including start, stop, and restart functionalities.

### 11. Zombie
- Script: `102-zombie.c`
- Description: Creates zombie processes in C.
