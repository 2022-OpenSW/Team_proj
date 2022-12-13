# Team_proj
***2022-2 오픈소스 팀 프로젝트*** <br>
> mmdetection을 이용한 K-fashion 분류


* 김정현(팀장)
* 장영서
<br>

> 학습 실행 방법 <br> 
1. mmdetection clone
2. default_runtime.py, coco.py 파일을 위 코드로 대체
3. mmdetecion 디렉토리에서 아래 코드 실행

* Run training <br> 
` python tools/train.py configs/_base_/default_runtime.py `<br>
* Run testing <br> 
` python tools/test.py configs/_base_/default_runtime.py work_dirs\default_runtime/latest.pth --show `
