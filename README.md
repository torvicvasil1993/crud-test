# crud-test

oc create -f users-template.yaml

oc new-app --template users-app-template -p BRANCH_NAME=main -p APP_GIT_URL=https://github.com/torvicvasil1993/crud-test -p PROJECT_NAME=torvicvasil-dev -p APP_NAME=users-app


mysql --password=password --user=usersapp
