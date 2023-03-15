# crud-test

oc create -f users-template.yaml

oc new-app --template usersapp-template -p BRANCH_NAME=main -p APP_GIT_URL=https://github.com/torvicvasil1993/crud-test -p PROJECT_NAME=torvicvasil-dev -p APP_NAME=usersapp


mysql --password=password --user=usersapp
