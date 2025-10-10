# Iceberg study

- Iceberg hands-on 학습 내용을 기록한다.
- 학습한 내용은 `iceberg/notebooks` 경로에 jupyter notebook 형태로 기록한다.

## Udemy 
* 강의 이름: Apache Iceberg: The Complete Masterclass (Hands-On)
 
<br>

## iceberg-spark-minio 환경 구성 방법
> - Spark, Iceberg, MinIo, Jupyter 를 이용한 Spark-Iceberg 실습 환경 구성
> - 원본 git 저장소: https://github.com/suraj-darekar/iceberg-spark-minio.git

<br>

### Steps to Install 
* CLI Commands
```bash
# docker compose 실행
$ docker-compose -f docker-compose.yaml up -d
또는
# make goal 실행
$ make start.docker.compose.for.iceberg
```

* Verify Services
```bash
  http://localhost:8888/tree/notebooks      - jupyter notebook
  http://localhost:9001      - minio
  http://localhost:18080    - spark history server
```
* Jupyter notebook(http://localhost:8888/)
* Spark history server(http://localhost:18080/)

* MinIO(http://localhost:9001/)
> ID: admin / Password: password

![minio_login_page.png](images/minio_login_page.png)
![minio_home.png](images/minio_home.png)

<br>

### Iceberg files 확인하는 방법
: mino 를 s3 카탈로그 경로로 설정해두었기 때문에 mino 컨테이너의 data 경로에서 자료를 확인할 수 있다.

![iceberg files](./images/how_to_check_iceberg_in_mino.png)

<br>
