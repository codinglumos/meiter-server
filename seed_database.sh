rm db.sqlite3
rm -rf ./metierapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations metierapi
python3 manage.py migrate metierapi
python3 manage.py loaddata users
python3 manage.py loaddata metieruser
python3 manage.py loaddata metiercustomer
python3 manage.py loaddata tokens
python3 manage.py loaddata reactions
python3 manage.py loaddata comments
python3 manage.py loaddata services
python3 manage.py loaddata favorites
