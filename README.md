# Team_proj
***2022-2 오픈소스 팀 프로젝트*** <br>
> mmdetection을 이용한 K-fashion 분류


* 김정현(팀장)
* 장영서
<br>

> 가상환경 구성
* Anaconda on CPU platform <br>
<a href="https://mmdetection.readthedocs.io/en/stable/get_started.html">Followed official doc </a>
<br>

> 데이터셋 구성
* Train : Val : Test = 6 : 2 : 2
* 분할 방법
  - 제공 받은 데이터셋에는 하나의 클래스에 대한 데이터가 여러 폴더로 나누어진 경우가 있었음
    * ex. onepiece(dress)는 4개의 폴더가 존재
      1. Train 데이터셋에는 모든 클래스의 최소 1개 폴더가 포함되도록
      2. onepiece(dress)와 같이 4개의 폴더인 경우에 남은 3개의 폴더를 Train, Val, Test에 랜덤 배치
<br>

> 모델 구성
* 이용 모델: Mask-RCNN using resnet 50 backbone
* Epoch = 1, Learning rate = 0.0025
<br>

> 학습 실행 방법 <br> 
1. Clone mmdetection in local
2. default_runtime.py, coco.py (in base codes) 파일을 위 코드로 대체<br>
_mmdetection/configs/\_base\_/default_runtime.py_<br>
_mmdet/datasets/coco.py_<br>
3. mmdetecion 디렉토리에서 아래 코드 실행

* Run training <br> 
` python tools/train.py configs/_base_/default_runtime.py `<br>
* Run testing <br> 
` python tools/test.py configs/_base_/default_runtime.py work_dirs\default_runtime/latest.pth --show `
