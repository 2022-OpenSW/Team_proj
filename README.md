# Team_proj
***2022-2 오픈소스 팀 프로젝트*** <br>
:bulb: <a href="https://github.com/open-mmlab/mmdetection">mmdetection</a>을 이용한 K-fashion 분류 
<br>

💻 __김정현 (팀장)__
* 전체 코드 개발
* Pull Request & Merge
* Train & Test 진행
<p><a href="https://github.com/Jhyunee"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white"></a></p>

💻 __장영서__
* 일부 코드 개발
* PPT 제작 및 발표
<p><a href="https://github.com/j-ys"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white"></a></p>
<br>

> 가상환경 구성
* Anaconda on CPU platform 
* Python 3.8.15, pytorch 1.13.0+cpu<br>
<a href="https://mmdetection.readthedocs.io/en/stable/get_started.html">Followed official doc</a>
<br>

> 데이터셋 구성
* Following coco dataset structure
* Train : Val : Test = 6 : 2 : 2
* 분할 방법
  - 제공 받은 데이터셋 - 하나의 클래스에 대한 데이터가 여러 폴더로 나누어져 존재<br>
    ex. onepiece(dress)는 4개의 폴더로 존재
    1. Train 데이터셋에는 **모든 클래스의 최소 1개 폴더**가 포함되도록
    2. onepiece(dress)와 같이 4개(다수)의 폴더인 경우, 남은 3개의 폴더를 Train, Val, Test에 랜덤 배치
  - Train, Val, Test dataset **동일 데이터 중복 사용 X**
* 경로 설정
  - coco_detection.py 상의 경로에 맞게 구성<br>
  ![image](https://user-images.githubusercontent.com/104143072/207796504-27d05890-836b-46ad-ac9e-17b0a38ad16a.png)<br>

  - 각각의 instances_default.json 내의 file_name 경로에 맞게 구성<br>
  ![image](https://user-images.githubusercontent.com/104143072/207796642-cfe4996e-dc05-48c2-a093-cdd1b84d324e.png)<br>
<br>

> 모델 구성
* Mask-RCNN using resnet50 backbone
* Epoch = 1, Learning rate = 0.0025
<br>

> 학습 실행 방법 <br> 
1. Clone mmdetection in local
2. default_runtime.py, coco.py (in base codes) 파일을 이 레포지토리 코드로 대체<br>
_mmdetection/configs/\_base\_/default_runtime.py_<br>
_mmdetection/mmdet/datasets/coco.py_<br>
3. mmdetecion 디렉토리에서 아래 코드 실행

* Run training <br> 
` python tools/train.py configs/_base_/default_runtime.py `<br>
* Run testing <br> 
` python tools/test.py configs/_base_/default_runtime.py work_dirs\default_runtime/latest.pth --show `
