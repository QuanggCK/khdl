import pandas as pd
L = pd.DataFrame({"ma": ["K1", "K1", "K2", "K3"], "v": [1, 2, 3, 4]})
R = pd.DataFrame({"ma": ["K1", "K1", "K2", "K4", "K4"], "w": [5, 6, 7, 8, 9]})
print(len(L.merge(R, on="ma")), len(L.merge(R, on="ma", how="left")))

# Da dap an dung la 5 6
