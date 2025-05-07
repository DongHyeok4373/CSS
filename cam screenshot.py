import cv2
import os
import time

def capture_one_frame(index, name):
    base_dir = r"C:\Users\ehdgu\Desktop\foot_dataset"
    save_dir = os.path.join(base_dir, name)
    os.makedirs(save_dir, exist_ok=True)

    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        print(f"❌ 카메라 {index} 열기 실패")
        return

    time.sleep(2)  # 카메라 안정화 시간

    ret, frame = cap.read()
    if ret:
        count = len(os.listdir(save_dir))  # 파일 개수 기반 번호 지정
        save_path = os.path.join(save_dir, f"{name}_{count:03}.jpg")
        success = cv2.imwrite(save_path, frame)
        print(f"✅ {name.upper()} 카메라 → 저장됨: {save_path}" if success else f"❌ 저장 실패")
    else:
        print(f"⚠️ {name.upper()} 카메라 프레임 캡처 실패")

    cap.release()

# 자동 순차 캡처 실행
if __name__ == "__main__":
    cameras = [
        (0, "left"),
        (1, "right"),
        (2, "top")
    ]

    for index, name in cameras:
        capture_one_frame(index, name)

    print("\n🎉 모든 카메라에서 1장씩 자동 촬영 완료!")
