# Simple file

print("File for viewing difference of Staging and Non-staging")

# should see the difference of pulling update first from central commit
# then, add unstage file to staging without merge conflict
# Git add, staged the file to the staging area
# now, let's modified to make the staging area to modified area
# we are now in tracking area


def simple(*args, **kwargs):
    listItems = [i for i in args]
    dictionary = {k: v for k, v in kwargs.items()}
    print('Operator arugments - *args - returns: \n',
          listItems, f"\n {'='*50} \n")
    print('Operator keyword arugments - **kwargs - returns: \n',
          dictionary)

# we are now in modified area
# let's do git fetch & see what happens
# Showing 17 commits behind & can be fast-forwarded
# which indicates that as long as local working directory are not commit 
# to central repository, everything will work fine
# hence, git pull does not come with any merge conflict
# we can then continue by running git add & commit & push
