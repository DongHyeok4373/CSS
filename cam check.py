import cv2

def check_available_cameras(max_tested=10):
    print("🔍 사용 가능한 카메라 탐색 중...\n")
    available = []
    for i in range(max_tested):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"✅ 카메라 {i} 인식됨")
            available.append(i)
            cap.release()
        else:
            print(f"❌ 카메라 {i} 없음")
    return available

if __name__ == "__main__":
    cams = check_available_cameras()
    print(f"\n🎯 인식된 카메라 인덱스 목록: {cams}")
