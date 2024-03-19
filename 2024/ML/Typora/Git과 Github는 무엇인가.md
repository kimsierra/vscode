###### **my project**

팀원:

김혜선: 리더

김혜발: 코디

김혜라: 문서작성

### **Git과 Github는 무엇인가?**

#### **Git**

- VCS(Version Control System)의 일종으로 프로그램의 버전 관리를 위한 툴.
- 시간(시간에 따른 버전 변화. v1 → v2)과 차원(비슷하지만 조금씩 다른 형상. 원본과 copy&update 본)의 두 축으로 관리를 해준다.

#### ** Github**

- Git으로 관리하는 프로젝트들을 온라인 공간에 공유해서 프로젝트 구성원들이 함께 소프트웨어를 만들어갈 수 있도록 돕는 코드 공유 및 협업 서비스
- 온라인 git 저장소는 모든 업로드와 다운로드를 커밋 단위로 주고 받는다. 팀원 A가 커밋을 해서 버전을 만들어 업로드하면 깃헙 상의 프로젝트는 해당 버전으로 최신화되고, 팀원 B가 완료한 작업을 커밋해서 올리기 위해서는 반드시 깃헙 상의 최신 커밋을 먼저 다운받아서 자기 컴퓨터에 있는 프로젝트에 적용부터 하도록 강제가 된다. 커밋 상의 충돌사항이 있다면 그것도 팀원 B의 컴퓨터에서 병합 등으로 해결 하여야 비로소 자신이 작업한 커밋을 공유 공간에 올릴 수 있다. 즉, 작업은 개개인이 원하는 공간에서 원하는 시간에 하되 공유공간에 올릴 때에는 깃헙이 중간에서 교통 정리를 하여 서로의 작업 간 loss가 발생하지 않도록 해준다.
- 전세계의 많은 오픈소스 프로젝트들이 깃헙에서 공유되고 있다는 점!

------

### **환경설정 (Window 기준)**

