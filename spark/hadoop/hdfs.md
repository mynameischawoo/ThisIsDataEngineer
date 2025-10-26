# Hadoop - HDFS
> Spark 학습 과정에서 같이 공부한 Hadoop, HDFS 내용을 기록한다.

## What is HDFS(Hadoop Distributed File System)?
* 하둡 클러스터에 데이터 파일을 저장하고 검색(Read)할 수 있도록 지원한다.


## Main Components of HDFS?
| Extentions   | Desc |
|--------------|--------------------------------|
| NM(Name Mode) | 파일 시스템의 메타데이터(파일 경로, 블록 위치)를 관리하는 중앙 서버 |
| DM(Data Node) | 실제 데이터 블록을 저장하고 클라이언트/NameNode 요청에 따라 블록을 읽고 쓰는 저장소 노드 |

## HDFS Architecture of a Hadoop Cluster

```mermaid
flowchart TD


    %% 하둡 마스터 노드 표시
    subgraph MasterNode["Node-1 (Master)"]
        NM["HDFS NN(NameNode)"]
    end
    

    %% 하둡 워커 노드 표시
    subgraph WorkerNode1["Node-2 (Workers)"]
        NM1["HDFS DN(DataNode)"]
    end
    subgraph WorkerNode2["Node-3 (Workers)"]
        NM2["HDFS DN(DataNode)"]
    end
    subgraph WorkerNode3["Node-42 (Workers)"]
        NM3["HDFS DN(DataNode)"]
    end

    %% 하둡 마스터, 워커 관계도
    
    MasterNode <--> WorkerNode1
    MasterNode <--> WorkerNode2
    MasterNode <--> WorkerNode3
    
```

## HDFS File Write Sequence

```mermaid
sequenceDiagram
autonumber
participant Client as Client (사용자)
participant NN as NameNode (메타데이터 관리)
participant DN1 as DataNode-1
participant DN2 as DataNode-2
participant DN3 as DataNode-3

%% --- Write 과정 ---
Client->>NN: 큰 데이터 파일 복사(write) 요청
NN-->>Client: 블록 저장할 DataNode 리스트 반환 (예: DN1, DN2, DN3)

par 블록 분산 저장
  Client->>DN1: 데이터 블록1 전송 (기본 128MB)
  Client->>DN2: 데이터 블록2 전송 (기본 128MB)
  Client->>DN3: 데이터 블록3 전송 (기본 128MB)
end

DN1-->>NN: 블록 저장 완료 보고 (BlockID, 위치)
DN2-->>NN: 블록 저장 완료 보고 (BlockID, 위치)
DN3-->>NN: 블록 저장 완료 보고 (BlockID, 위치)
NN->>NN: 파일 메타데이터 업데이트<br/>파일명, 경로, 사이즈, 블록ID, 블록 시퀀스, 블록 위치

```

## HDFS File Read Sequence

```mermaid
sequenceDiagram
autonumber
participant Client as Client (사용자)
participant NN as NameNode (메타데이터 관리)
participant DN1 as DataNode-1
participant DN2 as DataNode-2
participant DN3 as DataNode-3


%% --- Read 과정 ---
Client->>NN:파일 읽기(read) 요청
NN-->>Client: 해당 파일의 블록 메타데이터 반환<br/>(BlockID, 위치)
par 블록 병렬 읽기
  Client->>DN1: 블록1 읽기 요청
  Client->>DN2: 블록2 읽기 요청
  Client->>DN3: 블록3 읽기 요청
end
DN1-->>Client: 블록1 전송
DN2-->>Client: 블록2 전송
DN3-->>Client: 블록3 전송
Client->>Client: 블록들을 재조합 → 원본 파일 복원

```

## What is HDFS Metadata items?

| Items | Desc |
|------|------|
| **File Name (파일 이름)** | HDFS에 저장된 파일의 이름 |
| **HDFS File Path (HDFS 파일 경로)** | 파일이 저장된 HDFS 경로 (예: `/user/hadoop/input/data.txt`) |
| **File Size (파일 크기)** | 파일 전체 크기(바이트 단위) |
| **File Blocks (파일 블록)** | 파일이 분할된 블록 단위 데이터 조각들 |
| **Block ID (블록 아이디)** | 각 블록을 식별하기 위한 고유 ID |
| **Block Sequence (블록 순서)** | 파일을 이루는 블록들의 순서 정보 |
| **Block Location (블록 위치)** | 각 블록이 저장된 DataNode의 위치 정보 |
