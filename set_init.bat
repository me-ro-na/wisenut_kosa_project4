@echo off
set u_name=%username%
@REM 가상환경 서버 설정
call C:\Users\%u_name%\anaconda3\Scripts\activate.bat
call conda create -n pj4 python=3.8
call activate pj4
call conda install -c conda-forge numpy=1.19.5 jupyterlab pandas seaborn xlrd openpyxl pymysql sqlalchemy scikit-learn xgboost tensorflow nltk JPype1 gensim=3.8.3 python-levenshtein
call python -m pip install --no-cache-dir konlpy PyKomoran kss
call pip install Flask
call pip install BeautifulSoup4
call pip install selenium
call deactivate pj4
call conda deactivate

@REM 데이터 베이스
call C:\Windows\System32\cmd.exe /k " "C:\Program Files\MariaDB 10.7\bin\mysql.exe" "--defaults-file=C:\Program Files\MariaDB 10.7\data\my.ini" -uroot -pmariadb" < set_db.sql
echo Done init welcome pj4