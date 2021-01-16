
# Movies CRUD
 
  

영화 정보와 관련된 CRUD 기능을 Restful API로 구현한 과제입니다.
본 과제는 Python 3.8, Django 3.1 에서 작업하였습니다.
  


## Installation
- Python이 설치되지 않았다면 3.8 이상의 버전으로 설치 

### 1. Clone repository 

```sh
git clone https://github.com/ecila7290/movie_assignment.git
```
### 2. Dependency 설치
```sh
pip install -r requirements.txt
```

## Setup

### 1.  초기 세팅
- 각 명령은 프로젝트 최상위 디렉토리(/movie_assignment) 에서 실행합니다.

	#### 1-1. SECRET_KEY 설정
	Django에서 signature 암호화를 위해 제공되는 SECRET_KEY는, GitHub의 Guardian에 의해 업로드할 수 없습니다. 따라서 ```/movie_assignment/movie_assignment/settings.py```의 ```SECRET_KEY = my_settings.SECRET_KEY```에서 볼 수 있듯 별도의 파일에 작성하였고, gitignore를 통해 git이 추적하지 않도록 하였습니다.
	그렇기 때문에 프로젝트를 clone 후 my_settings.py를 최상위 디렉토리에 생성하여 SECRET_KEY를 다음과 같이 작성합니다.
	```python
	# my_settings.py
	SECRET_KEY='SECRET'
	```
	테스트용으로 'SECRET' 으로  만들었지만 더 안전한 키가 필요할 경우 [Djecrety | Django Secret Key Generator](https://djecrety.ir/) 와 같은 곳에서 무작위 키를 생성할 수 있습니다.

	 #### 1-2. 데이터 모델 migration
	 models.py의 스키마를 데이터베이스에 migrate하기 위해 아래 명령을 실행합니다. 
	 ```python
	 python manage.py makemigrations 
	 python manage.py migrate
	```
	연결되는 데이터베이스는 기본 설정인 sqlite3 이며 ```/movie_assignment/movie_assignment/settings.py```의 ```DATABASES```에서 변경할 수 있습니다.

	#### 1-3. sample data 입력
	테스트용 샘플 데이터를 다음 명령을 통해 데이터베이스에 넣을 수 있습니다.
	```python
	python data_uploader.py
	```


### 2. 서버 실행
API가 잘 작동하는지 확인하기 위해 서버를 실행시켜야 합니다.

```python
python manage.py runserver
```

위 명령을 실행하면 서버가 localhost에서 실행되고, Postman, Curl 등으로 API가 제대로 동작하는지 확인할 수 있습니다.
다만 runserver 명령은 배포에는 적합하지 않으므로 테스트용으로만 사용하는 것을 권장합니다.

### 3. Unit test
```/movie_assignment/movie/test.py```에 unit test를 작성하였습니다.
unit test를 실행하려면 프로젝트 최상위 디렉토리에서 다음과 같이 명령을 입력하면 됩니다.
```python
python manage.py test
```

## API

API는 아래 Documentation에서 확인하실 수 있습니다.

https://documenter.getpostman.com/view/13210820/TVzVhvU8
