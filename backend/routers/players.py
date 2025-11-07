from fastapi import APIRouter

router = APIRouter(prefix="/players", tags=["Players"])

players = [
    {"id": 1, "name": "김준영", "birth": "2003.01.28", "position": "G", "height": 181, "weight": 72, "school": "건국대학교", "status": "대학 졸업 예정"},
    {"id": 2, "name": "프레디", "birth": "2003.02.02", "position": "C", "height": 203, "weight": 100, "school": "건국대학교", "status": "대학 졸업 예정"},
    {"id": 3, "name": "하주형", "birth": "2003.06.23", "position": "G", "height": 183, "weight": 75, "school": "건국대학교", "status": "대학 졸업 예정"},
    {"id": 4, "name": "신우철", "birth": "2002.07.08", "position": "G", "height": 180, "weight": 80, "school": "울산대학교", "status": "대학 졸업 예정"},
    {"id": 5, "name": "이민철", "birth": "2003.06.20", "position": "G", "height": 186, "weight": 78, "school": "명지대학교", "status": "대학 졸업 예정"},
    {"id": 6, "name": "박지환", "birth": "2003.11.17", "position": "G", "height": 192, "weight": 84, "school": "명지대학교", "status": "대학 졸업 예정"},
    {"id": 7, "name": "최홍준", "birth": "2002.05.31", "position": "G", "height": 177, "weight": 78, "school": "명지대학교", "status": "대학 졸업 예정"},
    {"id": 8, "name": "김휴범", "birth": "2003.08.20", "position": "G", "height": 180, "weight": 73, "school": "중앙대학교", "status": "대학 졸업 예정"},
    {"id": 9, "name": "송재환", "birth": "2003.04.26", "position": "G", "height": 188, "weight": 85, "school": "단국대학교", "status": "대학 졸업 예정"},
    {"id": 10, "name": "최강민", "birth": "2002.07.08", "position": "G", "height": 188, "weight": 88, "school": "단국대학교", "status": "대학 졸업 예정"},
    {"id": 11, "name": "홍동명", "birth": "2003.05.09", "position": "G", "height": 186, "weight": 79, "school": "상명대학교", "status": "대학 졸업 예정"},
    {"id": 12, "name": "이주민", "birth": "2002.10.21", "position": "F", "height": 194, "weight": 96, "school": "성균관대학교", "status": "대학 졸업 예정"},
    {"id": 13, "name": "이건영", "birth": "2003.06.09", "position": "G", "height": 181, "weight": 77, "school": "성균관대학교", "status": "대학 졸업 예정"},
    {"id": 14, "name": "노완주", "birth": "2003.06.08", "position": "F", "height": 193, "weight": 91, "school": "성균관대학교", "status": "대학 졸업 예정"},
    {"id": 15, "name": "신지원", "birth": "2003.05.18", "position": "F, C", "height": 197, "weight": 97, "school": "한양대학교", "status": "대학 졸업 예정"},
    {"id": 16, "name": "박민재", "birth": "2003.08.04", "position": "F", "height": 195, "weight": 84, "school": "한양대학교", "status": "대학 졸업 예정"},
    {"id": 17, "name": "김선우", "birth": "2003.07.28", "position": "G", "height": 175, "weight": 71, "school": "한양대학교", "status": "대학 졸업 예정"},
    {"id": 18, "name": "임정현", "birth": "2002.08.11", "position": "F", "height": 192, "weight": 89, "school": "동국대학교", "status": "대학 졸업 예정"},
    {"id": 19, "name": "지용현", "birth": "2002.03.19", "position": "C", "height": 201, "weight": 97, "school": "동국대학교", "status": "대학 졸업 예정"},
    {"id": 20, "name": "이상현", "birth": "2003.12.13", "position": "G", "height": 189, "weight": 77, "school": "동국대학교", "status": "대학 졸업 예정"},
    {"id": 21, "name": "김민규", "birth": "2002.04.19", "position": "F", "height": 196, "weight": 90, "school": "고려대학교", "status": "대학 졸업 예정"},
    {"id": 22, "name": "박정환", "birth": "2003.03.16", "position": "G", "height": 180, "weight": 76, "school": "고려대학교", "status": "대학 졸업 예정"},
    {"id": 23, "name": "이건희", "birth": "2003.12.14", "position": "G", "height": 186, "weight": 80, "school": "고려대학교", "status": "대학 졸업 예정"},
    {"id": 24, "name": "지승현", "birth": "2003.04.11", "position": "F", "height": 193, "weight": 92, "school": "경희대학교", "status": "대학 졸업 예정"},
    {"id": 25, "name": "안세준", "birth": "2002.04.10", "position": "F", "height": 196, "weight": 90, "school": "경희대학교", "status": "대학 졸업 예정"},
    {"id": 26, "name": "우상현", "birth": "2003.04.01", "position": "G", "height": 189, "weight": 82, "school": "경희대학교", "status": "대학 졸업 예정"},
    {"id": 27, "name": "이영웅", "birth": "2003.08.21", "position": "G", "height": 181, "weight": 77, "school": "조선대학교", "status": "대학 졸업 예정"},
    {"id": 28, "name": "안성우", "birth": "2003.06.07", "position": "G", "height": 184, "weight": 82, "school": "연세대학교", "status": "대학 졸업 예정"},
    {"id": 29, "name": "이규태", "birth": "2002.04.04", "position": "F, C", "height": 199, "weight": 99, "school": "연세대학교", "status": "대학 졸업 예정"},
    {"id": 30, "name": "여찬영", "birth": "2004.01.08", "position": "G", "height": 182, "weight": 74, "school": "건국대학교", "status": "대학 재학"},
    {"id": 31, "name": "김윤성", "birth": "2004.01.19", "position": "F, C", "height": 198, "weight": 90, "school": "성균관대학교", "status": "대학 재학"},
    {"id": 32, "name": "강성욱", "birth": "2004.09.15", "position": "G", "height": 184, "weight": 75, "school": "성균관대학교", "status": "대학 재학"},
    {"id": 33, "name": "배형직", "birth": "2004.01.03", "position": "G", "height": 178, "weight": 75, "school": "울산대학교", "status": "대학 재학"},
    {"id": 34, "name": "이한결", "birth": "2003.10.17", "position": "G", "height": 181, "weight": 74, "school": "동국대학교", "status": "대학 재학"},
    {"id": 35, "name": "김명진", "birth": "2003.08.14", "position": "F", "height": 199, "weight": 92, "school": "동국대학교", "status": "대학 재학"},
    {"id": 36, "name": "백승혁", "birth": "2004.03.31", "position": "G", "height": 185, "weight": 76, "school": "동국대학교", "status": "대학 재학"},
    {"id": 37, "name": "윤기찬", "birth": "2004.07.29", "position": "F", "height": 194, "weight": 93, "school": "고려대학교", "status": "대학 재학"},
    {"id": 38, "name": "문유현", "birth": "2004.06.08", "position": "G", "height": 181, "weight": 81, "school": "고려대학교", "status": "대학 재학"},
    {"id": 39, "name": "강지훈", "birth": "2003.07.22", "position": "C", "height": 203, "weight": 99, "school": "연세대학교", "status": "대학 재학"},
    {"id": 40, "name": "강태현", "birth": "2005.04.08", "position": "G, F", "height": 198, "weight": 85, "school": "연세대학교", "status": "대학 재학"},
    {"id": 41, "name": "이유진", "birth": "2005.01.14", "position": "G, F", "height": 199, "weight": 84, "school": "연세대학교", "status": "대학 재학"},
    {"id": 42, "name": "양우혁", "birth": "2007.05.03", "position": "G", "height": 181, "weight": 73, "school": "삼일고등학교", "status": "고교 졸업 예정"},
    {"id": 43, "name": "송한준", "birth": "2007.06.02", "position": "G, F", "height": 198, "weight": 85, "school": "광신방송예술고등학교", "status": "고교 졸업 예정"},
    {"id": 44, "name": "임동일", "birth": "2003.12.23", "position": "C", "height": 214, "weight": 113, "school": "중앙대학교", "status": "대학 졸업 예정"},
    {"id": 45, "name": "김민규", "birth": "2006.05.21", "position": "G", "height": 178, "weight": 75, "school": "안양고등학교", "status": "고교 졸업"},
    {"id": 46, "name": "안다니엘", "birth": "2004.02.02", "position": "G", "height": 184, "weight": 80, "school": "사이먼 프레이저 대학교", "status": "대학 졸업 예정"},
]

top_names = ["문유현", "윤기찬", "강지훈", "이규태", "이유진", "김명진", "강성욱", "프레디", "최강민", "양우혁"]

players = sorted(players, key=lambda p: top_names.index(p["name"]) if p["name"] in top_names else len(top_names))

@router.get("/")
def get_players():
    return players
