#
# pandas로 데이터 열기
#
import os
import pandas as pd
import numpy as np


print(os.getcwd())
DATA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
print(DATA)


def path(file):
    return os.path.join(DATA, file)


x = 3.141592
print(f"{x:.2f}")
print(f"{x:10.3f}")

df = pd.read_csv(path("11_설비센서_ai4i.csv"), encoding="utf-8-sig")
print(df.shape)
print(list(df.columns))
print(df.head())
print(df.dtypes)


print(df.describe().round(2))

#
# 상관계수
#
# >> 두 열이 같이 움직이는 정도를 -1 ~ 1로 나타낸 숫자.
# 1에 가까우면 하나가 오를 때 다른 것도 오르고, -1이면 반대, 0은 무관
# 숫자 열끼리만 계산되므로 문자열은 빼야 함
dig_col = df.drop(columns=["설비ID", "타입"])

print(dig_col.corr().round(4))

# -
dirty = pd.read_csv(path("12_제조센서_전처리.csv"), encoding="utf-8-sig")
print("=" * 60)
print(dirty)
print(dirty.isna().sum())

print(dirty.duplicated().sum())
print(dirty[dirty.duplicated(keep=False)])  # keep=False >> 중복된 짝을 보여줌


clean = dirty.copy()
clean.drop_duplicates(inplace=True)
clean.loc[clean["회전수"] < 0, "회전수"] = np.nan
# 문법 .loc[조건, 열] = 조건에 맞는 행의 그 열 칸. 거기에 NaN을 삽입
print(clean)

for i in ["온도", "압력", "회전수"]:
    med = clean[i].median()
    clean[i] = clean[i].fillna(med)

print(clean)
print(clean.isna().sum().sum(), len(clean))


#
# numpy 배열로
#
x = df["공기온도"].values
y = df["공정온도"].values
print(x)


print(dirty[dirty["진동"] > 3.2][["측정ID", "설비명", "진동", "상태"]])
