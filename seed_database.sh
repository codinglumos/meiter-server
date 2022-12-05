rm db.sqlite3
rm -rf ./metierapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations metierapi
python3 manage.py migrate metierapi
python3 manage.py loaddata users
python3 manage.py loaddata comments
python3 manage.py loaddata customers
python3 manage.py loaddata creators
python3 manage.py loaddata services