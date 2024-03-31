# how to run

## setup

```shell
pip install -r requirements.txt
```

```shell
mkdir intermediate ckpt model_ckpt output
```

## run

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

## monitoring gpu

```shell
nvidia-smi -l 5
```
