# project_one

Possibly a flight tracker

## API

[opensky api](https://github.com/openskynetwork/opensky-api)

## Downloading flights data from [Kaggle](https://www.kaggle.com)

First you'll need to make a free [Kaggle account](https://www.kaggle.com/account/login?phase=startRegisterTab&returnUrl=%2Fdatasets%2Fmahoora00135%2Fflights).

Once you have created an account click on your profile image and select 'settings'. Once there you will see
a section for API. Go ahead and create a new API key by clicking 'Create New Token'. This will start the
which will contain your username and api key.

Place the kaggle json in a .env file to protect you access credentials.

## Installing OpenSkyApi

![Used the pip install method](installing_opensky_screen_shot.png)
Run ```pip install -e src/python3/python```
**if there is an error with using python3 then just use python/python instead both python 2 & 3 are compatible**

## Deployment flow

When starting a new task it is always best to work in a new branch
**if not on main branch**
```git switch main```
```git pull origin main```
```git checkout -b <branch-name>```

Make sure to commit and push often
```git status```
```git add .```
```git commit -m 'commit message'```
```git push```
**if it is the first time pushing your branch to the remote repo use**
```git push --set-upstream origin <branch-name>```

## Branch Discipline

There are two branch that will contain all contributors work.
Those are ```stage``` and ```main```. ```main``` is the Sacred branch.
```main``` can not be pushed to by any branch. Project manager will handle
updating ```main```. ```stage``` can be updated by any branch but needs at least 2 people
to review the merge request before it can be approved. ```stage``` will serve at the
testing ground for contributor code additions. If and when ```stage``` is free of
conflict it will then be merged into main