- Git & Git bash, Sourcetree (GUI), VS Code 설치
- VS Code에서 터미널 열기 (ctrl + `)
- VS Code 기본 터미널을 git bash로 변경 (ctrl + shift + p → select default profile 검색 → Git bash 선택)

------

### **Git 설정 및 프로젝트 생성**

#### **Git 최초 설정**

```cmd
# 1. 유저 설정
git config --global user.name "username"
git config --global user.email "username@gmail.com"

# 확인
git config --global user.name
git config --global user.email

# 2. 기본 브랜치명 변경
git config --global init.defaultBranch main
git config --global init.defaultBranch
```

 

#### **프로젝트 생성**

- 프로젝트 폴더 생성 후 VS code에서 폴더 열기
- git에서 관리하지 않을 파일 설정 : .gitignore 파일 생성 후 파일에 관리하지 않을 파일 저장
  (https://git-scm.com/docs/gitignore 참조)

```cmd
## 터미널 열어서 폴더 경로에서 git 연동 
git init

## git 현재 상태 확인
git status


## .gitignore 파일 설정
# 모든 file.c
file.c

# 최상위 폴더의 file.c
/file.c

# 모든 .c 확장자 파일
*.c
```

------

### **Git에 파일 반영하기**

```python
## 버전에 파일 담기
git add filename.py

# 모든 파일 담기
git add .

# git add 취소하기
git rm --cached <file>

## 버전으로 묶어주기
# vi 입력모드로 진입
git commit

# 커밋 메세지 한 번에 작성
git commit -m "comment"

# 커밋 이력 확인
git log
```

 

파일에 변경사항이 있는 경우 deleted, modified, added file 모두 git add로 반영해줄 수 있다.

```
# 파일 변경 사항 자세히 보기 k : up, j : down, :q : 닫기
git diff

# add와 commit을 한번에 하기 (untracked file이 없을 때)
git commit -am "comment"
```

------

### **이전 버전으로 돌아가기**

- Reset : 현재 버전을 지우고 이전 버전으로 돌아가기
- Revert : 현재 버전을 그대로 두고 이전 버전으로 돌아가는 commit을 새로 생성
  - 돌아가는 액션도 기록으로 남겨둘 필요가 있을 때
  - 지금까지의 변화는 살리되 특정 버전에서의 작업만 수정이 필요할 때
  - 특히 협업 시에는 공유된 커밋을 삭제하는 것이 매우 크리티컬하다

```
## Reset
# 되돌아갈 시점의 커밋 해시 복사
git reset --hard (돌아갈 커밋 해시)

# 백업한 git 파일로 reset 이전으로 돌아가는 경우 git은 여전히 reset이 적용된 상태를 인식한다
# 현재 커밋 상태로 초기화. 현재는 없지만 reset하면서 다시 생성된 파일은 수동으로 삭제해준다
git reset --hard


## Revert
# 수정할 커밋의 해시를 찾는다
git revert (수정할 커밋 해시)
:wq

# 커밋 수정 내용이 이후 커밋의 코드에 영향을 주는 경우 conflict가 발생하게 된다
# "Replace Lions with Leopards" 커밋을 revert하면 이후 leopard를 수정하는 부분에서 conflict
git revert 6909f6ca6ab597a8b78cfcfc99ee8ca6a85a539a

# 커밋 revert로 삭제가 필요한 leopards.yaml 삭제
git rm leopards.yaml
git revert --continue
:wq

# revert 시에는 commit이 동시에 되는데 commit 없이 revert 하고 싶을 때 
# (다른 액션도 함께 커밋하고 싶을 때)
git revert --no-commit (수정할 커밋 해시)

# 커밋되지 않은 것들을 지우고 현재 커밋 상태로 초기화하고 싶을 때
git reset --hard
```

------

### **Branch** 

#### **Branch는 왜 필요한가?**

- Branch는 분기된 차원으로 프로젝트를 하나 이상의 모습으로 관리해야 할 때
  (실배포용, 테스트 서버용, 새로운 시도용 등)
- 여러 작업들이 각각 독립되어 진행될 때 각각의 차원에서 작업한 뒤 확정된 것을 메인 브랜치에 통합한다

 

#### **Branch 생성/ 이동/ 삭제**

```
# 브랜치 생성
git branch (신규 브랜치 명)

# 브랜치 목록 확인
git branch

# 다른 브랜치로 이동
git switch (신규 브랜치 명)

# 브랜치 생성과 이동을 동시에 하기
git switch -c (신규 브랜치 명)

# 브랜치 삭제하기
# 지워질 브랜치에만 있는 내용의 커밋이 있을 경우(=다른 브랜치로 가져오지 않은 내용이 있는 경우) 
# -d 대신 -D로 강제 삭제
git branch -d (삭제할 브랜치 명)


# 브랜치 이름 변경
git branch -m (기존 브랜치 명) (신규 브랜치 명)

# 여러 브랜치의 내역을 한번에 보기
git log --al --decorate --oneline --graph
```

 

#### **Branch 합치기**

- Merge : 두 브랜치를 한 커밋에 이어붙이는 방식
  - 브랜치 사용 내역을 남길 필요가 있을 때
  - 다른 형태의 merge도 있음



![img](https://blog.kakaocdn.net/dn/dYgvmH/btrWg1B6a0L/HkC24hYXQd36K7FlTbU71K/img.jpg)![img](https://blog.kakaocdn.net/dn/b9ClaD/btrWggzpd01/APTOF9NynXws7jZlErGinK/img.jpg)

https://www.atlassian.com/git/tutorials/merging-vs-rebasing



```
# merge로 합치기

# 합쳐져서 주요 대상이 될 브랜치로 이동
# merge는 reset으로 되돌리기가 가능함. merge하기 전 해당 브랜치의 마지막 시점으로 reset
git switch main
git merge add-coach

# 병합된 브랜치는 삭제
git branch -d add-coach
```

 

- Rebase : 브랜치를 다른 브랜치에 이어붙이는 방식
  - 한 줄로 깔끔히 정리된 내욕을 유지하기 원할 때
  - 이미 팀원들과 공유한 커밋에 대해서는 사용하지 않는 것이 적합함



![img](https://blog.kakaocdn.net/dn/dYgvmH/btrWg1B6a0L/HkC24hYXQd36K7FlTbU71K/img.jpg)![img](https://blog.kakaocdn.net/dn/beuCaY/btrWedXuWgi/47vOlbOuY6ElhKxq9AqeeK/img.jpg)



```
# Rebase로 합치기
# merge와 반대로 합쳐질 브랜치로 이동한다
git switch new-teams
git rebase main

# new-teams 브랜치가 main에 합쳐졌지만 아직 main은 new-teams 브랜치의 끝에 있지 않다.
# 따라서 main 브랜치로 이동 후 new-teams의 시점으로 fast-forward해준다
git merge new-teams

# 합친 브랜치 삭제
git branch -d new-teams
```

 

충돌이 발생하는 경우 - 파일의 같은 위치에 다른 내용이 입력된 상황이라면?

```
## merge에서 충돌이 발생하는 경우
git switch main
git merge conflict-1

# Auto-merging tigers.yaml
# CONFLICT (content): Merge conflict in tigers.yaml
# Automatic merge failed; fix conflicts and then commit the result.

# 당장 충돌 해결이 어렵다면 merge 중단
git merge --abort

# 해결 가능 시 충돌 부분 수정 후 git add, commit으로 병합 완료
git add .
git commit
:wq

## rebase에서 충돌이 발생하는 경우
# 오류 메세지와 git status 확인
# 당장 해결이 어려운 경우 중단
git rebase --abort

# 해결 가능 시 충돌 부분 수정한 뒤 아래 명령어 수행 (continue하여 또 충돌이 있는 지 찾는다)
# 충돌이 해결될 때까지 반복
git add .
git rebase --continue
:wq

# main에서 git merge conflict-2로 merge하여 마무리
git switch main
git merge conflict-2
git branch -d conflict-1
git branch -d conflict-2
```

------

### **Github 사용하기**

- Personal access token 만들기

   

  \- github에 파일을 올릴 때 이 토큰이 필요함

  - 우측 상단의 프로필 - Settings
  - Developer Settings
  - Personal access tokens - Generate new token
  - repo 및 원하는 기능에 체크, 기간 설정 뒤 Generate token
  - 토큰 안전한 곳에 보관해 둘 것

- 토큰 컴퓨터에 저장하기

  - Windows 자격 증명 관리자
  - Windows 자격 증명 선택
  - git:[https://github.com](https://github.com/) 자격 정보 생성
  - 사용자명과 토큰 붙여넣기

- Repository는 프로젝트 단위로 구성

  - Public : 모두에게 공개되는 프로젝트
  - Private : 허용된 인원만 볼 수 있는 프로젝트

- Repository의 settings - collaborators에서 협업할 팀원 추가

------

### **원격 저장소 사용하기**

#### **git과 github 연동하기**

```
# 로컬에 원격 저장소 추가 후 푸시 (repository 명령어 복붙)

# 여기서는 https 프로토콜 사용
# 로컬의 git 저장소에 원격 저장소로의 연결 추가
git remote add origin (원격 저장소 주소)

# 브랜치 명 수정
git branch -M main

# 로컬 저장소의 커밋 내역을 원격으로 push (업로드). origin의 main branch로 push
git push -u origin main


# 원격 저장소 목록보기
git remote
git remote -v

# 원격 지우기 (github repository가 지워지는 것이 아니라 로컬 프로젝트와의 연결만 삭제)
git remote remove (origin 등 원격 이름)
# Github에서 프로젝트 다운받기

# 프로젝트를 다운받고자 하는 폴더에서 우클릭 - Git Bash here
git clone (원격 저장소 주소, https://github.com/gin-girin-grim/git-practice.git)
```

 

#### **Push & Pull**

```
# 원격으로 커밋 밀어올리기 (push)
git push

# 원격으로 커밋 당겨오기 (pull)
git pull
# pull 할 것이 있을 때 push를 해버리면?
git push
# To https://github.com/gin-girin-grim/git-practice.git
# ! [rejected]        main -> main (fetch first)
# error: failed to push some refs to 'https://github.com/gin-girin-grim/git-practice.git'
# hint: Updates were rejected because the remote contains work that you do
# hint: not have locally. This is usually caused by another repository pushing
# hint: to the same ref. You may want to first integrate the remote changes
# hint: (e.g., 'git pull ...') before pushing again.
# hint: See the 'Note about fast-forwards' in 'git push --help' for details.

# 우선 먼저 pull을 하고 push를 해준다
# 1-1. merge 방식
git pull --no-rebase

# 1-2. rebase 방식
# pull 상의 rebase는 협업 시에도 사용 OK
git pull --rebase

# 2. push
git push
# 협업 시 충돌이 발생하는 경우?
# 이후는 merge/rebase 방식과 동일함. 충돌 처리 후 git add ., git commit
git pull --no-rebase
git pull --rebase
# 로컬의 내역을 강제로 push 하기
# 먼저 로컬의 충돌 전 커밋으로 reset 후
git push --force
```

####  

#### **원격의 Branch 다루기**

```
# 로컬에서 브랜치 만들어 원격에 push 해보기
git branch -c from-local

# git push 하면 신규 브랜치에서 어디로 push 할 지 정해져있지 않으니 명시해달라는 에러 발생
git push

# fatal: The current branch from-local has no upstream branch.
# To push the current branch and set the remote as upstream, use
# 
#     git push --set-upstream origin from-local
# 
# To have this happen automatically for branches without a tracking
# upstream, see 'push.autoSetupRemote' in 'git help config'.


# push 해 줄 브랜치를 명시해준다
git push --set-upstream origin from-local
git push -u origin from-local   # 동일한 코드

# 원격 브랜치 목록까지 보기
git branch --all
git branch -a
# 원격의 브랜치를 로컬로 받아오기
# 원격에 브랜치를 생성해도 원격 저장소 상태를 받아오지 않으면 로컬에서 변화를 볼 수 없음
$ git fetch
From https://github.com/gin-girin-grim/git-practice
 * [new branch]      from-remote -> origin/from-remote

git branch -a

# 로컬에도 같은 이름의 브랜치를 생성하여 연결 및 switch
# 원격에서 로컬로 from-remote 브랜치를 복사하고, 이후에도 로컬의 from-remote 브랜치와 
# 원격의 from-remote 브랜치를 연동하겠다는 의미
git switch -t origin/from-remote
# 원격의 브랜치 삭제
git push (원격 이름) --delete (원격의 브랜치 명)
git push origin --delete from-remote
```