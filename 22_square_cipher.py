import cv2
import numpy as np

text = '''oomktvziqtaovmmpxzoqrzsxlpwpgoj
uDQEMISYnnVYnvyWRhHsDXnSCXAVVZj
tZbknedErdpvAwQWpUiLqOxIqpafvXp
dXoAVWcKppbEPuaqmXWjXJwRoRFOoEg
pDiRUXlQjKJlslskVpGwtljGyVJPxHv
bQsQNKxCsdYMdQPJiBmyrsuOrJQOtXg
pMekeinUaMoDXqFzweLKipkBuggnsUv
eQFYCJSKfBgHaJgZnZoWmOmAOJLVQHi
hljrplajyKNXtwmfOjRwOqcqeeplyzy
gkFOltsOyrPgIaerIaSjQQaVMyEhfyd
vEaRHbBzfrcwJbCZmHdddLpuEJwspbt
sXQGkwpKaTZmWJiZzpbkpHNiToawxKn
wJpIKbGhnLjVAJNcxrqkKEJCKCOocSv
mTRDNDpFtRUmcHoRELeSqXoGUIIsuYu
ajeHaSVlQGLaEprSQarDzTomJdAWfqb
zIJLHRBXMvNDegYeaoVRDuWBbdSBtLv
xIeKdAYwajGHMgRLDGgDinBiLNBgatb
kHepNsCQSJjTRmQrCHYWJqIPOVAUOer
rvhmZfmogPglGNuLyAuSivBctlvVfzb
qBJdHUkSaTArlgkhtHPyGhXOPkwmkBq
rvbzZfwvLtTnhyXVHPlwsuGZQnNiNcm
yCMtAVwYVgtZHVNznolGMBETIHFmoWj
wfezbysbvOzsAhxSZFFAfOouyHldEYh
gNHKKSFUtcUxfRyXHMugYBtAxBwDJZh
rHmsozuNeoJqyzMDHsNbUDwzaNLtdxr
bVmQMHyNndOWCZLnhrPxZXCYLDTWQre
aSiEEJjZtoRpUzgsxsiiGzvnRpKLMrk
qTzGCKvNhUhjrmCjAdwQAvkgqHyJZLm
sSxzwjxAnWesTszIxirRwcWIXUPtwwa
nTDEMTRGyhzdCtkTTDWbxdSjsNYlfXz
eawtidzosgaofjxxyfcdoiulemirqap
'''

# 文字列　幅


def convert_1d_to_2d(l, cols):
    return [l[i:i + cols] for i in range(0, len(l), cols)]


bin_list = []
for char in text:
    if(char.isupper()):
        bin_list.append(1)
    elif(char.islower()):
        bin_list.append(0)


bin_list_2d = convert_1d_to_2d(bin_list, 31)

img = np.full((50, 50, 3), 128, dtype=np.uint8)
for i in range(31):
    for j in range(31):
        if(bin_list_2d[i][j] == 1):
            cv2.rectangle(img, (i, j), (i+1, j+1),
                          (255, 255, 255), thickness=-1)
        elif(bin_list_2d[i][j] == 0):
            cv2.rectangle(img, (i, j), (i+1, j+1), 0, thickness=-1)

cv2.imwrite('22_square_cipher.png', img)
