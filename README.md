# Neostack Gateway

## Components

![MeshSerial Architecture-GW Applications Relationship drawio](https://user-images.githubusercontent.com/24751868/176628396-7ce526db-a884-4695-a62a-03965e51c859.png)

- Mesh API: Bluetooth Mesh Serial 모델을 조작하기 위한 API 서비스
- REST API: FastAPI를 기반으로 Gateway를 REST API를 통해 조작하는 서비스
- EventProxy: DB 모델, Mesh API, REST API, Gateway Application에 명령을 전달하는
프록시 서비스.
- GW Application: Gateway의 동작을 수행하는 application 서비스
