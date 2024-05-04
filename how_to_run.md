# how to run

## setup

```shell
pip install -r requirements.txt
```

```shell
mkdir intermediate ckpt model_ckpt output
```

## run (default)

### train run

```shell
python -m splade.train config.checkpoint_dir=./ckpt
```

### indexing run

```shell
python -m splade.index config.checkpoint_dir=./ckpt config.index_dir=./model_ckpt
```

### retrieve run

```shell
python -m splade.retrieve config.checkpoint_dir=./ckpt config.index_dir=./model_ckpt config.out_dir=./output
```

## run (msmarco)

download

https://microsoft.github.io/msmarco/Datasets

ensemble distil dataset

```shell
wget https://download.europe.naverlabs.com/splade/sigir22/data.tar.gz
tar xvzf data.tar.gz
```

continue or restart download

```shell
wget -c https://download.europe.naverlabs.com/splade/sigir22/data.tar.gz
```

### train run

```shell
SPLADE_CONFIG_NAME=config_splade++_ensembledistil python -m splade.train config.checkpoint_dir=./ckpt
```

### indexing run

```shell
SPLADE_CONFIG_NAME=config_splade++_ensembledistil python -m splade.index config.checkpoint_dir=./ckpt config.index_dir=./model_ckpt
```

### retrieve run

```shell
SPLADE_CONFIG_NAME=config_splade++_ensembledistil python -m splade.retrieve config.checkpoint_dir=./ckpt config.index_dir=./model_ckpt config.out_dir=./output
```

## monitoring gpu

```shell
nvidia-smi -l 5
```

## docker run (toy data)

build

```shell
docker-compose build
```

run

```shell
docker-compose -f compose.yml -f compose.train.yml up
```

```shell
docker-compose -f compose.yml -f compose.index.yml up
```

```shell
docker-compose -f compose.yml -f compose.retrieve.yml up
```

## use japanese dataset

### download japanese dataset

```shell
mkdir -p data/mmarco/google/collections/ data/mmarco/google/queries/dev/ data/mmarco/google/queries/train/ data/mmarco/google/queries/full_dev/
```

*download dataset*

- https://huggingface.co/datasets/unicamp-dl/mmarco/tree/main/data/google

collections

```shell
wget -c -O data/mmarco/google/collections/raw.tsv https://huggingface.co/datasets/unicamp-dl/mmarco/resolve/main/data/google/collections/japanese_collection.tsv
```

dev dataset

```shell
wget -c -O data/mmarco/google/queries/dev/raw.tsv https://huggingface.co/datasets/unicamp-dl/mmarco/resolve/main/data/google/queries/dev/japanese_queries.dev.small.tsv
```

validation dataset

```shell
wget -c -O data/mmarco/google/queries/full_dev/raw.tsv https://huggingface.co/datasets/unicamp-dl/mmarco/resolve/main/data/google/queries/dev/japanese_queries.dev.tsv
```

train dataset

```shell
wget -c -O data/mmarco/google/queries/train/raw.tsv https://huggingface.co/datasets/unicamp-dl/mmarco/resolve/main/data/google/queries/train/japanese_queries.train.tsv
```
