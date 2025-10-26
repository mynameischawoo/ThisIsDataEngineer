# Hadoop - HDFS
> Spark 학습 과정에서 같이 공부한 Hadoop, HDFS 내용을 기록한다.

## What is HDFS(Hadoop Distributed File System)?
* 하둡 클러스터에 데이터 파일을 저장하고 검색할 수 있도록 지원한다.


## Main Components of HDFS?
| Extentions   | Desc |
|--------------|--------------------------------|
| NM(Name Mode) | 파일 시스템의 메타데이터(파일 경로, 블록 위치)를 관리하는 중앙 서버 |
| DM(Data Node) | 실제 데이터 블록을 저장하고 클라이언트/NameNode 요청에 따라 블록을 읽고 쓰는 저장소 노드 |