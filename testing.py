import pandas as pd


# df1 = pd.read_json(r"C:\Users\Vishwas\Desktop\Projects\large_language_models\AI_jam_workshop\example\test_embeddings.json")
# df2 = pd.read_json(r"C:\Users\Vishwas\Desktop\Projects\large_language_models\AI_jam_workshop\example\train_embeddings.json")
# appended_df = pd.concat([df1, df2], ignore_index=True)
# print(appended_df)

with open(r"C:\Users\Vishwas\Desktop\Projects\large_language_models\AI_jam_workshop\example\test_embeddings.json", "r", encoding="UTF8") as f:
    raw_data = f.read()
print(raw_data)
print(pd.DataFrame(raw_data))
