import subprocess
import os

def run_git(args, env=None):
    git_exe = r"C:\Program Files\Git\cmd\git.exe"
    cmd = [git_exe] + args
    res = subprocess.check_output(cmd, env=env, text=True)
    return res.strip()

commits = [
    ("6ef75901ff64d3349692385c61d0100e67d71cd1", [], "🎉 init: 프로젝트 초기화 및 Data Analysis Tutor 기본 뼈대 구성"),
    ("a5e15c21ab662083d8ebe018d081bcfae6be6b59", ["6ef75901ff64d3349692385c61d0100e67d71cd1"], "🐳 chore: 개발 컨테이너(Dev Container) 환경 설정 추가"),
    ("ef12b5409d867c4644b68689cfb5e1f747453cdf", ["6ef75901ff64d3349692385c61d0100e67d71cd1"], "✨ feat: 20문항 모의고사(기초/심화) 시스템 로직 구현"),
    ("d4b2bd85e30f411647027184c7800d1af0205ce3", ["ef12b5409d867c4644b68689cfb5e1f747453cdf", "a5e15c21ab662083d8ebe018d081bcfae6be6b59"], "🔀 merge: 원격 저장소(main) 동기화 및 Dev Container 반영"),
    ("5f5af0cff0e27ca07867ce4521d733d2bbd03bf6", ["d4b2bd85e30f411647027184c7800d1af0205ce3"], "💄 style: 공통 UI/UX 디자인 테마 적용"),
    ("4727ec97ad5f63e6dc035f9c8f3da3794732fb7f", ["5f5af0cff0e27ca07867ce4521d733d2bbd03bf6"], "☁️ feat: Supabase 연동을 통한 클라우드 리더보드 시스템 구축"),
    ("fd213fa5751c6d4f64d025498b5d7414e5e47451", ["4727ec97ad5f63e6dc035f9c8f3da3794732fb7f"], "💄 style: Streamlit 기본 레이아웃 커스텀 및 헤더/푸터 디자인 수정"),
    ("52bb38613a669975b61a9b1bf8e44b0bd9653795", ["fd213fa5751c6d4f64d025498b5d7414e5e47451"], "✨ feat: 데이터 시각화 관련 문항 추가 및 문제 재생성 기능 구현"),
    ("3dff0f7d68b44175b26de2b52c7e25c935ac6a51", ["52bb38613a669975b61a9b1bf8e44b0bd9653795"], "✨ feat: 학습(Study) 모드 및 실전 모의고사(Exam) 모드 로직 분리"),
    ("3a6db1527a834aa5fd0095a27069ae8dbe8aa6ac", ["3dff0f7d68b44175b26de2b52c7e25c935ac6a51"], "✨ feat: 타이머 시스템 구축 및 모의고사 레이아웃 최적화"),
    ("db1c647e46395a0292c9f95ce2006123088c8c74", ["3a6db1527a834aa5fd0095a27069ae8dbe8aa6ac"], "🐛 fix: 탭 전환 시 발생하는 레이아웃 떨림(Layout Shift) 버그 수정"),
    ("63ba0e3e5895f263b8b2a1317f3893c7264732a3", ["db1c647e46395a0292c9f95ce2006123088c8c74"], "📱 style: 모바일/스마트폰 디바이스 지원 반응형 웹 레이아웃 적용"),
    ("6bfd78704480e142426945d08f5ad545c3d46099", ["63ba0e3e5895f263b8b2a1317f3893c7264732a3"], "💄 style: 애플리케이션 전체 UI/UX 시스템 고도화 및 리팩토링")
]

mapping = {}

for old_hash, old_parents, new_msg in commits:
    tree = run_git(["log", "-1", "--format=%T", old_hash])
    author_name = run_git(["log", "-1", "--format=%an", old_hash])
    author_email = run_git(["log", "-1", "--format=%ae", old_hash])
    author_date = run_git(["log", "-1", "--format=%ad", old_hash])
    
    env = os.environ.copy()
    env["GIT_AUTHOR_NAME"] = author_name
    env["GIT_AUTHOR_EMAIL"] = author_email
    env["GIT_AUTHOR_DATE"] = author_date
    env["GIT_COMMITTER_NAME"] = author_name
    env["GIT_COMMITTER_EMAIL"] = author_email
    env["GIT_COMMITTER_DATE"] = author_date
    
    cmd_args = ["commit-tree", tree, "-m", new_msg]
    for p in old_parents:
        cmd_args.extend(["-p", mapping[p]])
        
    new_hash = run_git(cmd_args, env=env)
    mapping[old_hash] = new_hash
    print(f"Mapped {old_hash[:7]} -> {new_hash[:7]}")

last_old_hash = commits[-1][0]
last_new_hash = mapping[last_old_hash]
run_git(["reset", "--hard", last_new_hash])
print("Branch successfully updated to rewritten history!")
