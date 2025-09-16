echo ">>>>> Installing Python dependencies..."
pip install -r configuration/requirements.txt
 
echo ">>>>> Starting Gunicorn with UvicornWorker..."
exec gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app