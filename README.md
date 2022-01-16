# NTU_project2_Phoneme Classification

## 專案介紹
Framewise phoneme prediction from speech.

train a deep neural network classifier to predict the phonemes for each frame from the speech corpus TIMIT.

![image](https://user-images.githubusercontent.com/77257138/148779391-04dbe551-cdd2-4991-b02d-44ad73037a3d.png)
## 軟硬體配置
* CPU: Intel(R) Xeon(R) (6-cores)
* GPU: Tesla K80 (11.44GB)
* OS： Window10
* Pytorch: 1.10.0
* keras: 2.7.0
* tensorflow: 2.7.0
* Memory: 12.69GB
## 資料來源
The DARPA TIMIT Acoustic-Phonetic Continuous Speech Corpus (TIMIT)

The TIMIT corpus of reading speech has been designed to provide speech data for the acquisition of acoustic-phonetic knowledge and for the development and evaluation of 
automatic speech recognition systems.

link: https://academictorrents.com/details/34e2b78745138186976cbc27939b1b34d18bd5b3
## 資料基本資訊
training dataset shape: (1229932, 429)  

testing dataset shape: (451552, 429)


## 前處理
Acoustic Features(聲學特徵) - MFCCs (Mel Frequency Cepstral Coefficients)

![image](https://user-images.githubusercontent.com/77257138/148779813-09c935f8-efd3-458b-bfe1-73d5b00c7ee0.png)
![image](https://user-images.githubusercontent.com/77257138/148779831-68fd8f84-2ad0-4ab4-b0b6-d2afae49705d.png)

## 模型

## Metrics
CROSSENTROPYLOSS

![image](https://user-images.githubusercontent.com/77257138/148780873-c5a60568-bc3b-4494-87c3-fe4bd144974a.png)

Note:This criterion combines LogSoftmax and NLLLoss in one single class.
## 成果
epoch: 20
* Train Acc: 0.790643 Loss: 0.636623 
* Val Acc: 0.699732 loss: 0.964269
## Reference
https://speech.ee.ntu.edu.tw/~hylee/ml/2021-spring.html
