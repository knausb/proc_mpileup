

import numpy as np
import pandas as pd

df = pd.DataFrame(columns=["name", "mask", "weapon"],
                  index=["trait_10002", "trait_00003", "trait_00001"])
df.loc["trait_10002"] = ["Raphael", "red", "sai"]
df.loc["trait_00001"] = ["Donatello", "purple", "bo staff"]
df.loc["trait_00003"] = ["Leo", "blue", "katana"]

df.to_csv("turtles.csv")

