import gc
from pathlib import Path

import pandas as pd
from datasets import load_dataset


def main() -> None:
    print("donwload japanese mmarco")

    dataset_name = "bclavie/mmarco-japanese-hard-negatives"
    train_dataset = load_dataset(dataset_name)
    train = train_dataset["train"]
    
    df = pd.DataFrame({
        "qid": train["query"],
        "pos": train["positives"],
        "neg": train["negatives"],
    })
    print(df.shape)

    filepath = Path("data/bclavie/mmarco-japanese-hard-negatives/raw.tsv")
    filepath.parent.mkdir(exist_ok=True, parents=True)

    df.to_csv(filepath, sep="\t", header=None, index=None)
    print(f"save '{filepath}'")
    
    print("DONE")


if __name__ == "__main__":
    main()
