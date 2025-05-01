sudo docker compose --env-file ~/Projects/PostMaster/PostMasterCommon/dev-environment.env -f ~/Projects/PostMaster/PostMasterCommon/dev-compose.yml up -d


python manage.py makemigrations
python manage.py migrate

