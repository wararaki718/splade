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

```shell
cd dataset
wget https://msmarco.z22.web.core.windows.net/msmarcoranking/triples.train.small.tar.gz
```

continue or restart download

```shell
wget -c https://msmarco.z22.web.core.windows.net/msmarcoranking/triples.train.small.tar.gz
```

### train run

```shell
SPLADE_CONFIG_NAME=config_splade++_selfdistil python -m splade.train config.checkpoint_dir=./ckpt
```

### indexing run

```shell
SPLADE_CONFIG_NAME=config_splade++_selfdistil python -m splade.index config.checkpoint_dir=./ckpt config.index_dir=./model_ckpt
```

### retrieve run

```shell
SPLADE_CONFIG_NAME=config_splade++_selfdistil python -m splade.retrieve config.checkpoint_dir=./ckpt config.index_dir=./model_ckpt config.out_dir=./output
```

## monitoring gpu

```shell
nvidia-smi -l 5
```
