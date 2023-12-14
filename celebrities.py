import boto3

# boto3 클라이언트 초기화
rekognition = boto3.client('rekognition')

# S3 버킷 이름과 파일명 설정
bucket_name = 'bucket_name'
file_name = 'file_name'

# Rekognition을 이용하여 유명인 인식
response_celeb = rekognition.recognize_celebrities(
    Image={
        'S3Object': {
            'Bucket': bucket_name,
            'Name': file_name
        }
    }
)

# 유명인을 찾았는지 확인하고 정보 출력
if 'CelebrityFaces' in response_celeb and len(response_celeb['CelebrityFaces']) > 0:
    celebrities = response_celeb['CelebrityFaces']
    for celebrity in celebrities:
        print("인물 이름:", celebrity['Name'])

        # 감정 상태 분석
        response_faces = rekognition.detect_faces(
            Image={
                'S3Object': {
                    'Bucket': bucket_name,
                    'Name': file_name
                }
            },
            Attributes=['ALL']
        )

        # 얼굴을 찾았는지 확인하고 감정 상태 출력
        if 'FaceDetails' in response_faces and len(response_faces['FaceDetails']) > 0:
            face_details = response_faces['FaceDetails']
            for face_detail in face_details:
                if 'Emotions' in face_detail and len(face_detail['Emotions']) > 0:
                    emotions = face_detail['Emotions']
                    highest_confidence_emotion = max(emotions, key=lambda x: x['Confidence'])
                    print("Type:", highest_confidence_emotion['Type'])
                    print("confidence:", highest_confidence_emotion['Confidence'])
                else:
                    print("감정 상태를 찾을 수 없습니다.")
        else:
            print("얼굴을 찾을 수 없습니다.")
else:
    print("유명인을 찾을 수 없습니다.")
