# DS-Live-022122's Cohort Repository!

A repository for all lecture, review, or other resources for the Flatiron School's Live Data Science 022122 Cohort.

![choices](https://media.giphy.com/media/ouE6OPO1MADM4/giphy.gif)

## Written Instructions to Connect to This Repository:

**We will go through and follow these instructions together in a lecture during Week 1 - no rush!** 

1. FORK this repository, creating a copy on your own GitHub account

2. Then clone your fork down to your local computer
```
git clone https://github.com/[yourusername]/DS-Live-022122.git
```

3. Add the `/flatiron-school/` version as the `upstream` (to pull future changes)
```
git remote add upstream https://github.com/flatiron-school/DS-Live-022122.git
```

4. You can make changes to the notebooks now! Remember to push your changes to your forked version of the repo (to put your local changes up online):
```
git add [filename]
git commit -m 'message here'
git push
```

### Whenever you want to get updated notes:

5. Grab the changes from the upstream repo
```
git fetch upstream
```

6. Merge new changes onto your local repo
```
git merge upstream/main -m "meaningful message about what you're updating"
```
