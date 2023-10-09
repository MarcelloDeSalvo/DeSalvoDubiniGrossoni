# DeSalvoDubiniGrossoni

# Introduction
eMall is a software project that was created for PoliMi's Software Engineering 2 course during the 2022–2023 academic year. It is focused on the analysis, design, implementation, and testing of a system in accordance with the RASD (Requirement Analysis and Specification Document) and DD (Design Document).

# Overview
There are two types of users: Drivers and Charging Point Operators that can manage all the charging stations through another private section of the website
Drivers of eMall can:
- Locate nearby charging stations
- Access information about the charging station
- Book and start charging sessions

A CPO can:
- Manage current charging points and add new ones.
- Decide on prices and provide discounts
  
![Home page](https://i.imgur.com/AIMcuV3.png)
![Charging station](https://i.imgur.com/UgeF8pq.png)
![Booking](https://i.imgur.com/8LZWFXe.png)


# Installation
We decided to split the main 4 projects in separate branches
```bash
1 - DeSalvoDubiniGrossoni -> Documents
2 - front-end -> eMSP + CPMS website
3 - emsp-back-end -> eMSP backend
4 - cpms-back-end -> CPMS backend
```
Alternatively you can open the respective folders inside the IT folder as separate projects..
  
## Git worktree
In order to setup the repo we strongly suggest to use git worktree and setup different folders to run each branch independently

```bash
1] - Clone the main repo
2] - Inside the main repo execute
git worktree add ../emall_frontend front-end
git worktree add ../emsp_backend emsp-back-end
git worktree add ../cpms_backend cpms-back-end

This should create three separate folders that you can now open independently

3] - Follow the instruction inside the README of each branch
```
