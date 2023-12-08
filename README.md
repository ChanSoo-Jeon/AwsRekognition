# AwsRekognition

![js](https://img.shields.io/badge/amazonaws-569A31?style=for-the-badge&logo=amazonaws&logoColor=white)
![js](https://img.shields.io/badge/amazons3-232F3E?style=for-the-badge&logo=amazons3&logoColor=white)
![js](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white)



1. celebrities - aws의 s3버킷에 들어있는 유명인의 jpg파일을 rekognition.recognize_celebrities를 사용하여 유명인을 탐색하고, 해당 인물의 감정 상태 출력
2. texting - aws의 s3버킷에 들어있는 텍스트가 그려져 있는 jpg파일에서 rekognition.detect_text를 사용하여 텍스트를 인식하여 출력
3. pricechk - 동영상을 프레임별로 잘라서 rekognition으로 객체 탐색 후, 가격 매핑하여 label과 price와 jpg출력
