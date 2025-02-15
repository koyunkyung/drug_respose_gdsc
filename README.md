# 세포주 및 약물 특성을 활용한 약물 반응성 예측

## 개요

**GDSC (Genomics of Drug Sensitivity in Cancer)** 데이터셋을 활용해 특정 세포주와 약물의 특성에 따른 약물 반응성(`ln_ic50`)을 예측하는 것을 목표로 합니다. 트랜스포머 기반 딥러닝 모델을 설계하여 약물-세포주 간의 상호작용을 학습하며, 이를 통해 암 치료에서 효과적인 약물을 추천할 수 있는 모델을 개발합니다. 바이오 데이터의 다양한 임베딩 및 인코딩 방식에 따른 모델의 성능 차이를 비교하는 것을 주요 목표로 합니다.

---

## 파일 구조

- **`data/`**
  - `processed/`: 필터링 후의 데이터셋과 임베딩 후의 데이터셋
  - `raw/`: 원본 GDSC 데이터와 cell line-disease의 연결 정보를 담고 있는 annotations 데이터

- **`experiments/`**
  - `best_model.pth`: 학습된 트랜스포머 모델
  - `training_log.txt`: 학습 로그 파일
  - `hyperparameter_tuning.py`: 하이퍼파라미터 튜닝 스크립트

- **`notebooks/`**
  - `exploratory_analysis.ipynb`: 분석에 사용된 변수들의 통계적 특성 파악
  - `training_visualization.ipynb`: 모델 학습 과정 시각화

- **`src/`**
  - `preprocessing/`: 데이터 전처리 스크립트, 다양한 임베딩 함수들, SMILES 데이터를 받아오는 함수 스크립트
  - `train.py`: 트랜스포머 모델 학습 코드
  - `evaluate.py`: 모델 성능 평가 코드
  - `model.py`: 트랜스포머 모델 정의
  - `main.py`: 설계된 함수를 모두 실행해 모델의 성능을 보여주는 코드

---

## 사용된 기술

이 프로젝트는 PyTorch를 기반으로 한 딥러닝 프레임워크를 사용하며, 주요 기술은 다음과 같습니다:

- **트랜스포머 모델**:
  - 세포주와 약물의 임베딩 벡터를 학습하여 상호작용을 예측합니다.
- **데이터 전처리**:
  - 세포주(`cell_line_name`) 및 약물(`drug_name`) 변수를 LabelEncoder, scBERT 사전학습 모델, rdKit 등을 사용해 모델에 적합한 형태로 변환합니다.
- **평가 메트릭**:
  - RMSE, R² 스코어를 활용하여 예측 성능을 평가합니다.

---

GDSC 데이터셋은 암 치료에서 약물의 효능과 관련된 세포주 및 약물 특성을 포함하고 있습니다. 데이터셋은 다음의 링크에서 확인할 수 있습니다:
- [GDSC 공식 웹사이트](https://www.cancerrxgene.org/)

---
