import sys
import subprocess

övning = sys.argv[1] if len(sys.argv) > 1 else None

övningar = {
    "1": "övningar/övning1_markdown/main.py",
    "2": "övningar/övning2_json/main.py",
    "3": "övningar/övning3_streaming/main.py",
    "4": "övningar/övning4_text_och_kod/main.py",
    "5": "övningar/övning5_template_prompting/main.py",
}

if övning in övningar:
    subprocess.run(["python3", övningar[övning]])
else:
    print("Ange en övning (1-5) att köra, t.ex:")
    print("python3 run.py 3")
