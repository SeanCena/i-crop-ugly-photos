# Uncumin hax

Erase enemies/political dissidents/your ex out of your photos with the power of opencv

To run (after starting your venv and installing dependencies):

```
export FLASK_APP=main.py
export FLASK_ENV=development **(if you want to i guess)**
export GOOGLE_APPLICATION_CREDENTIALS=gcp_creds.json
flask run
```

Note: put your gcp json secrets thing in the root directory and call it gcp_creds.json