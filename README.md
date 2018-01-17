# Docker Workshop

## Przydatne Linki
**Cheatsheet: [LINK](https://www.docker.com/sites/default/files/Docker_CheatSheet_08.09.2016_0.pdf)**

**Instalacja Ubuntu / Windows: [LINK](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/) / [LINK](https://docs.docker.com/docker-for-windows/install/)**

**NVIDIA Docker: [LINK](https://github.com/NVIDIA/nvidia-docker)**

**Publiczne repozytorium obrazów: [LINK](https://hub.docker.com/)**


## Tworzenie kontenerów

```
docker run {PARAMETRY} {OBRAZ}
np. docker run --name ubuntu1604 -v /home/ktagowski/projects:/project -p 9122:22 -it library/ubuntu:16.04
```
#### Parametry instrukcji docker run:

| Parametr | Opis |
| --- | --- |
| **-it**  | Podłączenie do terminala  |
| **--name** {NAZWA}    |  Nadanie nazwy    |
| **-v** /home/ktagowski/projects:/projects | Montowanie folderu gospodarze w zadanym punkcie montowania w konterze |
| **-p** 9122:22 | Mapowanie portu 9122 (host) na 22 (kontener) |
| **library/ubuntu:1604** | library/ubuntu odnosi sie do adresu obrazu, a 1604 oznacza wybrany tag, domyślnie pobierany jest obraz z tagiem latest|

## Obsługa dockera
| Komenda  | Opis  |
|---|---|
| **docker exec -it bash** {ID_KONTENERA} | Utworzenie nowego procesu bash w danym kontenerze i podłączenie go do obecnie używanego terminala|
| **docker ps** | 	Wylistowanie aktywnych kontenerów |
| **docker ps -a** |	Wylistowanie aktywnych wszystkich kontenerów |
| **docker images** |	Wylistowanie obrazów |
| **docker rm** {ID_KONTENERA}  | Usunięcie kontenera |
| **docker rmi** {ID_OBRAZU} |	Usunięcie obrazu |
| **docker start** {ID_KONTENERA} |	Uruchomienie kontenera |
| **docker stop** {ID_KONTENERA} |	Zatrzymanie kontenera |

## Czyszczenie
| Komenda  | Opis  |
|---|---|
| **docker rm -f $(docker ps -aq)** |	Usunięcie wszystkich kontenerów |
| **docker rmi $(docker images -q)** |	Usunięcie wszystkich obrazów |
