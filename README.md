# Activate virtual env
source streamlit-env/bin/activate

# Run hello_world.py
streamlit run hello_world.py --server.enableCORS false --server.enableXsrfProtection false

# Pasos para subirlo a Producción
git add .

git commit -m "add netflix"

git push origin main