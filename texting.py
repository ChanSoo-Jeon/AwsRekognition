import boto3

# boto3 클라이언트 초기화
rekognition = boto3.client('rekognition')

# S3 버킷 이름과 파일명 설정
bucket_name = 'cchomework'
file_name = 'text-1.jpg'

response = rekognition.detect_text(
    Image={
        'S3Object': {
            'Bucket': bucket_name,
            'Name': file_name
        }
    }
)

# 감지된 텍스트 출력
if 'TextDetections' in response and len(response['TextDetections']) > 0:
    print("인식된 텍스트:")
    for text_detection in response['TextDetections']:
        print(text_detection['DetectedText'])
else:
    print("텍스트를 찾을 수 없습니다.")