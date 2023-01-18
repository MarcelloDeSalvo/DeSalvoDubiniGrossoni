# DeSalvoDubiniGrossoni

# Installation
We decided to split the main 4 projects in separate branches
```bash
1 - DeSalvoDubiniGrossoni -> Documents
2 - front-end -> eMSP + CPMS website
3 - emsp-back-end -> eMSP backend
4 - cpms-back-end -> CPMS backend
```

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