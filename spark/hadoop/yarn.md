# Hadoop - YARN
> Spark 학습 과정에서 같이 공부한 Hadoop, YARN 내용을 기록한다.

## What is Hadoop?
* 하둡은 YARN, HDFS, Map/Reduce 세 가지 핵심 기능을 제공하는 분산형 데이터 처리 플랫폼이다.

## What is YARN(Yet Another Resource Manager)?
- YARN은 하둡의 리소스 관리자 매니저(클러스터 운영 체제)이다.


## What is Role of YARN?
- 여러 애플리케이션을 Hadoop 클러스터에서 실행하고 애플리케이션 간에 리소스를 공유할 수 있도록 한다.

## Main Components of YARN?
| Extentions   | Desc |
|--------------|--------------------------------|
| RM(Resource Manager) | 클러스터 전체 자원(CPU, 메모리)을 스케줄링·할당하는 중앙 관리자 |
| NM(Node Manager) | 각 노드에서 컨테이너 실행·모니터링을 담당하는 에이전트 |
| AM(Application Master) | 특정 애플리케이션의 실행을 관리하며 RM에 자원 요청하고 NM에 컨테이너 실행 지시 |

## YARN Architecture of a Hadoop Cluster
```mermaid
flowchart TD
    subgraph MasterNode["Node-1 (Master)"]
        NN["HDFS NameNode"]
        RM["YARN RM(ResourceManager)"]
    end

    subgraph WorkerNode1["Node-2 (Workers)"]
        DN1["HDFS DataNode"]
        NM1["YARN NM(NodeManager)"]
    end

    subgraph WorkerNode2["Node-3 (Workers)"]
        DN2["HDFS DataNode"]
        NM2["YARN NM(NodeManager)"]
    end

    subgraph WorkerNode3["Node-4 (Workers)"]
        DN3["HDFS DataNode"]
        NM3["YARN NM(NodeManager)"]
    end

    MasterNode <--> WorkerNode1
    MasterNode <--> WorkerNode2
    MasterNode <--> WorkerNode3

```
* NM은 정기적으로 RM에게 각 노드의 상태를 보고한다.

## How to Execute an Application in a Hadoop Cluster
>  클라이언트는 하둡 클러스터 RM에게 애플리케이션을 제출해야한다.
```mermaid
flowchart TD


    %% Client
    Client["👤 Client"]
    %% Client → RM 애플리케이션 제출
    Client -.->|Submit Application| RM

    %% 하둡 마스터 노드 표시
    subgraph MasterNode["Node-1 (Master)"]
        RM["YARN RM(ResourceManager)"]
    end
    

    %% 하둡 워커 노드 표시
    subgraph WorkerNode1["Node-2 (Workers)"]
        NM1["YARN NM(NodeManager)"]
        AM1["AM(ApplicationMaster)"]
    end

    subgraph WorkerNode2["Node-3 (Workers)"]
        NM2["YARN NM(NodeManager)"]
    end

    subgraph WorkerNode3["Node-4 (Workers)"]
        NM3["YARN NM(NodeManager)"]

    end

    %% 하둡 마스터, 워커 관계도
    
    MasterNode <--> WorkerNode1
    MasterNode <--> WorkerNode2
    MasterNode <--> WorkerNode3
    RM -.->|AM 실행 요청| NM1
    NM1 -.->|AM 실행| AM1
```

<br/>

* Application Master 컨테이너는 제출한 애플리케이션 코드를 실행한다.
* 이 때, 컨테이너는 CPU, Memory 리소스 집합체를 의미한다.
### Application submission and execution sequence

<br/>

```mermaid
sequenceDiagram
autonumber
participant Client as Client (사용자)
participant RM as ResourceManager
participant AM as ApplicationMaster
participant NM as NodeManager
participant C as Containers

Client->>RM: 애플리케이션 실행 요청 제출
RM->>NM: 첫 컨테이너 할당 지시 (ApplicationMaster 실행)
NM->>AM: ApplicationMaster 컨테이너 시작
AM->>RM: 추가 리소스(컨테이너) 요청
RM->>AM: 컨테이너 리스트 반환
AM->>NM: 컨테이너 생성 요청
NM->>C: 컨테이너 실행 (태스크 수행)
C->>AM: 작업 결과/진행 상황 보고
NM->>RM: 주기적으로 노드 상태 보고 
AM->>RM: 애플리케이션 종료 보고 (성공/실패)
RM->>Client: 애플리케이션<br/>실행 상태/로그 보고
```

* 즉, 각 애플리케이션은 서로 다른 AM 컨테이너 안에서 실행 된다.