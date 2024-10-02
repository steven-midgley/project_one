# project_one

Possibly a flight tracker

## Deployment flow

 When starting a new task it is always best to work in a new branch
		- ```git switch main```
			**if not on main branch**
		- ```git pull origin main```
		- ```git checkout -b <branch-name>```

	Make sure to commit and push often
		- ```git status```
		- ```git add .```
		- ```git commit -m 'commit message'```
		- ```git push```
			**if it is the first time pushing your branch to the remote repo use: ```git push --set-upstream origin <branch-name>```**

## Branch Discipline

	There are two branch that will contain all contributors work.
	Those are ```stage``` and ```main```. ```main``` is the Sacred branch. 
	```main``` can not be pushed to by any branch. Project manager will handle
	updating ```main```. ```stage``` can be updated by any branch but needs at least 2 people
	to review the merge request before it can be approved. ```stage``` will serve at the testing ground for contributor code additions. If and when ```stage``` is free of conflict it will
	then be merged into main