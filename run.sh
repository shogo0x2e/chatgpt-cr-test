#!/bin/bash

# イメージ名を定義
IMAGE_NAME="my-python"

# Dockerfileをビルド
docker build -t $IMAGE_NAME .

echo -e "\n\n---------------------------------------\n\n"

# イメージを実行
docker run $IMAGE_NAME
