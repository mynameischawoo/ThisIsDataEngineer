# Iceberg study

## Udemy 
* 강의 이름: Apache Iceberg: The Complete Masterclass (Hands-On)
 

## iceberg-spark-minio 환경 구성
> Spark, Iceberg, MinIo, Jupyter 를 이용한 Spark-Iceberg 실습 환경 구성

> git 저장소: https://github.com/suraj-darekar/iceberg-spark-minio.git

### Steps to Install 
* CLI Commands
```bash
docker-compose -f docker-compose.yaml up -d
```

* Verify Services
```bash

  http://localhost:8888/tree - jupyter notebook
  http://localhost:9001      - minio
```

* MinIO(http://localhost:9001/)
> ID: admin / Password: password

![minio_login_page.png](images/minio_login_page.png)
![minio_home.png](images/minio_home.png)