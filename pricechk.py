import boto3
import cv2
import os

object_images = {
    'Laptop': 'laptop.JPG',
    'Mobile Phone': 'phone.JPG',
    'Headphones': 'headphone.JPG'
}

#AWS 계정 정보
aws_access_key_id = ''
aws_secret_access_key = ''
aws_region = ''

# AWS Rekognition 클라이언트 생성
rekognition = boto3.client(
    'rekognition',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)

# 비디오 파일 경로
video_path = 'your_video.mp4'
printed_labels = set()
# OpenCV를 사용하여 비디오 읽기
cap = cv2.VideoCapture(video_path)

frame_count = 0
frame_rate = cap.get(cv2.CAP_PROP_FPS)
frame_interval = int(frame_rate)

#object 가격 매핑
object_prices = {
    'Laptop': 'KRW 2,390,000',
    'Mobile Phone': 'KRW 999,900',
    'Headphones': 'KRW 494,000'
}

# 프레임별로 처리
while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    frame_count += 1

    if frame_count % frame_interval != 0:
        continue

    # 프레임 파일로 저장
    frame_filename = f"frame_{frame_count}.jpg"
    cv2.imwrite(frame_filename, frame)

    # Rekognition으로 객체 감지
    with open(frame_filename, 'rb') as image:
        response = rekognition.detect_labels(
            Image={'Bytes': image.read()},
            MaxLabels=10,  # 최대 레이블 수
            MinConfidence=99  # 최소 정확도
        )

        found_objects = {}
        for label in response['Labels']:
            if label['Name'] in object_prices and label['Confidence'] >= 99: #정확도 99이상만 체크
                price = object_prices[label['Name']]
                image_path = object_images[label['Name']]
                if label['Name'] not in printed_labels:  # 중복 체크
                    found_objects[label['Name']] = {'price': price, 'image_path': image_path}
                    printed_labels.add(label['Name'])

        if found_objects:
            print(f"Frame {frame_count} Detected Objects, Prices, and Images:")
            for obj, data in found_objects.items():
                print(f"Object: {obj}, Price: {data['price']}")
                image = cv2.imread(data['image_path'])
                cv2.imshow(f"{obj}", image)
                cv2.waitKey(3000) #이미지를 3초간 보여줌 5000->5초
                # 이미지를 보여준 후 자동으로 창을 닫음
                cv2.destroyAllWindows()

    #저장된 frame images 삭제
    os.remove(frame_filename)


cap.release()
cv2.destroyAllWindows()
