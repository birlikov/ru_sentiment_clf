docker run -v "$PWD":/usr/workdir -p 80:80 -ti ru_sentiment_clf_image /bin/bash -c "python web_app.py"
